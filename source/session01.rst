**************************
Session One: Introductions
**************************

| In which you are introduced to this class, your instructors, your environment
| and your new best friend, Python.

.. image:: /_static/python.png
    :align: center
    :width: 38%

xkcd.com/353

Introduction to Your Instructors
================================

here we are


Introduction to This class
==========================

.. rst-class:: center large

Python Programming


Why Python?
-----------

.. rst-class:: center large

Python Is Versatile


Why Python?
-----------

Used for:

.. rst-class:: build

* CS education (this course!)
* Application scripting (GIS, GNU Radio, Blender...)
* Systems administration and "glue"
* Web applications (Django etc. etc. etc.)
* Scientific/technical computing (a la MATLAB, Mathematica, also BioPython etc. ..)
* Software tools (automated software testing, distributed version control, ...)
* Research (natural language, graph theory, distributed computing, ...)


Why Python?
-----------

Used by:

.. rst-class:: build

* Beginners
* Professional software developers, computer system administrators, ...
* Professionals OTHER THAN computer specialists: biologists, urban planners,
  ...
* You don't need to immerse yourself in Python to be productive


Why Python?
-----------

Gets many things right:

.. rst-class:: build

*  Readable -- looks nice, makes sense
*  No ideology about best way to program -- object-oriented programming,
   functional, etc.
*  No platform preference -- Windows, Mac, Linux, ...
*  Easy to connect to other languages -- C, Fortran - essential for
   science/math
*  Large standard library
*  Even larger network of external packages
*  Countless conveniences, large and small, make it pleasant to work with


What is Python?
---------------

.. rst-class:: build

* Dynamic
* Object oriented
* Byte-compiled
* Interpreted


What is Python?
---------------

.. rst-class:: center large

But what does that mean?


Python Features
---------------

Features:

.. rst-class:: build

* Unlike C, C++, C\#, Java ... More like Ruby, Lisp, Perl, Matlab, Mathematica
  ...
* Dynamic - no type declarations

  * programs are shorter
  * programs are more flexible
  * less code means fewer bugs

* Interpreted - no separate compile, build steps - programming process is
  simpler


What's a Dynamic language
-------------------------

Dynamic typing.

* Type checking and dispatch happen at run-time

.. code-block:: pycon

    >>> x = a + b

.. rst-class:: build

* What is ``a``?
* What is ``b``?
* What does it mean to add them?
* ``a`` and ``b`` can change at any time before this process


What's a Dynamic language
-------------------------

Strong typing.

.. code-block:: pycon

    >>> a = 5
    >>> type(a)
    <type 'int'>
    >>> b = '5'
    >>> type(b)
    <type 'str'>

.. rst-class:: build

* **everything** has a type.
* the *type* of a thing determines what it can do.


Duck Typing
-----------

.. rst-class:: center large

"If it looks like a duck, and quacks like a duck -- it's probably a duck"


Duck Typing
-----------

.. rst-class:: center large

If an object behaves as expected at run-time, it's the right type.


Python Versions
---------------

Python 2.x

.. rst-class:: build

* "Classic" Python
* evolved from original

Python 3.x ("py3k")

.. rst-class:: build

* Updated version
* Removed the "warts"
* Allowed to break code

.. rst-class:: build

(but really not all that different)


Python Versions
---------------

This program uses Python 2.7 not Python 3.

.. rst-class:: build

