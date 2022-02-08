Plotting in matplotlib
======================

At the start of the worksheet we saw how to create a simple plot with
matplotlib. In this section I show some example programs that make plots but
your task is to run these and then change then and see if you can plot other
things. Explore what you can do rather than just running the examples!

We saw a simple plot earlier but let's try something more complicated:
```python
# plot_sin.py

import matplotlib.pyplot as plt
import math

# Create x as a list of 300 numbers equally spaced from 0 to 20
numpoints = 300
xmin = 0
xmax = 20
delta_x = (xmax - xmin) / (numpoints - 1)
x = [xmin + i*delta_x for i in range(numpoints)]

# Create y as a list of corresponding y values for y = sin(x)
y = [math.sin(xi) for xi in x]

# Now plot them:
plt.plot(x, y)
plt.show()
```
You can run that with
```console
$ python plot_sin.py
```
You should see a window like this appear:
![Sin plot](plot_sin.svg)

Using numpy arrays
==================

Above creating the lists of `x` and `y` values is awkward. We can use `numpy`
to make that more convenient. Numpy gives us an array class that we can use to
quickly apply mathematical functions to lost of values e.g.:
```python
>>> import numpy as np
>>> x = np.array([1, 2, 3, 4])
>>> x
array([1, 2, 3, 4])
>>> x + x
array([2, 4, 6, 8])
```
Numpy also gives as mathematical functions that can operate on the elements of
arrays:
```python
>>> y = np.sin(x)
>>> y
array([ 0.84147098,  0.90929743,  0.14112001, -0.7568025 ])
```
The `arange` function is like the Python `range` function but it gives us an
array. Here we can create an array of numbers from `0` to `10` in steps of
`1.5`:
```python
>>> np.arange(0, 10, 1.5)
array([0. , 1.5, 3. , 4.5, 6. , 7.5, 9. ])
```
The `linspace` function can be used to get an array with a fixed number of
points between two values. Here we create an array of 9 values from `0` to
`10`:
```python
>>> np.linspace(0, 10, 9)
array([ 0.  ,  1.25,  2.5 ,  3.75,  5.  ,  6.25,  7.5 ,  8.75, 10.  ])
```
We can use numpy arrays directly with matplotlib. Using all these the plotting
example above can be just:
```python
x = np.linspace(0, 20, 300)
y = np.sin(x)
plt.plot(x, y)
```
You can find plenty more information about `numpy` arrays here:
<https://numpy.org/doc/stable/user/quickstart.html>

More advanced plotting
======================

When we use `plt.plot` what happens is that a "figure" with an "axes" is
created implicitly. For more advanced plotting it is better to create these
explicitly yourself. That makes it possible to create a figure with multiple
axes e.g.:
```python
# axplot.py

import matplotlib.pyplot as plt
import numpy as np

#
# Create a figure (a window)
# Add two subplots in a 1x2 grid (one plot on the left and one on the right)
# ax_left will be the left axes (number 1)
# ax_right will be the right axes (number 2)
#
fig = plt.figure(figsize=(6, 3))
ax_left = fig.add_subplot(1, 2, 1)
ax_right = fig.add_subplot(1, 2, 2)

# x values [0, 0.05, 0.10, ...]
x = np.linspace(0, 15, 300)
sinx = np.sin(x)
cosx = np.cos(x)

# Plot sinx on the left
ax_left.plot(x, sinx, color='green', linewidth=3)
ax_left.set_title('Plot of sin(x)')

# Plot cosx on the right
ax_right.plot(x, cosx, color='red', linewidth=3)
ax_right.set_title('Plot of cos(x)')

plt.show()
```
You should see a window like this appear:
![Sin/cos plot](axplot.svg)

More plotting!
==============

Here's another program that creates four plots:
```python
# axplot2.py

import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(6, 6))
ax_upper_left = fig.add_subplot(2, 2, 1)
ax_upper_right = fig.add_subplot(2, 2, 2)
ax_lower_left = fig.add_subplot(2, 2, 3)
ax_lower_right = fig.add_subplot(2, 2, 4)

# x values [0, 0.05, 0.10, ...]
x = np.linspace(0, 10, 21)
expx = np.exp(x)  # exponential function

# line plot
ax_upper_left.plot(x, expx)

# line plot with logarithmic y axis
ax_upper_right.semilogy(x, expx)

# line plot with logarithmic x and y axes
ax_lower_left.loglog(x, expx)

# Scatter plot
ax_lower_right.scatter(x, expx)

plt.show()
```
If you run this you should see:
![Exp plot](axplot2.svg)

**Exercise**: play around with these examples and try out different kinds of
plots. You can find many more examples here:
<https://matplotlib.org/stable/tutorials/introductory/sample_plots.html>
(Click on any of the images to see the code that makes the plot.)
