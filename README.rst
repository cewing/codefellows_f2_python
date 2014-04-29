*********************
Foundations 2: Python
*********************

This repository houses presentations and class materials for the Code Fellows
Foundations 2 course in Python programming.

The documentation is written in `ReStructuredText`_ and output formats are
included for html, epub and `html5slides`_ (via the excellent `hieroglyph`_
package).

.. _ReStructuredText: http://docutils.sourceforge.net/rst.html
.. _html5slides: https://code.google.com/p/io-2012-slides/
.. _hieroglyph: http://docs.hieroglyph.io/en/latest/index.html


Building The Documents
======================

To isolate the packages required to build this documentation from your system
Python, create a `virtualenv`_. I highly recommend using `virtualenvwrapper`_
to manage your virtual environments:


.. code-block:: bash

    $ mkproject cff2py
    New python executable in cff2py/bin/python
    Installing setuptools, pip...done.
    Creating /path/to/projects/cff2py
    Setting project for cff2py to /path/to/projects/cff2py
    [cff2py]$

.. _virtualenv: http://virtualenv.org
.. _virtualenvwrapper: http://virtualenvwrapper.readthedocs.org:


Once a virtual environment is established, clone this repository:

.. code-block:: bash

    
    (cff2py)$ git clone https://github.com/cewing/codefellows_f2_python.git
    ...
    (cff2py)$ cd codefellows_f2_python

Once that is complete, you can install all the required packages with `pip`_:

.. _pip: http://www.pip-installer.org

.. code-block:: bash

    (cff2py)$ pip install -r requirements.txt

Finally, build the documentation using one of the output targets. To build the
plain html version, for example:

.. code-block:: bash

    (cff2py)$ make html
    sphinx-build -b html -d build/doctrees   source build/html
    Running Sphinx v1.2.2
    ...
    build succeeded.

    Build finished. The HTML pages are in build/html.
    (cff2py)$

Or the html5 slides:

.. code-block:: bash

    (cff2py)$ make slides
    sphinx-build -b slides -d build/doctrees   source build/slides
    Running Sphinx v1.2.2
    ...
    Build finished. The HTML slides are in build/slides.


License
=======

Copyright 2014 Christopher Barker and Cris Ewing.

Thanks to Jon Jacky and Brian Dorsey, who developed the materials from which
this course was derived.

This work is licensed under the Creative Commons Attribution-ShareAlike 4.0
International License. To view a copy of this license, visit
http://creativecommons.org/licenses/by-sa/4.0/ or send a letter to Creative
Commons, 444 Castro Street, Suite 900, Mountain View, California, 94041, USA.

A copy of this license in text format is included in this package under the
``docs`` directory
