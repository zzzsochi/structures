from .markers import AttributeNotSet, NoDefault


class BaseDescriptor(object):
    def __init__(self, name, default=AttributeNotSet):
        self.name = name
        self.default = default

    def __get__(self, instance, owner):
        if instance is not None:
            ret = instance.__data__.get(self.name, self.default)

            if ret is AttributeNotSet or ret is NoDefault:
                raise AttributeError(self.name)
            else:
                return ret

        else:
            return self

    def __set__(self, instance, value):
        if not isinstance(instance, type):
            if value != instance.__data__.get(self.name):
                instance.__fields_changed__.add(self.name)

            if value is not AttributeNotSet:
                instance.__data__[self.name] = value
            else:
                instance.__data__[self.name] = AttributeNotSet
        else:
            setattr(instance, self.name, value)

    def __delete__(self, instance):
        if not isinstance(instance, type):
            instance.__data__[self.name] = AttributeNotSet


class FieldDescriptor(BaseDescriptor):
    def __init__(self, name, field):
        super().__init__(name)
        self.field = field
        self.func = field.func
        self.default = field.default

    def __get__(self, instance, owner):
        if instance is not None and self.name not in instance.__data__:
            instance.__data__[self.name] = self.field.default

        return super().__get__(instance, owner)

    def __set__(self, instance, value):
        if not isinstance(instance, type):
            super().__set__(instance, self.func(value))
        else:
            super().__set__(instance, value)


class StructureDescriptor(BaseDescriptor):
    def __init__(self, name, structure_class):
        super().__init__(name)
        self.structure_class = structure_class

    def __get__(self, instance, owner):
        if instance is not None and self.name not in instance.__data__:
            instance.__data__[self.name] = self.structure_class()

        return super().__get__(instance, owner)


    def __set__(self, instance, value):
        if not isinstance(instance, type):
            if isinstance(value, self.structure_class):
                instance.__data__[self.name] = value

            elif value is AttributeNotSet:
                instance.__data__[self.name] = AttributeNotSet

            else:
                raise TypeError('Value must be a type {!r}, but {!r}.'
                    ''.format(self.structure_class, type(value)))

        else:
            super().__set__(instance, value)

    def __call__(self):
        return self.structure_class()
