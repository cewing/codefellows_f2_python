
.. Foundations 2: Python slides file, created by
   hieroglyph-quickstart on Wed Apr  2 18:42:06 2014.


********************************************************************************************************
Session Five: Advanced Argument passing, List and Dict Comprehensions, Lambda and Functional programming
********************************************************************************************************



================
Review/Questions
================

Review of Previous Class
------------------------

  * Dictionaries
  * Exceptions
  * Files, etc.


Homework review
---------------
  
  Homework Questions?
  
  My Solutions to the dict/set lab:
    

=========================
Advanced Argument Passing
=========================

Keyword arguments
-----------------

When defining a function, you can specify only what you need -- in any order

.. code-block:: ipython

    In [151]: def fun(x,y=0,z=0):
            print x,y,z
       .....:
    In [152]: fun(1,2,3)
    1 2 3
    In [153]: fun(1, z=3)
    1 0 3
    In [154]: fun(1, z=3, y=2)
    1 2 3


.. nextslide::


A Common Idiom:

.. code-block:: python    

    def fun(x, y=None):
        if y is None:
            do_something_different
        go_on_here



.. nextslide::

Can set defaults to variables

.. code-block:: ipython

    In [156]: y = 4
    In [157]: def fun(x=y):
        print "x is:", x
       .....:
    In [158]: fun()
    x is: 4


.. nextslide::

Defaults are evaluated when the function is defined

.. code-block:: ipython
    
    In [156]: y = 4
    In [157]: def fun(x=y):
        print "x is:", x
       .....:
    In [158]: fun()
    x is: 4
    In [159]: y = 6
    In [160]: fun()
    x is: 4



Function arguments in variables
-------------------------------

function arguments are really just
 - a tuple (positional arguments) 
 - a dict (keyword arguments) 

.. code-block:: python

    def f(x, y, w=0, h=0):
        print "position: %s, %s -- shape: %s, %s"%(x, y, w, h)

    position = (3,4)
    size = {'h': 10, 'w': 20}

    >>> f( *position, **size)
    position: 3, 4 -- shape: 20, 10



Function parameters in variables
--------------------------------

You can also pull the parameters out in the function as a tuple and a dict:

.. code-block:: ipython

    def f(*args, **kwargs):
        print "the positional arguments are:", args
        print "the keyword arguments are:", kwargs

    In [389]: f(2, 3, this=5, that=7)
    the positional arguments are: (2, 3)
    the keyword arguments are: {'this': 5, 'that': 7}



LAB
---

Let's do this right now:

keyword arguments

* Write a function that has four optional parameters (with defaults):
  
  - foreground_color
  - background_color
  - link_color
  - visited_link_color
  
* Have it print the colors (use strings for the colors)
* Call it with a couple different parameters set
* Have it pull the parameters out with ``*args, **kwargs`` 


============================
List and Dict Comprehensions
============================

List comprehensions
-------------------
A bit of functional programming


consider this common for loop structure:

.. code-block:: python  

    new_list = []
    for variable in a_list:
        new_list.append(expression)

This can be expressed with a single line using a "list comprehension"

.. code-block:: python

    new_list = [expression for variable in a_list]


.. nextslide::


What about nested for loops?

.. code-block:: python      

    new_list = []
    for var in a_list:
        for var2 in a_list2:
            new_list.append(expression)

Can also be expressed in one line:

.. code-block:: python      

    new_list =  [exp for var in a_list for var2 in a_list2]

You get the "outer product", i.e. all combinations.

(demo)

.. nextslide::

But usually you at least have a conditional in the loop:

.. code-block:: python  

    new_list = []
    for variable in a_list:
        if something_is_true:
            new_list.append(expression)

You can add a conditional to the comprehension:

.. code-block:: python  

    new_list = [expr for var in a_list if something_is_true]



(demo)

.. nextslide::

Examples:

.. code-block:: ipython  

    In [341]: [x**2 for x in range(3)]
    Out[341]: [0, 1, 4]

    In [342]: [x+y for x in range(3) for y in range(5,7)]
    Out[342]: [5, 6, 6, 7, 7, 8]
    
    In [343]: [x*2 for x in range(6) if not x%2]
    Out[343]: [0, 4, 8]



.. nextslide::

Remember this from last week?

