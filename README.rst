Java Project Manager
====================

.. contents::

Summary
-------


Installation
------------
Note: The installation script would create a bin folder in your home directory and add three Python
files to it.  It will also add a hidden file, .java-project-manager, to your home directory.

Inside a terminal:
^^^^^^^^^^^^^^^^^^

1) Navigate to a directory where you wish to clone the repository
2) Clone the repo via:

   .. code-block:: bash

      $ git clone git@github.com:pchan37/java-project-manager

3) Navigate to the root of the repository

   .. code-block:: bash

      $ cd java-project-manager

4) Run the installation script

   .. code-block:: bash

      $ . ./install.sh


Usage
-----
After installation, you have five additional shell functions at your disposal:

- *create_project*

  - Prompts you for how many directories to create and then prompts you for the name of each
    directory
  - Create the directories and populate them with stub files

    - The main class file with the same name as the directory/package (ie Hello.java)
    - The test class file with the same name as the directory/package except with the additonal of
      Tester (HelloTester.java)

- *add <filename>*

  - Create a new file, filename, with the package line already inserted
  - Open the file via Emacs

- *generate*

  - Generate the makefile/make.bat for that particular project/package

- *clean*

  - Remove the folder containing the class files for the project/package

- *compile*

  - Remove the folder containing the class files for the project/package
  - Compiles the files in the package

- *run*

  - Remove the folder containing the class files for the project/package
  - Compile the files in the package
  - Run the program

- *javatest*

  - Tests your program and see which cases are wrong as well as how many are wrong
  - Requires in<number>.txt and out<number>.txt for the given input and expected output respectively

Version History
---------------

Version 0.2.4
^^^^^^^^^^^^^
- Added uninstallation script
- Added a compile function
- Added a new function, javatest, giving access to the new testing framework support

  - compiles and runs your code, compares your output to expected output
  - print which cases are solved incorrectly, as well as how many are incorrect

Version 0.2.1
^^^^^^^^^^^^^
- Fixed the suffix when prompting for the nth directory
- Improved the add file function to add the stub for the class (ie public class <classname>{})
- Added feedback message when creating directories

Version 0.2
^^^^^^^^^^^
- Wrote SkeletonGeneratorInterface, a program that simplify access to the functionalities provided
  by the SkeletonGenerator class
- Wrote java-project-manager.sh, a file containing shell functions allowing you to:

  - create project directories
  - add files
  - generate makefile/make.bat
  - remove your class files
  - and run your code

Version 0.1
^^^^^^^^^^^
- Wrote the SkeletonGenerator class, which would do most of the heavy lifting
- Running SkeletonGenerator.py would allow you to create project directories/packages, each
  directory would contain:

  - Stub files for the main class and the test/driver class
  - makefile and make.bat (for Windows installation without make)

    - *make clean* or *make.bat clean* to remove class files
    - *make run* or *make.bat run* to remove class files, compile, and run your class
  - add_file.py (script to create new Java files with the package line already added)
