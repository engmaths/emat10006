# plot_sin.py

import matplotlib.pyplot as plt
import math

# Create x as a list of 300 numbers equally spaced from xmin to xmax
numpoints = 300
xmin = 0
xmax = 20
delta_x = (xmax - xmin) / (numpoints - 1)
x = [xmin + i*delta_x for i in range(numpoints)]

# Create y as a list of corresponding y values for y = sin(x)
y = [math.sin(xi) for xi in x]

# Now plot them:
plt.plot(x, y)
plt.savefig('plot_sin.svg')
plt.show()
