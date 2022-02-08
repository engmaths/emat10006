# axplot2.py

import matplotlib.pyplot as plt
from math import exp

fig = plt.figure(figsize=(6, 6))
ax_upper_left = fig.add_subplot(2, 2, 1)
ax_upper_right = fig.add_subplot(2, 2, 2)
ax_lower_left = fig.add_subplot(2, 2, 3)
ax_lower_right = fig.add_subplot(2, 2, 4)

# x values [0, 0.05, 0.10, ...]
x = [i*0.5 for i in range(20)]
expx = [exp(xi) for xi in x]

# line plot
ax_upper_left.plot(x, expx)

# line plot with logarithmic y axis
ax_upper_right.semilogy(x, expx)

# line plot with logarithmic x and y axes
ax_lower_left.loglog(x, expx)

# Scatter plot
ax_lower_right.scatter(x, expx)

plt.show()
