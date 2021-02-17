#!/usr/bin/env python
#
# Author: Oscar Benjamin
# Date: Feb 2021
# Description:
#   Command line script to find integer roots of polynomials with
#   integer coefficients.


#-------------------------------------------------------------------#
#                                                                   #
#                   Command-line interface                          #
#                                                                   #
#-------------------------------------------------------------------#

PROGRAM_EXPLANATION = """
Usage:
$ python roots.py COEFF1 COEFF2 ...

Find integer roots of a polynomial with integer coefficients.

Example:

Find the roots of x^4 - 3x^3 - 75x^2 + 475x - 750.

$ python roots.py 1 -3 -75 475 -750
-10
3
5
"""


def main(*arguments):
    """Main entry point for the program"""
    if not arguments:
        print(PROGRAM_EXPLANATION)
        return

    poly = parse_coefficients(arguments)
    roots = integer_roots(poly)
    print_roots(roots)


def parse_coefficients(arguments):
    """Convert string arguments to integer

    >>> parse_coefficients(["2", "3"])
    [2, 3]
    """
    return [int(arg) for arg in arguments]


def print_roots(roots):
    """Print the roots one per line if there are any

    >>> print_roots([2, 3])
    2
    3
    """
    if roots:
        roots_str = [str(r) for r in roots]
        print('\n'.join(roots_str))


#-------------------------------------------------------------------#
#                                                                   #
#                      Polynomial functions                         #
#                                                                   #
#-------------------------------------------------------------------#


class BadPolynomialError(Exception):
    """Raised by polynomial routines when the polynomial is invalid"""
    pass


def _check_poly(poly):
    """Raise BadPolynomialError if poly is invalid.

    A valid poly should be a list of int with leading coefficient non-zero or
    an empty list in the case of a zero polynomial.
    """
    msg = None
    if not isinstance(poly, list):
        msg = "poly should be a list"
    if not all(isinstance(coeff, int) for coeff in poly):
        msg = "All coefficients should of type int"
    if poly and not poly[0]:
        msg = "Leading coefficient should no nonzero"
    if msg is not None:
        raise BadPolynomialError(msg)


def integer_roots(poly):
    """Find integer roots of a polynomial p(x)

    Parameters
    ==========

    poly: list of integer coefficients representing the polynomial p(x)

    Returns
    =======

    roots: list of integer roots x such that p(x) = 0

    Examples
    ========

    Find roots of x^2 + 4*x + 4:

    >>> integer_roots([1, 4, 4])
    [-2]

    In the case of the zero polynomial an empty list of roots is returned:

    >>> integer_roots([])
    []
    """
    # Handle invalid or zero polynomials
    _check_poly(poly)
    if not poly:
        return []

    maxval = abs(poly[-1])
    candidates = range(-maxval, maxval+1)
    roots = [x for x in candidates if is_root(poly, x)]
    return roots


def evaluate_polynomial(poly, xval):
    """Evaluate the polynomial p(x) at x = xval

    Parameters
    ==========

    poly: list of integer coefficients representing the polynomial p(x)
    xval: value to evaluate the polynomial at

    Returns
    =======

    yval: integer giving p(xval)

    Examples
    ========

    Evaluate x^2 + 4*x + 4 at x=10

    >>> evaluate_polynomial([1, 4, 4], 10)
    144
    """
    # Handle invalid or zero polynomials
    _check_poly(poly)
    if not poly:
        return 0

    yval = poly[0]
    for coeff in poly[1:]:
        yval = coeff + yval * xval
    return yval


def is_root(poly, xval):
    """Check if xval is a root of the polynomial p(x)

    Parameters
    ==========

    poly: list of integer coefficients representing the polynomial p(x)
    xval: value of candidate root

    Returns
    =======

    True if xval is a root of poly. Otherwise returns False.

    Examples
    ========

    Is 10 a root of x^2 + 4*x + 4?

    >>> is_root([1, 4, 4], 10)
    False
    """
    return evaluate_polynomial(poly, xval) == 0


#-------------------------------------------------------------------#
#                                                                   #
#                           Unit tests                              #
#                                                                   #
#-------------------------------------------------------------------#

#
# Run these tests with pytest:
#
#    $ pytest roots.py
#

def test_evaluate_polynomial():
    assert evaluate_polynomial([], 1) == 0
    assert evaluate_polynomial([1], 2) == 1
    assert evaluate_polynomial([1, 2], 3) == 5
    assert evaluate_polynomial([1, 2, 1], 4) == 25

    # Invalid inputs should raise BadPolynomialError
    from pytest import raises
    raises(BadPolynomialError, lambda: evaluate_polynomial([0], 1))
    raises(BadPolynomialError, lambda: evaluate_polynomial({}, 1))
    raises(BadPolynomialError, lambda: evaluate_polynomial([[1]], 1))


def test_is_root():
    assert is_root([], 1) is True
    assert is_root([1], 1) is False
    assert is_root([1, 1], 1) is False
    assert is_root([1, 1], -1) is True
    assert is_root([1, -1], 1) is True
    assert is_root([1, -1], -1) is False
    assert is_root([1, -5, 6], 2) is True
    assert is_root([1, -5, 6], 3) is True
    assert is_root([1, -5, 6], 4) is False

    # Invalid inputs should raise BadPolynomialError
    from pytest import raises
    raises(BadPolynomialError, lambda: is_root([0], 1))
    raises(BadPolynomialError, lambda: is_root({}, 1))
    raises(BadPolynomialError, lambda: is_root([[1]], 1))


def test_integer_roots():
    # In the case of the zero polynomial every value is a root but we return
    # the empty list because we can't list every possible value!
    assert integer_roots([]) == []
    assert integer_roots([1]) == []
    assert integer_roots([1, 1]) == [-1]
    assert integer_roots([2, 1]) == []
    assert integer_roots([1, -5, 6]) == [2, 3]
    assert integer_roots([1, 5, 6]) == [-3, -2]
    assert integer_roots([1, 2, 1]) == [-1]
    assert integer_roots([1, -2, 1]) == [1]
    assert integer_roots([1, -2, 1]) == [1]
    assert integer_roots([1, -3, -75, 475, -750]) == [-10, 3, 5]

    # Invalid inputs should raise BadPolynomialError
    from pytest import raises
    raises(BadPolynomialError, lambda: integer_roots([0]))
    raises(BadPolynomialError, lambda: integer_roots({}))
    raises(BadPolynomialError, lambda: integer_roots([[1]]))


if __name__ == "__main__":
    import sys
    arguments = sys.argv[1:]
    main(*arguments)
