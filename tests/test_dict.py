import decimal
from unittest import TestCase

from structures import *


class FromDictTests(TestCase):
    def test_from_dict(self):
        class TestClass(Structure):
            i = Integer(13)
            s = String('qwerty')
            d = Decimal('5.36')

        test = from_dict(TestClass, {'i': '26', 's': 'ytrewq', 'd': '98.2'})
        self.assertEqual(test.i, 26)
        self.assertEqual(test.s, 'ytrewq')
        self.assertEqual(test.d, decimal.Decimal('98.2'))

        test = from_dict(TestClass, {'i': 36.6, 'attr': '345'})
        self.assertEqual(test.i, 36)
        self.assertEqual(test.s, 'qwerty')
        self.assertEqual(test.d, decimal.Decimal('5.36'))
        self.assertEqual(test.attr, '345')


    def test_from_dict_recurcive(self):
        class TestClass(Structure):
            i = Integer(13)
            s = String('qwerty')

            class sub(Structure):
                i = Integer

        test = from_dict(TestClass, {'i': '26', 's': 'ytrewq',
                                     'sub': {'i': '100'}})
        self.assertEqual(test.i, 26)
        self.assertEqual(test.s, 'ytrewq')
        self.assertEqual(test.sub.i, 100)


class ToDictTests(TestCase):
    def test_to_dict(self):
        class TestClass(Structure):
            i = Integer(13)
            s = String('qwerty')

        test = TestClass()
        self.assertEqual(to_dict(test), {'i': 13, 's': 'qwerty'})


    def test_to_dict_recurcive(self):
        class TestClass(Structure):
            i = Integer(13)
            s = String('qwerty')

            class sub(Structure):
                i = Integer(26)

        test = TestClass()
        self.assertEqual(to_dict(test), {'i': 13, 's': 'qwerty', 'sub': {'i': 26}})
