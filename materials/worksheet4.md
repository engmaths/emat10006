EMAT10006: Further Computer Programming

Week 4 -- Git in Pairs, Matplotlib and Numpy

------------------------------------------------------------------------

**Please make sure to sit at the same desks as last week, so that your
TA knows where you are!**\
For this week's worksheet, and the second assignment, you will need to work
with one or two partners which should be someone from your TA group.

Today we will be:

1.  plotting a simple projectile using matplotlib and numpy,

2.  learning how to work with a partner with git,

Matplotlib and numpy - A simple projectile
==========================================

You can either do this task in your pair, or separately.

Suppose we want to plot the motion of a simple projectile in the $x,y$ plane.
We can use the following equations to calculate the displacement in $x$ and
$y$ at time $t$ as:
$$
  x = v_0 t \cos\theta
    \qquad \text{and} \qquad
  y = v_0 t \sin\theta - 0.5gt^2,
$$
where $v_0$ is the initial velocity, $\theta$ is the initial launch angle and
$g$ is the gravitational acceleration constant, see figure

Download the [projectiles.py](projectiles.py). This contains a very simple
`Projectiles` class which calculates the displacement of a projectile after
some time with certain initial conditions.

Exploring the code
------------------

Note: Before you can run the code you need to make sure that you have
`matplotlib` and `numpy` installed. You can test by importing them:
```python
>>> import numpy
>>> import matplotlib
```
If you installed Python using Anaconda then you should have these modules
already installed. If you get an `ImportError` then you'll need to install
`numpy` and `matplotlib` now.

First thing to do when faced with new code is to investigate it in the python
console. You will want to import `numpy` as `np`, this is a convention:
```python
import numpy as np
```
Import the `Projectile` class into an interactive python session and try
running some of the examples given in the doc string. What is returned?

Try using some different values.

Can you write a function which stores the projectile position over some period
of time, i.e. the trajectories of the projectiles?

Plotting the projectile
-----------------------

Now that we have some data, we want to start plotting it. Have a look at this
tutorial:
<https://matplotlib.org/stable/tutorials/introductory/pyplot.html>
Make the following plots:

Some line plots showing the trajectories of projectiles with different initial
conditions.

A multi-line plot comparing different trajectories.

A scatter plot showing the total displacement in $x$ with different initial
conditions.

Pushing, pulling, and merge conflicts
=====================================

This exercise requires you to work in your pairs. We will walk through how to
push and pull to a remote repo that you share. Along the way you should get a
better idea of why Git is so useful when collaborating on projects, as well as
some of the complications that it brings!

![A schematic of your local and remote repositories, showing how changes
can be pushed and pulled around.](git-commands.svg)

Note that throughout this exercise I'm going to 'hold your hand' a lot less
than previous weeks. You should by now know to run `git status` (and maybe
`git log`) regularly. You should also be very comfortable with the sequences
of commands needed to commit and push changes up to a repo. If not, go back to
the worksheet from week 13, or watch Wednesday's lecture on re/play.

You must take the initiative on walkthroughs like this to make sure that you
understand everything that you do, and all of the output that Git gives you.
If you don't fully understand anything, make sure to ask your TA.

Firstly, let's get a repo up and running with a local clone for either of you.

Just one of you should make a new repo. If you can't remember how to create a
new repo go back to the worksheet from week 13. It's basically just a matter
of hitting the green 'New' button on your GitHub homepage and following the
instructions. Don't forget to make it private! Call it 'week16-push-pull'.

From now on I'll refer to the person that made the repo as the 'owner' and the
other person in the pair as the 'collaborator'.  Notice that in the following
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
Essentially you just need to get the URL from the 'Clone or download' button,
then -- in a suitable directory on your machine -- run the terminal command:

```shell
$ git clone https://github.com/uob-simon/week14-push-pull
```

with the correct URL. You now both have *local* repos which are clones of the
GitHub repo. If you both run `git remote -v` it should show you both have the
same 'origin', which is a URL to the remote GitHub repo. So although you have
local different copies of the repo, the remote repo that you push commits to
and pull commits from is *the same* for both of you.

The owner should now add some stuff to the local repo. I'd recommend adding
the projectiles.py file from the previous exercise. They can do this by
copying and pasting it into their local repo (using the terminal ideally!)
then adding, commiting and pushing it up to the GitHub repo. Again refer back
to previous worksheets if you haven't got the hang of this yet.

Both of you can now look on the GitHub repo webpage, and see the new file and
commit.

If the collaborator runs `git status` it still shows up-to-date, but they
actually need to pull down the changes now. If they tried to push their own
changes up, Git wouldn't let them before they've pulled. More on this in a
moment. For now, the collaborator should run `git pull` to pull down the
changes to their local repo to work on.

You know both have your own local repo and the shared one online. See
the figure below for a useful way to picture this. Notice how there's no
arrows connecting the two local repos; all changes must go through the
remote GitHub repo. Let's now intentionally cause some problems\...

Firstly, let's see what happens when one of you tries to push changes to
the remote repo without first having pulled down.

**Collaborator**: make some minor changes to projectiles.py. Add, commit, and
push them. Get in the habit of making good commit messages which concisely
describe the changes you've made -- even if the changes are minor. E.g. change
the value of the constant `GRAVITY` to 9.814 and use the commit message "Alter
GRAVITY constant to 4 significant figures". REMEMBER: you should be running
`git diff` before pushing changes to check you haven't accidentally made
changes you don't want to push.

**Owner**: also make some changes. But for now add them to README.md.  Just
add some text or something. Then add, commit and try to push the commit.

You should see some scary message telling you your push was rejected. Read
this carefully, Git is actually being very helpful here and tells you
precisely the problem; which is that someone else has pushed changes which you
don't have yet. You need to integrate the changes from the remote repo before
you can push to it.

**Owner**: pull down the changes, noting the info Git gives you about what you
just pulled. (Exit from vim by hitting Shift+Z+Z). As long as you didn't both
make changes to the same lines of projectiles.py, it should 'merge' the
changes to your files automatically. Git can do this because the differences
between the remote repo and yours aren't 'conflicting', i.e. they weren't on
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

If the collaborator now opens projectiles.py they will see that Git has
inserted a bunch of stuff to help us resolve the merge conflict.  For example,
I changed the value of GRAVITY and so did my collaborator, and now I see:

```python
<<<<<<< HEAD
GRAVITY = 0.9813
=======
GRAVITY = 0.9812
>>>>>>> bf3f0ea2df966d6476c5ff47cca7aaee885cde27

```

at the top of projectiles.py. We can see Git has shown us both versions of the
change to the line where `GRAVITY` is assigned. The one between `<<<<<<< HEAD`
and the equals signs is my local change; and the line between the equals signs
and `>>>>>>> bf3f0...` is my collaborator's changes that I have attempted to
merge. (Owner: run `git log` -- can you see where that big long hex string
that the collaborator is seeing comes from?)

Git doesn't know which of these versions should be the one that is kept. It
has no way of knowing who is 'correct', and so Git is asking you to sort out
your own mess! Essentially, delete the line that you do not want to keep, and
leave the line in you do want to keep. Then, remove all of the Git stuff (i.e.
the lines starting `>>>`, `===` and `<<<`). *You want to have a working Python
file at the end!*

Once you have done this, all you need to do is re-add the file using `git add`
to tell Git that you have resolved the conflict.  Commit and push as normal.
Conflict resolved!

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
allow for more control over what ends up on a shared remote repo. At this
point, who the 'owner' is and who the collaborators are really matters, as it
is them who is ultimately in charge of what is merged onto the remote's master
branch.
