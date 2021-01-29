#!/usr/bin/env python
#
# This script simulates a bouncing ball using the Euler method and primitive
# collision detection. The result is shown as a matplotlib animation.
#
# The ball bounces higher and higher demonstrating the instability of the
# Euler method for this problem.

from __future__ import print_function

import numpy as np
import matplotlib

# Matplotlib code for animation and circles
#matplotlib.use('Agg')
from matplotlib.pyplot import figure, show, Circle
from matplotlib.animation import FuncAnimation

# Derivative function for an object falling under gravity having height y and
# velocity v. The system parameters (g etc) are defined below.
#
# The system has smooth dynamics given by
#
#    dx/dt = f(x, t)
#
# where this Python function defines f. A bouncing ball has the ODE:
#
#    d2x/dt2 = -g
#
# which has the first-order form
#
#    dxdt = v
#    dvdt = -g
#
# We package this up as a single ODE for 2D vector X = [y, v]
#
def f_ball(X, t):
    '''Derivative function for the ball in 1st order form.'''
    y, v = X
    dydt = v
    dvdt = -g
    dXdt = [dydt, dvdt]
    return dXdt

# Gravitational constant
g = 10  # m/s^2

# Dimensions of enclosure and ball
yB = 0 # m  (height of the floor)
R  = 1 # m  (radius of ball)

# Initial time, position and velocity of ball
y0 = 2   # m
v0 = 0   # m/s
t0 = 0   # s
X0 = [y0, v0]  # Initial state vector

# Euler method to update the state of a system with derivative f
#
# Finds X2 corresponding to t2 if the system begins at t1 in state X1.
#
def euler_step(f, X1, t1, t2):
    '''Euler step from X1 at t1 to X2 at t2.'''
    dXdt = f(X1, t)
    dt = t2 - t1
    X2 = X1 + dt * np.array(dXdt)
    return X2

# Euler method in combination with collision detection
def update_ball(X1, t1, t2):
    '''Update ball position for both gravity and bounce'''
    # Smooth motion
    X2 = euler_step(f_ball, X1, t1, t2)
    y, v = X2
    # Collision
    if y - R < yB:
        v = -v
    X2 = y, v
    return X2


if __name__ == "__main__":

    #
    # matplotlib's bizarre animation API...
    #
    fig = figure()
    ax = fig.add_axes([0.15, 0.15, 0.70, 0.70])
    ax.set_xlim([-5, 5])
    ax.set_ylim([yB, yB + 10])
    ball_mpl = Circle([0, y0], R, color='r')
    ax.add_patch(ball_mpl)

    # Makes the axes square so that the circle is circular...
    #
    # Need to wait until the first frame of the animation to do this.
    def make_axes_square():
        fw, fh = fig.get_size_inches()
        r = fw/fh
        b = 0.15
        h = 0.70
        w = h / r
        l = (1 - w)/2.
        ax.set_position([l, b, w, h])

    # This is called on each frame of the animation (i is the frame number)
    def animate(i):
        if i == 0:
            make_axes_square()
        # The actual update code
        global X, t  # Matplotlib's API sort of needs globals
        X = update_ball(X, t, t+dt)
        t = t + dt
        y, v = X

        # Print the energy to see that it is conserved...
        E = g*y + 0.5*v**2
        print('E =', E)

        # Update the ball in the display
        ball_mpl.center = (0, y)
        return (ball_mpl,)

    # Simulation parameters
    X = X0    # state vector
    t = t0    # time
    dt = 0.05 # s (time step)

    # Actually show the animation
    anim = FuncAnimation(fig, animate, interval=int(1000*dt), blit=True)
    show()
