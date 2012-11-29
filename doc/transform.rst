===================================================
Transformation structures into a dict and backwards
===================================================

E.g. transfirmation structures into a dict is used
for passing structures to **pickle**...


to_dict(structure)
~~~~~~~~~~~~~~~~~~

The function creates a dict with structure's contents. It works recursively. 

    >>> from structures import *
    >>> class S(Structure):
    ...     class s(Structure):
    ...         i = Integer(13)
    ...     f = Float(3.14)
    ...     l = List([1, set([2, 3])])
    ...
    >>> s = S()
    >>> assert to_dict(s) == {'s': {'i': 13}, 'f': 3.14, 'l': [1, set([2, 3])]}


from_dict(structure_class, data)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The function creates structure **structure_class** from the dict **data**.
It creates substructures appropriate types too i.e. it works recursively.

    >>> from structures import *
    >>> class S(Structure):
    ...     class s(Structure):
    ...         i = Integer(13)
    ...     f = Float(3.14)
    ...     d = Decimal('8.62')
    ...
    >>> s = from_dict(S, {'s': {'i': 26}, 'd': '2.64', 'f': 9.82})
    >>> assert s.f == 9.82
    >>> assert s.s.i == 26
    >>> s.d
    Decimal('2.64')
