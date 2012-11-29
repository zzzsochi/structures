# coding: utf8

from nose.tools import *

from structures import *


def test_from_dict():
    import decimal

    class TestClass(Structure):
        i = Integer(13)
        s = String('qwerty')
        d = Decimal('5.36')

    test = from_dict(TestClass, {'i': '26', 's': 'ytrewq', 'd': '98.2'})
    eq_(test.i, 26)
    eq_(test.s, u'ytrewq')
    eq_(test.d, decimal.Decimal('98.2'))

    test = from_dict(TestClass, {'i': 36.6, 'attr': '345'})
    eq_(test.i, 36)
    eq_(test.s, u'qwerty')
    eq_(test.d, decimal.Decimal('5.36'))
    eq_(test.attr, '345')


def test_from_dict_recurcive():
    class TestClass(Structure):
        i = Integer(13)
        s = String('qwerty')

        class sub(Structure):
            i = Integer

    test = from_dict(TestClass, {'i': '26', 's': 'ytrewq',
                                 'sub': {'i': '100'}})
    eq_(test.i, 26)
    eq_(test.s, u'ytrewq')
    eq_(test.sub.i, 100)


def test_to_dict():
    class TestClass(Structure):
        i = Integer(13)
        s = String('qwerty')

    test = TestClass()
    eq_(to_dict(test), {'i': 13, 's': u'qwerty'})


def test_to_dict_recurcive():
    class TestClass(Structure):
        i = Integer(13)
        s = String('qwerty')

        class sub(Structure):
            i = Integer(26)

    test = TestClass()
    eq_(to_dict(test), {'i': 13, 's': u'qwerty', 'sub': {'i': 26}})
