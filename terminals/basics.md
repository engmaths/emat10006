# Basics of Python

This unit is aimed at students who have seen Python before but are perhaps a
bit rusty with it. If you've never seen Python before or can't remember it
very well then I recommend to you to follow a more detailed tutorial such as
[the one at python.org](https://docs.python.org/3/tutorial/index.html). In
particular right now we want to make sure that we're fully up to date with
numbers, strings and lists. These are all described [in this page of the
python.org tutorial](https://docs.python.org/3/tutorial/introduction.html) so
read that unless you already know everything.

The `python.org` tutorial is aimed at the general Python programmer and our
target is scientific programming so we have a slightly different emphasis here
which is why I've written the following about numbers. We will also soon be
using multi-dimensional arrays so a good understanding of *slicing* is
essential. There are [exercises](#exercises) at the bottom to test your
understanding of both numbers and slicing.

## Numbers

Python has three basic numeric types: `int`, `float`, and `complex`. As you
can probably guess the `int` type is for integers. We create an object of type
`int` every time we have a decimal literal e.g. `1234`:

```python
>>> a = 12
>>> a + a
24
>>> a * 2
24
>>> a - 3
9
>>> a ** 2
144
>>> type(a)
<class 'int'>
>>> a / 2
6.0
>>> type(a / 2)
<class 'float'>
```

So we can do all the standard operations with `int` and we will generally get
back an `int` with the exception of *division* which gives an expression of type
`float`. We can see that it is a float because the number is shown with a `.0`
at the end.

Unusually among programming languages the standard `int` type in Python has
unlimited range: it can be used for arbitrarily large integers. So if you want
to know how many ways you can order a deck of cards then you can easily find
it:

```python
>>> import math
>>> math.factorial(52)
80658175170943878571660636856403766975289505440883277824000000000000
```

In most programming languages the basic integer type would overflow before
representing such large numbers. The `int` type can only do integers though so
we also have the `float` type:

```python
>>> b = 2.5
>>> b
2.5
>>> b * 2
5.0
>>> b / b
1.0
>>> c = 1e3
>>> c
1000.0
>>> import math
>>> math.sin(1.0)
0.8414709848078965
```

The `math` module provides standard mathematical functions mostly for working
with `float` numbers. You can read the documentation for [the math module
here](https://docs.python.org/3/library/math.html).

The `float` type represents non-integer number using [standard 64-bit IEEE 754
binary floating point](https://en.wikipedia.org/wiki/Double-precision_floating-point_format#IEEE_754_double-precision_binary_floating-point_format:_binary64)
as is standard in most modern programming languages. This floating point
format allows us to represent positive or negative numbers from roughly as
small as $10^{-300}$ to as big as $10^{300}$ with a precision of around 15
decimal digits.

You can see the effect of having (approximately) 15 digits of precision when
we get *additive underflow*:

```python
>>> 1e15
1000000000000000.0
>>> 1e15 + 1
1000000000000001.0
>>> 1e16
1e+16
>>> 1e16 + 1
1e+16
>>> 1e16 + 1 == 1e16
True
```

Likewise we also have conversion overflow/underflow:

```python
>>> 1e350
inf
>>> float(10**350)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
OverflowError: long int too large to convert to float
>>> 1e-350
0.0
```

Finally since we are using *binary* floating point some simple looking
non-integer numbers will not be represented exactly leading to sometimes
surprising results:

```python
>>> 0.01 + 0.11
0.12
>>> (0.12 - 0.01) - 0.11
0.0
>>> (0.12 - 0.11) - 0.01
-5.204170427930421e-18
```

These results are only surprising because it looks as if the numbers 0.01,
0.01, and 0.12 are represented exactly. In *binary* floating point there is
no possible way to represent these numbers exactly. We can see the *exact*
value represented by a `float` with e.g.:

```python
>>> import decimal
>>> print(decimal.Decimal(0.01))
0.01000000000000000020816681711721685132943093776702880859375
```

Finally we have the `complex` type which as you can imagine represents complex
numbers:

```python
>>> z = 1 + 1j
>>> z
(1+1j)
>>> z**z
2j
>>> z.real
1.0
>>> z.imag
1.0
>>> abs(z)
1.4142135623730951
```

The `complex` type represents complex numbers using a pair of floats for the
real and imaginary parts.

You can read more about Python's standard numeric types [in the
documentation](https://docs.python.org/3/library/stdtypes.html#typesnumeric).

## Strings

Strings are described in the [python.org
tutorial](https://docs.python.org/3/tutorial/introduction.html#strings) and
also the [official
docs](https://docs.python.org/3/library/stdtypes.html#textseq). I'm not going
to repeat that stuff here but I will mention a few things

String objects are an example of a *sequence* type. There are other sequence
types e.g. `list`, `tuple` that we shall see shortly. What this means is that
we can *index* and *slice* a string:

```python
>>> s = 'foobar'
>>> s[0]
'f'
>>> s[1]
'o'
>>> s[2]
'o'
>>> s[3]
'b'
>>> s[0:3]
'foo'
>>> s[3:]
'bar'
>>> s[-1]
'r'
>>> s[:-1]
'fooba'
>>> s[-2]
'a'
>>> s[::2]
'foa'
>>> s[::-1]
'raboof'
```

Slicing and indexing are critically important in Python and for us in this
unit in particular. You need to make sure that you understand each of the
expressions above perfectly (see also the [exercises](#exercises) below).

Like most other sequence types strings can be added or multiplied:

```python
>>> s
'foobar'
>>> s + s
'foobarfoobar'
>>> 3*s
'foobarfoobarfoobar'
```

We can also use the special `in` operator to test if a string contains a
*substring*:

```python
>>> 'foo' in 'foobar'
True
>>> 'arf' in 'foobar'
False
>>> 'arf' in 2*'foobar'
True
```

Strings also have a number of methods such as `.startswith`, `.upper` etc.
There is plenty more information about strings in [the
docs](https://docs.python.org/3/library/stdtypes.html#textseq) but you can
also get a list of string methods and query each one using the built-in help
function of the interpreter:

```python
>>> dir(str)
['__add__', '__class__', '__contains__', '__delattr__', '__doc__', '__eq__',
'__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__',
'__gt__', '__hash__', '__init__', '__iter__', '__le__', '__len__', '__lt__',
'__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__',
'__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__',
'__subclasshook__', 'capitalize', 'center', 'count', 'encode', 'endswith',
'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha',
'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable',
'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip',
'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition',
'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase',
'title', 'translate', 'upper', 'zfill']
```

To query a method e.g. the `.startswith` method you can call `help` on it.
The `help` function will open a help page in the terminal showing:

```python
>>> help(str.startswith)
Help on method_descriptor:

startswith(...)
    S.startswith(prefix[, start[, end]]) -> bool
    
    Return True if S starts with the specified prefix, False otherwise.
    With optional start, test S beginning at that position.
    With optional end, stop comparing S at that position.
    prefix can also be a tuple of strings to try.
```

(press `q` to exit the help screen)

This kind of help is sometimes more useful when you just need reminding about
a method/function than when you've never seen it before. In this case a google
would probably give a better introductory explanation. A more
straight-forward version is that the `.startswith` method is used to find
out whether or not a string *starts with* another string:

```python
>>> s
'foobar'
>>> s.startswith('foo')
True
>>> s.startswith('bar')
False
>>> 'bar' in s
True
```

As the `'bar'` example shows this is not the same as using the `in` operator -
the `.startswith` method was introduced to discourage programmers from
incorrectly using `in` like this.

## Exercises

1. Explain what happens here:

```python
>>> (1 + 1e-15)
1.000000000000001
>>> (1 + 1e-15)-1e-15
1.0
>>> x = 1
>>> y = 1e-16
>>> x + y
1.0
>>> x + y == x
True
>>> (x + y) - y
0.9999999999999999
>>> x + (y - y)
1.0
```

2. What about this?

```python
>>> x = 10**16
>>> x + 1 == x
False
>>> x
10000000000000000
>>> x + 1
10000000000000001
>>> x + 1 == x
False
>>> y = 1e16
>>> y
1e+16
>>> y + 1
1e+16
>>> y + 1 == y
True
```

3. Find the smallest integer that cannot be represented exactly as a `float`.

4. Given a `list` (or `string`) what expression gives a `list` (or `string`)
   containing the first 5 elements of the `list`?

5. How can you get all elements *after* the first 5 elements of a `list`?

6. How about the *last* 5 elements of the `list`?

7. How would you get only the even indexed elements of a list?

8. How can you convert a number to a string (or a string to a number)?

## Finished?

If you're happy with these you can move on to [loops, conditionals and
functions](../basics2/).
