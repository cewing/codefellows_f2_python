
.. Foundations 2: Python slides file, created by
   hieroglyph-quickstart on Wed Apr  2 18:42:06 2014.

**********************
Session Seven: More OO
**********************

.. rst-class:: large centered

| Multiple Inheritance,
| Properties,
| Class and Static Methods,
| Special and Magic Methods


More on Subclassing
===================

Watch This Video:

http://pyvideo.org/video/879/the-art-of-subclassing

.. rst-class:: left

Seriously, well worth the time.

What's a Subclass For?
----------------------

The most salient points from that video are as follows:

**Subclassing is not for Specialization**

**Subclassing is for Reusing Code**

**Bear in mind that the subclass is in charge**


Multiple Inheritance
--------------------

Multiple inheritance: Inheriting from more than one class

Simply provide more than one parent.

.. code-block:: python

    class Combined(Super1, Super2, Super3):
        def __init__(self, something, something else):
            # some custom initialization here.
            Super1.__init__(self, ......)
            Super2.__init__(self, ......)
            Super3.__init__(self, ......)
            # possibly more custom initialization


(calls to the super class ``__init__``  are optional -- case dependent)

.. nextslide:: Method Resolution Order

.. code-block:: python

    class Combined(Super1, Super2, Super3)

Attributes are located bottom-to-top, left-to-right

* Is it an instance attribute ?
* Is it a class attribute ?
* Is it a superclass attribute ?

  * is the it an attribute of the left-most superclass?
  * is the it an attribute of the next superclass?
  * and so on up the hierarchy...

* Is it a super-superclass attribute ?
* ... also left to right ...

http://python-history.blogspot.com/2010/06/method-resolution-order.html

.. nextslide:: Mix-ins

Provides an subset of expected functionality in a re-usable package.

Why would you want to do this?

Hierarchies are not always simple:

* Animal

  * Mammal

    * GiveBirth()
    
  * Bird
    
    * LayEggs()
    
Where do you put a Platypus?

Real World Example: `FloatCanvas`_

.. _FloatCanvas: https://github.com/svn2github/wxPython/blob/master/3rdParty/FloatCanvas/floatcanvas/FloatCanvas.py#L485

**Careful About This Pattern**


.. nextslide:: New-Style Classes

All the class definitions we've been showing inherit from ``object``.

This is referred to as a "new style" class.

They were introduced in python2.2 to better merge types and classes, and clean
up a few things.

There are differences in method resolution order and properties.

**Always Make New-Style Classes.**

The differences are subtle, and may not appear until they jump up to bite you.


.. nextslide:: ``super()``

``super()``: use it to call a superclass method, rather than explicitly calling
the unbound method on the superclass.

instead of:

.. code-block:: python  

    class A(B):
        def __init__(self, *args, **kwargs)
            B.__init__(self, *argw, **kwargs)
            ...

You can do:

.. code-block:: python  

    class A(B):
        def __init__(self, *args, **kwargs)
            super(A, self).__init__(self, *argw, **kwargs)
            ...

.. nextslide:: Caveats

Caution: There are some subtle differences with multiple inheritance.

You can use explicit calling to ensure that the 'right' method is called.


.. nextslide:: Background

Two seminal articles about ``super()``:

"Super Considered Harmful" -- James Knight

https://fuhm.net/super-harmful/

"super() considered super!"  --  Raymond Hettinger

http://rhettinger.wordpress.com/2011/05/26/super-considered-super/}

(Both worth reading....)


Properties
==========

.. rst-class:: left
.. container::

    One of the strengths of Python is lack of clutter.

    Attributes are simple and concise:

    .. code-block:: ipython

        In [5]: class C(object):
                def __init__(self):
                        self.x = 5
        In [6]: c = C()
        In [7]: c.x
        Out[7]: 5
        In [8]: c.x = 8
        In [9]: c.x
        Out[9]: 8


Getter and Setters?
-------------------

But what if you need to add behavior later?

.. rst-class:: build

* do some calculation
* check data validity
* keep things in sync


.. nextslide::

.. code-block:: ipython

    In [5]: class C(object):
       ...:     def __init__(self):
       ...:         self.x = 5
       ...:     def get_x(self):
       ...:         return self.x
       ...:     def set_x(self, x):
       ...:         self.x = x
       ...:
    In [6]: c = C()
    In [7]: c.get_x()
    Out[7]: 5
    In [8]: c.set_x(8)
    In [9]: c.get_x()
    Out[9]: 8


<shudder> This is ugly and verbose -- `Java`_?

.. _Java: http://dirtsimple.org/2004/12/python-is-not-java.html

.. nextslide:: properties

When (and if) you need them:

.. code-block:: python

    class C(object):
        def __init__(self, x=5):
            self._x = x
        def _getx(self):
            return self._x
        def _setx(self, value):
            self._x = value
        def _delx(self):
            del self._x
        x = property(_getx, _setx, _delx, doc="docstring")

Now the interface is still like simple attribute access!

.. rst-class:: centered small

[demo: :download:`properties_example.py <./supplements/properties_example.py>`]


.. nextslide:: "Read Only" Attributes

Not all the arguments to ``property`` are required.

You can use this to create attributes that are "read only":

.. code-block:: ipython

    In [11]: class D(object):
       ....:     def __init__(self, x=5):
       ....:         self._x = 5
       ....:     def getx(self):
       ....:         return self._x
       ....:     x = property(getx, doc="I am read only")
       ....:
    In [12]: d = D()
    In [13]: d.x
    Out[13]: 5
    In [14]: d.x = 6
    ---------------------------------------------------------------------------
    AttributeError                            Traceback (most recent call last)
    <ipython-input-14-c83386d97be3> in <module>()
    ----> 1 d.x = 6
    AttributeError: can't set attribute

.. nextslide:: Syntactic Sugar
