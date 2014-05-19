
.. Foundations 2: Python slides file, created by
   hieroglyph-quickstart on Wed Apr  2 18:42:06 2014.

*****************************************************************************
Session Seven: More OO: Special Methods, Properties, class and static methods
*****************************************************************************

===================
More on Subclassing
===================

Overriding __init__
-----------------------

``__init__`` common method to override

You often need to call the super class ``__init__``  as well}

.. code-block:: python  
    
    class Circle(object):
        color = "red"
        def __init__(self, diameter):
            self.diameter = diameter
    ...

    class CircleR(Circle):
        def __init__(self, radius):
            diameter = radius*2
            Circle.__init__(self, diameter)


exception to the "don't change the method signature" rule.


More subclassing
----------------

You can also call the superclass' other methods:

.. code-block:: python  

    class Circle(object):
    ...
        def get_area(self, diameter):
            return math.pi * (diameter/2.0)**2

    class CircleR2(Circle):
    ...
        def get_area(self):
            return Circle.get_area(self, self.radius*2)

There is nothing special about ``__init__``  except that it gets called automatically when a new instance is created.

When to Subclass
----------------

"Is a" relationship: Subclass/inheritance}

"Has a" relationship: Composition}

.. nextslide::

"Is a" vs "Has a"

You may have a class that needs to accumulate an arbitrary number of objects.

A list can do that -- so should you subclass list?

Ask yourself:

* Is your class a list (with some extra functionality)?

or

* Does you class HAVE a list?

You only want to subclass list if your class could be used anywhere a list can be used.

====================
Multiple Inheritance
====================

multiple inheritance
--------------------
Multiple inheritance: Pulling from more than one class

.. code-block:: python  

    class Combined(Super1, Super2, Super3):
        def __init__(self, something, something else):
            Super1.__init__(self, ......)
            Super2.__init__(self, ......)
            Super3.__init__(self, ......)


(calls to the super class ``__init__``  are optional -- case dependent)

.. nextslide::

Attribute resolution -- left to right}

* Is it an instance attribute ?
* Is it a class attribute ?
* Is it a superclass attribute ?
  
   - is the it an attribute of the left-most superclass?
   - is the it an attribute of the next superclass?
   -  and so on up the hierarchy...
  
* Is it a super-superclass attribute ?
* ... also left to right ...

http://python-history.blogspot.com/2010/06/method-resolution-order.html

Mix-ins
-------

Why would you want to do this?}

Hierarchies are not always simple:

* Animal

  * Mammal

    * GiveBirth()
    
  * Bird
    
    * LayEggs()
    
Where do you put a Platypus?

Real World Example: ``FloatCanvas``

New Style classes
-----------------

You will see reference to "new style" classes

These derive from ``object`` 

Introduced in python2.2 to better merge types and classes, and clean up a few things.

Differences in method resolution order and properties.

Mostly the same, often makes no difference.

My advice: always subclass from ``object``.

super
-----

``super()``: use it to call a superclass method, rather than explicitly calling it.

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

Caution: There are some subtle differences with multiple inheritance.

.. nextslide::

Two seminal articles about ``super()``:

"Super Considered Harmful" -- James Knight

https://fuhm.net/super-harmful/

"super() considered super!"  --  Raymond Hettinger

http://rhettinger.wordpress.com/2011/05/26/super-considered-super/}

(Both worth reading....)


