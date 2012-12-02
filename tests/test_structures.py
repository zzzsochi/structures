from nose.tools import *

from structures import *


def test_Integer():
    class TestClass(Structure):
        a1 = Integer
        a2 = Integer(13)
        a3 = Integer('127')

    test1 = TestClass()
    test2 = TestClass()

    assert not hasattr(test1, 'a1')
    assert hasattr(test1, 'a2')
    assert hasattr(test1, 'a3')

    assert not hasattr(test2, 'a1')
    assert hasattr(test2, 'a2')
    assert hasattr(test2, 'a3')

    eq_(type(test1.a2), int)
    eq_(type(test1.a3), int)
    eq_(type(test2.a2), int)
    eq_(type(test2.a3), int)

    eq_(test1.a2, 13)
    eq_(test1.a3, 127)
    eq_(test2.a2, 13)
    eq_(test2.a3, 127)

    test1.a1 = 3.14

    assert hasattr(test1, 'a1')
    assert not hasattr(test2, 'a1')

    eq_(test1.a1, 3)
    eq_(type(test1.a1), int)

    test1.a2 = 9.82
    eq_(test1.a2, 9)
    eq_(type(test1.a2), int)

    test2.a2 = '127'
    eq_(test2.a2, 127)
    eq_(type(test2.a2), int)

    assert hasattr(test1, 'a1')
    assert hasattr(test1, 'a2')
    assert hasattr(test1, 'a3')

    del test1.a1
    assert not hasattr(test1, 'a1')
    assert hasattr(test1, 'a2')
    assert hasattr(test1, 'a3')

    del test1.a3
    assert not hasattr(test1, 'a1')
    assert hasattr(test1, 'a2')
    assert not hasattr(test1, 'a3')


def test_Float():
    class TestClass(Structure):
        a1 = Float
        a2 = Float(9.82)
        a3 = Float(13)
        a4 = Float('3.14')

    test1 = TestClass()
    test2 = TestClass()

    assert not hasattr(test1, 'a1')
    assert hasattr(test1, 'a2')
    assert hasattr(test1, 'a3')
    assert hasattr(test1, 'a4')

    assert not hasattr(test2, 'a1')
    assert hasattr(test2, 'a2')
    assert hasattr(test2, 'a3')
    assert hasattr(test2, 'a4')

    eq_(test1.a2, 9.82)
    eq_(test1.a3, 13.0)
    eq_(type(test1.a3), float)
    eq_(test1.a4, 3.14)

    eq_(test2.a2, 9.82)
    eq_(test2.a3, 13.0)
    eq_(type(test2.a3), float)
    eq_(test2.a4, 3.14)

    test1.a1 = 8

    assert hasattr(test1, 'a1')
    assert not hasattr(test2, 'a1')

    eq_(test1.a1, 8.0)
    eq_(type(test1.a1), float)

    test1.a2 = '9.82'
    eq_(test1.a2, 9.82)
    eq_(type(test1.a2), float)

    test2.a2 = '127'
    eq_(test2.a2, 127.0)
    eq_(type(test2.a2), float)

    assert hasattr(test1, 'a1')
    assert hasattr(test1, 'a2')
    assert hasattr(test1, 'a3')

    del test1.a1
    assert not hasattr(test1, 'a1')
    assert hasattr(test1, 'a2')
    assert hasattr(test1, 'a3')

    del test1.a3
    assert not hasattr(test1, 'a1')
    assert hasattr(test1, 'a2')
    assert not hasattr(test1, 'a3')


def test_Boolean():
    class TestClass(Structure):
        a1 = Boolean
        a2 = Boolean(False)
        a3 = Boolean(True)
        a4 = Boolean('qwerty')
        a5 = Boolean(0)

    test = TestClass()

    assert not hasattr(test, 'a1')
    assert hasattr(test, 'a2')
    assert hasattr(test, 'a3')
    assert hasattr(test, 'a4')
    assert hasattr(test, 'a5')

    eq_(type(test.a2), bool)
    eq_(type(test.a3), bool)
    eq_(type(test.a4), bool)
    eq_(type(test.a5), bool)

    eq_(test.a2, False)
    eq_(test.a3, True)
    eq_(test.a4, True)
    eq_(test.a5, False)

    test.a1 = [1, 2, 3]
    assert hasattr(test, 'a1')
    eq_(type(test.a1), bool)
    eq_(test.a1, True)

    test.a1 = []
    assert hasattr(test, 'a1')
    eq_(type(test.a1), bool)
    eq_(test.a1, False)

    assert hasattr(test, 'a1')
    assert hasattr(test, 'a2')
    assert hasattr(test, 'a3')

    del test.a1
    assert not hasattr(test, 'a1')
    assert hasattr(test, 'a2')
    assert hasattr(test, 'a3')

    del test.a3
    assert not hasattr(test, 'a1')
    assert hasattr(test, 'a2')
    assert not hasattr(test, 'a3')


