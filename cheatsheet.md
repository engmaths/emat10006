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
