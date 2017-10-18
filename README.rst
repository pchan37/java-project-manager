Java Project Manager
====================

.. contents::

Summary
-------


Installation
------------
Note: The installation script would create a bin folder in your home directory and add two Python
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

- *run*

  - Remove the folder containing the class files for the project/package
  - Compile the files in the package
  - Run the program

Version History
---------------

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