.. code-block:: python  

    [name for name in dir(__builtin__) if "Error" in name]
    ['ArithmeticError',
     'AssertionError',
     'AttributeError',
     'BufferError',
     'EOFError',
     ....



Set Comprehensions
------------------

You can do it with sets, too:

.. code-block:: python  

    new_set = { value for variable in a_sequence }


same as for loop:

.. code-block:: python  

    new_set = set()
    for key in a_list:
        new_set.add(value)



.. nextslide::

Example: finding all the vowels in a string...

.. code-block:: ipython      

	In [19]: s = "a not very long string"

	In [20]: vowels = set('aeiou')

	In [21]: { let for let in s if let in vowels }
	Out[21]: {'a', 'e', 'i', 'o'}

Side note: why did I do ``set('aeiou')`` rather than just `aeiou` ?


Dict Comprehensions
-------------------

Also with dictionaries

.. code-block:: python

    new_dict = { key:value for variable in a_sequence}


same as for loop:

.. code-block:: python

    new_dict = {}
    for key in a_list:
        new_dict[key] = value



.. nextslide::

Example

.. code-block:: ipython

    In [22]: { i: "this_%i"%i for i in range(5) }
    Out[22]: {0: 'this_0', 1: 'this_1', 2: 'this_2',
              3: 'this_3', 4: 'this_4'}


(not as useful with the ``dict()``  constructor...)


===================
Anonymous functions
===================

lambda
------

.. code-block:: ipython

    In [171]: f = lambda x, y: x+y
    In [172]: f(2,3)
    Out[172]: 5

Content can only be an expression -- not a statement

Anyone remember what the difference is?


Called "Anonymous": it doesn't need a name.

It's a python object, it can be stored in a list or other container

.. code-block:: ipython

    In [7]: l = [lambda x, y: x+y]
    In [8]: type(l[0])
    Out[8]: function


And you can call it:

.. code-block:: ipython

    In [9]: l[0](3,4)
    Out[9]: 7


Functions as first class objects
---------------------------------

You can do that with "regular" functions too:

.. code-block:: ipython    

    In [12]: def fun(x,y):
       ....:     return x+y
       ....:
    In [13]: l = [fun]
    In [14]: type(l[0])
    Out[14]: function
    In [15]: l[0](3,4)
    Out[15]: 7



======================
Functional Programming
======================

map
---

``map``  "maps" a function onto a sequence of objects -- It applies the function to each item in the list, returning another list


.. code-block:: ipython    

    In [23]: l = [2, 5, 7, 12, 6, 4]
    In [24]: def fun(x):
                 return x*2 + 10
    In [25]: map(fun, l)
    Out[25]: [14, 20, 24, 34, 22, 18]


But if it's a small function, and you only need it once:

.. code-block:: ipython

    In [26]: map(lambda x: x*2 + 10, l)
    Out[26]: [14, 20, 24, 34, 22, 18]


filter
------

``filter``  "filters" a sequence of objects with a boolean function --
It keeps only those for which the function is True

To get only the even numbers:

.. code-block:: ipython

    In [27]: l = [2, 5, 7, 12, 6, 4]
    In [28]: filter(lambda x: not x%2, l)
    Out[28]: [2, 12, 6, 4]



reduce
------

``reduce``  "reduces" a sequence of objects to a single object with a function that combines two arguments

To get the sum:

.. code-block:: ipython

    In [30]: l = [2, 5, 7, 12, 6, 4]
    In [31]: reduce(lambda x,y: x+y, l)
    Out[31]: 36


To get the product:

.. code-block:: ipython

    In [32]: reduce(lambda x,y: x*y, l)
    Out[32]: 20160


Comprehensions
--------------

Couldn't you do all this with comprehensions?

Yes:

.. code-block:: ipython

    In [33]: [x+2 + 10 for x in l]
    Out[33]: [14, 17, 19, 24, 18, 16]
    In [34]: [x for x in l if not x%2]
    Out[34]: [2, 12, 6, 4]


(Except Reduce)

But Guido thinks almost all uses of reduce are really ``sum()`` 

Functional Programming
----------------------

Comprehensions and map, filter, reduce are all "functional programming" approaches}

``map, filter``  and ``reduce``  pre-date comprehensions in Python's history

Some people like that syntax better

And "map-reduce" is a big concept these days for parallel processing of "Big Data" in NoSQL databases.

(Hadoop, MongoDB, etc.)


A bit more about lambda
------------------------

Can also use keyword arguments}

.. code-block:: ipython
    
    In [186]: l = []
    In [187]: for i in range(3):
        l.append(lambda x, e=i: x**e)
       .....:
    In [189]: for f in l:
        print f(3)
    1
    3
    9

Note when the keyword argument is evaluated: this turns out to be very handy!

=========
Homework
=========


List comprehensions
--------------------

Note: this is a bit of a "backwards" exercise --
we show you code, you figure out what it does.

As a result, not much to submit -- but so we can give you credit, submit a file with a solution to the final problem.

.. code-block:: python

	>>> feast = ['lambs', 'sloths', 'orangutans', 'breakfast cereals', 'fruit bats']

	>>> comprehension = [delicacy.capitalize() for delicacy in feast]

What is the output of:

.. code-block:: python

	>>> comprehension[0]
	???

	>>> comprehension[2]
	???

(figure it out before you try it)

2. Filtering lists with list comprehensions


.. code-block:: python

	>>> feast = ['spam', 'sloths', 'orangutans', 'breakfast cereals',
	            'fruit bats']

	>>> comprehension = [delicacy for delicacy in feast if len(delicacy) > 6]

What is the output of:

.. code-block:: python

	>>> len(feast)
	???

	>>> len(comprehension)
	???

(figure it out first!)

3. Unpacking tuples in list comprehensions


