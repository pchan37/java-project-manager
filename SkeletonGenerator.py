import os
import platform
import sys

class SkeletonGenerator:

    def __init__(self, base_directory=''):
        self.base_directory = base_directory

    def _ensure_proper_format(self, directory_name):
        UNIX_DIRECTORY_FORM = directory_name.replace('\\', '/')
        WINDOWS_DIRECTORY_FORM = directory_name.replace('/', '\\')

        OS_TYPE = platform.system()
        OS_SPECIFIC_DIRECTORY_FORM = WINDOWS_DIRECTORY_FORM if OS_TYPE == 'Windows' else UNIX_DIRECTORY_FORM

        index_of_last_slash = OS_SPECIFIC_DIRECTORY_FORM.find(os.path.sep)
        if index_of_last_slash > 0:
            DIRNAME = OS_SPECIFIC_DIRECTORY_FORM[:index_of_last_slash]
            BASENAME = OS_SPECIFIC_DIRECTORY_FORM[index_of_last_slash + 1:]
            properly_formatted_basename = BASENAME[:1].lower() + BASENAME[1:]
        else:
            DIRNAME = '.'
            properly_formatted_basename = OS_SPECIFIC_DIRECTORY_FORM[:1].lower() + OS_SPECIFIC_DIRECTORY_FORM[1:]
        return os.path.join(DIRNAME, properly_formatted_basename)

    def _get_directories_from_user(self):
        num_times_to_prompt = raw_input('How many directories do you wish to create? ')
        if num_times_to_prompt.isdigit():
            num_times_to_prompt = int(num_times_to_prompt)
        else:
            print 'Error: {} is not a valid number!'.format(num_times_to_prompt)
            raise SystemExit(1)
        user_directories_list = []
        print 'Note: Use Upper CamelCase'
        for i in xrange(num_times_to_prompt):
            directory_name = raw_input('Give me the {}th directory name: '.format(i + 1))
            properly_formatted_path = self._ensure_proper_format(directory_name)
            path_with_base_directory = os.path.normpath(os.path.join(self.base_directory, properly_formatted_path))
            user_directories_list.append(path_with_base_directory)
        return user_directories_list

    def create_directories(self, *directories):
        if not directories:
            directories = self._get_directories_from_user()
        for directory_name in directories:
            properly_formatted_path = self._ensure_proper_format(directory_name)
            try:
                os.makedirs(directory_name)
            except OSError as e:
                message = 'Failed to create directory: {}.  '
                message += 'Please ensure you have write permissions!'
                print message.format(directory_name)
                raise SystemExit(1)
        return directories

    def generate_makefile(self, PACKAGE_DIRECTORY_NAME, java_test_filename):
        JAVA_CLASS_NAME = java_test_filename[:java_test_filename.find('.java')]

        del_class_files_command = 'rm -rf {}'.format(PACKAGE_DIRECTORY_NAME)
        compile_files_command = 'javac -d . *.java'.format(PACKAGE_DIRECTORY_NAME)
        run_file_command = 'java {}.{}'.format(PACKAGE_DIRECTORY_NAME, JAVA_CLASS_NAME)

        content = '{}\n'.format('clean:')
        content += '\t{}\n'.format(del_class_files_command)

        content += '\n'
        content += '{}\n'.format('run:')
        content += '\t{}\n'.format(del_class_files_command)
        content += '\t{}\n'.format(compile_files_command)
        content += '\t{}\n'.format(run_file_command)

        return content

    def generate_makebat_file(self, PACKAGE_DIRECTORY_NAME, java_test_filename):
        JAVA_CLASS_NAME = java_test_filename[:java_test_filename.find('.java')]

        del_class_files_command = 'del /s /q {}'.format(PACKAGE_DIRECTORY_NAME)
        compile_files_command = 'javac -d . *.java'.format(PACKAGE_DIRECTORY_NAME)
        run_file_command = 'java {}.{}'.format(PACKAGE_DIRECTORY_NAME, JAVA_CLASS_NAME)

        content = '@echo off\n'
        content += 'IF "%~1" == "" (\n'
        content += '  echo "Target not provided!  Please read the README for specific instructions"\n'
        content += ') ELSE (\n'
        content += '  IF "%~1" == "clean" (\n'
        content += '     {}\n'.format(del_class_files_command)
        content += '  )\n'
        content += '  IF "%~1" == "run" (\n'
        content += '     {}\n'.format(del_class_files_command)
        content += '     {}\n'.format(compile_files_command)
        content += '     {}\n'.format(run_file_command)
        content += '  )\n'
        content += ')\n'
        return content

    def create_skeleton(self, dirname, java_filename, java_test_filename):
        java_filename_no_ext = java_filename[:java_filename.find('.java')]
        PACKAGE_DIRECTORY_NAME = java_filename_no_ext[:1].lower() + java_filename_no_ext[1:]

        with open(os.path.join(dirname, java_filename), 'a') as java_file:
            class_name = java_filename[:java_filename.find('.java')]
            java_file.write('package {};\n\n'.format(PACKAGE_DIRECTORY_NAME))
            java_file.write('public class {}{{\n\t\n}}'.format(class_name))
        with open(os.path.join(dirname, java_test_filename), 'a') as java_test_file:
            class_name = java_test_filename = java_test_filename[:java_test_filename.find('.java')]
            java_test_file.write('package {};\n\n'.format(PACKAGE_DIRECTORY_NAME))
            java_test_file.write('public class {}{{\n\n    public static void main(String[] args){{\n        \n    }}\n\n}}'.format(class_name))
        return True

    def create_make_files(self, dirname, java_filename, java_test_filename):
        java_filename_no_ext = java_filename[:java_filename.find('.java')]
        PACKAGE_DIRECTORY_NAME = java_filename_no_ext[:1].lower() + java_filename_no_ext[1:]

        with open(os.path.join(dirname, 'makefile'), 'w') as makefile:
            makefile_content = self.generate_makefile(PACKAGE_DIRECTORY_NAME, java_test_filename)
            makefile.write(makefile_content)
        with open(os.path.join(dirname, 'make.bat'), 'w') as makebat_file:
            makebat_content = self.generate_makebat_file(PACKAGE_DIRECTORY_NAME, java_test_filename)
            makebat_file.write(makebat_content)
        return True

    def create_add_file_script(self, dirname, java_filename):
        java_filename_no_ext = java_filename[:java_filename.find('.java')]
        PACKAGE_DIRECTORY_NAME = java_filename_no_ext[:1].lower() + java_filename_no_ext[1:]

        with open(os.path.join(dirname, 'add_file.py'), 'a') as add_file_script:
            add_file_script.write('#!/usr/bin/env python\n\n')
            add_file_script.write('{}\n\n'.format('import os, subprocess, sys'))
            add_file_script.write('{}\n'.format('with open(sys.argv[1], "w") as java_file:'))
            package_line = 'java_file.write("package {};")'.format(PACKAGE_DIRECTORY_NAME)
            add_file_script.write('\t{}\n'.format(package_line))
            add_file_script.write('subprocess.Popen(["emacs", sys.argv[1]], env=dict(os.environ, **{"XLIB_SKIP_ARGB_VISUALS":"1"}))')
        return True

    def create_project_files(self, *directories):
        if not directories:
            directories = self.create_directories()
        for DIRNAME in directories:
            index_of_last_slash = DIRNAME.rfind(os.path.sep)

            if index_of_last_slash > 0:
                BASENAME = DIRNAME[index_of_last_slash + 1:]
                base_filename = BASENAME[:1].upper() + BASENAME[1:]
            else:
                base_filename = DIRNAME[:1].upper() + DIRNAME[1:]

            JAVA_FILENAME = '{}.java'.format(base_filename)
            JAVA_TESTER_FILENAME = '{}Tester.java'.format(base_filename)

            try:
                self.create_skeleton(DIRNAME, JAVA_FILENAME, JAVA_TESTER_FILENAME)
                self.create_make_files(DIRNAME, JAVA_FILENAME, JAVA_TESTER_FILENAME)
                self.create_add_file_script(DIRNAME, JAVA_FILENAME)
            except OSError as e:
                print 'Failed to create files, please check that you have write permissions!'
                raise SystemExit(1)


def main():
    if len(sys.argv) > 1:
        sg = SkeletonGenerator(sys.argv[1])
        sg.create_project_files()
    else:
        sg = SkeletonGenerator()
        sg.create_project_files()

if __name__ == '__main__':
    main()
