@def title = "Terminals worksheet"

# Terminals

Week 1 -- using Python from the command line

## Getting started

Please read through the following bits of housekeeping before attempting
the remaining worksheet tasks.

## Setting up your computer

This worksheet has been written assuming you have set up your computer first.
You will need to first make sure you have:

1.  A bash shell installed,
2.  Python 3.X installed,
3.  Python 3 on your computer's PATH variable.

If you are running **Linux** or **OSX**, they come with a bash terminal as
standard. So all you need to do is download the correct version of Python
(3.X), and add it to your PATH after opening a terminal by typing `export
PATH="PATH:your_python_path"`, where `your_python_path` is replaced with the
location of your Python3 installation. You can find the location of your
Python3 installation from within Python itself. For example on OSX it
might look like:
```python
>>> import sys
>>> sys.executable
'/Library/Frameworks/Python.framework/Versions/3.8/bin/python3'
```
That means that in the terminal I should run:
```console
$ export PATH="PATH:/Library/Frameworks/Python.framework/Versions/3.8/bin"
```
That will ensure that when I run `python` in the terminal it runs Python 3.

If you are running **Windows** it is recommended to install git for windows
which comes with a "git bash" terminal that uses the same commands as the
terminals on OSX or Linux. Many of the example commands below will not work in
the standard Windows "DOS" terminal.

## Using the terminal

The terminal (or command line) is an essential part of any operating
system. It's an efficient way to navigate a file system, open files, run
executables and make time-saving scripts. Pretty much anything you do by
clicking around on a GUI (Graphical User Interface) can be done in the
terminal, often more efficiently.

## Basic terminal commands

First open up a terminal. A terminal window will open, with some stuff
followed by a line that reads `bash-4.2$` telling you the computer is running
version 4.2 of bash, and the `$` is the bash prompt, indicating you can enter
bash commands.

So let's try our first bash commands! Type `ls` and hit enter. You should see
something like this:

```console
$ ls
Desktop  Documents  Downloads
```

The `ls` command is a special terminal command that means list the contents of
the current directory. In this case the directory is my user directory and it
shows all of the folders that are contained within it. After you hit enter the
terminal will run the `ls` command and the `ls` command will print out a list
of the files and folders in the current directory: this appears on the second
and third lines (bin, Desktop etc.).

Note that from now on that shaded section above is how you can expect to see
terminal commands demonstrated. I've omitted the stuff before the prompt, but
what comes immediately after the prompt is the command you should type before
hitting enter. Also because we are on different machines, you can expect the
output to sometimes look a little different, as you will have different
folders and files to me!

The next two commands we want to learn in addition to `ls` are `pwd` and `cd`.
The `pwd` command is short for "print working directory" and will print out
the current working directory. This is the folder that you are currently
working in. The `cd` command is short for "change directory" and is used to
change to a new working directory. You can then use `ls` to see what is in the
new working directory:

```console
$ pwd
/home/sw1850
$ ls
Desktop  Documents  current
$ cd current/emat10006
$ ls
index.html Makfile src/
$ pwd
/home/sw1850/current/emat10006
```

In the session above I use `pwd` to show that I am currently in the directory
`/home/sw1850` (this is the name of my user directory on this computer).
Within my user directory is a folder called `current` which contains things I
am currently working on. In there is a folder called `emat10006web` which
contains the files used for working on this unit. If I want to work in that
directory I can change to it by typing `cd current/emat10006web`. Afterwards
my current working directory is `/home/sw1850/current/emat10006web` and if I
run `ls` it will show me the contents of this new directory.

- **Exercise:** Try these commands out yourself. Get comfortable moving
  between directories, looking at files and the working directory as you go.

- **Exercise:** Can you figure out what entering the command `cd ..` does?

You may have found some issues when using `cd` to move around if a directory
has a space character in it. The `cd` command sees strings separated by a
space as two separate strings and will try to change to a directory named by
the string before the space.  This is why it's a good idea to avoid using
spaces, and instead use dashes (-) or underscores (\_), when naming files and
folders. You can get around this by using quotation marks, e.g.  `cd  'My
Directory'`.

You can do all of things you might do in a formal file browser in the
terminal! Below I've demonstrated lots of new commands.

- **Exercise**: Try all of these commands for yourself. Work out what they
  each do by checking your directory with `ls` before moving onto the next
  command.

If you're unsure what they do, try checking their help function by typing the
command followed by `--help`, for example `cp --help` (you should only need to
read the top of the help).

Lines starting with a `#` are comments, which you don't need to enter, but
contain extra questions or tips.

```console
  $ mkdir new-work
  $ cd new-work
  $ touch foo.txt
  $ # make sure to ls after each command!
  $ touch ../bar.txt
  $ # where is bar.txt?
  $ gedit foo.txt
```

