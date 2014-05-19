
.. _unicode_suppliment:

*******
Unicode
*******

==================
Unicode in Python
==================

Background
-----------

A good starting point for Unicode:


The Absolute Minimum Every Software Developer Absolutely,
Positively Must Know About Unicode and Character Sets (No Excuses!)

http://www.joelonsoftware.com/articles/Unicode.html

Go read it!

.. nextslide

Everything is bytes

If it's on disk or transmitted over a network, it's bytes

Python provides some abstractions to make it easier to deal with bytes


.. nextslide


Unicode is a biggie

Strings vs Unicode:

(``str()``  vs. ``bytes()``  vs. ``unicode()``  )

Python 2.x vs 3.x

(actually, dealing with numbers rather than bytes is big -- but we take that for granted)

.. nextslide

Strings are sequences of bytes

Unicode strings are sequences of platonic characters

Platonic characters cannot be written to disk or network!

(ANSI -- one character == one byte -- so easy!)

.. nextslide

The ``unicode``  object lets you work with characters

"Encoding" is converting from a unicode object to bytes

"Decoding" is converting from bytes to a unicode object


.. nextslide

::    

    import codecs
    ord()
    chr()
    unichr()
    str()
    unicode()
    encode()
    decode()


Unicode Literals
----------------

1) Use unicode in your source files:

.. code-block:: python  

    # -*- coding: utf-8 -*-


2) escape the unicode characters:

.. code-block:: python  

    print u"The integral sign: \u222B"
    print u"The integral sign: \N{integral}"


lots of tables of code points online:

http://inamidst.com/stuff/unidata/

sample:``code\hello_unicode.py``

Unicode
-------

Use unicode objects in all your code

(that's why we've been doing ``u"a string"``)

decode on input

encode on output

Many packages do this for you (XML processing, databases, ...)

Gotcha:
  Python has a default encoding (usually ascii)

.. nextslide::

Python Docs Unicode HowTo:

http://docs.python.org/howto/unicode.html

"Reading Unicode from a file is therefore simple:"

.. code-block:: python  

    import codecs
    f = codecs.open('unicode.rst', encoding='utf-8')
    for line in f:
        print repr(line)


Encodings Built-in to Python:

http://docs.python.org/2/library/codecs.html#standard-encodings}

Unicode LAB
-----------

* Find some nifty non-ascii characters you might use.

  - Create a unicode object with them in two different ways.
  - :download:`here  <./hello_unicode.py>` is one example

* Here are two files:

  - :download:`text.utf16  <./text.utf16>`.
  - :download:`text.utf32  <./text.utf32>`.
  - read the contents into unicode objects

* write some of the text from the first exercise to file.

* read that file back in.


(reference: http://inamidst.com/stuff/unidata/)

NOTE: if your terminal does not support unicode -- you'll get an error trying to print. Try a different terminal or IDE, or google for a solution

