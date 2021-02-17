EMAT10006: Further Computer Programming\

Week 19 -- Git Branches and Python Classes\

------------------------------------------------------------------------

**Please note, even if you have an extension for Assignment 2, you
should not work on it in this lab. Not completing this worksheet will
put everyone else in your group at a significant disadvantage going
forward into Assignment 3.**

For this week's worksheet, and the final assignment, you will need to
work in groups of four. All the people in your group **must** be in your
TA group. Most TA groups have 8 students, so this should work in most
cases. Where there aren't 8, make sure you check your group sizes with
your TA / Simon or Chanelle before getting started. There should be **no
groups of five or two** and wherever possible, groups should be of
four!\
Your TA has a sheet which needs to be filled out with who is in each
group.\
Today we will be fixing and extending a library database program in your
groups. Along the way we will:

1.  learn to use *branches* in Git to help workflow in larger groups,

2.  practice using classes and inheritance in Python.

Using branches to work simultaneously
=====================================

Many people consider branching to be Git's 'killer feature', and the
main reason why its use is so commonplace in code development. Branching
allows you to diverge from the main development line of some code, and
make changes without messing up the main line. Later, when you and your
collaborators are happy with the changes on the branch, it can be merged
back to the main line of development. Meanwhile other branches may have
been made by others, and by using *pull requests* (a feature of GitHub,
not Git) we can make informed decisions on which branches should be
merged with the master, and when.\
Branches allow us to maintain a robust 'workflow', where all changes to
code are made on copies of the master; this means the master only ever
contains reviewed, finished and bug-free code. Common reasons for
branching might be to fix bugs, or add new features, which is exactly
what we are going to do here.\
From now on, we are never going to commit changes directly to our
master, and we are also never going to push directly to the remote
repo's master! Instead we are going to make branches, where we can write
experimental code without having to worry about messing up the whole
project. We will then use pull-requests to merge our changes once they
are complete.\
As usual, carefully follow through the following steps, making sure you
understand each bullet point beofre moving on to the next. If you are
unsure at any point, discuss it in your group, and ask your TA.

-   First off, accept this 'assignment' on GitHub classroom. **Don't
    worry this isn't an actual, marked assessment** -- it's just an easy
    way to get you the template code. Inside the repo is a part-finished
    and slightly buggy library databasing program, complete with some
    data. Read the program's readme to understand how it works. The
    program makes extensive use of classes and class hierarchy. If you
    need a reminder of scope, inheritance and the object-orientated side
    of Python, then have a look at [[this
    tutorial]{.underline}](https://docs.python.org/3/tutorial/classes.html).

-   Sort out your GitHub Classroom team with all three / four of you in.
    For now, split into two pairs, one pair is going to fix some
    existing bugs in the code and one pair is going to add a new
    feature. Each pair use one just one computer each. Clone the repo so
    there are now three repos in total: one on the bug-fixing pair's
    machine, one on the feature pair's machine, and the remote one on
    GitHub.

-   Your local repos already in fact have a branch! Typing
    `git status`{.text}, you'll notice it tells you you are on a branch
    called master. Git makes this branch when you clone the repo, and
    gives it the default name 'master'. Note that each pair's master
    branch is *their own* master branch, it is not shared, and the
    remote repo has it's own too. GitHub denotes these in a similar way
    to paths on your computer, e.g. `origin/master`{.text} refers to the
    remote repo's master (since by default GitHub calls the remote repo
    'origin').

-   Branches are basically just simple 'pointers', pointing to a
    particular commit in the commit history. If you were to start making
    commits now, the commit that master is pointing to would
    automatically move forward to each new commit. This is how we've
    been working so far.

-   Each pair make a new branch. Do this by using the command
    `git branch branch_name`{.text}, where one pair replaces
    `branch_name`{.text} with `bug-fix`{.text} and the other pair
    replaces it with `new-feature`{.text}. These are the names of your
    branches. This creates a new branch, pointing at the current commit.
    So currently, master and the new branch are both pointing to the
    same commit, the initial commit. Below I'll refer to 'your new
    branch', and I mean either bug-fix or new-feature, whichever you are
    working on.

-   Git keeps track of which branch you are on using a special unique
    pointer called HEAD. HEAD is currently pointing at master, and
    master is pointing at the initial commit.