At this point gedit (a text editor installed on the lab computers)
should open, and you should add some text (use multiple lines, and some
tab characters too), save it then close the window. Note that the prompt
will not appear in the terminal while gedit is still open.

```console
$ cat foo.txt
$ cat foo.txt -A
$ # what do you think those extra characters represent?
$ cp foo.txt foo2.txt
$ mv foo2.txt new-foo.txt
$ cat foo.txt new-foo.txt
$ mv ../bar.txt bar.txt
$ echo hello there
$ echo hello there > bar.txt
$ # now try looking at the contents of bar.txt
$ echo foo.txt
$ # is this what you expected to see?
$ rm foo.txt
$ cd ..
$ rm -r new-work
```

Below are some useful tips and shortcuts to make you super-speedy when
using the terminal:

"Tab auto complete" helps avoid typing out lengthy file / directory names, and
reduces typos. Whenever you start typing the name of a file or directory, hit
the Tab key and the terminal will try and automatically complete what you are
typing based on what's in the directory. E.g. say I enter `ls` in my current
directory and see 3 folders:

```console
$ ls
lecture_notes/  homework_questions/ homework_solutions/
```

If I type `cd l` and hit tab it completes to `cd lecture_notes`. If I type `cd
ho` and hit tab multiple times, it cycles between `cd homework_questions` and
`cd homework_solutions`. Hitting enter runs the command as usual. Navigate to
somewhere with lots of folders / files and play around with this. Try just
typing `cd ` (with a space) and hitting tab twice -- what happens? Try
accessing a folder within a folder, e.g. `cd lecture_notes/week1/` using tab
to autocomplete both parts of the path.

You can cycle through old commands using the arrow keys. Try hitting the up
arrow key a few times, then hit enter to run the displayed command.

Try typing the command `history` and hitting enter. You'll see a list of
previously entered command with numbers next to them, e.g.

```console
$ history
  121 rm some_rubbish.txt
  122 cd homework_solutions
  123 ls
  124 cd engmaths/week13
```

Then typing e.g. `!122` and hitting enter will run `cd homework_solutions`.

The previously typed command can always be referred to as `!!`. This can be
useful is you forgot something at the end or start of your previous command.

You may have noticed that you cannot move the terminal cursor using the mouse.
To move to the start of the line we use `Ctrl-a`, to move the end of the line
we use `Ctrl-e`. To move forward and backward by character use `Ctrl-f`, and
`Ctrl-b`.  You should never really use arrow keys.

- **Exercise:** try all of these out!

## Hello World!

Next, we are going to make a Hello World program. Of course you've
already done this in Python, but we are going to run it from the
terminal.

Start by opening a text editor (on lab computers we recommend gedit) and
writing a Hello World program. Save it as `hello.py` *taking careful note of
where you save it!* (If you're getting confident with the terminal, try just
entering: `gedit hello.py`, this will create a new file and open it for
editing straight away, write your script and save and quit and the terminal
will be ready to go again. Hopefully you're starting to see benefits of using
the terminal!)

Open the terminal, and using the commands you learned above, navigate to the
folder where your `hello.py` script is saved.

To run the `hello.py` Python script we run the `python` command and give it
the name of the script we want it to run:

```console
$ python hello.py
Hello World!
```

There's our expected output! Here the `python` command tells the computer to
run `python.exe` (the Python interpreter) with the path of our script
`hello.py` as an argument (more on this below). Python then knows to execute
this Python script.  Note, that since we first navigated to the directory
where `hello.py` is located, the relative path was just the name of the file;
but in general we could provide a path to a script in a different directory,
or use an absolute path.

But how does the terminal know to understand the `python` command? It isn't a
standard bash command, like `pwd` or `cd`. The answer is because `python` is
on the computer's PATH environment variable. This variable specifies a set of
directories which contain executable programs which you might frequently want
to run. Python is one such program and so when you type `python` into the
terminal, the computer looks through the directories in its PATH variable,
looking for one called `python.exe` which it then runs. This saves you having
to remember and type out the absolute paths of commonly used executables.The
same goes for all of the terminal commands you are using, they stored in some
directory on the PATH. Look at what's on your PATH variable using `echo $PATH`
(the `$` here tells the terminal that `PATH` is a variable, try to run it
without the `$`. The terminal now sees the word `PATH` as a plain old string).

## Python Interactive Mode

Another thing we can do with the `python` command in the terminal
is just to enter the Python interactive mode. It behaves a bit like a
terminal but where you type Python commands. Just type `python`
and hit enter, and you'll see a welcome message and the `$`
prompt will change to a `>>>`, Python's prompt. From here you can
now type in Python commands (but not bash commands until you quit Python
interactive mode by typing `quit()`).

