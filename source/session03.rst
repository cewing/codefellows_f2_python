***********************************************
Session Three: Sequences, Iteration and Strings
***********************************************

Review/Questions
================

Review of Previous Session
--------------------------

.. rst-class:: build

* Functions
* Booleans
* Modules


Homework Review
---------------

.. rst-class:: center large

Any questions that are nagging?


Sequences
=========

.. rst-class:: center large

Ordered collections of objects


What is a Sequence?
-------------------

Remember Duck Typing?  A *sequence* can be considered as anything that supports
*at least* these operations:

.. rst-class:: build

* Indexing
* Slicing
* Membership
* Concatenation
* Length
* Iteration


Sequence Types
--------------

There are seven builtin types in Python that are *sequences*:

* strings
* Unicode strings
* lists
* tuples
* bytearrays
* buffers
* xrange objects

We will start today considering mostly the string types. But what we say here
applies to all the sequence types.


Indexing
--------

Items in a sequence may be looked up by *index* using the subscription
operator: ``[]``

Indexing starts at zero

.. code-block:: ipython

    In [98]: s = u"this is a string"
    In [99]: s[0]
    Out[99]: u't'
    In [100]: s[5]
    Out[100]: u'i'


.. nextslide::

You can use negative indexes to count from the end:

.. code-block:: ipython

    In [105]: s = u"this is a string"
    In [106]: s[-1]
    Out[106]: u'g'
    In [107]: s[-6]
    Out[107]: u's'

.. nextslide::

Indexing beyond the end of a sequence causes an IndexError:

.. code-block:: ipython

    In [4]: s = [0, 1, 2, 3]
    In [5]: s[4]
    ---------------------------------------------------------------------------
    IndexError                                Traceback (most recent call last)
    <ipython-input-5-42efaba84d8b> in <module>()
    ----> 1 s[4]

    IndexError: list index out of range


Slicing
-------

Slicing a sequence creates a new sequence with a range of objects from the
original sequence.

It also uses the subscription operator (``[]``), but with a twist.

``sequence[start:finish]`` returns all sequence[i] for which start <= i < finish:

.. code-block:: ipython

    In [121]: s = "a bunch of words"
    In [122]: s[2]
    Out[122]: 'b'
    In [123]: s[6]
    Out[123]: 'h'
    In [124]: s[2:6]
    Out[124]: 'bunc'
    In [125]: s[2:7]
    Out[125]: 'bunch'

.. nextslide:: Helpful Hint

Think of the indexes as pointing to the spaces between the items::

       a       b   u   n   c   h       o   f
     |   |   |   |   |   |   |   |   |   |
     0   1   2   3   4   5   6   7   8   9



.. nextslide:: Slicing

You do not have to provide both ``start`` and ``finish``:

.. code-block:: ipython

    In [6]: s = u"a bunch of words"
    In [7]: s[:5]
    Out[7]: u'a bun'
    In [8]: s[5:]
    Out[8]: u'ch of words'

Either ``0`` or ``len(s)`` will be assumed, respectively.

As a corollary: ``seq[:b] + seq[b:] == seq``.


.. nextslide:: Slicing

Slicing takes a third argument, ``step`` which controls which items are
returned:

.. code-block:: ipython

    In [289]: string = u"a fairly long string"
    In [290]: string[0:15]
    Out[290]: u'a fairly long s'
    In [291]: string[0:15:2]
    Out[291]: u'afil ogs'
    In [292]: string[0:15:3]
    Out[292]: u'aallg'
    In [293]: string[::-1]
    Out[293]: u'gnirts gnol ylriaf a'


.. nextslide:: Slicing vs. Indexing


Though they share an operator, slicing and indexing have a few important
differences:

Indexing will always return one object, slicing will return a sequence of
objects.

Indexing past the end of a sequence will raise an error, slicing will not:

.. code-block:: ipython

    In [129]: s = "a bunch of words"
    In [130]: s[17]
    ----> 1 s[17]
    IndexError: string index out of range
    In [131]: s[10:20]
    Out[131]: ' words'
    In [132]: s[20:30]
    Out[132]: "