def test_Decimal():
    import decimal

    class TestClass(Structure):
        a1 = Decimal
        a2 = Decimal(13)
        a3 = Decimal('3.14')

    test = TestClass()

    assert not hasattr(test, 'a1')
    assert hasattr(test, 'a2')
    assert hasattr(test, 'a3')

    eq_(type(test.a2), decimal.Decimal)
    eq_(type(test.a3), decimal.Decimal)

    eq_(test.a2, decimal.Decimal(13))
    eq_(test.a3, decimal.Decimal('3.14'))

    test.a1 = '9.82'
    assert hasattr(test, 'a1')
    eq_(type(test.a1), decimal.Decimal)
    eq_(test.a1, decimal.Decimal('9.82'))

    test.a2 = '3.14'
    eq_(type(test.a2), decimal.Decimal)
    eq_(test.a2, decimal.Decimal('3.14'))

    assert hasattr(test, 'a1')
    assert hasattr(test, 'a2')
    assert hasattr(test, 'a3')

    del test.a1
    assert not hasattr(test, 'a1')
    assert hasattr(test, 'a2')
    assert hasattr(test, 'a3')

    del test.a3
    assert not hasattr(test, 'a1')
    assert hasattr(test, 'a2')
    assert not hasattr(test, 'a3')


def test_Bytes():
    class TestClass(Structure):
        a1 = Bytes
        a2 = Bytes(b'default_bytes')

    test = TestClass()

    assert not hasattr(test, 'a1')
    assert hasattr(test, 'a2')

    eq_(type(test.a2), bytes)
    eq_(test.a2, b'default_bytes')

    test.a1 = b'test_data_a1'
    eq_(type(test.a1), bytes)
    eq_(test.a1, b'test_data_a1')

    test.a2 = b'test_data_a2'
    eq_(type(test.a2), bytes)
    eq_(test.a2, b'test_data_a2')

    try:
        test.a1 = 'test_unicode_data_a1'
        raise AssertionError('Must raise TypeError exception.')
    except TypeError:
        pass

    try:
        test.a2 = 'test_unicode_data_a2'
        raise AssertionError('Must raise TypeError exception.')
    except TypeError:
        pass


def test_String():
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

    test = TestClass()

    assert not hasattr(test, 'a1')
    assert hasattr(test, 'a2')
    assert hasattr(test, 'a3')
    assert hasattr(test, 'a4')
    assert hasattr(test, 'a5')
    assert not hasattr(test, 'a6')
    assert hasattr(test, 'a7')
    assert hasattr(test, 'a8')
    assert not hasattr(test, 'a9')

    eq_(type(test.a2), str)
    eq_(type(test.a3), str)
    eq_(type(test.a4), str)
    eq_(type(test.a5), str)
    eq_(type(test.a7), str)
    eq_(type(test.a8), str)

    eq_(test.a2, 'ascii_str')
    eq_(test.a3, 'ascii_unicode')
    eq_(test.a4, '13')
    eq_(test.a5, str(3.14))
    eq_(test.a7, '\u041f\u0440\u0438\u0432\u0435\u0442')
    eq_(test.a8, '\u041f\u0440\u0438\u0432\u0435\u0442')

    test.a4 = '\u041f\u0440\u0438\u0432\u0435\u0442'
    eq_(type(test.a4), str)
    eq_(test.a4, '\u041f\u0440\u0438\u0432\u0435\u0442')

    test.a5 = '\u041f\u0440\u0438\u0432\u0435\u0442'.encode('UTF-8')
    eq_(type(test.a5), str)
    eq_(test.a5, '\u041f\u0440\u0438\u0432\u0435\u0442')

    try:
        test.a9 = '\u041f\u0440\u0438\u0432\u0435\u0442'.encode('UTF-8')
    except UnicodeDecodeError:
        pass
    else:
        raise AssertionError(repr(test.a9))

    test.a1 = b'qwerty'
    assert hasattr(test, 'a1')
    eq_(type(test.a1), str)
    eq_(test.a1, 'qwerty')

    assert hasattr(test, 'a1')
    assert hasattr(test, 'a2')
    assert hasattr(test, 'a3')
    assert hasattr(test, 'a4')
    assert hasattr(test, 'a5')
    assert not hasattr(test, 'a6')
    assert hasattr(test, 'a7')
    assert hasattr(test, 'a8')
    assert not hasattr(test, 'a9')

    del test.a1
    assert not hasattr(test, 'a1')
    assert hasattr(test, 'a2')
    assert hasattr(test, 'a3')
    assert hasattr(test, 'a4')
    assert hasattr(test, 'a5')
    assert not hasattr(test, 'a6')
    assert hasattr(test, 'a7')
    assert hasattr(test, 'a8')
    assert not hasattr(test, 'a9')

    del test.a3
    assert not hasattr(test, 'a1')
    assert hasattr(test, 'a2')
    assert not hasattr(test, 'a3')
    assert hasattr(test, 'a4')
    assert hasattr(test, 'a5')
    assert not hasattr(test, 'a6')
    assert hasattr(test, 'a7')
    assert hasattr(test, 'a8')
    assert not hasattr(test, 'a9')


