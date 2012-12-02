'''
In this module defined two function for creating
structures from dict and dict from structures.
It's need for serialize structures.
'''

import decimal

from .structure import Structure
from .structure import StructureDescriptor


__all__ = ['from_dict', 'to_dict']


def from_dict(structure_class, data):
    '''It builds structure from dict.'''
    struct_descs = []

    for desc in dir(structure_class):
        if isinstance(getattr(structure_class, desc), StructureDescriptor):
            struct_descs.append(desc)

    structure = structure_class()

    for attr, value in data.items():
        if isinstance(value, dict) and attr in struct_descs:
            s = from_dict(getattr(structure_class, attr).structure_class, value)
            setattr(structure, attr, s)
        else:
            setattr(structure, attr, value)

    return structure


def _prepare_to_dict(obj):
    '''Prepare object to build dict from structure.'''
    if isinstance(obj, Structure):
        return to_dict(obj)

    elif isinstance(obj, decimal.Decimal):
        return str(obj)

    elif isinstance(obj, list):
        return [_prepare_to_dict(o) for o in obj]

    elif isinstance(obj, tuple):
        return tuple([_prepare_to_dict(o) for o in obj])

    elif isinstance(obj, set):
        return set(_prepare_to_dict(o) for o in obj)

    elif isinstance(obj, frozenset):
        return frozenset(_prepare_to_dict(o) for o in obj)

    elif isinstance(obj, dict):
        return dict(((_prepare_to_dict(k), _prepare_to_dict(v))
                     for k, v in obj.items()))

    else:
        return obj


def to_dict(structure):
    '''It's builds dict from structure.'''
    struct_descs = []

    for desc in dir(structure.__class__):
        if isinstance(getattr(structure.__class__, desc), StructureDescriptor):
            struct_descs.append(desc)

    ret = {}
    for attr, value in structure:
        if attr in struct_descs:
            ret[attr] = to_dict(value)
        else:
            ret[attr] = _prepare_to_dict(value)
    return ret
