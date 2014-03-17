import decimal
from unittest import TestCase

from structures import *


class IntegerTests(TestCase):
    def setUp(self):
        class TestClass(Structure):
            a1 = Integer
            a2 = Integer(13)
            a3 = Integer('127')

        self.TestClass = TestClass
        self.test1 = TestClass()
        self.test2 = TestClass()

    def test_default(self):
        self.assertFalse(hasattr(self.test1, 'a1'))
        self.assertTrue(hasattr(self.test1, 'a2'))
        self.assertTrue(hasattr(self.test1, 'a3'))

        self.assertFalse(hasattr(self.test2, 'a1'))
        self.assertTrue(hasattr(self.test2, 'a2'))
        self.assertTrue(hasattr(self.test2, 'a3'))

        self.assertEqual(type(self.test1.a2), int)
        self.assertEqual(type(self.test1.a3), int)
        self.assertEqual(type(self.test2.a2), int)
        self.assertEqual(type(self.test2.a3), int)

        self.assertEqual(self.test1.a2, 13)
        self.assertEqual(self.test1.a3, 127)
        self.assertEqual(self.test2.a2, 13)
        self.assertEqual(self.test2.a3, 127)

    def test_setattr_float(self):
        self.test1.a1 = 3.14

        self.assertTrue(hasattr(self.test1, 'a1'))
        self.assertFalse(hasattr(self.test2, 'a1'))

        self.assertEqual(self.test1.a1, 3)
        self.assertEqual(type(self.test1.a1), int)

        self.test1.a2 = 9.82
        self.assertEqual(self.test1.a2, 9)
        self.assertEqual(type(self.test1.a2), int)

    def test_setattr_str(self):
        self.test2.a2 = '127'
        self.assertEqual(self.test2.a2, 127)
        self.assertEqual(type(self.test2.a2), int)

        self.assertFalse(hasattr(self.test1, 'a1'))
        self.assertTrue(hasattr(self.test1, 'a2'))
        self.assertTrue(hasattr(self.test1, 'a3'))

    def test_del(self):
        del self.test1.a1
        self.assertFalse(hasattr(self.test1, 'a1'))
        self.assertTrue(hasattr(self.test1, 'a2'))
        self.assertTrue(hasattr(self.test1, 'a3'))

        del self.test1.a3
        self.assertFalse(hasattr(self.test1, 'a1'))
        self.assertTrue(hasattr(self.test1, 'a2'))
        self.assertFalse(hasattr(self.test1, 'a3'))


class FloatTests(TestCase):
    def setUp(self):
        class TestClass(Structure):
            a1 = Float
            a2 = Float(9.82)
            a3 = Float(13)
            a4 = Float('3.14')

        self.TestClass = TestClass
        self.test1 = TestClass()
        self.test2 = TestClass()

    def test_default(self):
        self.assertFalse(hasattr(self.test1, 'a1'))
        self.assertTrue(hasattr(self.test1, 'a2'))
        self.assertTrue(hasattr(self.test1, 'a3'))
        self.assertTrue(hasattr(self.test1, 'a4'))

        self.assertFalse(hasattr(self.test2, 'a1'))
        self.assertTrue(hasattr(self.test2, 'a2'))
        self.assertTrue(hasattr(self.test2, 'a3'))
        self.assertTrue(hasattr(self.test2, 'a4'))

        self.assertEqual(self.test1.a2, 9.82)
        self.assertEqual(self.test1.a3, 13.0)
        self.assertEqual(type(self.test1.a3), float)
        self.assertEqual(self.test1.a4, 3.14)

        self.assertEqual(self.test2.a2, 9.82)
        self.assertEqual(self.test2.a3, 13.0)
        self.assertEqual(type(self.test2.a3), float)
        self.assertEqual(self.test2.a4, 3.14)

    def test_setattr_int(self):
        self.test1.a1 = 8

        self.assertTrue(hasattr(self.test1, 'a1'))
        self.assertFalse(hasattr(self.test2, 'a1'))

        self.assertEqual(self.test1.a1, 8.0)
        self.assertEqual(type(self.test1.a1), float)

    def test_setattr_float(self):
        self.test1.a2 = '9.82'
        self.assertEqual(self.test1.a2, 9.82)
        self.assertEqual(type(self.test1.a2), float)

        self.test2.a2 = '127'
        self.assertEqual(self.test2.a2, 127.0)
        self.assertEqual(type(self.test2.a2), float)

        self.assertFalse(hasattr(self.test1, 'a1'))
        self.assertTrue(hasattr(self.test1, 'a2'))
        self.assertTrue(hasattr(self.test1, 'a3'))

    def test_del(self):
        del self.test1.a1
        self.assertFalse(hasattr(self.test1, 'a1'))
        self.assertTrue(hasattr(self.test1, 'a2'))
        self.assertTrue(hasattr(self.test1, 'a3'))

        del self.test1.a3
        self.assertFalse(hasattr(self.test1, 'a1'))
        self.assertTrue(hasattr(self.test1, 'a2'))
        self.assertFalse(hasattr(self.test1, 'a3'))


