@def title = "Shell cheatsheet"

# Commands cheatsheet

## Navigation

```shell
$ pwd    # print working directory

$ cd newdir   # change directory to newdir
$ cd          # go to home directory
$ cd -        # go "back"
$ cd ..       # go "up"

$ ls          # list files in current directory
$ ls somedir  # list files in somedir
$ ls -A       # show all files
$ ls -l       # long listing

$ cat filename  # print file in terminal
```

## File manipulation

```shell
$ touch filename  # create empty file
$ mkdir dirname   # create empty directory

$ mv oldname newname   # rename/move file
$ mv filename somedir  # move file into directory
$ mv *.py somedir      # move all .py files into somedir

$ rm filename     # delete file
$ rmdir dirname   # delete empty directory
$ rm -r dirname   # delete directory and all files
$ rm -rf dirname  # (DANGEROUS) force delete everything

$ cp oldname newname     # copy file
$ cp -r oldname newname  # copy directory and contents
$ cp *.py somedir        # copy all .py files to somedir
```

## Python

```shell
$ python                # run Python in interactive mode
$ python3               # run Python 3 (on some systems)
$ python3 myscript.py   # run script with python3

$ chmod +x myscript.py  # make executable (need shebang)
$ ./myscript.py         # run myscript.py
```

## Git commands - creating a repo

Before we can use git commands we need to have a local repo and we need to
`cd` into the repo. We create a repo either by cloning from github or by using
`git init`.

Clone a repo:
```shell
$ git clone https://github.com/myusername/myrepo.git
$ cd myrepo           # go into the directory
```
Create a new repo locally:
```shell
$ mkdir myrepo        # make an empty directory
$ cd myrepo           # go into the directory
$ git init            # initialise repo (creates .git dir)
```

## Git commands

```shell
$ git status          # show current state (e.g. files changed)
$ git log             # show past commits

$ git diff            # show unstaged changes
$ git diff script.py  # show changes for script.py
$ git diff --cached   # show staged changes

$ git add script.py   # add script.py / stage changes
$ git commit -m "My commit message" # commit staged changes

$ git push            # send commits to github
$ git pull            # get commits from github
```

## Git workflows

Make changes and push to github:
```shell
$ cd myrepo           # cd to your local repo
$ git status          # check working directory is clean
$ git pull            # make sure up to date with github

<edit files, test changes are correct, etc>

$ git status          # check which files have been changed
$ git diff            # see what the changes are

<more editing after reviewing the diff?>

$ git add myfile1.py  # stage changes ready for commit
$ git commit -m "Description of changes made"
$ git push            # push the commit(s) to github
```