(demo)

Membership
----------

All sequences support the ``in`` and ``not in`` membership operators:

.. code-block:: ipython

    In [15]: s = [1, 2, 3, 4, 5, 6]
    In [16]: 5 in s
    Out[16]: True
    In [17]: 42 in s
    Out[17]: False
    In [18]: 42 not in s
    Out[18]: True

.. nextslide:: Membership in Strings

For strings, the membership operations are like ``substring`` operations in
other languages:

.. code-block:: ipython

    In [20]: s = u"This is a long string"
    In [21]: u"long" in s
    Out[21]: True

This does not work for sub-sequences of other types (can you think of why?):

.. code-block:: ipython

    In [22]: s = [1, 2, 3, 4]
    In [23]: [2, 3] in s
    Out[23]: False


Concatenation
-------------

Using ``+`` or ``*`` on sequences will *concatenate* them:

.. code-block:: ipython

    In [25]: s1 = u"left"
    In [26]: s2 = u"right"
    In [27]: s1 + s2
    Out[27]: u'leftright'
    In [28]: (s1 + s2) * 3
    Out[28]: u'leftrightleftrightleftright'


.. nextslide:: Multiplying and Slicing

You can apply this concatenation to slices as well, leading to some nicely
concise code:

from CodingBat: Warmup-1 -- front3

.. code-block:: python

    def front3(str):
      if len(str) < 3:
        return str+str+str
      else:
        return str[:3]+str[:3]+str[:3]

This non-pythonic solution can also be expressed like so:

.. code-block:: python

    def front3(str):
        return str[:3] * 3

Length
------

All sequences have a length.  You can get it with the ``len`` builtin:

.. code-block:: ipython

    In [36]: s = u"how long is this, anyway?"
    In [37]: len(s)
    Out[37]: 25

Remember, Python sequences are zero-indexed, so the last index in a sequence is
``len(s) - 1``:

.. code-block:: ipython

    In [38]: count = len(s)
    In [39]: s[count]
    ---------------------------------------------------------------------------
    IndexError                                Traceback (most recent call last)
    <ipython-input-39-5a33b9d3e525> in <module>()
    ----> 1 s[count]

    IndexError: string index out of range


Miscellaneous
-------------

There are a more operations supported by all sequences

.. nextslide:: Min and Max

All sequences also support the ``min`` and ``max`` builtins:

.. code-block:: ipython

    In [42]: all_letters = u"thequickbrownfoxjumpedoverthelazydog"
    In [43]: min(all_letters)
    Out[43]: u'a'
    In [44]: max(all_letters)
    Out[44]: u'z'

Why are those the answers you get? (hint: ``ord(u'a')``)


.. nextslide:: Index

All sequences also support the ``index`` method, which returns the index of the
first occurence of an item in the sequence:

.. code-block:: ipython

    In [46]: all_letters.index(u'd')
    Out[46]: 21

This causes a ``ValueError`` if the item is not in the sequence:

.. code-block:: ipython

    In [47]: all_letters.index(u'A')
    ---------------------------------------------------------------------------
    ValueError                                Traceback (most recent call last)
    <ipython-input-47-2db728a46f78> in <module>()
    ----> 1 all_letters.index(u'A')

    ValueError: substring not found

.. nextslide:: Count

A sequence can also be queried for the number of times a particular item
appears:

.. code-block:: ipython

    In [52]: all_letters.count(u'o')
    Out[52]: 4
    In [53]: all_letters.count(u'the')
    Out[53]: 2

This does not raise an error if the item you seek is not present:

.. code-block:: ipython

    In [54]: all_letters.count(u'A')
    Out[54]: 0


In-Class Lab
============

Celebrate Sequences

Exercises
---------

Write some functions that:

  * return a string with the first and last characters exchanged.
  * return a string with every other character removed
  * return a string with the first and last 4 characters removed, and every other char in between
  * return a string reversed (just with slicing)
  * return a string with the middle, then last, then first third in a new order


