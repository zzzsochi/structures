from unittest import TestCase

from structures import *


class StructuresTests(TestCase):
    def test_fields(self):
        class TestClass(Structure):
            integer = Integer(13)

        self.assertEqual(set(TestClass.__fields__), {'integer'})

    def test_inheritance_fields(self):
        class TestClass(Structure):
            integer = Integer(13)

        class InhTestClass(TestClass):
            boolean = Boolean

        self.assertEqual(set(TestClass.__fields__), {'integer'})
        self.assertEqual(set(InhTestClass.__fields__), {'integer', 'boolean'})

    def test_changed_fields(self):
        class TestClass(Structure):
            integer = Integer(13)

        td = TestClass()

        self.assertFalse(td.__fields_changed__)

        td.integer = 26
        self.assertTrue(td.__fields_changed__)
        self.assertEqual(td.__fields_changed__, {'integer'})


class DeeperTests(TestCase):
    def setUp(self):
        class TestClass(Structure):
            integer = Integer(13)

            class sub(Structure):
                integer = Integer(26)
                string = String('qwerty')

        self.TestClass = TestClass
        self.test = TestClass()

    def test_default(self):
        self.assertTrue(hasattr(self.test, 'integer'))
        self.assertTrue(hasattr(self.test, 'sub'))
        self.assertTrue(hasattr(self.test.sub, 'string'))

        self.assertEqual(type(self.test.integer), int)
        self.assertEqual(self.test.integer, 13)
        self.assertEqual(self.test.sub.string, 'qwerty')
        self.assertEqual(type(self.test.sub.string), str)

    def test_setattr(self):
        self.test.sub.string = 127
        self.assertEqual(self.test.sub.string, '127')
        self.assertEqual(type(self.test.sub.string), str)

    def test_setattr_sub(self):
        sub = self.TestClass.sub()
        sub.integer = 3.14
        sub.string = 987
        sub.attr = 'qwerty'

        self.test.sub = sub
        self.assertEqual(self.test.sub.integer, 3)
        self.assertEqual(type(self.test.sub.integer), int)
        self.assertEqual(self.test.sub.string, '987')
        self.assertEqual(type(self.test.sub.string), str)
        self.assertEqual(self.test.sub.attr, 'qwerty')
        self.assertEqual(type(self.test.sub.attr), str)

        self.assertRaises(TypeError, setattr, *(self.test, 'sub', self.TestClass()))


class InheritanceTests(TestCase):
    def setUp(self):
        class TestClass(Structure):
            i = Integer
            s = String('qwerty')
            b = Boolean(True)
            f = Float(3.14)
            v = None

        class SubTestClassA(TestClass):
            l = List([])
            t = Tuple(())

        class SubTestClassB(TestClass):
            d = Dict({})

        self.TestClass = TestClass
        self.SubTestClassA = SubTestClassA
        self.SubTestClassB = SubTestClassB

        self.test = TestClass()
        self.sub_test_a_1 = SubTestClassA()
        self.sub_test_a_2 = SubTestClassA()
        self.sub_test_b = SubTestClassB()

    def test_is(self):
        self.assertIsNot(self.sub_test_a_1.l, self.sub_test_a_2.l)
        self.assertIs(self.sub_test_a_2.t, self.sub_test_a_2.t)

    def test_defaults(self):
        self.assertFalse(hasattr(self.test, 'l'))
        self.assertRaises(AttributeError, getattr, self.test, 'l')
        self.assertFalse(hasattr(self.test, 't'))
        self.assertRaises(AttributeError, getattr, self.test, 't')
        self.assertFalse(hasattr(self.test, 'd'))
        self.assertRaises(AttributeError, getattr, self.test, 'd')

    def test_attrs(self):
        attrs = lambda s: [a for a, v in s]
        self.assertTrue(set(attrs(self.test)).issubset(attrs(self.sub_test_a_1)))
        self.assertTrue(set(attrs(self.test)).issubset(attrs(self.sub_test_a_2)))
        self.assertEqual(set(attrs(self.sub_test_a_1)), set(attrs(self.sub_test_a_2)))
        self.assertTrue(set(attrs(self.test)).issubset(attrs(self.sub_test_b)))

        self.assertRaises(AttributeError, getattr, self.sub_test_a_1, 'd')
        self.assertRaises(AttributeError, getattr, self.sub_test_b, 'l')

    def test_getattrs(self):
        self.assertRaises(AttributeError, getattr, self.sub_test_a_1, 'i')
        self.sub_test_a_1.i = 3.14
        self.assertEqual(self.sub_test_a_1.i, 3)

        self.assertRaises(AttributeError, getattr, self.sub_test_a_2, 'i')
        self.sub_test_a_2.i = 6.28
        self.assertEqual(self.sub_test_a_2.i, 6)

        self.assertRaises(AttributeError, getattr, self.sub_test_b, 'i')
        self.sub_test_b.i = 12.56
        self.assertEqual(self.sub_test_b.i, 12)
