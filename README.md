# Automated-Menu-Driven-Program
An automated menu driven program that interacts with the operating system to open the applications or software using Python.  

## Problem Statement: Convert the OS based program into a menu driven program using Python Code which will execute the required user query when user will give the input as a text.

### How to add a path of a software or directory on MacOS through CLI

1. First run this **command**

`$ nano .zshrc`

2. Append your path to the end of the commands mentioned in the file as for example:

`$ export PATH = "/Applications/:$PATH"`

3. Press Ctrl + X

4. Press capital Y

5. Then press enter 

6. To check whether the path is added to the system path, enter the following command:

`$ echo $PATH`
 
Note: the above commands will add all the macOS applications present in the applications folder to the system path

You can access the application from the Terminal as:

`$ open -a "ApplicationName.app"`

Note: A challenge given by IIEC Rise Community, a training program mentored by Mr. Vimal Daga

