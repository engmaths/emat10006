# Scientific libraries in Python

Python is a general purpose programming language that can be used for making
many different types of program. Because of this it does not come
automatically equipped with libraries for doing scientific work - this is why
I advised to install Anaconda Python rather than use the normal "Python"
installer. This does not mean that Python is not suitable for scientific work.
We just need to understand that we should install the scientific bits on top.
They don't come included because many people use Python for other things.

## Numpy/scipy

The main scientific Python package that we want is called `numpy` but we also
want `scipy`. Test that you have them installed with

```python
>>> import numpy
>>> import scipy
```

If nothing happens they are installed.

Briefly `numpy` provides us with:

1. A fundamental N-dimensional array type that we can use for representing
   vectors, matrices, and higher-order tensors. This is very similar to arrays
   in Matlab - and not the same as lists, tuples, etc in Python.

2. An interface to a BLAS library for doing standard linear algebra operations
   (matrix multiplication, solving linear systems etc)

3. Routines for Fourier Transforms

4. Routines for different kinds of random numbers

5. Some other commonly used scientific stuff.

We also want `scipy` which provides:

1. Signal processing

2. Optimisation routines (minimisation, root-finding etc.)

3. "Special" functions (obscure mathematical functions)

4. Sparse matrices

5. Integration routines

6. Stats stuff.

7. Loads more stuff that I don't know about

For our purposes numpy and scipy are basically the same thing but arbitrarily
divided into two different packages.

You can find a quick tutorial on [numpy
here](https://numpy.org/doc/stable/user/quickstart.html). There is
also [this
page](https://numpy.org/doc/stable/user/numpy-for-matlab-users.html)
which notes the important differences between Matlab and numpy. You can also
find the code for both [numpy](https://github.com/numpy/numpy) and
[scipy](https://github.com/scipy/scipy) on GitHub.

## Matrices or arrays?

Numpy has a function `matrix` which creates a "matrix" instead of a 2D array.
Do *not* use this function. Never use it. More information can be found
[here](https://numpy.org/doc/stable/user/numpy-for-matlab-users.html).
When I say "matrix" below I mean that you should create a 2D array using the
`array` function.

## Exercises

1. Given a numpy array `a = np.array([1, 2, 3])` what does `a+a` give us and what
   about `a*3`? What would happen if `a` were a list `a=[1, 2, 3]` instead?
1. How do you create a matrix using Numpy?
1. Given two matrices `M1` and `M2` what does `M1 * M2` give us? How do we
   compute the *matrix product* of two matrices instead? (Compare with Matlab)
1. Given a Matrix $\mathrm{M}$ and vector $\mathrm{b}$ how do I compute
   the solution $\mathrm{x}$ of the system of equations $\mathrm{M\,x =
   b}$
1. How do I sum a matrix along its rows/columns?
1. How do I generate a matrix of random numbers that are normally distributed?
   What about numbers uniformly distributed between 0 and 1?
1. How do I slice a matrix to cut off the last row and the last column?
1. Give a Matrix `M` what does `M<2` give us?
1. What about `M[M<2]`?
1. What about `M[1<M<2]` or `M[1<M and M < 2]` or `M[(1<M) & (M<2)]`?
1. What about about `M[1:-1,1:-1]` or `M[[1, 2], [1, 2]]`?
1. How can you find the determinant of a matrix, or the transpose?
1. What about the eigenvectors and eigenvalues?
1. How do we create vectors/matrices of 64-bit floats? What about 8-bit
    unsigned integers?
1. If `M` is a vector of *unsigned* integers what does `M[:] = -1` do?
1. Explore the memory use of matrices using the `nbytes` attribute. Can you
    make sense of it?
1. The function `odeint` is described in the
    [docs](https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.odeint.html)
    Use it to solve the ODE $\dot{x} = x$ with initial condition $x(0)=1$. The
    true solution has $x(1)=\mathrm{e}$ so what is the error in the
    numerical estimate of $x(1)$?
1. How do we use `odeint` to solve a second order ODE e.g. $\ddot{x} = -x$?
    What is the error in the numerical estimate of $x(1)$?
