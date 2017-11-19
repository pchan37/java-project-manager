import mmap
import os
import re
import subprocess

import SkeletonGenerator

class ProjectTester(object):

    def __init__(self, java_filename):
        if not java_filename.endswith('.java'):
            print 'Invalid filename!'
            raise SystemExit(1)
        self.java_filename = java_filename
        self.java_filename_without_extension = java_filename[:java_filename.find('.java')]

    def _get_input_file(self):
        files_in_current_directory = [filepath for filepath in os.listdir('.') if os.path.isfile(filepath)]
        pattern = re.compile('(in(\d)+\.txt(?!~))', re.IGNORECASE)
        possibleInputFilenames = []
        for filepath in files_in_current_directory:
            match = pattern.search(filepath)
            if match:
                possibleInputFilenames.append(match.group(0))
        if len(possibleInputFilenames) == 0:
            print 'ERROR: Could not find the input file!'
            raise SystemExit(1)
        elif len(possibleInputFilenames) > 1:
            print 'ERROR: Found multiple possible input files!'
            raise SystemExit(1)
        else:
            return possibleInputFilenames[0]

    def _get_output_file(self):
        files_in_current_directory = [filepath for filepath in os.listdir('.') if os.path.isfile(filepath)]
        pattern = re.compile('(out(\d)+\.txt(?!~))', re.IGNORECASE)
        possibleOutputFilenames = []
        for filepath in files_in_current_directory:
            match = pattern.search(filepath)
            if match:
                possibleOutputFilenames.append(match.group(0))
        if len(possibleOutputFilenames) == 0:
            print 'ERROR: Could not find the output file!'
            raise SystemExit(1)
        elif len(possibleOutputFilenames) > 1:
            print 'ERROR: Found multiple possible output files!'
            raise SystemExit(1)
        else:
            return possibleOutputFilenames[0]

    def compile_java_file(self, dirname, java_filename, java_test_filename):
        sg = SkeletonGenerator.SkeletonGenerator()
        sg.create_make_files(dirname, java_filename, java_test_filename)
        if subprocess.call(['make', 'compile']) != 0:
            print 'ERROR: {} failed to compile!'.format(self.java_filename)
            raise SystemExit(1)
        else:
            print 'Compiled {} successfully!'.format(self.java_filename)
        subprocess.call(['rm', 'makefile'])
        subprocess.call(['rm', 'make.bat'])

    def run_and_redirect_java_file(self, dirname, java_filename, java_test_filename):
        with open('out.txt', 'wb') as your_answer_file:
            sg = SkeletonGenerator.SkeletonGenerator()
            sg.create_make_files(dirname, java_filename, java_test_filename)
            print 'Running {}...'.format(self.java_filename)
            if subprocess.call(['make', 'run'], stdout=your_answer_file) != 0:
                print 'ERROR: {} failed to run successfully!'.format(self.java_filename_without_extension)
                raise SystemExit(1)
            else:
                print 'Ran {} successfully!'.format(self.java_filename_without_extension)
            subprocess.call(['rm', 'makefile'])
            subprocess.call(['rm', 'make.bat'])

    def _get_line_count(self, filename):
        with open(filename) as f:
            return len(f.readlines())

    def compare_java_file_output(self):
        input_filename = self._get_input_file()
        output_filename = self._get_output_file()
        your_answer_filename = 'out.txt';

        try:
            with open(input_filename) as f:
                input_file = mmap.mmap(f.fileno(), 0, prot=mmap.PROT_READ)
            with open(output_filename) as f:
                output_file = mmap.mmap(f.fileno(), 0, prot=mmap.PROT_READ)
            with open(your_answer_filename) as f:
                your_answer_file = mmap.mmap(f.fileno(), 0, prot=mmap.PROT_READ)

            num_of_input_lines_per_one_output = self._get_line_count(input_filename) / self._get_line_count(output_filename)
            index = 0
            error_count = 0
            your_answer = your_answer_file.readline()
            while your_answer:
                expected_output = output_file.readline()
                input_lines = [input_file.readline() for _ in xrange(num_of_input_lines_per_one_output)]

                if your_answer != expected_output:
                    print 'ERROR at case {}'.format(index + 1)
                    print 'Input:'
                    print ''.join(input_lines)
                    print ''
                    print 'Your output: {} Expected output: {}'.format(your_answer.strip(), expected_output.strip())
                    print ''
                    error_count += 1

                index+= 1
                your_answer = your_answer_file.readline()

            print 'Total Errors: {}/{}'.format(error_count, index)
        except IOError as e:
            print 'Error opening or reading files!'

    def clean_up(self, dirname, java_filename, java_test_filename):
        sg = SkeletonGenerator.SkeletonGenerator()
        sg.create_make_files(dirname, java_filename, java_test_filename)
        subprocess.call(['make', 'clean'])
        subprocess.call(['rm', 'makefile'])
        subprocess.call(['rm', 'make.bat'])
        try:
            os.remove('out.txt')
        except OSError as e:
            pass
