# plot.py

import matplotlib.pyplot as plt

# These numbers correspond to y = x**2
x = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
y = [0, 0.01, 0.04, 0.09, 0.16, 0.25, 0.36, 0.49, 0.64, 0.81, 1.0]

# Create a plot of y against x
plt.plot(x, y)

# Creating the plot with plt.plot does not mean that we can see the plot!
# We need to "show" the plot:
plt.savefig('plot1.svg')
plt.show()
