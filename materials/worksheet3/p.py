# plot.py

import math
import matplotlib.pyplot as plt

# SUVAT equations
#
# This will give the path of a projectile launched at angle theta and initial
# speed v0

GRAVITY = 0.98 # m/s^2

theta = math.pi/4    # 45 deg - launch angle
v0 = 1          # m/s    - initial speed

uy = v0*math.sin(theta) # m/s - initial vertical velocity
ux = v0*math.cos(theta) # m/s - horizontal velocity
ay = -GRAVITY      # m/s^2 - vertical acceleration

t = [0.01*n for n in range(100)]
y = [uy*ti + 1/2*ay*ti**2 for ti in t]  # constant acceleration
x = [ux*ti for ti in t]                 # constand speed

# Create a plot of y against x
plt.plot(x, y, linewidth=3, color='black')
plt.xlabel(r'$x\,(\mathrm{m})$')
plt.ylabel(r'$y\,(\mathrm{m})$', rotation=0)
plt.title('Trajectory of projectile')
plt.xlim([0, 0.7])
plt.ylim([0, 0.3])

# Creating the plot with plt.plot does not mean that we can see the plot!
# We need to "show" the plot:
plt.savefig('plot1.svg')
plt.show()
