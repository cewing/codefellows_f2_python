***********************************************************
Setting up your Mac for Python and this class
***********************************************************

==================
Getting The Tools
==================

OS-X comes with Python out of the box, but not the full setup you'll need for development, and this class.

**Note**:

If you use ``macports`` or ``homebrew`` to manage \*nix software on your machine, feel free to use those for ``python``, ``git``, etc, as well. If not, then read on.

Python
-------

While OS-X does provide python our of the box -- it tends not to have the latest version, and you really don't want to mess with the system installation. So I recommend installing an independent installation from ``python.org``:

Download and install Python 2.7.8 from Python.org:

https://www.python.org/ftp/python/2.7.8/python-2.7.8-macosx10.6.dmg

Simple as that.

Terminal
---------

The built-in "terminal" application works fine. Find it in:

::

  /Applications/Utilities/Terminal

Drag it to the dock to easy access.

git
----

Get a git client -- the gitHub GUI client may be nice -- I honestly don't know.

There are a coupole options for a commadn line client. The version from:

http://git-scm.com/download/mac

Works great, but you need the XCode command line tools, which you can get from the Apple App Store. This is a good option is you think you'll need a complier at some point anyway.

(If you try running "git" on the command line after installing, it should send you there). 

Warning: it is a BIG download. Once installed, run it so it can initialize itself.

Antoher option is the git client from:

http://sourceforge.net/projects/git-osx-installer/

It's a bigger install, but has everything you need out of teh box -- no need to install XCode.


After either of these is installed, the ``git`` command should work:

.. code-block:: bash

  $ git --version
  git version 1.8.5.2 (Apple Git-48)

pip
---

``pip`` is the Python package installer. Unfortunately, it doesn't come out of the box with Python2.7, so you need to install it:

https://pip.pypa.io/en/latest/installing.html

download ``get-pip.py`` from that site, and run it with python::

  $ python get-pip.py

It should download and install ``pip`` (and ``setuptools``)

You can now use pip to install other packages.

iPython
--------

One we are going to use in class is ``iPython``::

  $ pip install ipython

You should now be able to run ``iPython``::

    $ ipython
	Python 2.7.8 (v2.7.8:ee879c0ffa11, Jun 29 2014, 21:07:35) 
	Type "copyright", "credits" or "license" for more information.

	IPython 2.0.0 -- An enhanced Interactive Python.
	?         -> Introduction and overview of IPython's features.
	%quickref -> Quick reference.
	help      -> Python's own help system.
	object?   -> Details about 'object', use 'object??' for extra details.