class BooleanTests(TestCase):
    def setUp(self):
        class TestClass(Structure):
            a1 = Boolean
            a2 = Boolean(False)
            a3 = Boolean(True)
            a4 = Boolean('qwerty')
            a5 = Boolean(0)

        self.TestClass = TestClass
        self.test = TestClass()

    def test_default(self):
        self.assertFalse(hasattr(self.test, 'a1'))
        self.assertTrue(hasattr(self.test, 'a2'))
        self.assertTrue(hasattr(self.test, 'a3'))
        self.assertTrue(hasattr(self.test, 'a4'))
        self.assertTrue(hasattr(self.test, 'a5'))

        self.assertEqual(type(self.test.a2), bool)
        self.assertEqual(type(self.test.a3), bool)
        self.assertEqual(type(self.test.a4), bool)
        self.assertEqual(type(self.test.a5), bool)

        self.assertEqual(self.test.a2, False)
        self.assertEqual(self.test.a3, True)
        self.assertEqual(self.test.a4, True)
        self.assertEqual(self.test.a5, False)

    def test_setattr_list(self):
        self.test.a1 = [1, 2, 3]
        self.assertTrue(hasattr(self.test, 'a1'))
        self.assertEqual(type(self.test.a1), bool)
        self.assertEqual(self.test.a1, True)
        self.assertTrue(hasattr(self.test, 'a1'))

    def test_setattr_list_empty(self):
        self.test.a1 = []
        self.assertTrue(hasattr(self.test, 'a1'))
        self.assertEqual(type(self.test.a1), bool)
        self.assertEqual(self.test.a1, False)
        self.assertTrue(hasattr(self.test, 'a1'))

    def test_del(self):
        del self.test.a1
        self.assertFalse(hasattr(self.test, 'a1'))
        self.assertTrue(hasattr(self.test, 'a2'))
        self.assertTrue(hasattr(self.test, 'a3'))

        del self.test.a3
        self.assertFalse(hasattr(self.test, 'a1'))
        self.assertTrue(hasattr(self.test, 'a2'))
        self.assertFalse(hasattr(self.test, 'a3'))


class DecimalTests(TestCase):
    def setUp(self):
        class TestClass(Structure):
            a1 = Decimal
            a2 = Decimal(13)
            a3 = Decimal('3.14')

        self.TestClass = TestClass
        self.test = TestClass()

    def test_default(self):
        self.assertFalse(hasattr(self.test, 'a1'))
        self.assertTrue(hasattr(self.test, 'a2'))
        self.assertTrue(hasattr(self.test, 'a3'))

        self.assertEqual(type(self.test.a2), decimal.Decimal)
        self.assertEqual(type(self.test.a3), decimal.Decimal)

        self.assertEqual(self.test.a2, decimal.Decimal(13))
        self.assertEqual(self.test.a3, decimal.Decimal('3.14'))

    def test_setattr_str(self):
        self.test.a1 = '9.82'
        self.assertTrue(hasattr(self.test, 'a1'))
        self.assertEqual(type(self.test.a1), decimal.Decimal)
        self.assertEqual(self.test.a1, decimal.Decimal('9.82'))

        self.test.a2 = '3.14'
        self.assertEqual(type(self.test.a2), decimal.Decimal)
        self.assertEqual(self.test.a2, decimal.Decimal('3.14'))

        self.assertTrue(hasattr(self.test, 'a1'))
        self.assertTrue(hasattr(self.test, 'a2'))
        self.assertTrue(hasattr(self.test, 'a3'))

    def test_del(self):
        del self.test.a1
        self.assertFalse(hasattr(self.test, 'a1'))
        self.assertTrue(hasattr(self.test, 'a2'))
        self.assertTrue(hasattr(self.test, 'a3'))

        del self.test.a3
        self.assertFalse(hasattr(self.test, 'a1'))
        self.assertTrue(hasattr(self.test, 'a2'))
        self.assertFalse(hasattr(self.test, 'a3'))


