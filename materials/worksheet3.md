EMAT10006: Further Computer Programming

Week 3 -- Git in Pairs, functions and packages

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
plt.savefig('plot1.svg') # save to a file
plt.show()							 # show on screen
```
You can run that with
```console
$ python plot.py
```
You should see a window open with something looking like this:
![Simple quadratic plot](plot1.svg)

We will look more at how to use matplotlib later in the unit but for now you
can use this simple program as an example while practising pushing and pulling
with your partner.


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

Just one of you should make a new repo. From now on I'll refer to the person
that made the repo as the 'owner' and the other person in the pair as the
'collaborator'. Notice that in the following guide, although I get either the
owner or collaborator to do certain tasks, these could be accomplished by
either -- it's just an easy way of distinguishing between you both (see the
N.B. at the bottom of this section for more info on being the 'owner' of a
repo).

The owner should go to the settings tab on their new repo and go to 'Manage
access'. From here click the 'Invite a collaborator' button, and add the
collaborator to the project by finding them via their GitHub username. The
collaborator should then get an email, asking them to accept the invitation.
Now both the owner and the collaborator should be able to see the new repo
online, despite it being private.

You should now both clone the repo onto your computers. If you can't remember
how to do this, check back to the previous worksheet.  Essentially you just
need to get the URL from the 'Code' button on GitHub, then -- in a suitable
directory on your machine -- run the terminal command:

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

Ensure when both of you run `git status` you have a clean working tree, and you
have pulled any changes.

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
conflict.  Commit and push as normal. Conflict resolved!

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
multiple people is a bad idea in larger projects. Later in the unit we might
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

## Functions

The part of this worksheet is about reading and critical reflection. I'm
assuming that you've already read [functions](../functions). I'm also assuming
that you have written some code in the past e.g. for a previous project.

It is often said among programmers that code is "read more often than it is
written". The point is that you should put effort into making code readable
even if that takes a small amount of extra time when you are writing the code.
That time will be repaid many times later when you end up having to read the
code. A strange thing happens when programming though: it is quite easy to
write code that makes sense to you in the exact moment that you are writing it
but is actually impossible to understand. The code might "work" but a future
reader (including you in a month's time) might have no chance of being able to
understand it.

You might say that as long as the code works it doesn't matter if any human
can understand it but that makes it impossible to improve the code later. It's
also impossible to fix bugs or take pieces of the code and reuse them for
other things if no one understands it any more. Most importantly if you are a
beginner at programming: if you learn how to write readable code then it is
not much harder than writing unreadable code. This is a skill that once
mastered means that everything you produce is naturally better.

**Exercise**: go back over the code that you have written in the past and
consider the following:

* Have you been using functions in your code?
* Are there places where your code is repetitive that would benefit from using
  functions?
* What names have you given your functions?
   * Do your functions names convey any meaning?
   * Can you understand what your functions do from their names and the way
     that they are used without needing to look at the code inside the
     functions?
   * What kinds of words are you using for your function names? Are they nouns,
     verbs, adjectives...?
* Are your functions pure or not? Have you been cleanly separating input,
  output and pure functions?
* Can you actually understand your own code that you wrote some time ago? If
  you show it to someone else can they understand it?
* Do any of your functions look like a piece of code that could ever be reused
  as part of a future programming project?
