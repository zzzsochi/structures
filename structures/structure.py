from .descriptors import StructureDescriptor
from .markers import AttributeNotSet, NoDefault
from .fields import Field

__all__ = ['Structure']


class StructureMetaClass(type):
    '''Metaclass for structure'''
    def __init__(cls, name, base, cls_dict):
        for attr, field in cls_dict.items():
            if isinstance(field, type) and issubclass(field, Field):
                field = field()

            if hasattr(field, 'contribute_to_structure'):
                field.contribute_to_structure(cls, attr)

            else:
                setattr(cls, attr, field)

    def contribute_to_structure(cls, structure, name):
        setattr(structure, name, StructureDescriptor(name, cls))


class Structure(object, metaclass=StructureMetaClass):
    '''Basic class for building structures of data'''
    def __init__(self):
        self.__data__ = {}

    def __iter__(self):
        for attr in dir(self):
            if not (attr.startswith('__') and attr.endswith('__')):
                try:
                    yield (attr, getattr(self, attr))
                except AttributeError:
                    continue
