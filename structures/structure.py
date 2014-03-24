from .descriptors import StructureDescriptor
from .markers import AttributeNotSet, NoDefault
from .fields import Field

__all__ = ['Structure']


class StructureMetaClass(type):
    '''Metaclass for structure'''
    def __init__(cls, name, bases, cls_dict):
        cls.__fields__ = {}

        for base in reversed(bases):
            if hasattr(base, '__fields__'):
                cls.__fields__.update(base.__fields__.copy())

        for attr, field in cls_dict.items():
            if isinstance(field, type) and issubclass(field, Field):
                field = field()

            if hasattr(field, 'contribute_to_structure'):
                field.contribute_to_structure(cls, attr)

            else:
                setattr(cls, attr, field)

        super().__init__(name, bases, cls_dict)

    def contribute_to_structure(substructure, structure, name):
        setattr(structure, name, StructureDescriptor(name, substructure))


class Structure(object, metaclass=StructureMetaClass):
    '''Basic class for building structures of data'''
    def __init__(self):
        self.__data__ = {}
        self.__fields_changed__ = set()

    def __iter__(self):
        for attr in dir(self):
            if not (attr.startswith('__') and attr.endswith('__')):
                try:
                    yield (attr, getattr(self, attr))
                except AttributeError:
                    continue
