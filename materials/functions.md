@def title = "Functions"

# Functions

## What is a function?

Mathematically we understand the idea of a function like $f(x) = x^2$. Here a
function associates each element of the "input" set with an element from the
"output" set, like $f(2) = 4$ or $f(3) = 9$. In Python we can create functions
like this as well:
```python
def square(x):
    return x**2

y = square(3)

print(y)  # prints 9
```
In the mathematical concept of a function all that matters is its "output".
However in programming we have a different concept of a function where the
function can also *do* things. The statements in the function are *executed*
and can have effects e.g.:
```python
def show_information():
    print("Important information")

show_information()  # prints output
```
Here the function has no inputs or outputs. When we "call" the function
information is printed out on the screen. A function like this with no
"output" is obviously not like the mathematical concept of a function. In some
programming languages this kind of function has a different name and is known
as a "procedure" or "subroutine". However in Python these are all just
functions. A function that does not return anything is just considered to be a
function that returns the special value `None` e.g.:
```python
>>> z = show_information()
Important information
>>> print(z)
None
```
So the definition of a function in Python is really just that it is:

* A named block of code that can be called from elsewhere
* Has one or more parameters ("inputs")
* Returns a value (possibly `None`) or raises an exception

(We will discuss exceptions later)

## Why functions?

There are several reasons why functions are good:

* Modularisation: break up program into small pieces
* Good function names improve readability
* Reuse code
* Don't repeat yourself (DRY)
* One place to fix bugs
* Separation of concerns

Let's consider each of these ideas in turn

## Example

Using functions makes it possible to break a large program into small pieces
that are easier to understand separately. If I have a 1000 line program and
there is a bug in the output of the function called `square` I know that I
only need to look at the function `square` and any other functions it calls. I
should not need to look through all of the code to find the problem.

Breaking up parts of the program into functions also makes it possible to give
each part a name and well-defined expected behaviour. Here is some code that
calculates the factorial of `x`:
```python
x = 3

xfact = 1
while x != 0:
    xfact *= x
    x -= 1

print(xfact)
```
At the end of this loop `xfact` will be equal to the factorial of `x`. However
if you saw that code on its own would you understand what it was?

We can put this code into a function to make the intention clearer:
```python
def factorial(x):
    """Computes x! for any nonnegative integer x"""
    xfact = 1
    while x != 0:
        xfact *= x
        x -= 1
    return xfact

x = 3
xfact = factorial(x)
print(xfact  # prints 6
```
Now that we have a function we can give it a name. Hopefully someone who sees
`xfact = factorial(x)` will know what that means without needing to actually
go and look at the code *inside* the function. That makes the code that *uses*
the function simpler and clearer.

**NOTE** It's important to focus on this point. The big advantage of using a
function is that it makes the code easier to understand at the point where the
function is *called*.

If someone does go to look at the code for the `factorial` function then they
will see that its scope is clearly defined: it is for integers and they must
not be negative. In fact if you try the function above with `factorial(-1)`
it will go into an infinite loop (use Ctrl-C to interrupt Python from an
infinite loop).

Going into an infinite loop is not nice so we might try to improve that but
the main point is that we should be clear what each function is designed for
and what is intended to do. Here if someone writes `factorial(-1)` then we can
say that it is a mistake to do that because the function is not designed for
negative inputs.

Compartmentalising the code in this way makes it possible to explain what each
part is for, what it does and how it should be used.


## DRY: Don't repeat yourself

The DRY acronym is used often by programmers. The idea is that if you have the
same code in multiple places throughout your program then problems can emerge.
Let's consider an example:
```
x = 3
xfact = 1
while x != 0:
    xfact *= x
    x -= 1

z = 5
zfact = 1
while z != 0:
    zfact *= z
    z -= 1
```
Here I've copied the same code twice because I wanted to do the same thing
twice. Now though what happens if I find a bug in that code? I will have to
fix the bug in two places. That doesn't sound so hard except that I might not
know all the places where the same code is being used throughout my codebase.
If there is a bug in a function then I know that there will be only one place
where that function is defined. I can fix the bug there and then all the
places that call the function will get fixed at the same time.

