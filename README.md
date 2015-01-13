# Assignment Numerical Integrals
Prerequisites:
~~~
sudo apt-get install pep8 pyflakes make
~~~

Don't forget to:
+ Install pep8 and pyflakes, **VERY IMPORTANT!**
+ Put your names in the $(STUDENT_NAMES) variable in the makefile.
+ Put your names in all the python files
+ Run `make` frequently to prevent a lot of work later on.

## Framework guide
Use this framework to do the assignment of Numerical Integrals. This is mainly
to prevent students from writing spaghetti python code, and to speed-up the
task of grading.

Fill in the code in the apporiate places. All the files correspond with the
assignments on uva.sowiso.nl. You may alter the functions if needed, but let
the general idea of the framework the same.

+ Makefile
    The makefile included in this directory is essential for this handing in
    your code. Running `make` will run pep8 and pyflakes when some change has
    been made to your python code. It creates a deliverable every time you run
    make. But before it does, the code is checked for syntax using pep8 and
    unused or undefined variables.

