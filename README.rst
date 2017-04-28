CatsAss
=======

.. image:: https://img.shields.io/pypi/v/CatsAss.svg
        :target: https://pypi.python.org/pypi/CatsAss

Seriously the cats ass. Seriously.

*Now with Colors!*

.. image:: https://github.com/Duroktar/CatsAss/blob/master/images/CatsAss_colorz.png?raw=true

WTF is it?
==========

CatsAss is the cats ass for sneaking cats into your daily workflow. the_cats_ass() introspects
the function you call it from and returns the local variables PrettyPrinted with a Cat! Not
only is the data PrettyPrinted, but you can also add syntax highlighting or create your own custom
KittyPrinter classes!


**So instead of this kinda stuff..**

.. code-block:: python

    def cat_tail_shape_determiner_function(n):
        a, b = 0, 1
        rv = [a]
        while a < n:
           print('a:', a)
           print('b:', b)
           print('rv:', rv)
           a, b = a + b, b
           rv.append(a)
        return rv


**Do this.**

.. code-block:: python

    from catsass import the_cats_ass

    def cat_tail_shape_determiner_function(n):
        a, b = 0, 1
        rv = [a]
        while a < n:
           print( the_cats_ass() )
           a, b = a + b, b
           rv.append(a)
        return rv

----

.. image:: https://github.com/Duroktar/CatsAss/blob/master/images/CatsAss_demo.png?raw=true

**It's the cats ass!!**


Colorz!
-------

*Requires: pygments and crayons packages*

    pip install --user pygments crayons

Just swap out the_cats_ass() with the color cat of your choice!

.. code-block:: python

    from catsass import tuxedo_cat

    def TuxedoCat(n):
        its = [
            "The       ",
            " cats     ",
            "   ass..  ",
            "Seriously."
        ]
       print( tuxedo_cat() )  # See list below for more cats



.. image:: https://github.com/Duroktar/CatsAss/blob/master/images/CatsAss_colorz_dark.png?raw=true

Available colored cats - `calico_cat`, `tuxedo_cat`

- *Minimum terminal width of 80 characters recommended*
- MIT_ licensed

.. _MIT: https://en.wikipedia.org/wiki/MIT_License


Installation
============

**Requires python 3.6**

To install CatsAss, run this command in your terminal:

.. code-block:: console

    $ pip install CatsAss


If you don't have `pip`_ installed, this `Python installation guide`_ can guide
you through the process.

.. _pip: https://pip.pypa.io
.. _Python installation guide: http://docs.python-guide.org/en/latest/starting/installation/


Customization
-------------

The `catsass.PrettyKitty` class can be used directly to produce your own
color combinations or custom titles. In the next release you will be able
to add your own ascii-art and coloring schemes yourself, for now we can
only modify arguments. Here's what's available..

- **colors**: set True to activate colorz
- **coat**: 'calico_colorz' or 'tuxedo_colors'
- **logo_colorz**: 'logo_colorz' or 'dark_logo_colorz'
- **title**: Can be set to any string. defaults to "Meowed with love by Duroktar, 2017"

- **ctx**: when used with the_cats_ass this is filled in with the name of the calling function. But any hashable object works.
- **data**: the actual data you wish to be pretty-printed.

Example:

.. code-block:: python

    from catsass import PrettyKitty

    data = {*zip('abcde', range(5))}

    print(PrettyKitty("Magic!", data, colors=True, coat='tuxedo_colors',
          logo_colorz='dark_logo_colorz', title="Dude, where's my car?")


Bugs
----

CatsAss works by inspecting the stack frames, which isn't always
the right context. In this case it isn't really the cats ass
anymore.. Luckily you can poke the cat in different places
until you get the context you want.

.. code-block:: python

    from catsass import the_cats_ass, comb, Cats


    def long_cat_tail():
        def cat_tail_shape_determiner_function(n):
            a, b = 0, 1
            rv = [a]
            while a < n:
               print( poke_the_cat(Cats.TAIL, catnip=True) )
               a, b = a + b, b
               rv.append(a)
            return rv
        return cat_tail_shape_determiner_function(100)


Issues
------

Deep personal ones, yes.

Coding
------

Duroktar - duroktar@gmail.com


Legal
-----

- The CatsAss logo was created with the help of this great site -
  http://patorjk.com/software/taag/#p=display&f=Graffiti&t=CatsAss

- The ascii-OCTOCAT was taken from https://github.com/audy/catsay, MIT.

- The OCTOCAT design is the exclusive property of GitHub. All rights reserved.

----

*This package was originally created with* PyRelease_ *package maker.* 2017

.. _PyRelease: https://github.com/pyrelease/pyrelease