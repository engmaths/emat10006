@def title = "Git, github and testing worksheet"

# Git, github and testing

For the remainder of this unit we will assume that you are relatively
comfortable using the terminal to navigate through directories and
perform basic tasks such as running Python scripts. Therefore please
make sure you have attempted the majority of last week's sheet on using
the terminal before attempting the remainder of this sheet.

Also notice that there are some useful links -- including a terminal
commands 'cheat sheet' -- on https://uobfcp.github.io/fcpnotes/\
Today we will be:

1.  making a Github account,

2.  learning basic Git commands, and making our first Git repository,

3.  cloning an existing repository, and learning about testing in
    Python,

4.  getting set-up with Assignment 1 using Github classroom.

## Installing git

**Windows users**: You should have already installed "git bash" last week.
That means that you already have git installed on your computer now.

**OSX users**: Open the terminal and type `git`. If it you see output from git
then it is already installed. Otherwise it should open a messagebox asking if
you want to install the "OSX command line tools": follow the instructions to
install the tools. Then you will have git installed.

**Lab machines** The Linux machines in the lab already have git so you do not
need to install it.

**Other Linux users**: Install using your package manager e.g. `sudo apt install git`.

## Getting a GitHub Account

For the remainder of this unit you will need a GitHub account. Here, we
walk through the process of getting one using your university email
address. GitHub is the largest host of source code in the world, with
tens of millions of public repositories. It provides remote Git servers
for free, giving users a place to store their repositories online. This
makes it easy to collaborate with other programmers, work remotely, as
well as share code publicly.