def test_List():
    class TestClass(Structure):
        a1 = List
        a2 = List([])
        a3 = List(range(10))

    test1 = TestClass()
    test2 = TestClass()

    assert not hasattr(test1, 'a1')
    assert hasattr(test1, 'a2')
    assert hasattr(test1, 'a3')

    assert test1.a2 is not test2.a2
    assert test1.a3 is not test2.a3

    eq_(test1.a2, [])
    eq_(test1.a3, list(range(10)))

    eq_(type(test1.a2), list)
    eq_(type(test1.a3), list)

    test1.a1 = (1, 2, 3)
    test1.a2 = set([4, 5, 6])
    test1.a3 = dict.fromkeys([7, 8, 9])

    eq_(type(test1.a1), list)
    eq_(type(test1.a2), list)
    eq_(type(test1.a3), list)

    eq_(test1.a1, [1, 2, 3])
    eq_(test1.a2, [4, 5, 6])
    eq_(set(test1.a3), set([7, 8, 9]))

    del test1.a1
    assert not hasattr(test1, 'a1')
    assert hasattr(test1, 'a2')
    assert hasattr(test1, 'a3')

    del test1.a3
    assert not hasattr(test1, 'a1')
    assert hasattr(test1, 'a2')
    assert not hasattr(test1, 'a3')


def test_Tuple():
    class TestClass(Structure):
        a1 = Tuple
        a2 = Tuple([])
        a3 = Tuple(range(10))

    test1 = TestClass()
    test2 = TestClass()

    assert not hasattr(test1, 'a1')
    assert hasattr(test1, 'a2')
    assert hasattr(test1, 'a3')

    eq_(test1.a2, ())
    eq_(test1.a3, tuple(range(10)))

    eq_(type(test1.a2), tuple)
    eq_(type(test1.a3), tuple)

    test1.a1 = (1, 2, 3)
    test1.a2 = set([4, 5, 6])
    test1.a3 = dict.fromkeys([7, 8, 9])

    eq_(type(test1.a1), tuple)
    eq_(type(test1.a2), tuple)
    eq_(type(test1.a3), tuple)

    eq_(test1.a1, (1, 2, 3))
    eq_(test1.a2, (4, 5, 6))
    eq_(set(test1.a3), set([7, 8, 9]))

    del test1.a1
    assert not hasattr(test1, 'a1')
    assert hasattr(test1, 'a2')
    assert hasattr(test1, 'a3')

    del test1.a3
    assert not hasattr(test1, 'a1')
    assert hasattr(test1, 'a2')
    assert not hasattr(test1, 'a3')


def test_Set():
    class TestClass(Structure):
        a1 = Set
        a2 = Set([])
        a3 = Set(range(10))

    test1 = TestClass()
    test2 = TestClass()

    assert not hasattr(test1, 'a1')
    assert hasattr(test1, 'a2')
    assert hasattr(test1, 'a3')

    assert test1.a2 is not test2.a2
    assert test1.a3 is not test2.a3

    eq_(test1.a2, set())
    eq_(test1.a3, set(range(10)))

    eq_(type(test1.a2), set)
    eq_(type(test1.a3), set)

    test1.a1 = set([1, 2, 3])
    test1.a2 = set([4, 5, 6])
    test1.a3 = dict.fromkeys([7, 8, 9])

    eq_(type(test1.a1), set)
    eq_(type(test1.a2), set)
    eq_(type(test1.a3), set)

    eq_(test1.a1, set([1, 2, 3]))
    eq_(test1.a2, set([4, 5, 6]))
    eq_(set(test1.a3), set([7, 8, 9]))

    del test1.a1
    assert not hasattr(test1, 'a1')
    assert hasattr(test1, 'a2')
    assert hasattr(test1, 'a3')

    del test1.a3
    assert not hasattr(test1, 'a1')
    assert hasattr(test1, 'a2')
    assert not hasattr(test1, 'a3')


