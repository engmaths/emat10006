# Bouncing balls

## Assignment outline

You will provide a code repository demonstrating your solutions to the
problems below. You should also make a very short report including each of
your figures. The report should explain the mathematical principles behind
your analysis and interpret the numerical results. Take the time to format
your figures nicely.

Your code should be well written and neatly separated into different .py
files. Each should calculate one of the numbers or figures requested by the
sections below. Reduce duplication by putting frequently used code into
separate modules and importing from them. Use comments, doc-strings etc to
make your code easier to read.

## Workflow

1. Create a new git repository (e.g. on GitHub) called "bouncing".

2. Use `git clone <URL>` to clone the repository to your computer (bitbucket
   provides the command with the URL filled in so that you can paste it into a
   terminal.

3. Go into the folder with `cd` and use `git status` to check that everything
   is setup correctly.

4. For each exercise below you should work through the exercise and then:
   1. Use `git add` to add any new files you've created or files you've
      changed.
   2. Use `git diff` or `git diff --cached` to see changes before you commit
      them.
   3. Commit with a meaningful message using `git commit -m 'meaningful message'`

5. When you're done working on any particular machine (or every now and again)
   use `git push` to send your changes to the git repository on your hosting
   service (e.g. bitbucket).

6. As you're going along write a report including your findings (and figures).

7. Submit a zip of your repository (the folder called "bouncing") including
   all files and the .git folder along with a PDF of your report.

## Assignment problems

1. Use the Euler method to solve the ODE $\dot{x} = x$ with initial
   condition $x(0) = 1$. You should use this to estimate $x(1)$ using
   different timesteps. Produce a (nicely formatted) plot with double
   logarithmic scale showing how the error depends on the size of the timestep
   $\Delta t$.

   1. Ensure that you have a function called `euler_step` that does a single Euler step.
   1. Also make a function called `solve_to` which solves from $x_1,t_1$ to $x_2,t_2$
      in steps no bigger than `deltat_max`.
   1. Make a function called `solve_ode` that uses `solve_to` and `euler_step`
      to generate a series of numerical solution estimates $x_1,x_2,x_3,\dots$.
      This should be similar to scipy's `odeint` function.

2. Repeat part 1 using the [4th-order Runge-Kutta
   method](https://en.wikipedia.org/wiki/Runge%E2%80%93Kutta_methods#The_Runge.E2.80.93Kutta_method).
   1. Make it so that when calling `solve_ode` you can choose whether to use the Euler
      method or RK4.
   1. How does the error depend on $\Delta t$ now? How does this compare
      with the error for the Euler method (put this in the same plot)?
   1. Find step-sizes for each method that give you the same error - how long
      does each method take? (you can use the `time` command when running your
      Python script)

3. (Essential!) Extend your Euler and RK4 routines to be able to work with
   *systems* of ODEs. Use this to solve the 2nd order ODE $\ddot{x} = - x$
   which is equivalent to the system $\dot{x} = y, \dot{y} = -x$. Plot the
   results. What should the true solutions be? What goes wrong with the
   numerical solutions if you run them over a large range of $t$? (This is
   perhaps clearer if you plot $x$ against $\dot{x}$ rather than $x$ against
   $t$.)
