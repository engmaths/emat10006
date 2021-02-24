@def title = "Functions, exceptions and testing"

# Functions, exceptions and testing

This worksheet is about writing functions, using exceptions and also testing
your code with `pytest`.

## Functions

The first part of this worksheet is about reading and critical reflection. I'm
assuming that you've already read [functions](../functions). I'm also assuming
that you have written some code in the past e.g. for a previous project.

It is often said among programmers that code is "read more often than it is
written". The point is that you should put effort into making code readable
even if that takes a small amount of extra time when you are writing the code.
That time will be repaid many times later when you end up having to read the
code. A strange thing happens when programming though: it is quite easy to
write code that makes sense to you in the exact moment that you are writing it
but is actually impossible to understand. The code might "work" but a future
reader (including you in a month's time) might have no chance of being able to
understand it.

You might say that as long as the code works it doesn't matter if any human
can understand it but that makes it impossible to improve the code later. It's
also impossible to fix bugs or take pieces of the code and reuse them for
other things if no one understands it any more. Most importantly if you are a
beginner at programming: if you learn how to write readable code then it is
not much harder than writing unreadable code. This is a skill that once
mastered means that everything you produce is naturally better.

**Exercise**: go back over the code that you have written in the past and
consider the following:

* Have you been using functions in your code?
* Are there places where your code is repetitive that would benefit from using
  functions?
* What names have you given your functions?
   * Do your functions names convey any meaning?
   * Can you understand what your functions do from their names and the way
     that they are used without needing to look at the code inside the
     functions?
   * What kinds of words are you using for your function names? Are they nouns,
     verbs, adjectives...?
* Are your functions pure or not? Have you been cleanly separating input,
  output and pure functions?
* Can you actually understand your own code that you wrote some time ago? If
  you show it to someone else can they understand it?
* Do any of your functions look like a piece of code that could ever be reused
  as part of a future programming project?


## Testing

**Note**: You will need to have `pytest` installed to follow through the
examples here. If you installed Python using Anaconda then you should already
have `pytest` installed. If your `$PATH` is set up correctly you should be
able to run `pytest` in the terminal. The output looks something like this:
```
$ pytest
====================================================== test session starts =======================================================
platform darwin -- Python 3.8.5, pytest-6.2.0, py-1.10.0, pluggy-0.13.1
rootdir: /Users/enojb/current/sympy/sympy, configfile: pytest.ini
plugins: instafail-0.4.2, xdist-2.1.0, cov-2.10.1, doctestplus-0.8.0, forked-1.3.0
collected 0 items
```
If the `pytest` command does not work but you do have `pytest` installed then
one of the following should work:
```
$ python -m pytest
$ python3 -m pytest
$ py -m pytest
```
If you need to install `pytest` then you might be able to install it with
```
$ python -m pip install pytest
```

# Using pytest

The `pytest` library is for [unit
testing](https://en.wikipedia.org/wiki/Unit_testing). It is used to run tests
that check if code works correctly. The documentation for `pytest` is
[here](https://docs.pytest.org/en/stable/).

To use `pytest` we just need to put some functions with names that begin with
`test_` in our Python file. Here's a simple example of a Python script with a
function that is tested with `pytest`:
```python
# square.py

def square(x):
    """Returns the square of x"""
    return x * x

def test_square():
    assert square(0) == 0
    assert square(2) == 4
    assert square(-2) == 4
```
If you save that code in a file `square.py` then you can use `pytest` to run
the tests in the `test_square` function that check that the `square` function
is working correctly:
```console
$ pytest square.py
============================================ test session starts =============================================
platform darwin -- Python 3.8.5, pytest-6.2.0, py-1.10.0, pluggy-0.13.1
rootdir: /Users/enojb/current/emat10006/materials
plugins: instafail-0.4.2, xdist-2.1.0, cov-2.10.1, doctestplus-0.8.0, forked-1.3.0
collected 1 item

square.py .                                                                                             [100%]

============================================= 1 passed in 0.02s ==============================================
```
The key part of the output here is "1 passed" which means that 1 test was run
and it passed as expected.

Now put this into a file called `cube.py`:
```python
# cube.py

def cube(x):
    """Returns the cube of x"""
    return 0  # <--- This obviously doesn't work correctly

def test_square():
    assert cube(0) == 0
    assert cube(2) == 8
    assert cube(-2) == 8
```
This time we have a function `cube` that does not actually work because it
always returns 0 instead of computing $x^3$. If we run `pytest` now then it
the tests will fail:
```console
$ pytest cube.py
============================================ test session starts =============================================
platform darwin -- Python 3.8.5, pytest-6.2.0, py-1.10.0, pluggy-0.13.1
rootdir: /Users/enojb/current/emat10006/materials
plugins: instafail-0.4.2, xdist-2.1.0, cov-2.10.1, doctestplus-0.8.0, forked-1.3.0
collected 1 item

cube.py F                                                                                              [100%]

================================================== FAILURES ==================================================
________________________________________________ test_square _________________________________________________

    def test_square():
        assert cube(0) == 0
>       assert cube(2) == 8
E       assert 0 == 8
E        +  where 0 = cube(2)

cube.py:9: AssertionError
========================================== short test summary info ===========================================
FAILED cube.py::test_square - assert 0 == 8
============================================= 1 failed in 0.19s ==============================================
```
Now `pytest` shows that the tests have failed. It says "1 failed" meaning that
1 test was run and it failed.

**Exercise**: Fix the cube function so that it works and so that `pytest`
shows the tests passing.


# Test driven development

The idea of test driven development (TDD) is that the process of writing code
takes place like this:

1. Decide what functions you will have in your program.
2. Write tests for those functions
3. Write the code for the functions
4. Check that the tests pass

If the tests represent a good check in the correctness of the code then this
should mean that your code is now correct. The key part now is what happens if
you later want to make changes to the code. For example if you think that the
code is correct but it runs slowly and you want to to improve it then you can
rewrite the code. If it then runs faster and still passes the tests then that
can reassure you that it is still correct after the changes.

If you discover a bug in your code that means it gives incorrect output then
the procedure is:

1. Add a test for the bug and verify that the test fails.
2. Fix the code so that the tests pass again.

In this way every time a bug is discovered more tests are added. Any future
change to the code will need to pass all the tests that were ever added.

Here's an example Python file that has a bug:
```python
# det.py

def determinant(M):
    """Compute the determinant of a square matrix M

    The input matrix should be given as a list of lists.

    >>> M = [[1, 2], [3, 4]]
    >>> determinant(M)
    -1
    """
    # M is an NxN matrix
    N = len(M)

    if N == 2:
        # Handle 2x2 as the base case
        [[a, b], [c, d]] = M
        return a*d - b*c
    else:
        # Recurse using Laplace expansion for 3x3 or larger
        det = 0
        for j in range(N):
            det += (-1)**j * M[0][j] * determinant(minor(M, 0, j))
        return det


def minor(M, i, j):
    """Get the (i, j) minor of the matrix M

    The (i, j) minor of M is the matrix formed by removing the ith row and jth
    column from M.

    >>> minor([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 0, 1)
    [[4, 6], [7, 9]]
    """
    # Remove the ith row and jth column
    return [Mi[:j] + Mi[j+1:] for Mi in M[:i] + M[i+1:]]


def test_determinant():
    assert determinant([[1, 2], [3, 4]]) == -2
    assert determinant([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == 0
    assert determinant([[1, 2, 3], [4, 5, 6], [7, 8, 10]]) == -3
```
The first bug here is that the `determinant` function does not correctly
handle `1x1` or `0x0` matrices correctly e.g.:
```python
>>> determinant([[2]])  # should be 2
0
>>> determinant([])     # should be 1
0
```
The determinant of a $1 \times 1$ matrix should just be the entry of the
matrix! The determinant of a $0 \times 0$ matrix is tricky but in fact it
should always be 1.

**Exercise**: Add tests for $1 \times 1$ and $0 \times 0$ matrices. Fix the
`determinant` function so that it works for those cases as well.

**Exercise**: Add tests for the `minor` function.

Try running the tests with the `--doctest-modules` argument. You should see
this:
```console
$ pytest --doctest-modules det.py 
============================================ test session starts =============================================
platform darwin -- Python 3.8.5, pytest-6.2.0, py-1.10.0, pluggy-0.13.1
rootdir: /Users/enojb/current/emat10006/materials
plugins: instafail-0.4.2, xdist-2.1.0, cov-2.10.1, doctestplus-0.8.0, forked-1.3.0
collected 3 items                                                                                            

det.py F..                                                                                             [100%]

================================================== FAILURES ==================================================
_________________________________________ [doctest] det.determinant __________________________________________
002 Compute the determinant of a square matrix M
003 
004     The input matrix should be given as a list of lists.
005 
006     >>> M = [[1, 2], [3, 4]]
007     >>> determinant(M)
Expected:
    -1
Got:
    -2

/Users/enojb/current/emat10006/materials/det.py:7: DocTestFailure
========================================== short test summary info ===========================================
FAILED det.py::det.determinant
======================================== 1 failed, 2 passed in 0.04s =========================================
```
Now `pytest` is testing the examples shown in the docstring and the example is
clearly incorrect!

**Exercise**: Fix the doctest example in the `determinant` docstring. Verify
that the tests pass.


## Polynomials

The final exercise in this sheet is to make a program that can find integer
roots of polynomials that have integer coefficients. The basic program can be
found [here](roots.py). When working the program behaves like this:
```console
$ python roots.py 1 -5 6
2
3
```
This is showing that the roots of $x^2 - 5x + 6$ are $2$ and $3$.

**Exercise**: Download the `roots.py` script and run `pytest` on it. Three
functions need to be implemented:
* The `evaluate_polynomial(p, x)` function calculates the value of the
  polynomial $p(x)$ at `x`. For example `evaluate_polynomial([1, 2, 1], 3)`
  calculates $p(3)$ where $p(x) = x^2 + 2x + 1$:

      >>> evaluate_polynomial([1, 2, 1], 3)
      16

  There are many ways to implement this but the most efficient is to use
  [Horner's method](https://en.wikipedia.org/wiki/Horner%27s_method).
* The `is_root(p, x)` function returns True if `x` is a root of $p(x)$ e.g.

      >>> is_root([1, 2, 1], 3)
      False

  This is because $3$ is not a root of $x^2 + 2x + 1$. It's easy to check if
  `x` is a root of `p`: we just calculate $p(x)$ and see if it gives zero.
* The `integer_roots(p)` function returns the integer roots of the polynomial
  $p(x)$. This works using the [rational root
  theorem](https://en.wikipedia.org/wiki/Rational_root_theorem). A simple
  observation is that given e.g. a polynomial $ax^3 + bx^2 + cx + d$ then any
  integer root must satisfy $|x| \le |d|$. So if for example $d$ is 4 then the
  only possibilities for integer roots are $\{-4,-3,-2,-1,0,1,2,3,4\}$. We can
  test each of these possibilities in a loop to see if any is a root (using
  the `is_root` function).
* Some of the tests check that a particular exception is being raised by a
  function for particular inputs. To make those tests pass you will need to
  add `raise BadPolynomialError` in those functions.

See the tests for more examples. Add the code for those functions so that the
tests pass. Some of the tests use the `pyest` function `raises`. This is used
to check that calling the function with those arguments raises a particular
error. You will need to test for those cases and use something like
```
raise BadPolynomialError("Polynomial should be a list of coefficients")
```

The final program should be able to find the integer roots of a
polynomial when run from the command line.