Clearly it would be much nicer to have a function and do:
```python
x = 3
xfact = factorial(x)
z = 5
zfact = factorial(z)
```
Another point is that it is easier to check whether or not a function has a
bug then it is for an arbitrary block of code. I can just call the function
with different inputs:
```python
>>> factorial(3)
6
>>> factorial(4)
24
>>> factorial(2)
2
>>> factorial(1)
1
>>> factorial(0)
1
```
A pure function like this is defined only by what its inputs and outputs are.
Nothing else needs to be considered.


## Types of functions

The simplest kind of function to reason about is a function like `factorial`
above which is a *pure* function. We say that a function is pure if

* It will always return the same output when given the same input.
* Calling the function has no observable effect apart from returning the
  output.

An example of a non-pure function would be the `show_information` function
that I referred to above. Since that prints information on the screen it has
an observable effect. If we were to call the function twice then it would
result in the message being printed twice. With a pure function I never need
to call it more than once with the same inputs.

An example of a function that gives different outputs for the same inputs
would be the `time` function. This function returns the current time as a
number of seconds since Jan 1st 1970:
```python
>>> from time import time
>>> time()
1613506295.333666
>>> time()
1613506296.163819
```
This is not a pure function since I can call it with the "same" inputs (it has
no inputs) but I get different values as output. This kind of function is also
more complicated to use. You have to think about exactly where in your program
you want to call this function because it would e.g. give a different value at
the beginning of your program than if it was called at the end.

It is not possible to use only pure functions throughout a programme but you
should try to put as much code as possible into pure functions. Of course
every programme will need to have some output (e.g. printing to the screen)
and that can not happen in a pure function. Generally it makes sense to
separate the functions in your program into:

* Input functions
* Output functions
* Pure functions

Here's a simple program showing this separation:
```python
# The main function often has to mix input and output
def main(infile, outfile):
    """
    Read numbers from infile, double them and write the results to outfile.
    """
    # input
    numbers = read_input_file(infile)
    # processing
    numbers = double(numbers)
    # output
    write_output_file(outfile, numbers)

# input function
def read_input_file(filename):
    with open(filename) as inputfile:
        numbers = [int(line) for line in inputfile]
    return numbers

# output function
def write_output_file(filename, numbers):
    with open(filename, 'w') as outputfile:
        for number in numbers:
            outputfile.write(str(number) + '\n')

# pure function
def double_numbers(numbers):
    return [2*number for number in numbers]


if __name__ == "__main__":
    import sys
    args = sys.argv[1:]
    main(*args)
```

## Naming functions

Function names should be considered carefully. Coming up with good names is
hard in general but it is something that can improve your code more than
anything else. The most important thing to think about a function name is
whether someone will be able to understand what it does when looking at the
function call:
```python
# Call func1
var1 = func1(var2)
```
Can you understand what that line of code does? Of course not! The variable
names `var1` and `var2` could refer to anything. The function name `func1`
suggests that `func1` is a function but otherwise tells us nothing about what
it does or what it returns or why it would be used.

Now try reading this:
```python
# All components are equally weighted
unit_mark = average(component_marks)
```
Can you understand what this line of code does? It is at least possible with
good variable and function names to extract some meaning from the code. Try
reading your code out load: "unit marks equals average of component marks"
reads almost like a meaningful sentence in English.

Another point to note is about the way that comments can improve the
readability of your code. Comments should not be used to make up for poorly
written code:
```python
# x is the name and y is the number
x = f(y)
```
Rather than a comment give these better names and use comments to explain
something that is important but not obvious from the code itself:
```
# Preferred name (not the legal name)
name = get_customer_name(customer_number)
```

## Style of function names

The convention in Python is to used snake-case for function names e.g.
`get_customer_name` rather than `getCustomerName` as is used in some other
languages. In general function names should be long unless the function is
very common. Core functions in a programming language often have short names
because they are used a lot. For example we have names like `print`, `sum`,
`len`, `str`, `int` etc. It makes sense to make these names short because:

* Everyone knows these functions (every Python programmer has to learn them)
* These functions are used a lot so giving them long names would make our code
  verbose.

However these conditions are almost never met by a function that *you* will
write in e.g. a student project. If a function only exists in one program and
is only called in one or two places then it should definitely have a name that
is long enough to make it clear what the function is doing.

It's also important to think about the name grammatically:

* Function names can be nouns like `sum` which returns "the sum"  of its
  inputs:

      >>> numbers = [1, 2, 3]
      >>> sum(numbers)
      6

