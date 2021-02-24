@def title = "Exceptions"

# Exceptions and tracebacks

## What is an exception

Programming languages like Python have the use of exceptions as an alternative
method of flow control. Most functions will have the possibility of
exceptional cases where they can not return something meaningful. For example
a `sqrt` function that is expected to return a real number will not be able to
return a correct real number when given a negative input. In programming
languages that don't have exceptions it is common to use a special return
value to indicate a failure:

```python
def isqrt(y):
    """Compute the integer square root of y.

    The *integer* square root of y is defined as the largest positive integer
    x such that x**2 <= y. In other words it is the square root rounded down.

    Returns -1 if the input was negative.
    """
    # Check input is a positive integer. Otherwise return -1 to indicate an
    # error
    if y < 0 or int(y) != y:
        return -1

    # Integer square root algorithm based on Newton-Raphson
    # Uses only integer arithmetic. Note that // is integer floor division.
    x = y
    while x**2 > y:
        x = (x + y//x) // 2
    return x


number = int(input("Please enter a positive integer:"))

square_root = isqrt(number)

# isqrt returns -1 to indicate an error:
if square_root == -1:
    print("Please enter a valid positive integer!")
else:
    print("Integer square root of", number, "is", square_root)
```

Using return values to indicate a failure can be awkward when there are many
functions that call each other  e.g.:
```python
def func1(x):
    result = func2(x)
    if result == -1:
        # handle error
    else:
        # do something useful

def func2(x):
    result = func3(x)
    if result == -1:
        # handle error
    else:
        # do something useful

def func3(x):
    result = func4(x)
    if result == -1:
        # handle error
    else:
        # do something useful

# And so on
```
Here because each function returns a special value to indicate a failure we
see that to handle the failure robustly we have to check for the special
failure value every time we call any of the functions. This is in fact
necessary in many programming languages but not in Python because we can use
exceptions. We can raise an exception using the `raise` statement like this:
```python
# raise.py

def func1(x):
    result = func2(x)
    # do something useful

def func2(x):
    result = func3(x)
    # do something useful

def func3(x):
    result = func4(x)
    # do something useful

def func4(x):
    if x < 0:
        raise ValueError("Negative numbers are not allowed!")
    # do something useful

value = func1(-10)
```
If we run the above we see:
```console
$ python raise.py
Traceback (most recent call last):
  File "raise.py", line 20, in <module>
    value = func1(-10)
  File "raise.py", line 4, in func1
    result = func2(x)
  File "raise.py", line 8, in func2
    result = func3(x)
  File "raise.py", line 12, in func3
    result = func4(x)
  File "raise.py", line 17, in func4
    raise ValueError("Negative numbers are not allowed!")
ValueError: Negative numbers are not allowed!
```
At the moment when the exception is raised execution is in `func4` which is
being called by `func3` which is being called by `func2` and so on. The
`raise` statement causes all of the functions to stop and none of them returns
any value. The default behaviour here is for the interpreter to crash out of
the program and print the traceback which is the error message that you can
see as output. This is useful because it means that none of the functions
`func1`, `func2` etc needs to check the output for a special error values like
`-1`. Instead each function simply calls the other function and presumes that
it succeeds. If there is a problem then the exception is raised and all
functions are cancelled.

For simple scripts this is a reasonable way of handling error cases: if
anything goes wrong the whole program aborts and prints our an error message.

## Tracebacks

Let's take another look at the "traceback"  output from Python:
```
$ python raise.py
Traceback (most recent call last):
  File "raise.py", line 20, in <module>
    value = func1(-10)
  File "raise.py", line 4, in func1
    result = func2(x)
  File "raise.py", line 8, in func2
    result = func3(x)
  File "raise.py", line 12, in func3
    result = func4(x)
  File "raise.py", line 17, in func4
    raise ValueError("Negative numbers are not allowed!")
ValueError: Negative numbers are not allowed!
```
You will have likely seen this kind of output when writing your own code. It
is worth noting how useful the information in the traceback is. It tells us
that at the moment the error was detected execution was at line 20 of the file
`raise.py` which was calling `func1` (at line 4 of `raise.py`) which was
calling `func2` etc. It also shows us the lines of code that were being
executed and shows us the exact line that raised the error (line 17 in
`func4`). This is very useful when you are writing your code and it does not
yet work because it shows you exactly where to look in your code to see what
the problem might be. If you have thousands of lines of code knowing exactly
where to look is extremely helpful.

## Catching exceptions

We can also prevent our program from crashing out by "catching" the exception
that was "raised". For this we use `try/except` like this:
```python
# catch.py

def func1(x):
    if x < 0:
        raise ValueError("Negative numbers not allowed")
    return x**2

try:
    result = func1(-3)
except ValueError:
    # This line is executed if the exception was raised:
    print("An error was found")
else:
    # This line is executed if an exception was not raised:
    print("the result is", result)
```
Now because we catch the exception using `except` our program does not crash.
Instead when we run the above program we will see:
```console
$ python catch.py
An error was found
```
It is tempting to use `try/except` like this so that you get a "nice" error
message rather than the nasty looking traceback that Python prints out be
default. Note though how much less useful this output is for identifying a
problem in your code: the traceback has much more information about what the
problem might be!

## Types of exceptions

There are many different types of exceptions such as `ValueError`,
`TypeError`, `OSError`. You can find a more complete list here:
<https://docs.python.org/3/library/exceptions.html>

Both the `raise` and `except` statements specify the type of exception to be
raised or caught and these have to match or the exception will not be caught.
For example if you `raise ValueError()` and then try to catch with `except
Typerror` then exception will not be caught. The program will crash out and
print the traceback just as if you had not used `try/except`.

A type of exception is a class and specifically it should be a subclass of
`Exception`. We can define our own kind of exception like this:
```python
# exception.py

class NegativeException(Exception):
    """Raised when input was negatve"""
    pass

def func1(x):
    if x < 0:
        raise NegativeException("Need positive number!")
    return x**2

try:
    result = func1(-10)
except NegativeException:
    print("We found a negative number")
else:
    print(result)
```
It is generally good practice to use a new exception type rather than reusing
the standard exception types to make sure that you don't catch the wrong
exception. Many bugs in your own code will lead to exceptions like
`ValueError` being raised and you want to be able to see the useful traceback
and error messages so that you can fix those bugs.