class BytesTests(TestCase):
    def setUp(self):
        class TestClass(Structure):
            a1 = Bytes
            a2 = Bytes(b'default_bytes')

        self.TestClass = TestClass
        self.test = TestClass()

    def test_default(self):
        self.assertFalse(hasattr(self.test, 'a1'))
        self.assertTrue(hasattr(self.test, 'a2'))

        self.assertEqual(type(self.test.a2), bytes)
        self.assertEqual(self.test.a2, b'default_bytes')

    def test_setattr_bytes(self):
        self.test.a1 = b'test_data_a1'
        self.assertEqual(type(self.test.a1), bytes)
        self.assertEqual(self.test.a1, b'test_data_a1')

        self.test.a2 = b'test_data_a2'
        self.assertEqual(type(self.test.a2), bytes)
        self.assertEqual(self.test.a2, b'test_data_a2')

    def test_setattr_str(self):
        self.assertRaises(TypeError, setattr, self.test, 'a1', 'test_unicode_data_a1')
        self.assertRaises(TypeError, setattr, self.test, 'a2', 'test_unicode_data_a2')

class StringTests(TestCase):
    def setUp(self):
        class TestClass(Structure):
            a1 = String
            a2 = String(b'ascii_str')
            a3 = String('ascii_unicode')
            a4 = String(13)
            a5 = String(3.14)
            a6 = String(enc='UTF-8')
            a7 = String('\u041f\u0440\u0438\u0432\u0435\u0442')    # 'Привет'
            a8 = String('\u041f\u0440\u0438\u0432\u0435\u0442'.encode('UTF-8'),
                        enc='UTF-8')
            a9 = String(enc='ASCII')

        self.TestClass = TestClass
        self.test = TestClass()

    def test_default(self):
        self.assertFalse(hasattr(self.test, 'a1'))
        self.assertTrue(hasattr(self.test, 'a2'))
        self.assertTrue(hasattr(self.test, 'a3'))
        self.assertTrue(hasattr(self.test, 'a4'))
        self.assertTrue(hasattr(self.test, 'a5'))
        self.assertFalse(hasattr(self.test, 'a6'))
        self.assertTrue(hasattr(self.test, 'a7'))
        self.assertTrue(hasattr(self.test, 'a8'))
        self.assertFalse(hasattr(self.test, 'a9'))

        self.assertEqual(type(self.test.a2), str)
        self.assertEqual(type(self.test.a3), str)
        self.assertEqual(type(self.test.a4), str)
        self.assertEqual(type(self.test.a5), str)
        self.assertEqual(type(self.test.a7), str)
        self.assertEqual(type(self.test.a8), str)

        self.assertEqual(self.test.a2, 'ascii_str')
        self.assertEqual(self.test.a3, 'ascii_unicode')
        self.assertEqual(self.test.a4, '13')
        self.assertEqual(self.test.a5, str(3.14))
        self.assertEqual(self.test.a7, '\u041f\u0440\u0438\u0432\u0435\u0442')
        self.assertEqual(self.test.a8, '\u041f\u0440\u0438\u0432\u0435\u0442')

    def test_setattr_str(self):
        self.test.a4 = '\u041f\u0440\u0438\u0432\u0435\u0442'
        self.assertEqual(type(self.test.a4), str)
        self.assertEqual(self.test.a4, '\u041f\u0440\u0438\u0432\u0435\u0442')

        self.test.a5 = '\u041f\u0440\u0438\u0432\u0435\u0442'.encode('UTF-8')
        self.assertEqual(type(self.test.a5), str)
        self.assertEqual(self.test.a5, '\u041f\u0440\u0438\u0432\u0435\u0442')

    def test_setattr_bytes_error(self):
        self.assertRaises(
            UnicodeDecodeError,
            setattr,
            self.test,
            'a9',
            '\u041f\u0440\u0438\u0432\u0435\u0442'.encode('UTF-8'))

    def test_setattr_bytes_with_enc(self):
        self.test.a1 = b'qwerty'
        self.assertTrue(hasattr(self.test, 'a1'))
        self.assertEqual(type(self.test.a1), str)
        self.assertEqual(self.test.a1, 'qwerty')

    def test_del(self):
        del self.test.a1
        self.assertFalse(hasattr(self.test, 'a1'))
        self.assertTrue(hasattr(self.test, 'a2'))
        self.assertTrue(hasattr(self.test, 'a3'))
        self.assertTrue(hasattr(self.test, 'a4'))
        self.assertTrue(hasattr(self.test, 'a5'))
        self.assertFalse(hasattr(self.test, 'a6'))
        self.assertTrue(hasattr(self.test, 'a7'))
        self.assertTrue(hasattr(self.test, 'a8'))
        self.assertFalse(hasattr(self.test, 'a9'))

        del self.test.a3
        self.assertFalse(hasattr(self.test, 'a1'))
        self.assertTrue(hasattr(self.test, 'a2'))
        self.assertFalse(hasattr(self.test, 'a3'))
        self.assertTrue(hasattr(self.test, 'a4'))
        self.assertTrue(hasattr(self.test, 'a5'))
        self.assertFalse(hasattr(self.test, 'a6'))
        self.assertTrue(hasattr(self.test, 'a7'))
        self.assertTrue(hasattr(self.test, 'a8'))
        self.assertFalse(hasattr(self.test, 'a9'))


