# Data structures in Python

Once again these are described in the [python.org
tutorial](https://docs.python.org/3/tutorial/datastructures.html). I only want
to add a few things here. As usual there are [exercises](#exercises) at the
bottom of the page.

## Lists, tuples, sets and dicts

Python has two basic types that take the role that an "array" would have in
some other languages (e.g. C and Java). These are called `list` and `tuple`.
Lists are *mutable* which means they can be modified. You can
insert/remove/append items of a `list`. You can also set items of a list
with the item-setting syntax `mylist[index] = newvalue`. The size of a list
can change.

Tuples are *immutable* which means you cannot do modify them. You can still
get items with `mytuple[index]` but you can't *set* them. This is mainly
useful since immutability leads to *hashability*. The property of being
hashable means that tuples (unlike lists) can be used as keys in other data
structures such as sets and dicts.

A `set` is an unordered collection of unique items, much like the mathematical
concept of a set. We can loop over a set but the items come in an undefined
order. A `dict` is like a set except that each element of the set is a *key*
which is associated with a corresponding *value*.

Here are some examples:

```python
# A list uses square brackets
mylist = [2, 3, 4, 1]

# A tuple uses round brackets (or no brackets)
mytuple = (2, 3, 4, 1)

# A set:uses curly brackets
myset = {2, 3, 4, 1} # same as {1, 2, 3, 4} or set(range(1, 5))

# A dict uses curly brackets and colon separated key:value pairs
mydict = {'Tom':50, 'Dick':60, 'Harry': 0}
```

## Performance

These data structures can often be used in the same ways but have very
different performance characteristics. For example with a list, it is
efficient to add/remove items (changing the size of the list) only at the end
of a large list. Removing an item at the beginning of a list is inefficient.
However sets are efficient at adding/removing any item.

Also we can ask whether `x in d` for any od these data structures `d`. This is
called containment testing; we test of `d` contains `x`. For large lists or
tuples this can be very inefficient as it involves looping through every item.
For sets or dicts this is efficient no matter how big the data structure is.

There are many other possible performance characteristics. You can see a
description of the performance characteristics
[here](https://wiki.python.org/moin/TimeComplexity).

## Exercises

1. Given two lists how do we construct a dict with keys from one and values
   from the other? E.g. if I have `[1, 2, 3]` and `[4, 5, 6]` then I want
   `{1:4, 2:5, 3:6}`.
1. Make a function that turns a dict of lists into a list of dicts. E.g if I
   have `{'a':[1, 2], 'b':[3, 4]}` then I want `[{'a':1, 'b':3}, {'a':2, 'b':4}]`.
1. Given matrices in the form of lists of lists e.g. `[[1, 2, 3], [4, 5, 6],
   [7, 8, 9]]` write a function that can multiply two matrices (returning a
   new matrix).
1. Test the performance of different operations with different types of data
   structures. You can make e.g. a large set with `set(range(N))` for large
   `N` and you may need to test these operations in a loop to ensure that the
   time difference becomes measurable.
1. For *really* large data structures can you see how much memory python is
   using? How much memory does your computer have?

## Finished?

If you're happy with these you can move on to [input/output](../fileio/).
