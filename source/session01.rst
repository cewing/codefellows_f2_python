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

.. rst-class:: build

Python Programming


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

.. rst-class:: build

We will use CPython 2.7 from python.org for this course.













Introduction to Your Environment
================================

A Slide
-------

.. rst-class:: build

* With a few
* Bullets but then again
* Not too many of them


Introduction to Python
======================

A Slide
-------

.. rst-class:: build

* With a few
* Bullets but then again
* Not too many of them


Slide With Bullets
------------------

* One Bullet
* Two Bullets
* Three Bullets

Slide with some Python Code
---------------------------

.. code-block:: python

    from foo import Bar

    sponge = Bar()
    for item in sponge:
        print item

