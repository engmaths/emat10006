EMAT10006: Further Computer Programming

Week 4 -- Git in Pairs, Matplotlib and Numpy

------------------------------------------------------------------------

For this week's worksheet, and the second assignment, you will need to work
with one or two partners which should be someone from your TA group.

In this worksheet we will

1. learning how to work with a partner with git

2. learn how to do plotting with matplotlib

Quick demo of plotting
======================

We'll get more on to plotting in the second half of the worksheet. Here is a
quick demonstration though. This should give you a starting piece of code that
you can use while working through the push/pull exercises below.

If you have matplotlib and numpy installed (install them with pip if you
don't) then you can use the following to create a plot that you can see on the
screen:
```python
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
```
You can run that with
```console
$ python plot.py
```
You should see a window open with something looking like this:
![Simple quadratic plot](plot1.svg)

We will look more at how to use matplotlib later in the worksheet but for now
you can use this simple program as an example while practising pushing and
pulling with your partner.


Pushing and pulling
===================

This exercise requires you to work in your pairs. We will walk through how to
push and pull to a remote repo that you share. Along the way you should get a
better idea of why Git is so useful when collaborating on projects, as well as
some of the complications that it brings!

Firstly here's a diagram showing roughly how the different git commands work
together and how where they move changes from and to:

![A schematic of your local and remote repositories, showing how changes
can be pushed and pulled around.](git-commands.svg)

The normal workflow is to:

1. Make changes to the code (the "workspace" or "workeing tree"). This is what
   happens when you edit your code files with your editor.

2. Use `git add` to register those changes with git. This stores the changes
   in the "index".

3. Use `git commit` to make a new commit with the changes that are stored in
   the "index".

4. Repeat steps 1-3 making new commits.

5. Use `git push` to send the commits to GitHub.

The other step that we haven't used yet is `git pull`. The pull command is the
opposite of the push command:

* `git push` sends commit from your local repo to the remote repo (from your
  computer to GitHub).

* `git pull` retrieves commit from the remore repo to your local repo (from
  GitHub to your computer).

So far we haven't used `git pull` because we haven't been working with anyone
else. If you are the only one making commits then there will never be any
commits on GitHub apart from the ones you pushed there. Once we start working
with other people we need a way to get their commits into the local repo and
that's what we `git pull` is for.


Push, pull exercise
===================

**Note**: this exercise is to be done in pairs (or groups of three).

Firstly, let's get a repo up and running with a local clone for either of you.

Just one of you should make a new repo. If you can't remember how to create a
new repo go back to the worksheet from week 13. It's basically just a matter
of hitting the green 'New' button on your GitHub homepage and following the
instructions. Don't forget to make it private! You could call it
'week4-push-pull'.

From now on I'll refer to the person that made the repo as the 'owner' and the
other person in the pair as the 'collaborator'. Notice that in the following
guide, although I get either the owner or collaborator to do certain tasks,
these could be accomplished by either -- it's just an easy way of
distinguishing between you both (see the N.B. at the bottom of this section
for more info on being the 'owner' of a repo).

The owner should go to the settings tab on their new repo and go to 'Manage
access'. From here click the 'Invite a collaborator' button, and add the
collaborator to the project by finding them via their GitHub username. The
collaborator should then get an email, asking them to accept the invitation.
Now both the owner and the collaborator should be able to see the new repo
online, despite it being private.

You should now both clone the repo onto your computers. Again, if you can't
remember how to do this, check back in with the worksheet from week 13.
Essentially you just need to get the URL from the 'Code' button on GitHub,
then -- in a suitable directory on your machine -- run the terminal command:

```shell
$ git clone https://github.com/uob-simon/week4-push-pull
```

with the correct URL. You now both have *local* repos which are clones of the
GitHub repo. If you both run `git remote -v` it should show you both have the
same 'origin', which is a URL to the remote GitHub repo. So although you have
local different copies of the repo, the remote repo that you push commits to
and pull commits from is *the same* for both of you.

The owner should now add some stuff to the local repo. Add a simple Python
script that does something. Copy a file (or create a new one) into the
directory of your local repo. Then use `git add`, `git commit` and `git push`
to send that file to GitHub. (Refer to previous git exercises) Both of you can
now look on the GitHub repo webpage, and see the new file.

If the collaborator runs `git status` it still shows up-to-date, but they
actually need to pull down the changes now. If they tried to push their own
changes up, Git wouldn't let them before they've pulled. More on this in a
moment. For now, the collaborator should run `git pull` to pull down the
changes to their local repo to work on.

You now both have your own local repo and the shared one online. See the
figure below for a useful way to picture this. Notice how there's no arrows
connecting the two local repos; all changes must go through the remote GitHub
repo.

![Pushing and pulling to synchronise](push-pull.svg)

Firstly, let's see what happens when one of you tries to push changes to
the remote repo without first having pulled down.

**Collaborator**: make some minor changes to a code file. Add, commit, and
push them. Get in the habit of making good commit messages which concisely
describe the changes you've made -- even if the changes are minor.

**Owner**: also make some changes. But for now add them to a different file.
Just add some text (e.g. a comment) or something. Then add, commit and try to
push the commit.

You should see some scary message telling you your push was rejected. Read
this carefully, Git is actually being very helpful here and tells you
precisely the problem; which is that someone else has pushed changes which you
don't have yet. You need to integrate the changes from the remote repo before
you can push to it.

**Owner**: pull down the changes, noting the info Git gives you about what you
just pulled. (Exit from vim by hitting Shift+Z+Z). As long as you didn't both
make changes to the same lines of projectiles.py, it should *merge* the
changes to your files automatically. Git can do this because the differences
between the remote repo and yours aren't *conflicting*, i.e. they weren't on
the same line in the same file.

**Owner**: run `git status`. It will say you are two commits ahead\... why
two? Use `git log` to find out. Then, push your changes up! Note how you don't
need to add or commit again.

**Exercise for both of you:** now try making changes to the same file, but
ensure the changes are on *different* lines. Both then try and push up without
pulling\... Whoever does this second should encounter a similar problem. Can
Git still merge the changes by itself?

Okay, so far so good. No major problems as Git is handling a lot of the work
for us. Look at the commits tab on the remote repo's webpage, noting how it
associates the commits with the user who made them. Let's now make things
worse by creating conflicts which Git can't resolve by itself.

Ensure when both of you run `git status` you have a clean working tree, and
you have pulled any changes.

Now both change *the same line in different ways*! Both `git diff` before you
push to make sure you have changed the same line! Only change one line for
now. Both add and commit the change.

Owner: push up your change to the online repo. Collaborator: run `git pull`
once the owner has pushed their changes.

Uh-oh, Git is now telling us we have a merge conflict. This is where there is
a conflict between the changes and Git can't sort out the merge by itself. You
should see something like:

```shell
$ git pull
remote: Enumerating objects: 14, done.
remote: Counting objects: 100% (13/13), done.
remote: Compressing objects: 100% (7/7), done.
remote: Total 8 (delta 1), reused 8 (delta 1), pack-reused 0
Unpacking objects: 100% (8/8), done.
From https://github.com/simonw23/merge_conflict_test
   3c06fa3..bf3f0ea  master     -> origin/master
Auto-merging projectiles.py
CONFLICT (content): Merge conflict in projectiles.py
Automatic merge failed; fix conflicts and then commit the result.
```

Git is telling us it tried to automatically merge the changes with your local
repo but failed because of a conflict. We must now fix the conflict locally
before re-committing our changes to the remote repo. Notice how the merge
conflict is a 'local' problem.

For example, I changed the value of a variable called GRAVITY and so did my
collaborator, and now I see:
```python
<<<<<<< HEAD
GRAVITY = 0.9813
=======
GRAVITY = 0.9812
>>>>>>> bf3f0ea2df966d6476c5ff47cca7aaee885cde27
```
at the top of projectiles.py (the file that we edited). We can see Git has
shown us both versions of the change to the line where `GRAVITY` is assigned.
The one between `<<<<<<< HEAD` and the equals signs is my local change; and
the line between the equals signs and `>>>>>>> bf3f0...` is my collaborator's
changes that I have attempted to merge. (Owner: run `git log` -- can you see
where that big long hex string that the collaborator is seeing comes from?)

Git doesn't know which of these versions should be the one that is kept. It
has no way of knowing who is 'correct', and so Git is asking you to sort out
your own mess! Essentially, delete the line that you do not want to keep, and
leave the line in you do want to keep. Then, remove all of the Git stuff (i.e.
the lines starting `>>>`, `===` and `<<<`). *You want to have a working Python
file at the end!*

Once you have done this and checked that your code works, all you need to do
is re-add the file using `git add` to tell Git that you have resolved the
conflict.  Commit and push as normal.  Conflict resolved!

**Owner**: pull down from the remote repo, and both of you run `git log` to
figure out what Git has done with either of your commits that caused the merge
conflict.

**Exercise:** Make sure both of you have practice resolving conflicts and
understand the output Git gives you to the terminal, as well as the indicators
it inserts into files when there is a merge conflict. Also, try changing
multiple lines each (some on the same line and some not). Does Git make you
resolve all of them yourself, or just the ones on the same line? What happens
if while one user is sorting a merge conflict the other user really winds them
up by pushing more changes before the original conflict is resolved?

Merge conflicts are mostly avoidable, by proper division of tasks and good
communication between collaborators. However they become almost inevitable as
the size of your projects and the size of your team both increase.
Understanding why they arise, minimizing how often they arise, and resolving
them are all key concepts in Git.

**Make sure both of you have understood the previous three cases you've just
gone through of pushing / pulling from the same remote repo.**

N.B. Practically speaking, pushing and pulling from the same remote repo by
multiple people is a bad idea in larger projects. Later in the unit we will
talk about 'forks' and 'branches', which are ways to manage different versions
of the same base code by getting Git to keep track of different changes in
isolation from each other. This makes it possible to have, for example, one
person working on a new feature and another person working on a bug-fix
simultaneously, before later merging branches back together in a sensible
order. We will also make use of a GitHub feature called 'pull requests', which
allow for more control over what ends up on a shared remote repo. At that
point, who the 'owner' is and who the collaborators are really matters, as it
is them who is ultimately in charge of what is merged onto the remote's master
branch.

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

More advanced plotting
======================

When we use `plt.plot` what happens is that a "figure" with an "axes" is
created implicitly. For more advanced plotting it is better to create these
explicitly yourself e.g.:
```python
# axplot.py

import matplotlib.pyplot as plt
from math import sin, cos

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
x = [i*0.05 for i in range(300)]
sinx = [sin(xi) for xi in x]
cosx = [cos(xi) for xi in x]

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

## More plotting!

Here's another program that creates four plots:
```python
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
```
If you run this you should see:
![Exp plot](axplot2.svg)

**Exercise**: play around with these examples and try out different kinds of
plots. You can find many more examples here:
<https://matplotlib.org/stable/tutorials/introductory/sample_plots.html>
(Many of the examples use numpy functions that we will discuss more later...)
