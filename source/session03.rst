***********************************************
Session Three: Sequences, Iteration and Strings
***********************************************

Review/Questions
================

Review of Previous Session
--------------------------

.. rst-class:: build

  * Values and Types
  * Expressions
  * Intro to functions

Homework Review
---------------

.. rst-class:: center large

Any questions that are nagging?


Sequences
=========
Sequences are ordered collections of objects

They can be indexed, sliced, iterated over,...

They have a length:  ``len(sequence)`` 

Common sequences (Remember Duck Typing?):


   * strings
   * tuples
   * lists


Indexing
========
square brackets for indexing: ``[]`` 

Indexing starts at zero
::
    

    In [98]: s = "this is a string"
    In [99]: s[0]
    Out[99]: 't'
    In [100]: s[5]
    Out[100]: 'i'



Indexing
========
Negative indexes count from the end

::
    

    In [105]: s = "this is a string"
    In [106]: s[-1]
    Out[106]: 'g'
    In [107]: s[-6]
    Out[107]: 's'



Slices
======
Slicing: Pulling a range out of a sequence
::
    

    sequence[start:finish]
    indexes for which:
    start <= i < finish



Slices
======
::
    

    In [121]: s = "a bunch of words"
    In [122]: s[2]
    Out[122]: 'b'
    In [123]: s[6]
    Out[123]: 'h'
    In [124]: s[2:6]
    Out[124]: 'bunc'
    In [125]: s[2:7]
    Out[125]: 'bunch'



Slices
======
the indexes point to the spaces between the items

::
    

       X   X   X   X   X   X   X   X
     |   |   |   |   |   |   |   |
     0   1   2   3   4   5   6   7



Slices
======
Slicing satisfies nifty properties:

::
    

    len( seq[a:b] ) == b - a
    seq[a:b] + seq[b:c] == seq



Slicing vs. Indexing
====================
Indexing returns a single element
::
    

    In [86]: l
    Out[86]: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    In [87]: type(l)
    Out[87]: list
    In [88]: l[3]
    Out[88]: 3
    In [89]: type( l[3] )
    Out[89]: int



Slicing vs. Indexing
====================
Unless it's a string:
::
    

    In [75]: s = "a string"
    In [76]: s[3]
    Out[76]: 't'
    In [77]: type(s[3])
    Out[77]: str



There is no single character type

Slicing vs. Indexing
====================
Slicing returns a sequence:
::
    

    In [68]: l
    Out[68]: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    In [69]: l[2:4]
    Out[69]: [2, 3]


Even if it's one element long
::
    

    In [70]: l[2:3]
    Out[70]: [2]
    In [71]: type(l[2:3])
    Out[71]: list



Slicing vs. Indexing
====================
Indexing out of range produces an error

::
    

    In [129]: s = "a bunch of words"
    In [130]: s[17]
    ----> 1 s[17]
    IndexError: string index out of range



Slicing just gives you what's there
::
    

    In [131]: s[10:20]
    Out[131]: ' words'
    In [132]: s[20:30]
    Out[132]: "


(demo)

Multiplying and slicing
=======================
from CodingBat: Warmup-1 -- front3
::
    

    def front3(str):
      if len(str) < 3:
        return str+str+str
      else:
        return str[:3]+str[:3]+str[:3]


or
::
    

    def front3(str):
        return str[:3] * 3



Slicing
=======
from CodingBat: Warmup-1 -- ``missing_char``  
::
    

    def missing_char(str, n):
      front = str[0:n]
      l = len(str)-1
      back = str[n+1:l+1]
      return front + back


::
    

    def missing_char(str, n):
        return str[:n] + str[n+1:]



Slicing
=======
you can skip items, too
::
    

    In [289]: string = "a fairly long string"
    In [290]: string[0:15]
    Out[290]: 'a fairly long s'
    In [291]: string[0:15:2]
    Out[291]: 'afil ogs'
    In [292]: string[0:15:3]
    Out[292]: 'aallg'



LAB
===
Write some functions that:

  * return a string with the first and last characters exchanged.
  * return a string with every other character removed
  * return a string with the first and last 4 characters removed, and every other char in between
  * return a string reversed (just with slicing)
  * return a string with the middle, then last, then first third in a new order