-   Use the command `git branch -a`{.text} to show all current branches.
    You can see local branches and remote branches. There are also clear
    indications where the HEAD is currently pointing (the asterisk, and
    sometimes colours depending on your terminal).

-   We want to work on our new branches, not on master, so we want HEAD
    to point to your new branch. The command
    `git checkout your_new_branch`{.text} moves the head to point at
    your new branch. Now, whenever you commit any changes, your new
    branch's pointer automatically moves to them, but the master branch
    stays at the initial commit. So if you were to checkout master
    again, the actual files in your local repo would be changed to
    reflect the commit that master was left on. More on this later, for
    now, a quick programming task for both pairs.

**Exercise**\
While on your new branches, either pair should do the following
exercises, making a couple of commits as normal while you do the task.
**But do not push anything yet!**

-   Bug-fix pair: The following four bugs have been identified:

    -   Adding lists of new items makes the old items disappear.

    -   The system does not raise any errors when an item is returned by
        a user who is not listed as the borrower.

    -   The searching ability is not very good. For example, if I search
        for "title=jurassic" it should return only the DVD "Jurassic
        World".

    -   When an item has been reserved by a user and the user then
        requests the item, the system says the item is unavailable
        because it has already been reserved.

-   Feature pair: The library would like to separate fiction and
    non-fiction books. Fiction books should have a genre attribute and
    non-fiction books should have a subject attribute. Please also
    change demo.py to reflect these changes.

Whoever finishes first should carry on with the walkthrough without
waiting for the other pair. I'll refer to those who finish first as Pair
1, and the others as Pair 2.\

-   So now, we're at a point where the master branch of all three repos
    is still pointing at the initial commit, and either pair's new
    branch is pointing to their most recent commit. We now want to merge
    all of these changes, and eventually have one unified master branch
    on the GitHub remote repo.

-   Firstly try switching back to your master branch, using
    `git checkout master`{.text}. Reload the files you changed\... all
    your changes have vanished! This is because you are now looking at
    the code as it was at the initial commit, because that is where
    master is pointing, and HEAD is now pointing at master. You haven't
    lost the changes though, as Git still has those commits. Git has
    just reverted your local repo to look like the commit that master is
    pointing at. What does `git log`{.text} show?

-   Pair 1: You now think the code on your branch is good to go. Push
    your branch up to the remote repo by entering the command
    `git push --set-upstream origin your_new_branch`{.text}. Go onto
    your remote reop's webpage on GitHub, and click branches. You'll see
    your branch there now, which has all your commits since opening the
    branch.

-   Pair 1: Click 'New pull request', enter an informative message if
    you like, then click 'Create new pull request'. Get Pair 2 to stop
    what they're doing, commit any changes to their branch and do the
    next few bullet points.

-   Pair 2: Pair 1 have created a pull request, which means they want to
    merge their branch on the remote repo with the master on the remote
    repo. You should first review their code, to make sure it works and
    doesn't have any bugs! This is good programming practice. To do this
    you will need your local repo to update itself with their new
    branch. Run the command `git fetch`{.text}, which fetches all the
    changes from your upstream, which here is origin (the remote repo on
    GitHub). Notice from the output that is has fetched their new
    branch.

-   Pair 2: Run `git checkout their_new_branch`{.text}, and your repo
    will now look like Pair 1's most recent commit, that they think is
    finished. You can now look at their changes, test out the new
    bug-fix / feature, etc.

-   Both pairs should now discuss the changes, and once everyone is
    happy, Pair 2 should go to the 'Pull requests' tab on the repo's
    webpage, and confirm the pull request, which will merge the branch
    to master on the remote repo. Note: since you are sat next to each
    other you can discuss in person but, when you are not, you can use
    GitHub's comments to discuss the changes.

-   Pair 1: pull down the changes from origin to your master.

-   Pair 2: checkout your master branch, and pull down the changes from
    origin. Now your master has all of Pair 1's changes, and master is
    pointing to the merge commit.

-   Pair 2: now you should merge your master branch into your new
    branch. This will bring Pair 1's changes and attempt to merge them
    with your changes. First checkout your new branch, then run
    `git merge master`{.text}. This will attempt to merge the changes on
    master into your new branch. This may happen automatically or there
    may be merge conflicts which will need resolving. Notice how merges
    have a *direction*. What we have just done is different to merging
    your new branch into master. Check `git log`{.text} to see the merge
    commit.

