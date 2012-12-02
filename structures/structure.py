__all__ = ['Descriptor', 'AttributeNotSet', 'Structure']

from .types import Type, NoDefault, NoInitFunc

AttributeNotSet = type('AttributeNotSet', (), {})


class Descriptor(object):
    def __init__(self, name,
                       func=lambda x: x,
                       default=NoDefault,
                       init_func=NoInitFunc):

        self.name = name
        self.func = func
        self.default = default
        self.init_func = init_func

    def __get__(self, instance, owner):
        if instance is not None:
            ret = instance.__data__.get(self.name, self.default)

            if ret is not AttributeNotSet and ret is not NoDefault:
                return ret
            else:
                raise AttributeError(self.name)

        else:
            return self

    def __set__(self, instance, value):
        if isinstance(instance, Structure):
            if value is not AttributeNotSet:
                instance.__data__[self.name] = self.func(value)
            else:
                instance.__data__[self.name] = AttributeNotSet

    def __delete__(self, instance):
        if isinstance(instance, Structure):
            instance.__data__[self.name] = AttributeNotSet


class StructureDescriptor(Descriptor):
    def __init__(self, name, structure_class):
        self.structure_class = structure_class
        super(StructureDescriptor, self).__init__(name)

    def __set__(self, instance, value):
        if isinstance(instance, Structure):
            if isinstance(value, self.structure_class):
                instance.__data__[self.name] = value

            elif value is AttributeNotSet:
                instance.__data__[self.name] = AttributeNotSet

            else:
                raise TypeError('Value must be a type %r, but %r.' %
                                            (self.structure_class, type(value)))

    def __call__(self):
        return self.structure_class()


class StructureMetaClass(type):
    '''Metaclass for structure.'''
    def __init__(cls, name, base, cls_dict):
        for attr, value in cls_dict.items():
            if (isinstance(value, Type) or
                (isinstance(value, type) and issubclass(value, Type))):

                setattr(cls, attr, Descriptor(attr, value.func,
                                                    value.default,
                                                    value.init_func))

            elif isinstance(value, StructureMetaClass):
                setattr(cls, attr, StructureDescriptor(attr, value))

            else:
                setattr(cls, attr, value)


class Structure(object, metaclass=StructureMetaClass):
    '''Basic class for building structures of data.'''
    def __init__(self):
        self.__data__ = {}
        for attr in dir(self):
            if hasattr(self.__class__, attr):
                value = getattr(self.__class__, attr)

                if isinstance(value, StructureDescriptor):
                    setattr(self, attr, value.structure_class())

                elif isinstance(value, Descriptor):
                    desc = getattr(self.__class__, attr)

                    if desc.init_func is not NoInitFunc:
                        default = desc.init_func()
                        if default is not NoDefault:
                            setattr(self, attr, desc.init_func())

                elif isinstance(value, StructureMetaClass):
                    setattr(self, attr, value())

    def __iter__(self):
        for attr in dir(self):
            if not (attr.startswith('__') and attr.endswith('__')):
                try:
                    yield (attr, getattr(self, attr))
                except AttributeError:
                    continue
