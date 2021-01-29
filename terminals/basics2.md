# Loops, conditionals, and functions

Like all programming languages Python has loops, conditionals and functions. I
will briefly write about these here but I don't want to repeat what's already
written better in other places. For more please refer to the [official
python.org tutorial](https://docs.python.org/3/tutorial/controlflow.html).

There are some [exercises](#exercises) below to test your understanding of
these concepts.

## Loops

Python has `while` statements which are more or less the same as in all
programming languages. It also has `for` loops and these are potentially
different from what you would be used to coming from other languages. The key
thing to understand about `for` loops in Python is that we loop over an
*object*:

```python
>>> stuff = [1, 2, -1, 3]
>>> for x in stuff:
...     print(x)
...
1
2
-1
3
```

In this example the object we loop over a `list` but we can also loop over
many other kinds of objects such as `strings`, `tuples`, `dicts`, `sets`, etc.
If you just want to loop over the numbers say from 0 to 3 we use the `range`
function:

```python
>>> for x in range(4):
...     print(x)
...
0
1
2
3
```

Note that `range(a, b)` gives a *half-open* range such as mathematically represented with
$[a,b)$ meaning the integers $x$ such that $a \le x \lt b$. When called
with one argument `range(b)` is the same as `range(0, b)`. Observe that there
are similarities between the arguments to `range` and the start, stop and step
indices used when slicing i.e. `range(a, b, c)` gives the indices of the
elements selected by `stuff[a:b:c]` (assuming neither of `a` or `b` is
negative).

## Functions

Functions are explained in more detail in the [official python.org
tutorial](https://docs.python.org/3/tutorial/controlflow.html#defining-functions).
Here I only want to add some comments of my own about how to use functions
well.

Python has functions: use them. If you are used to using Matlab you might have
gotten into the habit of not using functions very often because each function
needs a new .m file. In Python we can have as many functions as we like in a
file and it is common to have many small functions in one file. Functions are
good and you should make a habit of composing all your code from small
well-designed functions.

Some languages (e.g. C and Java) require any function/method to have strictly
defined types for both arguments and return values. Often these types must be
explicitly declared in the definition of the function. However in Python we
don't declare any types and it is possible to make a function that returns
different types of objects at different times e.g.:

```python
def f(n):
    if n < 0:
        return 'a string'
    else:
        return -n

print(f(1)) # returns int (-1)
print(f(-1)) # Returns a string ('a string')
```

This is due to the dynamic nature of Python and in *some* situations is
useful. In general though you should not do this. Functions should always
return the same type. For example, a function `f(n)` could be understood as
always taking an integer (`n`) and return an integer. Doc-strings are useful
and can be used to explain the types:

```python
def absolute_value(n):
    '''absolute_value(n) -> absolute value of number n'''
    if n < 0:
        return -n
    else:
        return n
```

(Why do I say `number` instead of `int`, `float`, etc.?)

## Pure functions

Also as much as possible functions should be *pure*. This is an important
programming style that will make your code better and easier to read/debug
etc. To clarify what this means let's divide the world of functions into 4
categories using two different properties.

Our first property is that of having *side-effects*. A function that has
side-effects is one that changes something each time it is called. Such a
function will effect the state of the world/program in some way other than
simply returning a value. Such a function can be said to *do* something. An
example would be a function called `switch_off` that switches off your
computer. Other examples would be if a function writes to a file, prints
something in the terminal or show something on the screen. We can divide all
functions into those that have side-effects and those that do not.

The second property we will use to distinguish functions is whether the value
of the function depends in some way on anything other than its input
arguments. An example of this would be a function `get_cpu_temperature` that
returns the current temperature of the CPU. Other examples would be functions
that read from files or depend on the state of global (non-constant)
variables. We can divide the world of functions into those that depend only on
their arguments and those that also depend on external state in some way.
Functions that only depend on their arguments have the important property that
they will always return the same value for the same input arguments.

A function which neither has side-effects nor depends on external state is
called a *pure* function. This corresponds to the mathematical definition of a
function as an object $$f: A \to B$$ that associates elements from a set $A$
with elements from a set $B$. Pure functions are very easy to analyse and
use in your code since their behaviour is isolated from all surrounding code.
We only need to look at the code *inside* the function (and then any functions
it calls) in order to understand what the function does.

By contrast with pure functions, when a function depends on external state
(e.g. global variables) we need to care about *when* the function was called
in order to understand what it will do. If a function depends on
the state of a global variable then we need to understand when the global
variable would be modified to understand the function. In this case we might
need to analyse an *entire* program checking for any time that the global
variable might be modified by some other code.

Likewise when functions have *side-effects* we also need to care about when
they are called. If for example two functions print something then calling
them in a different order changes the output of a program. Likewise calling
the function more than once is not equivalent to just calling it once.

We will therefore divide the world of functions into 4 categories:

1. Pure functions. These do not depend on external state and do not have
   side-effects. As much as possible we should build our code from pure
   functions.
2. Input functions. These depend on external state but do not have
   side-effects. Most programs will need to have some kind of input functions
   but we should carefully limit the places where we use these.
3. Output functions. These do not depend on external state but do have
   side-effects. Again most programs will probably want to have some output so
   we will need to use these but we should limit the places where these occur.
4. Other functions. These are functions that both depend on external state and
   have side-effects. We usually want to avoid doing this but it is usually
   necessary for the higher-level functions in a program (the `main` function
   would normally come under this category).

Pure functions are good and we should use them as much as possible but it is
also usually necessary to have some input/output so we can't only use them. We
should try to segregate them from everything else though. Generally we don't
want to have a function that does both input and output or that does input and
then does many calculations with the input. A standard pattern would be to
have a function for input, functions for processing, and then a function for
output.

## A short demo

Let's consider this with an example. Suppose I have a CSV file containing
student's grades and that its contents looks like:

```text
Tom,60
Dick,80
Harry,50
```

I have decided that actually I want to fail Dick (for plagiarism) so I want to
change his grade to zero. To do that I want to read the CSV file into some
data structure in memory, change the grade, and then write the result back out
to a CSV file. Here's a script that does exactly that (don't worry if you
don't fully understand this):

```python
#!/usr/bin/env python3
#
#  zero_students.py
#
#  Usage:
#
#    $ ./zero_students.py grades.csv grades_zeroed.csv Dave
#

import csv

def main(inputfile, outputfile, *students_to_zero):
    '''Read CSV from inputfile, zero grades and write CSV to outputfile

    inputfile: filename to read
    outputfile: filename to write zeroed results to
    students_to_zero: list of student names whose marks should be zero
    '''
    # Input name/grades CSV file
    names_grades = read_grades(inputfile)

    # Zero the grades for the named students
    zero_grades(names_grades, students_to_zero)

    # Output name/grades CSV file
    write_grades(outputfile, names_grades)

def read_grades(inputfile):
    '''Read CSV file into a list of (name,grade) tuples.'''
    with open(inputfile) as fin:
        reader = csv.reader(fin)
        names_grades = []
        for name, grade in reader:
            # note that grade is also a string here
            names_grades.append((name, grade))
    return names_grades

def write_grades(outputfile, names_grades):
    '''Write list of (name,grade) tuples to outputfile'''
    with open(outputfile, "w") as fout:
        writer = csv.writer(fout)
        for name, grade in names_grades:
            row = (name, grade)
            writer.writerow(row)


def zero_grades(names_grades, students_to_zero):
    '''Set grades to zero for students names in students_to_zero'''
    N = len(names_grades)
    for n in range(N):
        name, grade = names_grades[n]
        if name in students_to_zero:
            # Set grade to zero (grade is a string)
            names_grades[n] = (name, "0")


if __name__ == "__main__":
    import sys
    main(*sys.argv[1:])
```

I can run the above to see

```bash
$ ./zero_students.py grades.csv grades_zeroed.csv Dick
$ cat grades_zeroed.csv 
Tom,60
Dick,0
Harry,50
```

You may find the above confusing as it users a number of concepts that we
haven't covered yet. If you want to know then the docs and tutorial can tell
you more about
[the csv module](https://docs.python.org/3/library/csv.html),
[reading/writing
files](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files),
or what the `__name__` [part at the end is doing](https://docs.python.org/3/tutorial/modules.html#executing-modules-as-scripts).

I don't expect you to fully understand the program above but I want you to see
that it is neatly divided into an input function, an output function, and a
function in between that computes something. The middle function `zero_grades`
is to be considered our *pure function*. Actually technically it is not a pure
function since it modifies its input argument (`names_grades`) but that
doesn't matter so much.

What I want you to take from the above is the sense of the structure of a
Python script where we have many small functions and the functional division
between the input, output and in-between functions. As your code gets larger
this kind of structure will help to organise things.

Note that if you get good at Python then it can be a very succinct language.
The program above can be written in a shorter way like:

```python
#!/usr/bin/env python3
#
#    $ ./zero_students2.py grades.csv grades_zeroed.csv Dave ...
#
# Zero grades of named students.

import sys
import csv

_, inputfile, outputfile, *students_to_zero = sys.argv

with open(inputfile) as fin, open(outputfile, "w") as fout:
    reader = csv.reader(fin)
    writer = csv.writer(fout)
    for name, grade in reader:
        if name in students_to_zero:
            grade = "0"
        writer.writerow((name, grade))
```

This version mixes together reading and writing in the same loop which is
actually more efficient (for much larger CSV files) since it doesn't require
loading everything into memory at once. Unfortunately this necessarily
involves mixing together our code for input and output unless we use more
advanced features of the language such as *classes* or *generators*.

This kind of lazy code with no functions or structure is okay for small
programs like this but should be avoided if you have any sense that your code
will end up getting large.

## Good use of functions

We use functions to break up our programs making them easier to understand.
Well-written functions should ideally be small and easy to understand in
isolation. Generally I like a function to fit in the screen so that I can see
the whole thing all at once. Occasionally there are good reasons for larger
functions but only in rare situations.

It's important for a function to fit within the screen so that you can easily
see what it does. Ideally the way you divide up your program should mean that
it's easy to see what a function does and whether or not it is correct just by
quickly looking at it.

However the most important places where we want to quickly understand what a
function does are not where it is *defined* but where it is *called*. Usually
a function, say `f`, calls some other functions, say `g` and `h`. I want to be
able to look at (the definition of) `f` and verify its correctness, or change
it in some way without needing to also go and look at `g` and `h` to see what
they do.

So how do we improve the readability of something like the function `f` below?

```python
def f(a, b):
    c = g(a)
    return h(c, b)
```

Looking at this function it is really not clear what it does. The main problem
is in fact the *names* of the functions and variables. The function names
`f`, `g` and `h` convey nothing about what those functions do. That's bad
enough for `f` but I am at least *looking* at `f` right now so I can see its
code. The other functions `g` and `h` are somewhere else, perhaps in another
file. I have no way to understand what `g` and `h` do without finding them
because their names communicate nothing. It's very important when writing
functions to give them good names because of the distant readability effect
that the names have on the code. The same is also true in a more local sense
with the names of the variables `a`, `b` and `c`. To find out what `a` and `b`
are supposed to represent I'll probably need to go and read the code that
calls `f`. The variable  `c` is local to this function but is at least passed
to `h` so perhaps the definition of `h` will help me to understand what it is.

With the last paragraph in mind, look at the `zero_students.py` script above
and think about the names used there. The first function is called `main`.
There is a generally accepted convention that the action of a program is
contained within the `main` function. I know (or rather assume) when I look at
this function that it represents the program as a whole so this name is
communicating something to me.

Input functions normally have names like `read_X` or `get_X` to indicate their
purpose. Likewise output functions have names like `write_X`, `set_X`,
`print_X` etc. Sometimes we have a pair of input/output functions that are
supposed to act more or less like inverses. You can communicate this
relationship between functions by using consistent naming e.g.  `read_grades`
and `write_grades`.

Some functions *do* something like `zero_grades` and should have a name that
is a *verb* representing the action (zero is intended as a verb here - it
means to set something to zero). Note that this particular function does not
return a value. It modifies its argument which to me feels like an action.
If it did return a value then its name should represent the value returned.
For example I could change the `zero_grades` function to return a new list
instead of modifying the list passed in like so:

```python
def zeroed_grades(names_grades, students_to_zero):
    new_grades = []
    for name, grade in names_grades:
        if name in students_to_zero:
            grade = "0"
        new_grades.append((name, grade))
    return new_grades
```

Then we would call it like

```python
new_grades = zeroed_grades(names_grades, students_to_zero):
```

Now we can see that I have renamed the function as `zeroed_grades` which
is a noun description representing the object that it *returns*. This
`zeroed_grades` function is a true pure function and should be named after
its return value.

Notice how much information is conveyed by the names in that last line of
code. You could read that line of code in isolation from the entire rest of
the program and possibly understand what it does, what it returns, and what
each of its arguments represents. It almost communicates the entire meaning of
the program! Good use of names has a *big* impact on the readability of
your code.

## Exercises

1. Given a list of numbers `data = [2, 3, 1, -1]` write a loop that prints the
   square of each element of the list e.g.

```text
4
9
1
1
```

2. Now write a function that takes a list like `data` and *returns* a new list
   with each number squared i.e. `[4, 9, 1, 1]`.

3. Write a function that filters a list of numbers like `data`, giving a list
   containing only the positive numbers.

4. How would you print the elements of `data` in reverse?

5. Create your own factorial function. Is it faster or slower then
   `math.factorial` (try it with large numbers)?

6. Given that $\mathrm{e} = 1 + 1 + \frac{1}{2} + \frac{1}{3!} + \cdots + \frac{1}{n!} + \cdots$
   write a loop the calculates the value of $\mathrm{e}$ to approximately 10
   d.p.

7. Create a function that calculates the mean of a list of numbers.

8. Write a program (with a `main` function) that reads the arguments passed on
   the command line and prints their product so e.g.

```bash
$ ./product.py 3 4
12
$ ./product.py 3 4 2
24
```

9. The function `os.listdir` (see
   [docs](https://docs.python.org/2/library/os.html#os.listdir)) returns a
   list of the file and folder names in a given folder. Create a program that
   prints the names of all `.py` files in a given folder e.g.

```bash
$ ./lspy.py csv
zero_students2.py  zero_students3.py  zero_students.py
```

## Finished?

If you're happy with these you can move on to [data structures](../structures/).