1. In a web browser go to [github.com](https://github.com/). You can sign up
   to GitHub directly from the homepage. Enter an appropriate username, your
   university email address (e.g. ab12345\@bristol.ac.uk) and use a suitably
   strong password and click 'Sign up for GitHub'.

2.  **An important note on usernames:** usernames on GitHub are public.
    So while you can use whatever pseudonym you like, it will be visible
    to anyone. Therefore, if you would prefer to remain anonymous,
    choose a random unrecognisable username (but keep a note of what that
    username is!).

3.  Next you may asked to prove you're a human by doing a little
    puzzle\... When you've convinced them you are human, make sure the
    email preferences box is *unchecked* and click 'Next: Select a
    plan'.

4.  Next, make sure that 'Individual' is highlighted, and click the
    'Choose Free' button.

5.  Your account has been created! Scroll down to click 'Skip this step'
    to dodge the questions.

6.  You will now need to check your university email account for a
    verification link. Click on the 'Verify email address' button in the
    email to verify your account.

8.  The button will take you to a new repository page, but instead click
    on the tiny image in the top-right of the page and go to Settings.
    From there, go to Emails, and make sure that the box that says 'Keep
    my email addresses private' is *checked*.

9.  Create a personal access token:
    [following the instructions here](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token)

9.  All sorted, you can now move on to making your first repository!

# Our first Git repository

As you know from the lecture, a repository (or repo for short) is where you
store all the files for a particular project. Repos on GitHub have a unique
URL associated with them. If they are public, this means anyone can use this
URL to make their own clone of the code. The user can even make changes and,
if they think other users might also benefit from these changes, they can
  request that the owner incorporates the changes into the repo (a 'pull
  request').

Let's create our first repo, but we will keep ours private for now!

When you are signed in to GitHub, on the homepage, there's a green button on
the left labeled 'Create repository'. Press this and it will take you to a
page where we can make a blank repo.

Give your repo a suitable name (e.g. 'fcp-week14'), and a description if you
like, then make sure the Private option is selected. Tick the 'Initialise this
repository with a README' box, then click 'Create Repository'.

This creates a repo and takes you to that repo's unique page (notice the URL
has the format 'github.com/your\_user\_name/your\_repo\_name'). The only file
in the repo will be a README.md, and it tells you that it was created on the
'Initial commit'. The contents of the README.md is displayed at the bottom. It
is written in 'markdown' (hence the .md file suffix), but you can just think
of it as a txt file with some fancy formatting options similar to html.

There's lots of information on the repo's webpage which we will introduce in
the coming weeks. But first let's add some files and practice committing them
to our repo. First we're going to need a local 'clone' of the repo on our
computer, so that we can add and edit files on our computer before putting
them on the repo.

From the repo page, click the green 'Code' button, and copy the
link that it gives you. Then in a terminal window, navigate to a suitable
place to create a new local repo, such as Documents.  Then type `git clone`
followed by a space and the URL you just copied.

Note at this stage you might find that `git clone` fails saying something like
`authentication failed`. I found that this happened the first time I tried to
clone a repo using a new github account. Running the exact same command again
a second time fixed the problem (no idea why that works!).

If you are in Windows or OSX then in a strange pop-up window you will be asked
to enter your GitHub username and password. You might also need to click
"Authorise credential manager" or something like that...

If you are using the lab machines you will see an error at this point if you
did not previously create a personal access token. If you have created the
token then after running `git clone` you will be asked for your username and
password. The username is your GitHub username and the password should be your
personal access token.

Once you have done that you should see something like this:
```console
$ git clone https://github.com/uob-simon/fcp-week14.git
Cloning into 'fcp-week14'...
remote: Enumerating objects: 3, done.
remote: Counting objects: 100\% (3/3), done.
remote: Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
Unpacking objects: 100\% (3/3), done.
```
This is Git telling us it has succesfully cloned our online repo on GitHub
into a local repo on our computer. While on your computer, a repo is basically
just a folder with a special .git folder in it. If you `cd` into your new repo
and enter `ls -a` you'll see it. Git uses this folder to store all the data it
needs to do its version control magic, but you don't really need to worry
about what's in it.

We can clone any repo we have access to (i.e. if the repo is public, or we are
a collaborator on a private repo) by running `git clone repo_url`. You'll need
to do this to get the code for the assignment!

Okay, so we now have an exact copy of our online repo on our local machine.
These two instances of the repo do not 'sync' automatically like Google Drive
or Microsoft's OneDrive. If we make changes locally, they won't appear in our
online GitHub repo until we explicitly 'push' them there. Equally, if a
collaborator made changes to the GitHub repo, the changes won't appear locally
until we 'pull' them down. This gives us complete control over when and how
the contents of our repo changes.  Let's explore how we push changes from the
computer up to GitHub using Git now. This takes us through a few of the
fundamental Git commands and concepts. First up: making a commit.

# Making your first commit

When you have `cd`'ed into your repo, type `git status` and hit enter. Git
tells us that we are on the master branch (more on this in future weeks) and
that there is nothing to commit, and our working directory is clean.  This is
Git telling us that all is well -- we have not made any changes to the
contents of our new repo.

Let's add a simple Python script to our repo. When inside your repo directory,
type `gedit welcome.py` and copy this very simple script in there and save it:
```console
#! /usr/bin/python3
print("Welcome to my repository")
```
Type `ls` to see the new script, then try the command `git status` again.  You
should see something like:
```console
$ git status
 On branch master
 Untracked files:
   (use "git add <file>..." to include in what will be committed)

  welcome.py
nothing added to commit but untracked files present (use "git add" to track)
```
This essentially says that Git has noticed we have made a new file, but
until we add it using `git add`, Git is not going to do anything with it.

Get used to running `git status` after nearly every new command you enter to
check what Git is seeing, as it tracks changes to files, new files, etc.

So let's take Git's advice and 'add' our new file. Enter the command `git add
welcome.py`. Then try `git status` again. The output from Git now says there
is one new file, welcome.py, which comes under 'Changes to be committed'.

A quick aside: each Git **commit** is a record of what files have changed
since the previous commit. You can think of them as like snapshots of your
repo, which you take regularly to keep a tracked history of how your repo has
changed since it began. They form the foundation of Git's 'version control',
and allow you to go back to a previous state of the repo by going back to a
particular commit.

Back to our file: by adding it, the file is now in the Git 'staging area'. The
staging area is where we put the files that we wish to commit. So the files
listed under 'Changes to be committed:' when we run `git status` are in the
staging area.

Once we are happy with the new / changed files which are in the staging area,
we can make our commit. Type the following and you should see some similar
output:
```console
$ git commit -m "Add a new welcome script"
[master 60d6d24] Add a new welcome script
Committer: Simon Webber <sw1850@it075705.wks.bris.ac.uk>
1 file changed, 2 insertions(+)
create mode 100644 welcome.py
```
The string after the `-m` flag is the commit message. It can be whatever you
like, but it should be short, informative and usually worded like a command
(e.g. starting with "Add \... \", "Change \... \", "Fix \... \"). When you
look back at your commits the message will be included, so you should be able
to understand what state your repo was in just by looking through recent
commit messages. Notice also how Git gives a summary of what has changed: it
tells us one file has been changed, and that in that file there have been 2
'insertions'. Git keeps track of what has changed line-by-line, so these two
insertions refer to the two lines of code we added in our script.

So we've made our first commit! Next -- of course -- we try `git status`
again. You will see something like this:
```console
$ git status
 On branch master
 Your branch is ahead of 'origin/master' by 1 commit.
   (use "git push" to publish your local commits)

nothing to commit, working directory clean
```
This tells us two important things: firstly that our local repo is
now ahead of our online repo (which by default is called
`origin/master`) by the one commit we just made; and also
that our working directory is once again 'clean'. This means there
are no further new changes which require committing as we haven't
changed anything since our most recent commit.

So the current state of our GitHub (remote) repo and our local repo are
different: our local one contains our new welcome script and the remote one
does not. We will push our commit online shortly to bring them back inline,
but first we take a look at a few more important Git commands.

# Viewing diffs and logs

Let's make some changes to our `welcome.py` script, and see what Git can tell
us about those changes. I updated mine to include another print line following
the previous one. Entering `git status` we can see Git has seen the new
changes, and tells us there is a modified file which is not in the staging
area.

Now enter `git diff` and you should see output which looks something like
this:
```console
$ git diff
diff --git a/welcome.py b/welcome.py
index 04b3760..2748ae8 100644
--- a/welcome.py
+++ b/welcome.py
@@ -1,2 +1,3 @@
 #! /usr/bin/venv/python
 print("Welcome to my repository")
+print("There isn't much here yet")
```
That's quite a lot of output even for a small file! The first line, starting
with `diff` tells us the two files which the diff command is comparing:
`a/welcome.py` and `b/welcome.py`. These are the two different versions of our
script. Don't worry too much about the second line. The next two lines
starting with `+++` and `---` are giving us a key to identify either file by.
So changes to `a/welcome.py` will be marked with a plus symbol, and changes to
`b/welcome.py` will be marked with a minus symbol. Next comes the main part of
the diff, the 'diff chunks'. These tell us what is different between the two
versions, and where the difference occurs.  The line with the `@` symbols is
like a summary, and the lines after are the actual changes. Here, we can see
that version `a/welcome.py` has an additional line, denoted by the `+` and the
contents of the line.

**Exercise**: Try changing the file more and viewing the diff each time. What
happens when you modify an existing line and run diff?

The purpose of diffs will become clearer as your projects grow in size and as
you begin to collaborate on code. It gives you an instant way of seeing, for
example, changes a peer has made to a file since a previous commit -- even if
that file is buried among hundreds of other files and folder in your repo. For
now, concentrate on understanding the output it gives you!

Also always make sure to run diff *before* making a commit, to make sure you
aren't accidentally committing silly changes!

**Exercise:** Try changing an existing line and viewing the diff.  Can you see
what I mean by Git working 'line-by-line'?

**Exercise:** Add a new file to your repo (it can be anything -- another
Python script, or just a txt file). Then add and commit your changes, with a
suitable commit message. Make sure you `git status` regularly, and ensure you
understand *all* of what Git is telling you! Once you have committed these
changes, try editing both files and then running `git diff`. Interpret this
output. Also try `git diff welcome.py` to only see the diff for that file.

Note, diffs are opened in a special terminal mode. If you have a line with
just a colon on it that means there is more output to see, just hit enter to
see it. To exit press the Q key.

Now you have made a few commits, try running the command `git log`. This shows
all of your previous commits, with the commit message, who made the commit and
when. If you make regular commits the log should look like a timeline of
changes to your repo.  In the future, we will look at how you can change which
commit Git is looking at, allowing you to go back in the timeline to the state
of the repo at previous commits in your code's log.

Now we have a repo with a bunch of new commits and changes on it. Let's look
at how we now get those changes to our GitHub remote repo.

## Pushing our commits to github

Finally we are ready to push our commits up to our online repo.  Ensure your
working tree is clean when you run `git status`, and that it informs you that
you are a few commits ahead of `origin/master`.

Run the command `git push`, and you will see some output giving information on
the upload.

Check all of your commits have been pushed by running `git status`, you should
now see:
```console
$ git status
On branch master
Your branch is up to date with 'origin/master'.

nothing to commit, working tree clean
```
Now have a look at the changes online by going back to your repo's webpage.
You will see your new files, and next to their filenames, the commit message
belonging to the commit that they were last edited in. So if you did not
change the README.md, it should still say 'Initial commit'. You can also click
on the Commits tab and see all of your commits, similar to running the log
command in the terminal.

So now both of your repos are up-to-date with each other.

## Round up

At this point try playing around with it. Make changes to your code, commit
the changes, push them etc. Check `git log`, `git status` etc. Try to
understand what all of the commands do and familiarise yourself with them.
Check to see if you can see the changes on github.

Try starting again: create a new repo on github, clone the repo, add files,
commit them and push the commits up to github. Can you see your changes on
github?

Look at your repos on github. Explore the information that github has to show
about them. Take a look at a more complicated repo like the
[matplotlib repo](https://github.com/matplotlib/matplotlib).

Try sharing a repo with someone else. You'll need to know their GitHub username
for this. Go to your repo and click "settings" and then "manage access" and
then "invite a collaborator". They will then get an email asking if they want
to collaborate on your repository and if they accept then they should be able
to see your repo on GitHub and they should be albe to clone it with `git
clone`. The two (or more) of you could practice pushing and pulling to the same
repo. If you create your repo as public in the first place then anyone on the
internet will be able to see it but only collaborators will be able to make
changes.

Finally GitHub is a great place to back up all of your work. Why not store all
of your previously created code in a new repo there?

# That's all!