The interactive mode is great for trying out little code snippets,
finding the right in-built function, etc. Now is the perfect time to
re-familiarise yourself with some basic Python, as we won't have time to
revise things you were taught last term. Make sure you can remember how
to use:

-   variables: how to initialise them, the basic types, casting and
    scope

-   data structures such as lists, dictionaries and tuples: how to
    initialise them, access elements, append to them, and other basic
    functionality

-   basic control flow using conditional statements and loops

-   importing and using modules such as `math`

As you will remember, using interactive mode is only really for writing
a line or two of code. Practically, we will always be working with
Python scripts and running them from the terminal like we did with
`hello.py` above.

## Using a shebang

Add a line to the top of your `hello.py` script, so that it looks
like this:

This line at the top is called a shebang, or hash bang. Now you may not
think adding this would do anything, since lines starting with a
`#` in Python are comments and the interpreter ignores them. But
this line isn't for the Python interpreter, it's actually for the
operating system's program loader. The program loader will read the
first two bytes of a file, and if they are `0x23 0x21` (which, in
ascii, are the characters `#!`) it knows to treat this file as a
script. The script will then be passed to the executable mentioned on
the first line -- in our case the `python` command which calls
the Python interpreter. Python then reads the line as a comment, as
usual, and executes the script. The shebang must come write at the
beginning of the file.

Shebangs are used because it allows the person who wrote the script to control
how the script is run on a user's computer, rather than the other way around.
In our case for example, we have specified that our script should be run with
`python3`, rather than any other version of Python. This is useful because if
we released our script and a user runs it from the terminal as `python
hello.py`, then they might be running it with the wrong version of Python and
the behaviour might not be as we intended.

After adding the shebang to your script and saving it, run the following
commands:

```console
$ ls -l
-rw-r--r-- 1 sw1850 1049089     46  Jan 29 16:46 hello.py
$ chmod +x hello.py
$ ls -l
-rwxr-xr-x 1 sw1850 1049089     46 Jan 29 16:58 hello.py*
$ ./hello.py
Hello World
```

The `ls -l` command works like `ls` but shows more information. The first 10
characters of the line with the file information are the permissions the file
has. Notice how some of the dashes turn to `x` after the second command is
ran. The `chmod` command is short for "change mode", and it changes the mode
(or permissions) of the file. So `chmod +x hello.py` file has changed the
permission of the script to be executable (it can also change read and write
permissions, for example), and this is what the `x` is telling us. Changing
this 'bit' basically lets the operating system know this file is an
executable, and you should now find you can run your script by simply typing
`./hello.py` without explicitly invoking the Python interpreter. Try it!

It may seem like a minor addition, but shebangs are used universally by real
programmers when writing scripts to make them robust across platforms. You
should always use them from now on! Don't forget to change the executable
permission bit using `chmod +x filename.py` for each new script you write.

# Command line arguments

Command line arguments are the usual way in which a user tells a program how
they want it to run. You have heard the word 'arguments' before when talking
about functions in Python. Arguments are the inputs you give to a function,
and might paths to specify: how the function should run; provide some data;
provide files, etc.. It is a similar idea when we give a program arguments
from the command line, they are the inputs the program runs with, meaning a
user can specify how they want the program to run at the time of execution.

In fact we have already seen this several times -- you have been using command
line arguments all along! When entering the command `cd my_directory` into the
terminal, `my_directory` is an argument that is passed to `cd` specifying
which directory it should open. When we run `python hello.py`, we are passing
the path of our python script (in this case just `python.py`) to the
interpreter as an argument. Some of the commands you used earlier took two
arguments, such as `mv` which took a source and a destination. In actual fact
nearly all of these commands can take a variable number of arguments.

Try copying this simple Python script and saving it as `cl-arguments.py` The
program prints out the ./cl-arguments.py 10 foo 87.4
4 command line argument(s) inputted:
./cl-arguments.py
10
foo
87.4 command line arguments given at execution:
```python
#!/usr/bin/env python3

import sys

number_of_args = len(sys.argv)
print(number_of_args, "command line argument(s) inputted:")

for arg in sys.argv:
    print(arg)
```

Here's an example of executing this program from the command line:
```console
$ chmod +x cl-arguments.py
$ ./cl-arguments.py 10 foo 87.4
4 command line argument(s) inputted:
cl_arguments.py
10
foo
87.4
```

First we have imported the `sys` library, which allows access to a variable
called `argv`. This is the list of command line arguments that were given to
the Python interpreter upon execution, stored as strings. After that we print
`argv`'s length, then loop over the list printing each element. Play around
with running the program with different arguments -- spaces separate them, but
what if you use quotation marks? Are there characters it ignores? Notice how
the name of the script is the first (or zero-th) element of `sys.argv`. This
is because `argv` is the list of arguments provided to `python`, not
specifically to our script.

