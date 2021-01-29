# Getting set up with Python

## Outline

The purpose of this page is to

* Remember loosely what Python is
* Understand how to install it
* Check that the installed set up is correct
* Understand the basic usage of the Python interpreter
* Introduce the notation used in subsequent sections

Although this is mostly about setting Python up it is still worth reading even
if you already have Python set up on your computer. At a minimum you should
verify that you can run Python in the ways described below and that the
scientific modules are installed.

## Which interpreter?

Before we "install Python" it's worth taking a moment to consider what Python
is. Firstly it is programming language in which we can write Python code.
Secondly it is a *program* which we used to run our Python code. This program
is called the *interpreter*. Thirdly there is the Python standard library
which is a collection of additional code to go with the interpreter that we
can make use of in our code. Finally there is a broader eco-system of
"third-party" code written to go with your Python setup. In our case the
third-party stuff we're interested in is the code relevant to scientific
programming.

In fact there are a number of different interpreters that you can install and
use for running your Python code or that you can use in different
environments. Leaving aside the standard interpreter there are other
interpreters, notably [PyPy](https://www.pypy.org) (which is itself written in a
Python-like language) and [Jython](https://www.jython.org) (written in Java),
[MicroPython](https://micropython.org) for embedded systems and
[Brython](https://www.brython.info) (for running in browsers).

You don't need to use/install any of these different interpreters but it is
worth mentioning their existence at this point. Each of them can run basic
Python code equally well. Where they differ is in the more advanced features
that you won't normally need to know about and also that they are used in
different environments. The key point that's relevant to us here is that the
standard Python interpreter is the only one that works with the most commonly
used libraries for scientific computing in Python - so that's the one that we
want right now.

The standard Python interpreter is known as "CPython" (when we need to
distinguish it from the others). The "C" in CPython is for the C programming
language in which the interpreter is written: the interpreter is actually a C
program. You can see the code for it on [github
here](https://github.com/python/cpython).  In order to "install Python" here
we want to install the CPython interpreter.

We can install this using the [official installers from
python.org](https://www.python.org/downloads/) however it
would not come with all of the bits and pieces that we want. CPython is the
interpreter for the basic Python language which is a generic programming
language used in many different areas. It comes with an interpreter and the
"standard library" ("stdlib" for short) which is a set of modules for doing
common things. Usually though when we use Python for something - in our case
for *scientific* purposes - we will want to install some additional libraries.

Installing Python and then separately installing each of the different
libraries we want can be a pain for beginners to setup which is why installers
are provided that can bundle Python with other commonly used libraries. For
this reason I recommend to install the [Anaconda Python distribution from
continuum](https://www.anaconda.com/products/individual). In addition to the interpreter
and the stdlib this will install a large number of commonly used scientific
libraries such as `numpy` for Matlab-style arrays and `matplotlib` for
plotting that we are going to need to use in this unit.

However you install Python and these additional libraries it is important to
ensure that you can run Python from the terminal. Pay careful attention to any
options in the installer that refer to "adding Python to the PATH environment
variable" since this is the key to getting this set up right. If this isn't
right then you'll see something like "Unrecognised command: python". It's
possible to manually alter your `PATH` environment variable after installation
if necessary so that you can add the directory containing the Python
executable to it. If you are able to run Python in some way (e.g. using IDLE)
but the `python` command does not work in the terminal then you can see where
the executable is with

```python
>>> import sys
>>> print(sys.executable)
/usr/bin/python
```

This tells me that the executable is in the `/usr/bin/` directory so that's
the directory that needs to be on `PATH`.

Another confusion can occur here for OSX users. OSX comes with a version of
CPython preinstalled but that is the "system python" and you shouldn't mess
with it. Install a *different* Python using Anaconda as above (or
[homebrew](https://brew.sh) if that's what you're used to). You now need to
make sure that you can run this new version of Python when desired or
otherwise you won't be able to access the scientific Python libraries that you
install along with it. See below for checking the scientific libraries.

## Which Python version?

Another thing to think about here is the version of Python that you should
install. There are different versions of the Python language e.g. 3.4, 3.5
etc. A new version comes out roughly every 2 years. Usually each new version
is *backwards compatible* so that if you wrote code for say Python 3.4 then it
will still work with 3.5. However in going from Python 2.x to Python 3.x a
number of backward *incompatible* changes were introduced and the result is
that code written for Python 2 is unlikely to work for Python 3. The
differences are small but enough to mean that (unless carefully written) code
is unlikely to work in both versions.

Because Python 3 when released was incompatible with Python 2 many developers
continued to use Python 2 long after Python 3 was released. As an example I am
writing this on a new Mac Laptop running OSX 10.12. The system Python is
version 2.7 even though version 3.0 was released almost 10 years ago. The
current version of Python is 3.6. (This doesn't matter though because as
explained above I should install a separate Python and I will not use the
system Python for scientific work.)

In this unit we will be using Python 3 and you should install the most recent
version available (e.g. 3.6) but the exact version doesn't matter so much as
long as it is not Python 2.

It is important to know about the distinction between Python 2 and 3 just
because you may sometimes find yourself in an environment where Python 2 is
installed. The differences are reletively small so I will only mention two
differences here (because I have seen students caught out by them in the
past). In Python 2 `print` is a statement. So to print two variables `x` and
`y` with a space in between we write

```python
>>> print x, y     # Py2
```

Whereas in Python 3 `print` is a function and we would write

```python
>>> print(x, y)    # Py3
```

Another difference is that in Python 2 division of two `ints` gives another
`int` rounding towards minus infinity if necessary (floor division)

```python
>>> 21 / 2         # Py2
10
```

whereas in Python 3 we have "true division"

```python
>>> 21 / 2         # Py3
10.5
```

These differences are small in the grand scheme of things but they are enough
to mean that your code just won't work properly any more so the two Python
versions (2.x and 3.x) are essentially considered as distinct programming
languages - although they are *very* similar.

There are other differences that I don't want to go into here but the important
thing is to know that:

* There are difference between Python 2 and 3
* Different Python 3 versions e.g. 3.4, 3.5 etc are basically equivalent for
  our purposes.
* We will use Python 3 and you should install the most recent version of
  Python 3 that is available via your chosen method of installation.
* You may someday find yourself accidentally using Python 2 which could be
  very confusing when it happens.
* You can always check the Python version with `python --version` or
  `import sys; print(sys.version)`

## Running Python

There are actually many different ways to run Python so this is not a trivial
topic. Many of you will have prior experience using Python from
[IDLE](https://en.wikipedia.org/wiki/IDLE) which is
a graphical IDE (integrated development environment) having both an editor and
an interactive terminal. Typically when Python is installed IDLE will also be
installed along with some kind of shortcut that you can use to run IDLE. There
are also other IDEs used by Python programmers e.g.
[VS Code](https://code.visualstudio.com/) and [Spyder](https://spyder-ide.org/) are popular with scientific
programmers. Many people also like to write scientific code in the form of
[Jupyter notebooks](https://jupyter.org/). We will look at these things later.

### Interactive mode

Each of the above ways of running Python are useful in various different
situations. None of them can completely replace being able to run Python using
a command line though. That is why we are going to begin by running Python
from the system terminal by typing the command `"python"`:

```python
$ python
Python 2.7.3 (default, Oct 26 2016, 21:01:49)
[GCC 4.6.3] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> a = 2
>>> a + a
4
>>> print(a)
2
>>> for x in range(4):
...     print(x)
...
0
1
2
3
```

The above is how a quick terminal session on my computer looks where I run
Python and type a few interactive commands. Note the conventions that will be
used through these notes for a terminal session - I will assume that you
understand these throughout. The commands that I type in the terminal are on
the lines that begin with a `$` symbol. This is the standard terminal prompt
on Unixy (non-Windows) systems telling me that the terminal expects a command
line to be entered. On Windows the prompt may look different but within the
notes I will always use `$` to indicate a terminal prompt.

The command I run here is simply `"python"` with no arguments. This invokes
the Python interpreter in *interactive mode* so that after printing a startup
message I see the Python interactive prompt `>>>` which is the prompt for me
to enter some Python code. I can type a piece of Python code such as `a = 2`
and when I hit enter the interpreter will execute that code. If I type a
*statement* such as `a = 2` then the terminal will not usually output
anything. If I type an *expression* such as `a + a` then the terminal will print
the value of that expression i.e. `4` (the exception to this rule is that the
terminal will not print the special value `None`).

We can type a multiline piece of code such as the `for`-loop shown above. The
interpreter shows `...` to indicate that some lines are continuations of the
same section of code.

The Python interpreter in interactive mode is also called the Python *shell*.
However the normal non-Python terminal also has a different shell (called
`bash` on my machine) so this terminology can be a little confusing. The main
thing to take away from this - which is a common cause of confusion for
beginners - is that there are two different shells:

* The system shell has a `$` prompt and is for command lines
* The Python shell has a `>>>` prompt and is for Python code

Make sure that you don't get mixed up and type Python code into the system
shell or vice-versa - this will never achieve anything sensible.

### Exiting the interactive shell

There are a few ways to leave the interactive shell. I normally do it by
sending the EOF (end of file) signal. On Unixy (OSX, Linux, ...) systems you
send EOF with Ctrl-D. On Windows you press Ctrl-Z followed by Enter.
After exiting you should be back to the `$` prompt (or Windows equivalent).
You can then type command lines again. To reenter the Python shell run
`python` again.

Another way to exit is using Python code:

```python
$ python
Python 2.7.10 (default, Feb  7 2017, 00:08:15)
[GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import sys
>>> sys.exit()
$
```

### Normal mode

We can also add our code to a Python file with the extension `.py`.  Then we
can run the code file using the same interpreter but giving the filename on
the command line. This way of running the interpreter so that it reads code
from a file is called "normal-mode" to contrast with "interactive-mode".

Using whatever code editor you like create a file called `mystuff.py` and
insert the same code as was typed in the above interactive session i.e.:

```python
a = 2
a + a
print(a)
for x in range(4):
    print(x)
```

Now I'm assuming that your terminal is in the same folder that you saved the
file in - use `cd` to move to that folder if not. You can now run that Python
file with the command `python mystuff.py`:

```python
$ python mystuff.py
2
0
1
2
3
```

This is the normal way to use the Python interpreter to run your code. The
interactive prompt is useful for testing small pieces of code out but once
tested you should be putting all of your code into `.py` files and running
them like so. One important difference between the output above and
interactive mode is that the line `a + a` no longer prints anything out. This
is because expressions are only printed in interactive mode. When running
normally the interpreter will only print something if you tell it to with the
`print` function (contrast this with Matlab and its semicolon `;` output control).

### Check the scientific libraries

Please check at this point that you have the scientific libraries installed
using the interactive terminal:

```python
>>> import numpy
>>> import matplotlib
```

If all goes well these import statements will not appear to do anything
(except perhaps take a little time). If you see something like

```python
>>> import numpy
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ImportError: No module named numpy
```

then you don't have the scientific libraries installed. Or it could mean that
you're running the wrong Python since it is possible to have many installed...

Either way at this point you need to sort it out so that you can run the right
version of Python and have the scientific libraries installed.

## Summary

By now I am assuming that

* You have Python (and scientific libraries) installed.
* You have a text-editor suitable for programming installed.
* You can run Python using the `python` command from the terminal and know how
  to use the Python interactive shell.
* You can create a Python file and run it using `python myfile.py` from the
  terminal.
* You understand the difference between the system shell and the Python shell
  and know how to switch between them.
* You understand the notation used in showing the terminal sessions above.

If so then we're ready to move into the [basics of Python the language...](../basics/)
