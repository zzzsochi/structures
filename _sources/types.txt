===================
Types of attributes
===================

.. contents::


Standart types
==============
Default argument is took the first parametr in all standart types.
In case the class (not instance) is used, it is emulated
the absent this attribute.

   >>> from structures import *
   >>> class S(Structure):
   ...     d1 = Decimal
   ...     d2 = Decimal('2.62')
   ...
   >>> s = S()
   >>> s.d1
   Traceback (most recent call last):
     ...
   AttributeError: d1
   >>> s.d2
   Decimal('2.62')
   >>> s.d1 = '3.14'
   >>> s.d1
   Decimal('3.14')


A simple types
~~~~~~~~~~~~~~
+---------+-----------------+
|  Type   |       func      |
+=========+=================+
| Integer |       int       |
+---------+-----------------+
| Float   |      float      |
+---------+-----------------+
| Decimal | decimal.Decimal |
+---------+-----------------+
| Boolean |       bool      |
+---------+-----------------+
| Bytes   |       bytes     |
+---------+-----------------+
| Binary  |    deprecated   |
+---------+-----------------+
| String  |       str       |
+---------+-----------------+

Integer *(default=NoDefault)*
+++++++++++++++++++++++++++++
**int** is used for casting. It's used base 10 for strings.

Float *(default=NoDefault)*
+++++++++++++++++++++++++++
**float** is used for casting.

Decimal *(default=NoDefault)*
+++++++++++++++++++++++++++++
**decimal.Decimal** is used for casting.

Boolean *(default=NoDefault)*
+++++++++++++++++++++++++++++
**bool** is used for casting.

Bytes *(default=NoDefault)*
++++++++++++++++++++++++++++
**bytes** is used for casting.

Binary *(default=NoDefault)*
++++++++++++++++++++++++++++
**Deprecated**. Use `Bytes`.

String *(default=NoDefault, enc="UTF-8")*
+++++++++++++++++++++++++++++++++++++++++
**str** is used for casting.
Value **enc** is the encoding for casting from **bytes**.


Containers
~~~~~~~~~~
+-----------+-----------+
|   Type    |   func    |
+===========+===========+
|   List    |   list    |
+-----------+-----------+
|   Tuple   |   tuple   |
+-----------+-----------+
|   Set     |   set     |
+-----------+-----------+
| FrozenSet | frozenset |
+-----------+-----------+
|   Dict    |   dict    |
+-----------+-----------+

Defult values are recreated in the mutable containers types (*List, Set & Dict*)
during creating the instance of structure.

   >>> from structures import *
   >>> l = [1, 2]
   >>> class S(Structure):
   ...     ll = List(l)
   ... 
   >>> s1 = S()
   >>> s1.ll
   [1, 2]
   >>> assert s1.ll is not l
   >>> assert s1.ll == l
   >>> s2 = S()
   >>> assert s1.ll is not s2.ll
   >>> assert s1.ll == s2.ll


List *(default=NoDefault)*
++++++++++++++++++++++++++
**list** is used for casting.

Tuple *(default=NoDefault)*
+++++++++++++++++++++++++++
**tuple** is used for casting.

Set *(default=NoDefault)*
+++++++++++++++++++++++++
**set** is used for casting.

Dict *(default=NoDefault)*
++++++++++++++++++++++++++
**dict** is used for casting.


Date and time types
~~~~~~~~~~~~~~~~~~~
Value **format** is **time.strftime** formating string.
If it's **None** (default), ISO-like format is used.

DateTime *(default=NoDefault, format=None)*
+++++++++++++++++++++++++++++++++++++++++++
It accepts **datetime.datetime**, **datetime.date** (setting time as *00:00:00*)
and strings.

One of next formats is used for parsing strings if **format** is **None**:

   - ``YYYY-MM-DD HH:MM:SS.mmmmmm``
   - ``YYYY-MM-DDTHH:MM:SS.mmmmmm``
   - ``YYYY-MM-DD HH:MM:SS``
   - ``YYYY-MM-DDTHH:MM:SS``
   - ``YYYY-MM-DD HH:MM``
   - ``YYYY-MM-DDTHH:MM``
   - ``YYYY-MM-DD``

Date *(default=NoDefault, format=None)*
+++++++++++++++++++++++++++++++++++++++
It accepts **datetime.date**, **datetime.datetime** (date is took only)
and strings.

One of next formats is used for parsing strings if **format** is **None**
and date is took only:

   - ``YYYY-MM-DD HH:MM:SS.mmmmmm``
   - ``YYYY-MM-DDTHH:MM:SS.mmmmmm``
   - ``YYYY-MM-DD HH:MM:SS``
   - ``YYYY-MM-DDTHH:MM:SS``
   - ``YYYY-MM-DD HH:MM``
   - ``YYYY-MM-DDTHH:MM``
   - ``YYYY-MM-DD``

Time *(default=NoDefault, format=None)*
+++++++++++++++++++++++++++++++++++++++
It accepts **datetime.time**, **datetime.datetime** (time is took only)
and strings.

One of next formats is used for parsing strings if **format** is **None**
and time is took only:

   - ``YYYY-MM-DD HH:MM:SS.mmmmmm``
   - ``YYYY-MM-DDTHH:MM:SS.mmmmmm``
   - ``YYYY-MM-DD HH:MM:SS``
   - ``YYYY-MM-DDTHH:MM:SS``
   - ``YYYY-MM-DD HH:MM``
   - ``YYYY-MM-DDTHH:MM``
   - ``HH:MM:SS``
   - ``HH:MM``


Building custom types
=====================
Pleace read the **structures.types** module for detals... It's realy simple!