class ListTests(TestCase):
    def setUp(self):
        class TestClass(Structure):
            a1 = List
            a2 = List([])
            a3 = List(range(10))

        self.TestClass = TestClass
        self.test1 = TestClass()
        self.test2 = TestClass()

    def test_default(self):
        self.assertFalse(hasattr(self.test1, 'a1'))
        self.assertTrue(hasattr(self.test1, 'a2'))
        self.assertTrue(hasattr(self.test1, 'a3'))

        self.assertIsNot(self.test1.a2, self.test2.a2)
        self.assertIsNot(self.test1.a3, self.test2.a3)

        self.assertEqual(self.test1.a2, [])
        self.assertEqual(self.test1.a3, list(range(10)))

        self.assertEqual(type(self.test1.a2), list)
        self.assertEqual(type(self.test1.a3), list)

    def test_setattr_tuple(self):
        self.test1.a1 = (1, 2, 3)
        self.assertEqual(self.test1.a1, [1, 2, 3])
        self.assertEqual(type(self.test1.a1), list)

    def test_setattr_set(self):
        self.test1.a2 = set([4, 5, 6])
        self.assertEqual(self.test1.a2, [4, 5, 6])
        self.assertEqual(type(self.test1.a2), list)

    def test_setattr_dict(self):
        self.test1.a3 = dict.fromkeys([7, 8, 9])
        self.assertEqual(set(self.test1.a3), set([7, 8, 9]))
        self.assertEqual(type(self.test1.a3), list)

    def test_del(self):
        del self.test1.a1
        self.assertFalse(hasattr(self.test1, 'a1'))
        self.assertTrue(hasattr(self.test1, 'a2'))
        self.assertTrue(hasattr(self.test1, 'a3'))

        del self.test1.a3
        self.assertFalse(hasattr(self.test1, 'a1'))
        self.assertTrue(hasattr(self.test1, 'a2'))
        self.assertFalse(hasattr(self.test1, 'a3'))


class TupleTests(TestCase):
    def setUp(self):
        class TestClass(Structure):
            a1 = Tuple
            a2 = Tuple([])
            a3 = Tuple(range(10))

        self.TestClass = TestClass
        self.test = TestClass()

    def test_default(self):
        self.assertFalse(hasattr(self.test, 'a1'))
        self.assertTrue(hasattr(self.test, 'a2'))
        self.assertTrue(hasattr(self.test, 'a3'))

        self.assertEqual(self.test.a2, ())
        self.assertEqual(self.test.a3, tuple(range(10)))

        self.assertEqual(type(self.test.a2), tuple)
        self.assertEqual(type(self.test.a3), tuple)

    def test_setattr_tuple(self):
        self.test.a1 = (1, 2, 3)
        self.assertEqual(self.test.a1, (1, 2, 3))
        self.assertEqual(type(self.test.a1), tuple)

    def test_setattr_set(self):
        self.test.a2 = set([4, 5, 6])
        self.assertEqual(self.test.a2, (4, 5, 6))
        self.assertEqual(type(self.test.a2), tuple)

    def test_setattr_dict(self):
        self.test.a3 = dict.fromkeys([7, 8, 9])
        self.assertEqual(set(self.test.a3), set([7, 8, 9]))
        self.assertEqual(type(self.test.a3), tuple)

    def test_del(self):
        del self.test.a1
        self.assertFalse(hasattr(self.test, 'a1'))
        self.assertTrue(hasattr(self.test, 'a2'))
        self.assertTrue(hasattr(self.test, 'a3'))

        del self.test.a3
        self.assertFalse(hasattr(self.test, 'a1'))
        self.assertTrue(hasattr(self.test, 'a2'))
        self.assertFalse(hasattr(self.test, 'a3'))


