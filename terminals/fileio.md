# File input/output

Once again this is described in the [python.org
tutorial](https://docs.python.org/3/tutorial/inputoutput.html) I only want to
add a few things here. As usual there are [exercises](#exercises) at the
bottom of the page.

Depending on what libraries you are using there may be many high-level
convenience functions for quickly loading/saving objects of different types to
or from different file formats. We want to be able to have some understanding
of how to do elementary IO though so please ensure you understand how to work
with Python's file objects (as described in the tutorial). In practice though
when high-level functions for what you want already exist you should use them.

## Exercises

~~~
<ol>
<li>
~~~
Firstly attempt this question without using the
[csv module](https://docs.python.org/3.6/library/csv.html).

Make a function that can read a CSV file like

```text
Name,Grade
Tom,0
Dick,50
Harry,30
```

You should make a function that can read this into

1. A list of lists (including the header line)
2. A list of dicts
3. A dict of lists

The dict keys should be read from the file rather than assumed.

Now repeat the above exercises using the csv module.
~~~
</li>
<li>
~~~
Make a function that can read a Matrix from a CSV file such as

```text
1,2,3
4,5,6
7,8,9
```

Hence make a program that can take the filenames of two matrices on the
command line and multiply/add/subtract them, printing the result to stdout.
When run it should like like:

```bash
$ ./matrix.py A.csv + B.csv
3,4,6
1,2,54
6,3,6
```

~~~
</li>
</ol>
~~~

# Finished?

Make sure you've read through to the end of section 8 in the [python.org
tutorial](https://docs.python.org/3/tutorial/index.html).
