@def title = "Version control with git and github"

# Version control with git

## Outline

Topics:

* Version control
* Using git
* Github


# Git

* Version constrol system
* Useful for collaborating on large codebases
* Originally for Linux code (30 million lines)
* Created by [Linus Torvalds](https://en.wikipedia.org/wiki/Linus_Torvalds)
* [Rant](http://lkml.iu.edu/hypermail/linux/kernel/1707.3/02367.html)


## Github

* Provides a remote git server for free
* Has a web front-end for navigating the code
* Makes it easy to fork and open pull requests
* More on this later...

## Example - CPython

The code for Python itself is kept under version control using git and hosted
on github:

[https://github.com/python/cpython](https://github.com/python/cpython)


## Start a git project

* Create repo on Github
* Clone the repo

```shell
$ git clone https://github.com/myname/myrepo.git
$ cd myrepo
$ git status
```


## Change the code

```
$ git status       # Check all clean
$ gedit README.md  # Make changes and save
$ git status       # Shows changed files
$ git diff         # Shows the changes
```

```
diff --git a/t.py b/t.py
index c5d61cf..fbcc63c 100644
--- a/t.py
+++ b/t.py
@@ -1,7 +1,7 @@
 def myfunction(x):
     y = 2
     z = 3
-    return y + z - x
+    return [y + z - x]

 # here is some code
```

## Commit the changes

```shell
$ git status
$ git diff
$ git add README.md   # Tell git you want to commit
$ git commit -m "Add installation instructions in README"
```

## Commit history

Commits represent the history of your work

```
          initial commit -- A -- B -- C -- HEAD
```

Use `git log` to see the history (or look on github)

## Committing

* Always check (`status/diff`) before committing.
* Git saves the commit as a "version" of your code.
* Can make more changes and commits after
* Use good commit messages

## Push/pull

* Git stores commits in the `.git` folder.
* Use push to send them to github

```
$ git status   # Always check clean first
$ git log      # What am I pushing?
$ git push
```

Get changes *from* github:
```
$ git pull
```

## Push/pull

Send commits to and from github

```
push/pull
                               push
                           ----------->
          your computer                    github
                           <-----------
                               pull
```


## Git

* Stores every commit forever
* Use `git log` to see commits
* Can switch to old commits (`git checkout ab1234`)
* Use `git checkout master` to get to latest commit


# That's all