class SetTests(TestCase):
    def setUp(self):
        class TestClass(Structure):
            a1 = Set
            a2 = Set([])
            a3 = Set(range(10))

        self.TestClass = TestClass
        self.test1 = TestClass()
        self.test2 = TestClass()

    def test_default(self):
        self.assertFalse(hasattr(self.test1, 'a1'))
        self.assertTrue(hasattr(self.test1, 'a2'))
        self.assertTrue(hasattr(self.test1, 'a3'))

        self.assertIsNot(self.test1.a2, self.test2.a2)
        self.assertIsNot(self.test1.a3, self.test2.a3)

        self.assertEqual(self.test1.a2, set())
        self.assertEqual(self.test1.a3, set(range(10)))

        self.assertEqual(type(self.test1.a2), set)
        self.assertEqual(type(self.test1.a3), set)

    def test_setattr_set(self):
        self.test1.a1 = set([1, 2, 3])
        self.assertEqual(self.test1.a1, set([1, 2, 3]))
        self.assertEqual(type(self.test1.a1), set)

    def test_setattr_list(self):
        self.test1.a2 = [4, 5, 6]
        self.assertEqual(self.test1.a2, set([4, 5, 6]))
        self.assertEqual(type(self.test1.a2), set)

    def test_setattr_dict(self):
        self.test1.a3 = dict.fromkeys([7, 8, 9])
        self.assertEqual(set(self.test1.a3), set([7, 8, 9]))
        self.assertEqual(type(self.test1.a3), set)

    def test_del(self):
        del self.test1.a1
        self.assertFalse(hasattr(self.test1, 'a1'))
        self.assertTrue(hasattr(self.test1, 'a2'))
        self.assertTrue(hasattr(self.test1, 'a3'))

        del self.test1.a3
        self.assertFalse(hasattr(self.test1, 'a1'))
        self.assertTrue(hasattr(self.test1, 'a2'))
        self.assertFalse(hasattr(self.test1, 'a3'))


class DictTests(TestCase):
    def setUp(self):
        class TestClass(Structure):
            a1 = Dict
            a2 = Dict({})
            a3 = Dict(dict(zip(range(10), range(9, -1, -1))))

        self.TestClass = TestClass
        self.test1 = TestClass()
        self.test2 = TestClass()

    def test_default(self):
        self.assertFalse(hasattr(self.test1, 'a1'))
        self.assertTrue(hasattr(self.test1, 'a2'))
        self.assertTrue(hasattr(self.test1, 'a3'))

        self.assertIsNot(self.test1.a2, self.test2.a2)
        self.assertIsNot(self.test1.a3, self.test2.a3)

        self.assertEqual(self.test1.a2, {})
        self.assertEqual(self.test1.a3, dict(zip(range(10), range(9, -1, -1))))

        self.assertEqual(type(self.test1.a2), dict)
        self.assertEqual(type(self.test1.a3), dict)

    def test_setattr_dict(self):
        self.test1.a1 = {'a': 1, 'b': 2}
        self.assertEqual(self.test1.a1, {'a': 1, 'b': 2})
        self.assertEqual(type(self.test1.a1), dict)

    def test_setattr_list_of_tuples(self):
        self.test1.a2 = zip(['c', 'd'], [3, 4])
        self.assertEqual(self.test1.a2, {'c': 3, 'd': 4})
        self.assertEqual(type(self.test1.a2), dict)

    def test_del(self):
        del self.test1.a1
        self.assertFalse(hasattr(self.test1, 'a1'))
        self.assertTrue(hasattr(self.test1, 'a2'))
        self.assertTrue(hasattr(self.test1, 'a3'))

        del self.test1.a3
        self.assertFalse(hasattr(self.test1, 'a1'))
        self.assertTrue(hasattr(self.test1, 'a2'))
        self.assertFalse(hasattr(self.test1, 'a3'))


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
