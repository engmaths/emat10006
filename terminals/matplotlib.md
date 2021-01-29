# Plotting with matplotlib

Plotting in Python is usually done using the `matplotlib` library (although
other libraries do exist). `matplotlib` is build on top of `numpy` so that it
can use arrays for its internal calculations. You can find the [matplotlib
website here](https://matplotlib.org/). The code for matplotlib is on
[github](https://github.com/matplotlib/matplotlib).

First take a quick look at [this
tutorial](https://www.labri.fr/perso/nrougier/teaching/matplotlib/). As in
other cases this tutorial has more than we need so don't feel that you should
work through the whole thing (although don't let me stop you if you want to!).

Here's an example plotting script:

```python
#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2*np.pi, 100)
y = np.sin(x)

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.plot(x, y)
plt.show() # Show on the *screen

fig.savefig('sine.svg')
```

The above code gives us a figure like:

![](/assets/basics/sine.svg)

Normally I would dress this up a bit though so that I end up with something
like this:

```python
#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

def main(filename=None):
    '''Plot sine function and show on screen or save to file'''

    # Set the figure size in inches
    # and manually control the axes size
    fig = plt.figure(figsize=(4, 3))
    ax = fig.add_axes([0.20, 0.20, 0.70, 0.70])

    # Have a function to do the actual plotting to the axes object
    plot_sine(ax)

    # Show on screen or save to file if filename is provided
    if filename is None:
        plt.show()
    else:
        fig.savefig(filename) # Format chosen by extension


def plot_sine(ax):
    numpoints = 100
    x = np.linspace(0, 2*np.pi, numpoints)
    y = np.sin(x)

    ax.plot(x, y, color='black', linewidth=3)
    ax.set_xlim([0, np.pi])
    ax.set_ylim([-1, 1])

    # Use LaTeX for text
    ax.set_xlabel(r'$x$')
    ax.set_ylabel(r'$\sin{x}$', rotation=0)

    # Manually control axes ticks
    ax.set_xticks([0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi])
    ax.set_xticklabels([
        r'$0$',
        r'$\frac{\pi}{2}$',
        r'$\pi$',
        r'$\frac{3\pi}{2}$',
        r'$2\pi$',
    ], fontsize='large')
    ax.set_yticks([-1, 0, 1])


if __name__ == "__main__":
    import sys
    main(*sys.argv[1:])
```

We can show the plot on the screen by running this script like:

```bash
python sine2.py # shows on the screen
```

or we can save it to a file (format determined by filename extension) with:

```bash
python sine2.py sin2.pdf # saves to file
```

The resulting figure looks like:

![](/assets/basics/sine2.svg)

## Exercises

1. Create a script that uses `odeint` to solve the ODE $\ddot{x} = -\omega^2
   x$ with initial conditions $x(0) = 1$ and $\dot{x}(0) = 0$ and plots
   $x(t)$.
2. Adapt the above so that it plots both $x(t)$ and $\dot{x}(t)$ in
   different colours. Use a legend to indicate which is which and ensure that
   all axes are properly labelled. Adjust linewidth, colours, ticks etc to
   make the figure look better.
3. Adapt the above so that your figure has two subplots. One should be
   rectangular and as above. The other subplot appear below and should be the
   same width but square (how can you make it exactly square?). The lower
   subplot should show the solution in the *phase plane* i.e. it should show
   the trajectory in the space with axes $x$ and $\dot{x}$. Ensure that
   all axes etc are labelled.
4. Adapt the above so that it is a script that you can run as `python
   myscript.py 3 # Sets omega to 3` or `python myscript.py 3 myfigure.pdf`.
5. Given a function of two variables $f(x, y) = \frac{1}{1 + x^2 + y^2}$
   create a script that will plot the function as a "heat map". Can you get
   the axes ticks correct? Can you change the color scheme?
6. Create a script that will generate a CSV file with two columns of
   approximately random numbers representing two correlated variables. Make a
   script that can read this CSV file and show the result as a scatter plot.