def test_Dict():
    class TestClass(Structure):
        a1 = Dict
        a2 = Dict({})
        a3 = Dict(dict(zip(range(10), range(9, -1, -1))))

    test1 = TestClass()
    test2 = TestClass()

    assert not hasattr(test1, 'a1')
    assert hasattr(test1, 'a2')
    assert hasattr(test1, 'a3')

    assert test1.a2 is not test2.a2
    assert test1.a3 is not test2.a3

    eq_(test1.a2, {})
    eq_(test1.a3, dict(zip(range(10), range(9, -1, -1))))

    eq_(type(test1.a2), dict)
    eq_(type(test1.a3), dict)

    test1.a1 = {'a': 1, 'b': 2}
    test1.a2 = zip(['c', 'd'], [3, 4])

    eq_(type(test1.a1), dict)
    eq_(type(test1.a2), dict)

    eq_(test1.a1, {'a': 1, 'b': 2})
    eq_(test1.a2, {'c': 3, 'd': 4})

    del test1.a1
    assert not hasattr(test1, 'a1')
    assert hasattr(test1, 'a2')
    assert hasattr(test1, 'a3')

    del test1.a3
    assert not hasattr(test1, 'a1')
    assert hasattr(test1, 'a2')
    assert not hasattr(test1, 'a3')


def test_recurcive():

    class TestClass(Structure):
        integer = Integer(13)

        class sub(Structure):
            integer = Integer(26)
            string = String('qwerty')

    test = TestClass()

    assert hasattr(test, 'integer')
    assert hasattr(test, 'sub')
    assert hasattr(test.sub, 'string')

    eq_(type(test.integer), int)
    eq_(test.integer, 13)
    eq_(test.sub.string, 'qwerty')
    eq_(type(test.sub.string), str)

    test.sub.string = 127
    eq_(test.sub.string, '127')
    eq_(type(test.sub.string), str)

    sub = TestClass.sub()
    sub.integer = 3.14
    sub.string = 987
    sub.attr = 'qwerty'
    test.sub = sub
    eq_(test.sub.integer, 3)
    eq_(type(test.sub.integer), int)
    eq_(test.sub.string, '987')
    eq_(type(test.sub.string), str)
    eq_(test.sub.attr, 'qwerty')
    eq_(type(test.sub.attr), str)

    assert_raises(TypeError, setattr, *(test, 'sub', TestClass()))


def test_inheritance():
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

    test = TestClass()
    sub_test_a_1 = SubTestClassA()
    sub_test_a_2 = SubTestClassA()
    sub_test_b = SubTestClassB()

    assert sub_test_a_1.l is not sub_test_a_2.l
    assert sub_test_a_2.t is sub_test_a_2.t

    assert not hasattr(test, 'l')
    assert_raises(AttributeError, getattr, test, 'l')
    assert not hasattr(test, 't')
    assert_raises(AttributeError, getattr, test, 't')
    assert not hasattr(test, 'd')
    assert_raises(AttributeError, getattr, test, 'd')

    attrs = lambda s: [a for a, v in s]
    assert set(attrs(test)).issubset(attrs(sub_test_a_1))
    assert set(attrs(test)).issubset(attrs(sub_test_a_2))
    eq_(set(attrs(sub_test_a_1)), set(attrs(sub_test_a_2)))
    assert set(attrs(test)).issubset(attrs(sub_test_b))

    assert_raises(AttributeError, getattr, sub_test_a_1, 'd')
    assert_raises(AttributeError, getattr, sub_test_b, 'l')

    assert_raises(AttributeError, getattr, sub_test_a_1, 'i')
    sub_test_a_1.i = 3.14
    eq_(sub_test_a_1.i, 3)

    assert_raises(AttributeError, getattr, sub_test_a_2, 'i')
    sub_test_a_2.i = 6.28
    eq_(sub_test_a_2.i, 6)

    assert_raises(AttributeError, getattr, sub_test_b, 'i')
    sub_test_b.i = 12.56
    eq_(sub_test_b.i, 12)