-   **Exercise** Write a program which accepts up to 5 integers as
    command line arguments, and prints their sum to the terminal. If
    more than five are entered, instead print an error message.

Notice how the number of arguments given at the command line is not
necessarily fixed. Programs often take advantage of this to allow
optional arguments, or as a way of specifying how a program should run.
Again, we have already seen this, as we have seen that running
`python` with no arguments opens it in interactive mode; whereas
running it with a script filename, runs that script.

Try running the commands `python --help`, `python --version` or `ls -l`. These
arguments are called 'flags', and are the conventional way of allowing the
user to indicate how they want the program to run. They are usually
distinguished from other arguments by the prefix '--' but they are still just
strings. When you run Python with the `--help` flag, notice it lists all the
different flags you can specify.

## Using `__name__`

Lastly we are going to cover another convention used by programmers when
writing Python scripts. As you should have noticed, when Python scripts are
ran, the interpreter seems to start by running the lines of code it finds
which are *not* in a function. The convention in Python is that (usually) the
only code not in a function is inside a strange looking conditional statement,
like this:

```console
if __name__ == '__main__':
	main()	
```

This says that the function called `main` will only be ran if a variable
called `__name__` has the value `'main'`. Note that since this is the only
code in the script not in a function, if `__name__` does not equal `'main'`
then no further code will be executed.

The primary reason for doing this will become clearer a bit later in the
course, when we cover importing modules. But for those of you who can't wait
until then here is a brief description: when the Python interpreter reads a
source file it sets up a few variables first, before executing all the code.
One of those variables is called `__name__`. If your module (script) is being
ran as the main program (e.g.  `python foo.py` then this variable is set to
`__name__ = '__main__'`. Whereas if your module is being imported by another
script, e.g. `bar.py` contains the line `import foo.py`, then the `__name__`
is set to something else for `foo.py`. Therefore the conditional statement at
the end only executes when your module is the one being ran. Only then will
the main function in `foo.py` be ran. Otherwise the functions and stuff in
`foo.py` will be callable in `bar.py` once it has been imported, but the main
function in `foo.py` will not run on that import line.)

Essentially this allows your script to be either ran by itself, or imported
elsewhere for its functions. This is another convention you should get used to
doing yourself! Here's an example of a Python script which uses all of the
above conventions. The code is in a file called `upper-lower.py` on
Blackboard. Once you fully understand how it works, move on to the final task.

# Task: Writing a program using command line arguments

Now for your first actual programming task of the unit! Unlike with the Intro
to Programming unit, your assignments on this unit will require you to adhere
very closely to an assignment specification. This means, for example, that
your file names should be exactly as specified, and the arguments your program
takes and outputs it gives must be precisely as they are asked for. This is
how it would be for a real software engineer. This short task lets you
practice this, as well as the topics we've covered this week before your first
assignment next week.

Write a program called `averages.py` that can calculate the mean, median and
mode of some data.

The inputs to the program should be given through the command line, and
consist of:

-   Optional flags: `--mean`, `--mode`, `--median`
    or any combination of these (you may assume they must be in this
    order, even if some are omitted)

-   The program should expect the data to be integers entered as
    arguments (up to a maximum of 8 data points)

-   When ran without `--mean`, `--mode`, or
    `--median` the program should output all three averages. The
    format of the output should be exactly as shown below.

-   When ran with any combination of `--mean`, `--mode`,
    or `--median` it should output just those averages specified.

-   When an unrecognised flag is inputted, or non-integer data points
    are given, etc., appropriate error messages should be given.

-   **Extension**: The program should also accept an additional optional
    flag, `--file` (you may assume this always comes after the
    other flags). When ran with the `--file` flag, the program
    expects one non-flag input which should be the name of a .txt file
    in which there is the data, formatted as one integer per line (with
    no maximum number of data points)

Some example inputs and outputs:

```console
  $ python averages.py 1 2 3 4 5
  Mean: 3
  Median: 3
  Mode: 1, 2, 3, 4, 5
```

```console
  $ python averages.py --median --mode 1 1 1 1 1 2 2 2
  Median: 1
  Mode: 1
```

```console
  $ python averages.py --mean --file my-data.txt
  Mean: 43.5
```

```console
  $ python averages.py --mean --mode --file my-data.txt 4 5 24
  Error: expected one non-flag input when -file is specified
```

```console
  $ python averages.py --mode 1 4 5 1 4 5 6 7 7 7 7 7
  Error: expected max 8 integer data points
```

Before you start writing, think carefully about the control flow of your
program, and how to deal with the variety of different combinations of inputs.
You should also make sure you use functions to organise the code. As a
*minimum* it should have a main function then one function each for the mean,
median and mode calculations. Use this to help with efficiency: e.g. if the
user specifies only the mode, don't bother calculating the mean or median.
