==========================
The **structures** package
==========================

The **structures** package is a library for creating data structures with
type controling and casting. There is wide enough set of data types and
a convenient method of designing of new.
The **structures** are similar to the basicproperty_ but more user-friendly
and readable.

.. _basicproperty: http://python.org/pypi/basicproperty

The full documentation can be found there: http://packages.python.org/structures/0.5

Source code placed on github_.

.. _github: https://github.com/zzzsochi/structures


Concept
=======

All the structures are created from the class inheritance **Structure**: 

    >>> from structures import Structure
    >>> class S(Structure):
    ...     attr = 10
    ... 
    >>> s = S()
    >>> s.attr
    10
    >>> s.attr = 'string'
    >>> s.attr
    'string'

Structures can inherit from other structures.


Types of attributes
~~~~~~~~~~~~~~~~~~~

    >>> from structures import *
    >>> class S(Structure):
    ...     i = Integer
    ...     s = String('string')  # setting default value
    ...
    >>> s = S()
    >>> s.s
    u'string'
    >>> s.i
    Traceback (most recent call last):
     ...
    AttributeError: i

Now, if you assign a values to attributes *s* and *i* it will be
automatically cast to the appropriate types.

    >>> s.i = '13'
    >>> type(s.i), s.i
    (<type 'int'>, 13)
    >>> s.s = 3.14
    >>> type(s.s), s.s
    (<type 'unicode'>, u'3.14')
    >>> s.i = 'not a number'
    Traceback (most recent call last):
     ...
    ValueError: invalid literal for int() with base 10: 'not a number'


Structure can contain other structures
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    >>> from structures import *
    >>> class S(Structure):
    ...     class s(Structure):
    ...         i = Integer(13)
    ...     f = Float(3.14)
    ...     d = Decimal('8.62')
    ...
    >>> s = S()
    >>> isinstance(s.s, Structure)
    True
    >>> s.s.i
    13
    >>> s.s.i = 9.18
    >>> s.s.i
    9
