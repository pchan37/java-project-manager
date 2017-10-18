import os
import subprocess
import sys

import SkeletonGenerator

def get_java_filenames(directory_name):
    index_of_last_slash = directory_name.rfind(os.path.sep)
    if index_of_last_slash > 0:
        package_name = directory_name[index_of_last_slash + 1:]
    else:
        package_name = directory_name
    java_filename = '{}{}.java'.format(package_name[:1].upper(), package_name[1:])
    java_test_filename = '{}Tester.java'.format(java_filename[:java_filename.rfind('.java')])
    return java_filename, java_test_filename

def parse_sys_argv():
    command = sys.argv[1]
    directory = sys.argv[2]

    if command == 'create':
        sg = SkeletonGenerator.SkeletonGenerator(directory)
        directories = sg.create_directories()
        for directory_name in directories:
            java_filename, java_test_filename = get_java_filenames(directory_name)
            sg.create_skeleton(directory_name, java_filename, java_test_filename)
        return

    java_filename, java_test_filename = get_java_filenames(directory)
    if command == 'add':
        sg = SkeletonGenerator.SkeletonGenerator()
        if os.path.exists(sys.argv[3]):
            subprocess.Popen(['emacs', sys.argv[3]], env=dict(os.environ, **{'XLIB_SKIP_ARGB_VISUALS': '1'}))
            return
        sg.create_add_file_script('.', java_filename)
        subprocess.call(['python', 'add_file.py', sys.argv[3]])
        subprocess.call(['rm', 'add_file.py'])
    elif command == 'generate':
        sg = SkeletonGenerator.SkeletonGenerator()
        sg.create_make_files('.', java_filename, java_test_filename)
    elif command == 'clean':
        sg = SkeletonGenerator.SkeletonGenerator()
        sg.create_make_files('.', java_filename, java_test_filename)
        subprocess.call(['make', 'clean'])
        subprocess.call(['rm', 'makefile'])
        subprocess.call(['rm', 'make.bat'])
    elif command == 'run':
        sg = SkeletonGenerator.SkeletonGenerator()
        sg.create_make_files('.', java_filename, java_test_filename)
        subprocess.call(['make', 'run'])
        subprocess.call(['rm', 'makefile'])
        subprocess.call(['rm', 'make.bat'])
    else:
        print 'Illegal Argument Exception!'
        raise SystemExit(1)

def main():
    if len(sys.argv) > 1:
        parse_sys_argv()
    elif len(sys.argv) == 1:
        sg = SkeletonGenerator.SkeletonGenerator()
        sg.create_project_files()

if __name__ == '__main__':
    main()