.. code-block:: python

	>>> list_of_tuples = [(1, 'lumberjack'), (2, 'inquisition'), (4, 'spam')]

	>>> comprehension = [ skit * number for number, skit in list_of_tuples ]

What is the output of:

.. code-block:: python

	>>> comprehension[0]
	???

	>>> len(comprehension[2])
	???

4. Double list comprehension

.. code-block:: python

	>>> list_of_eggs = ['poached egg', 'fried egg']

	>>> list_of_meats = ['lite spam', 'ham spam', 'fried spam']

	>>> comprehension = [ '{0} and {1}'.format(egg, meat) for egg in list_of_eggs for meat in list_of_meats]

What is the output of:

.. code-block:: python

	>>> len(comprehension)
	???

	>>> comprehension[0]
	???

5. Creating a set with set comprehension


.. code-block:: python

	>>> comprehension = { x for x in 'aabbbcccc'}

What is the output of:

.. code-block:: python

	>>> comprehension
	???

6. Creating a dictionary with dictionary comprehension


.. code-block:: python

	>>> dict_of_weapons = {'first': 'fear', 'second': 'surprise',
	            'third':'ruthless efficiency', 'forth':'fanatical devotion',
	            'fifth': None}

	>>> dict_comprehension = { k.upper(): weapon for k, weapon in dict_of_weapons.iteritems() if weapon}

What is the output of:

.. code-block:: python

>>> 'first' in dict_comprehension
	???

	>>> 'FIRST' in dict_comprehension
	???

	>>> len(dict_of_weapons)
	???

	>>> len(dict_comprehension)
	???


See also:

https://github.com/gregmalcolm/python_koans

https://github.com/gregmalcolm/python_koans/blob/master/python2/koans/about_comprehension.py


7. Count even numbers


(submit this one to gitHub for credit on this assignment)

This is from CodingBat "count_evens" (http://codingbat.com/prob/p189616)

*Using list comprehension*, return the number of even ints in the given array.

Note: the % "mod" operator computes the remainder, e.g. ``5 % 2`` is 1. 

::

    count_evens([2, 1, 2, 3, 4]) → 3
    
    count_evens([2, 2, 0]) → 3
    
    count_evens([1, 3, 5]) → 0
    

.. code-block:: python

    def count_evens(nums):
       one_line_comprehension_here


dict and set comprehensions
----------------------------

Let's revisiting the dict/set lab -- see how much you can do with comprehensions instead. 

Specifically,  look at these:

First a slightly bigger, more interesting (or at least bigger..) dict:

.. code-block:: python

	food_prefs = {"name": u"Chris",
	              u"city": u"Seattle",
	              u"cake": u"chocolate",
	              u"fruit": u"mango",
	              u"salad": u"greek",
	              u"pasta": u"lasagna"}


1. Print the dict by passing it to a string format method, so that you get something like:

"Chris is from Seattle, and he likes chocolate cake, mango fruit, greek salad, and lasagna pasta"

2. Using a list comprehension, build a dictionary of numbers from zero to fifteen and the hexadecimal equivalent (string is fine).

3. Do the previous entirely with a dict comprehension -- should be a one-liner

4. Using the dictionary from item 1: Make a dictionary using the same keys but with the number of 'a's in each value. You can do this either by editing the dict in place, or making a new one. If you edit in place, make a copy first!


5. Create sets s2, s3 and s4 that contain numbers from zero through twenty, divisible 2, 3 and 4.
  
  a. Do this with one set comprehension for each set.
  
  b. What if you had a lot more than 3? -- Don't Repeat Yourself (DRY)
   
   - create a sequence that holds all three sets
   - loop through that sequence to build the sets up -- so no repeated code.

  c. Extra credit:  do it all as a one-liner by nesting a set comprehension in side s list comprehension..(OK, that may be getting carried away!)


lambda and keyword argument magic
-----------------------------------

Write a function that returns a list of n functions,
such that each one, when called, will return the input value,
incremented by an increasing number.

Use a for loop, ``lambda``, and a keyword argument

Not clear? here's what you should get

.. code-block:: ipython

	In [96]: the_list = function_builder(4)
    ### so the_list should contain n functions (callables)

	In [97]: the_list[0](2)
	Out[97]: 2
    ## the zeroth element of the list is a function that add 0
    ## to the input, hence called with 2, returns 2

	In [98]: the_list[1](2)
	Out[98]: 3
	## the 1st element of the list is a function that adds 1
	## to the input value, thus called with 2, returns 3

	In [100]: for f in the_list:
	    print f(5)
	   .....:     
	5
	6
	7
	8
    ### If you loop through them all, and call them, each one adds one more to the input, 5... i.e. the nth function in the list adds n to the input.


Extra credit:

Do it with a list comprehension, instead of a for loop


Recommended Reading
---------------------

* LPTHW: Ex 40 - 45

http://learnpythonthehardway.org/book/

* Dive Into Python: chapter 4, 5

http://www.diveintopython.net/toc/index.html

