# Version control with git

In this unit we want you to learn and use version control with `git`. There
are many resources already available for you to learn about this. Here I will
just explain the basic terminology.  You have probably heard people talk about
git/github/bitbucket etc. before without knowing what they were talking about.
There are a few related concepts here and it's easy to get them mixed up.

Firstly `git` is a couple of programs used for *version control*. Version
control is a way of systematically keeping track of your code making it easy
to:

1. Store multiple versions of your code
2. Undo changes to your code
3. Use (and edit) the same code in different places
4. Collaborate with other people using the same code

There are many different version control systems and as far as I can tell
`git` is the most popular for programmers. I personally use it for almost all
of my work. Specifically `git` is a command line program that you run from the
terminal. There are graphical `git` programs but I recommend learning at least
the basics of the command line version first since this is what is most often
used.

You can use `git` to keep track of the files on your computer. However it is
more often used to keep track of files across many computers (and between
different people). For this you will usually want to have a git `server`. When
you have access to a git server it is possible to `push` and `pull` your code
to and from the server. This enables you to store your code in one central
place but also use it in many other places.

There are *git hosting* companies, for example [github](https://github.com/)
and [bitbucket](https://bitbucket.org/product), that provide free git servers
that you can use if you open an account. These not only provide git servers
but also a web interface for viewing your code and convenient ways to
collaborate your code with other people (such as discussion pages, pull
requests, etc).

The python interpreter that we have been using is called CPython. CPython is
developed using GitHub. You can see the GitHub page and view the code for the
interpreter [here](https://github.com/python/cpython). Hopefully that gives
you an idea of what git/GitHub can do for a large code project. Of course we
will usually work on smaller projects but that doesn't stop git being useful.

Now that I've explained briefly explained what git is I want you to work your
way through the [atlassian
tutorial](https://www.atlassian.com/git/tutorials/learn-git-with-bitbucket-cloud).
For now I want you to understand everything in this tutorial except the part
about branches towards the end (feel free to read that but we don't need it
yet).

I will link to some additional resources but please understand that `git` is
more advanced than we really need. It is designed for professional programmers
and has many more commands and functionality than any of you will *ever* want
to use. I personally only know a small subset of its commands and that's still
plenty enough to be very useful.

A good place to look for resources on git is the [bitbucket tutorial
list](https://www.atlassian.com/git/tutorials). There is also the [official
git docs](https://git-scm.com/docs/user-manual.html) which give a more
complete description of the things that git can do - you do not need to read
all of that though!

## Exercises

1. Create a local git repository (create a folder, `cd` in and run `git init`).

2. Create a Python file in that folder and put some code in it. (What does
   `git status` show you now?)

3. Add the file with `git add`. What does `git status` show now?

4. Commit the file and add a commit message e.g. `git commit -m 'Adding some code...'`

5. Make changes to the file and run `git status` again. Now try `git diff` -
   can you understand the output?

6. Repeat these steps a few times until you're familiar i.e.
    1. Change/add files
    2. Run `git status`, `git diff` to see what's changed
    3. Use `git add`, `git commit` to commit the changes

7. Do you understand what `git diff --cached` does? (do you understand the
   difference between the commit, the staging area, and the working tree)?
   Look it up in the linked resources or ask someone...

8. Once you have a few commits use `git log` to to view them.

9. Now try running `git blame` on one of your files.

10. Create an online repo using a git hosting service (You can use bitbucket
    to make both private accounts and private repositories)

11. Link your local git repository with the hosting service (by pushing in all
    the changes - the service should provide instructions for this).

12. Use `git clone` to create a separate local repo in a different location
    from the one you were originally using.

13. Commit changes in one of your local repos, push them to the server and then
    pull them to the other local repo.

14. What happens if you try to push commits from repo A before pulling commits
    pushed by repo B?
