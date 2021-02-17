@def title = "Functions, exceptions and testing"

# Functions, exceptions and testing

## Functions in a script

```python
# myscript.py

def double(thing):
    """Doubles the thing"""
    return thing + thing

print(double(2))
print(double([1, 2]))
print(double("foo"))
```

Run in the terminal:

```shell
$ python myscript.py
4
[1, 2, 1, 2]
'foofoo'
```

## Functions in a module

```python
# mymodule.py

def double(thing):
    """Doubles the thing"""
    return thing + thing
```

Run in the *Python* shell:

```python
>>> from mymodule import double
>>> double(4)
8
```

## Why functions

* Break up program into small pieces
* Good function names improve readability
* Reuse code
* Don't repeat yourself (DRY)
* One place to fix bugs


## Case study: datetime module

Python stdlib datetime module:
<https://github.com/python/cpython/blob/master/Lib/datetime.py>

- 2500 lines of code for the module in total
- Almost all code is in functions (and methods)
- Around 200 functions total
- Average function length is less than 10 lines!
- Lots of comments and docstrings for explanation


## Function naming

* Python convention is snake case: `some_function_name()`
* Variable and function names can explain code
* Think about the name in the context of where the function will be *called*.
* Use a leading underscore for internal functions e.g. `_is_leap()`
* Comments should explain non-obvious things


## Function behaviour

Pure function:

* Always returns the same value given the same input arguments
* Does not have any other "side effects"

Example:
* `sum` is a pure function
* `print` is not (side effects)
* `time` is not (gives different values)


## Categorising functions:

Input/output functions are never pure

* Input functions (e.g. read from file)
* Output functions (e.g. print to screen)
* Pure functions

Every programme needs to have some inputs and outputs but you should try to
put as much as possible of the code in pure functions.


## Function names and grammar

* Name the function with a verb (imperative tense):
   * `print(obj)`
   * `load(filename)`
   * `mylist.sort()`

* Name the function with a noun (describe the return value)
   * `min(numbers)`
   * `len(mylist)`

* An adjective
   * `sorted(mylist)`
   * `mystring.upper()`

* Or a question?
   * `is_leap_year()`
   * `has_key()`


## Length of function names

* Functions that are used a lot can have short names e.g. `len`, `sum` etc.
* Some conventions for shortening are well known e.g. `num_people` for
  `number_of_people`.
* Otherwise prefer longer and more explicit names.


## Good names

Compare these:
```python
# Call func1
var1 = func1(var2)
```
```python
# All components are equally weighted
unit_mark = mean(component_marks)
```
Can you understand what is happening in each example?



## Raising exceptions

```python
def get_first_name(student_number):
    """Return first name of the student with this student number"""

    if student_number not in registered_students:
        raise ValueError("No such student registered %s" % student_number)

    details = registered_students[student_number]
    return details['firstname']
```

Use exceptions when it is not possible to return something sensible


## Seeing Exceptions

```python
>>> x = 2
>>> x.upper()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'int' object has no attribute 'upper'
>>> 2 + [3]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'int' and 'list'
```

## Traceback

```python
>>> import subprocess
>>> subprocess.run('foo')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File ".../lib/python3.8/subprocess.py", line 489, in run
    with Popen(*popenargs, **kwargs) as process:
  File ".../lib/python3.8/subprocess.py", line 854, in __init__
    self._execute_child(args, executable, preexec_fn, close_fds,
  File ".../lib/python3.8/subprocess.py", line 1702, in _execute_child
    raise child_exception_type(errno_num, err_msg, err_filename)
FileNotFoundError: [Errno 2] No such file or directory: 'foo'
```


## Traceback demo

Demo...

Make sure you read the traceback!


## Catching exceptions

```python
number_string = input("Please enter a number: ")
try:
    number = int(number_string)
except ValueError:
    print("Not a valid number. Found '%s'" % number_string)
```

* Catch exception to handle failure (if expected!)
* Usually best not to catch the exception
* Catch *only* the exception you expect