* Function names can be verbs like `print` which prints its inputs to the
  screen.

      >>> print("hello")
      hello

  where the function name is a verb it should usually be in the imperative
  tense. It is a command from you the programmer to the computer so it should
  be `print` and *not* `prints` or `printing`.

* Function names can also be adjectives consider the difference here:

      >>> mylist = [3, 2, 1]
      >>> mylist.sort()
      >>> mylist
      [1, 2, 3]
      >>> mylist2 = sorted(mylist)

  The `sort` method of lists sorts the list in place and does not return
  anything. It is therefore an action so we command the list to "sort" itself
  in the imperative tense. The `sorted` function returns a "sorted" version of
  the input list. The adjective `sorted` describes the object that is
  returned.

* Function names can be questions. It is common to make functions that return
  only either `True` or `False`. Such functions are very useful and the
  convention is to give them a name that resembles a question like:

      def is_positive(x):
          """True if x is positive, False otherwise"""
          if x > 0:
              return True
          else:
              return False

  Here we read this as "is x positive"? Other question names can begin with
  other words like `has_values`, `can_compute` and many more.


## Docstrings

When writing a function it is good practice to write a docstring. This is a
string, usually written with triple quotes `"""` that is immediately after the
function signature. This is used to

* explain what the function does
* explain what its parameters are
* explain what it returns
* show examples of usage

Example:
```
def average(numbers):
    """Returns average of numbers

    >>> average([1, 2, 3])
    2.0

    Parameters
        numbers: a list of numbers (e.g. `int` or `float`)
    Returns
        average: mean of the numbers
    """
    return sum(numbers) / len(numbers)
```
In real code it is quote common to have a docstring that is longer than the
actual code in the function itself. If the docstring is well written then it
should not be necessary to look at the actual code in order to understand what
the function does and how to use it. An example of usage showing both input
and output is extremely useful for helping someone to understand how to use
it.


# Exceptions

Sometimes it isn't possible for a function to return anything reasonable given
the inputs e.g. `factorial(-1)` or `int("qwe")`. Let's see what happens:
```python
>>> number_string = "123"
>>> number = int(number_string)
>>> number
123
>>> number_string = "hello"
>>> number = int(number_string)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: 'hello'
```
Here we use the `int` "function" to convert a string of digits into an
integer. However if we pass in a string like `"hello"` then it isn't possible
for `int` to return anything reasonable. It could return e.g. `None` but then
we would have to check whether it returns `None` every time we call it e.g.:
```python
number = int(number_string)
if number is None:
    print('Bad input')
else:
    # do something useful
```
We don't have to check because instead `int` refuses to return anything. It
raises an exception instead. In this case the exception is of a particular
type `ValueError` indicating that an incorrect value was passed to the
function. This is useful because it means that we can write code that doesn't
check the output of `int(number_string)`: it either returns a valid integer or
it raises an exception.

The exception stops our program altogether. If we do want to catch the
exception then we can do that with `try/except` e.g.:
```python
while True:
    # Ask the user to type in a string
    string = input('Enter a number: ')
    try:
        number = int(string)
    except ValueError:
        print('That is not a number!')
        continue  # goes back to the start of the loop
    # If we got here then no exception was raised.
    # Now number is a valid integer so exit the loop
    break
```
Usually though it is better not to catch exceptions like this. Just let the
program crash! The exception is either because of a bug in your code or
because your program has been run with invalid input. The simplest way to
handle that is just for the program to crash and the error message to be
printed out.

While I would caution against trying to catch exceptions most of the time it
is definitely good to raise exceptions for bad inputs. We can do that with
`raise`. Let's use that to improve the `factorial` function:
```python
def factorial(x):
    """Computes x! for any nonnegative integer x"""
    if not isinstance(x, int):
        raise TypeError("x should be of type int")
    if x < 0:
        raise ValueError("x should be nonnegative")
    xfact = 1
    while x != 0:
        xfact *= x
        x -= 1
    return xfact
```
Now if we try to compute `factorial(-1)` we will see:
```python
>>> factorial(-1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "t.py", line 6, in factorial
    raise ValueError("x should be nonnegative")
ValueError: x should be nonnegative
```
An immediate error message is much nicer than an infinite loop!

What is printed out with the `ValueError` is called the "stack trace". It
shows what functions were being called when the error occurred. It shows that
the error is raised from line 6 of the file `t.py` in the `factorial`
function. This is useful information that allows me to investigate the cause
of an error message like this if my program crashes.