-   Pair 2: Now finish your changes on your branch. Commit them, push
    the branch up to the remote, create a merge request, and both pairs
    follow through the above instructions the other way around. By the
    end all three master branches should be pointing at the same commit.

**N.B.** You may have noticed how *quick* branching is. It's more
noticeable on larger projects, but branching in using Git is very
efficient and lightweight. Files are never 'copy and pasted' or
duplicated anywhere. Branches are just files containing 40 bytes of
data, identifying which commit that branch is pointing to. Branching
using other version control systems (VCSs) often involves copying all or
most of the project to a new directory, meaning there's considerably
more 'cost' involved with making a branch, or moving between branches.\

Important lessons about workflow
--------------------------------

A *workflow* is an organised and repeatable pattern of working, which
encourages consistency, robustness and is shared by collaborators. The
pattern of work we have just done follows one particular workflow, which
is summarised in the figure below. The boxes are all branches, and you
can think of the arrows as the 'flow of commits' throughout the project,
with the associated Git / GitHub command in blue. Refer back to this
whenever you need to remind yourself of where you should be commiting,
and how.\
Assignment 3 will mark you based on how consistently your group uses
good workflow! We will be able to see how you have used branches by
looking through your merge commits.

![A schematic of the workflow we have used to update the library program
with a new feature and some bug-fixes. Each boxed-off grey region is a
different repo (2 local and one remote), each square inside is a branch
on that repo, and arrows represent how commits move
around.](workflow.pdf){width="90%"}

Some important observations about this workflow:

1.  We never commited any changed directly to our master branch! This is
    good practice, as it means master only ever has code on it which
    have been finished and reviewed. The only way your local master
    should change is by pulling from the remote's master. In the figure,
    the only place commits are actually made (besides merge commits) is
    on your new branches.

2.  From now on **all** changes should you make should be committed to a
    local branch and never to master. This branch should be pushed to
    remote. From here pull requests should be made to the master once
    the feature / bug has been completed.

3.  Again, notice how nothing is pushed directly to master on the remote
    either. This ensures all code which ends up on the master only gets
    there via a pull request which is reviewed by other team members.

New commands
------------

We've seen several new Git commands today, which are summarised here:

1.  `git branch branch_name`{.text}, creates a new branch called
    `branch_name`{.text}. HEAD remains where it was.

2.  `git branch -a`{.text} lists all existing branches, including local
    and remote branches. Also indicates which one HEAD is pointing at.

3.  `git checkout this_branch`{.text} moves HEAD to point at
    `this_branch`{.text}. This is how to move between branches. It's
    important to remember if you move HEAD to a branch which is pointing
    at a different commit to where you were previously, your files will
    be updated to reflect the commit that branch is pointing to.

4.  `git fetch`{.text} updates our local repo by fetching all of the
    latest branches from the remote repo. We can now checkout these
    branches to view branches which have been pushed up. Note no
    branches are merged, this does nothing to your local branches!

5.  `git merge other_branch`{.text} attempts to merge
    `other_branch`{.text} into the branch HEAD is currently pointing to.
    The merge may then go ahead automatically, depending on if there are
    any conflicts.

6.  It's perhaps useful to point out that `git pull`{.text} actually
    just runs `git fetch`{.text}, followed by `git merge`{.text}. So the
    way you will have used it until now, `git pull`{.text} just pulls
    commits from `origin/master`{.text} and immediately tries to merge
    them with your local master.

Further extensions to the library program
=========================================

Further extensions you could make to the library system include:

-   At the moment the system has no way of storing data. Every time
    demo.py is run, a new `Library`{.text} object is created. Can you
    add a way of storing the information so it can be reloaded?

-   Can you create a `User`{.text} class which would store information
    about the user? This would include a unique id number and all the
    items they have borrowed and reserved.

-   The library system is unable to fine users for returning books late.
    Can you add a way of working out how long items have been borrowed
    for, and if user needs to pay a fine.

Note that the above are just examples of some ways that the library
system could be extended, you might have other ideas of a interesting
and useful features. Your group should extend the library program by
adding two new features. Each pair should work on a separate feature and
aim to use the workflow detailed above.