* Adoption is growing fast
* A few key packages still not supported (https://python3wos.appspot.com/)
* Most code in the wild is still 2.x


Implementations
---------------

* Jython (JVM)
* Iron Python (.NET)
* PyPy -- Python written in Python (actually RPy...)

We will use CPython 2.7 from python.org for this course.













Introduction to Your Environment
================================

A Slide
-------

.. rst-class:: build

* With a few
* Bullets but then again
* Not too many of them














Basic Python Syntax
===================

.. rst-class:: center mlarge

| Expressions, Statements,
| Values, Types, and Symbols


Code structure
--------------

Each line is a piece of code.

Comments:

.. code-block:: pycon

    In [3]: # everything after a '#' is a comment

Expressions:

.. code-block:: pycon

    In [4]: # evaluating an expression results in a value

    In [5]: 3 + 4
    Out[5]: 7


Code structure
--------------

Statements:

.. code-block:: pycon

    In [6]: # statements do not return a value, may contain an expression

    In [7]: print "this"
    this

    In [8]: line_count = 42

    In [9]:


The Print Statement
-------------------

It's kind of obvious, but handy when playing with code:

.. code-block:: pycon

    In [1]: print "something"
    something

You can print multiple things: 

.. code-block:: pycon

    In [2]: print "the value is", 5
    the value is 5


The Print Statement
-------------------

Python automatically adds a newline, which you can suppress with a comma:


.. code-block:: pycon

    In [9]: def no_newline():
       ...:     print "the value is",
       ...:     print 5
       ...:

    In [10]: no_newline()
    the value is 5


The Print Statement
-------------------

Any python object can be printed (though it might not be pretty...)

.. code-block:: pycon

    In [1]: class bar(object):
       ...:     pass
       ...:

    In [2]: print bar
    <class '__main__.bar'>


Code Blocks
-----------

Blocks of code are delimited by a colon and indentation:

.. code-block:: python

    def a_function():
        a_new_code_block
    end_of_the_block

.. code-block:: python

    for i in range(100):
        print i**2

.. code-block:: python

    try:
        do_something_bad()
    except:
        fix_the_problem()


Indentation
-----------

Python uses whitespace to delineate structure.

This means that in Python, whitespace is **significant**.

The standard is to indent with **4 spaces**.

**SPACES ARE NOT TABS**


Indentation
-----------

These two blocks look the same:

.. code-block:: python

    for i in range(100):
        print i**2

.. code-block:: python

    for i in range(100):
        print i**2


Indentation
-----------

But they are not:

.. code-block:: python

    for i in range(100):
    \s\s\s\sprint i**2

.. code-block:: python

    for i in range(100):
    \tprint i**2

**ALWAYS INDENT WITH 4 SPACES**


Indentation
-----------

.. rst-class:: center large

NEVER INDENT WITH TABS


Values
------

.. rst-class:: build

* Values are pieces of unnamed data: ``42, 'Hello, world',``
* In Python, all values are objects

  * Try ``dir(42)``  - lots going on behind the curtain! (demo)

* Every value belongs to a type

  * Try ``type(42)`` - the type of a value determines what it can do (demo)


Values in Action
----------------

An expression is made up of values and operators

.. rst-class:: build

* An expression is evaluated to produce a new value:  ``2 + 2``

  *  The Python interpreter can be used as a calculator to evaluate expressions
     (demo)

* Integer vs. float arithmetic (demo)

  * Python 3 smooths this out
  * Always use ``/`` when you want float results, ``//`` when you want floored results

* Type conversions (demo)

  * This is the source of many errors, especially in handling text
  * Python 3 will not implicitly convert bytes to unicode

* Type errors - checked at run time only (demo)


Symbols
-------

Symbols are how we give names to values (objects).

.. rst-class:: build

* Symbols must begin with an underscore or letter
* Symbols can contain any number of underscores, letters and numbers
* Symbols don't have a type; values do

  * This is why python is 'Dynamic'


Symbols and Type
----------------

Evaluating the type of a *symbol* will return the type of the *value* to which
it is bound.

.. code-block:: pycon

    In [19]: type(42)
    Out[19]: int

    In [20]: type(3.14)
    Out[20]: float

    In [21]: a = 42

    In [22]: b = 3.14

    In [23]: type(a)
    Out[23]: int

    In [25]: a = b

    In [26]: type(a)
    Out[26]: float


Assignment
----------

A *symbol* is **bound** to a *value* with the assignment operator: ``=``

.. rst-class:: build

* This attaches a name to a value
* A value can have many names (or none!)
* Assignment is a statement, it returns no value


Assignment
----------

Evaluating the name will return the value to which it is bound

.. code-block:: pycon

    In [26]: name = "value"

    In [27]: name
    Out[27]: 'value'

    In [28]: an_integer = 42

    In [29]: an_integer
    Out[29]: 42

    In [30]: a_float = 3.14

    In [31]: a_float
    Out[31]: 3.14


In-Place Assignment
-------------------

You can also do "in-place" assignment with ``+=``.

.. code-block:: pycon

    In [32]: a = 1

    In [33]: a
    Out[33]: 1

    In [34]: a = a + 1

    In [35]: a
    Out[35]: 2

    In [36]: a += 1

    In [37]: a
    Out[37]: 3

also: ``-=, *=, /=, **=, \%=``

(not quite -- really in-place assignment for mutables....)


Multiple Assignment
===================

You can assign multiple variables from multiple expressions in one statement

.. code-block:: pycon

    In [48]: x = 2

    In [49]: y = 5

    In [50]: i, j = 2 * x, 3 ** y

    In [51]: i
    Out[51]: 4

    In [52]: j
    Out[52]: 243


Python evaluates all the expressions on the right before doing any assignments


Nifty Python Trick
------------------

Using this feature, we can swap values between two symbols in one statement:

.. code-block:: pycon

    In [51]: i
    Out[51]: 4

    In [52]: j
    Out[52]: 243

    In [53]: i, j = j, i

    In [54]: i
    Out[54]: 243

    In [55]: j
    Out[55]: 4

Multiple assignment and symbol swapping can be very useful in certain contexts


Deleting
--------

You can't actually delete anything in python...

``del``  only unbinds a name.

.. code-block:: ipython

    In [56]: a = 5

    In [57]: b = a

    In [58]: del a

    In [59]: a
    ---------------------------------------------------------------------------
    NameError                                 Traceback (most recent call last)
    <ipython-input-59-60b725f10c9c> in <module>()
    ----> 1 a

    NameError: name 'a' is not defined


Deleting
--------

The object is still there...python will only delete it if there are no
references to it.

.. code-block:: ipython

    In [60]: b
    Out[60]: 5

    In [61]: del b

    In [62]: b
    ---------------------------------------------------------------------------
    NameError                                 Traceback (most recent call last)
    <ipython-input-62-3b5d5c371295> in <module>()
    ----> 1 b

    NameError: name 'b' is not defined


Identity
--------

Every value in Python is an object.

Every object is unique and has a unique *identity*, which you can inspect with
the ``id`` *builtin*:

.. code-block:: pycon

    In [68]: id(i)
    Out[68]: 140553647890984

    In [69]: id(j)
    Out[69]: 140553647884864

    In [70]: new_i = i

    In [71]: id(new_i)
    Out[71]: 140553647890984


Testing Identity
----------------

You can find out if the values bound to two different symbols are the **same
object** using the ``is`` operator:

.. code-block:: pycon

    In [72]: count = 23

    In [73]: other_count = count

    In [74]: count is other_count
    Out[74]: True

    In [75]: count = 42

    In [76]: other_count is count
    Out[76]: False

(demo)


Equality
--------

You can test for the equality of certain values with the ``==`` operator

.. code-block:: pycon

    In [77]: val1 = 20 + 30

    In [78]: val2 = 5 * 10

    In [79]: val1 == val2
    Out[79]: True

    In [80]: val3 = u'50'

    In [81]: val1 = val3
    Out[84]: False

(demo)


Operator Precedence
-------------------

Operator Precedence determines what evaluates first:

.. code-block:: python

    4 + 3 * 5 != (4 + 3) * 5

To force statements to be evaluated out of order, use parentheses.


Common Operator Precedence
--------------------------

Parentheses and Literals:
  ``(), [], {}, ""``

Exponentiation:
  ``**``

Unary Signing:
  ``+x, -x``

Multiplication, Division, Modulus:
  ``*, /, %``

Addition, Subtraction:
  ``+, -``

Bitwise operations:
  ``<<, >>, &, ^, |``

Comparisons:
  ``<, <=, >, >=, !=, ==``

Membership and Identity:
  ``in, not in, is, is not``

Boolean operations:
  ``or, and, not``

Conditionals:
  ``if ... else``

Anonymous Functions:
  ``lambda``


string literals
===============

::
    

    'a string'
    "also a string"
    "a string with an apostophe: isn't it cool?"
    ' a string with an embedded "quote" '
    """ a multi-line
    string
    all in one
    """
    "a string with an \n escaped character"
    
    r'a "raw" string the \n comes through as a \n'
    


key words
=========

 A bunch:


::
    

    and       del       from      not       while
    as        elif      global    or        with
    assert    else      if        pass      yield
    break     except    import    print
    class     exec      in        raise
    continue  finally   is        return
    def       for       lambda    try



and the built-ins..
===================

 Try this:


``>>> dir(__builtins__)`` 

