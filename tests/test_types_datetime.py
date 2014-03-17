import datetime
from unittest import TestCase

from structures import *


class DatetimeTests(TestCase):
    def test_func_datetime(self):
        self.assertEqual(
            DateTime.func(datetime.datetime(2005, 1, 13, 18, 5, 10)),
            datetime.datetime(2005, 1, 13, 18, 5, 10))

        self.assertIsInstance(
            DateTime.func(datetime.datetime(2005, 1, 13, 18, 5, 10)),
            datetime.datetime)

    def test_func_date(self):
        self.assertEqual(
            DateTime.func(datetime.date(2005, 1, 13)),
            datetime.datetime(2005, 1, 13, 0, 0, 0))

        self.assertIsInstance(
            DateTime.func(datetime.date(2005, 1, 13)),
            datetime.datetime)

    def test_func_str__YYYY_MM_DD__hh_mm_ss__mmmm(self):
        self.assertEqual(
            DateTime.func('2005-01-13 18:05:10.1313'),
            datetime.datetime(2005, 1, 13, 18, 5, 10, 131300))

        self.assertIsInstance(
            DateTime.func('2005-01-13 18:05:10.1313'),
            datetime.datetime)

    def test_func_str__YYYY_MM_DD__hh_mm_ss(self):
        self.assertEqual(
            DateTime.func('2005-01-13 18:05:10'),
            datetime.datetime(2005, 1, 13, 18, 5, 10))

        self.assertIsInstance(
            DateTime.func('2005-01-13 18:05:10'),
            datetime.datetime)

    def test_func_str__YYYY_MM_DD__hh_mm(self):
        self.assertEqual(
            DateTime.func('2005-01-13 18:05'),
            datetime.datetime(2005, 1, 13, 18, 5))

        self.assertIsInstance(
            DateTime.func('2005-01-13 18:05'),
            datetime.datetime)

    def test_func_str__YYYY_MM_DD(self):
        self.assertEqual(DateTime.func('2005-01-13'), datetime.datetime(2005, 1, 13))
        self.assertIsInstance(DateTime.func('2005-01-13'), datetime.datetime)

    def test_func_str_bad(self):
        self.assertRaises(ValueError, DateTime.func, '18:05:10')
        self.assertRaises(ValueError, DateTime.func, '2005-01-13 18:05:10 bad datetime')

    def test_func_str_format__DD_MM_YYYY(self):
        self.assertEqual(
            DateTime.func('13/01/2005', '%d/%m/%Y'),
            datetime.datetime(2005, 1, 13))

        self.assertRaises(ValueError, DateTime.func, '2005-01-13', '%d/%m/%Y')

    def test_func_str_format__DD_MM_YYYY__hh_mm_ss(self):
        self.assertEqual(DateTime.func('13/01/2005 18:05:10', '%d/%m/%Y %H:%M:%S'),
            datetime.datetime(2005, 1, 13, 18, 5, 10))
        self.assertRaises(ValueError, DateTime.func, '2005-01-13 18:05:10',
                                                 '%d/%m/%Y %H:%M:%S')

    def test_func_typeerror(self):
        self.assertRaises(TypeError, DateTime.func, 13)


class DateTests(TestCase):
    def test_func_date(self):
        self.assertEqual(
            Date.func(datetime.date(2005, 1, 13)),
            datetime.date(2005, 1, 13))

        self.assertIsInstance(Date.func(datetime.date(2005, 1, 13)), datetime.date)

    def test_func_datetime(self):
        self.assertEqual(
            Date.func(datetime.datetime(2005, 1, 13, 18, 5, 10)),
            datetime.date(2005, 1, 13))

        self.assertIsInstance(
            Date.func(datetime.datetime(2005, 1, 13, 18, 5, 10)),
            datetime.date)

    def test_func_str__YYYY_MM_DD__hh_mm_ss__mmmm(self):
        self.assertEqual(
            Date.func('2005-01-13 18:05:10.1313'),
            datetime.date(2005, 1, 13))

        self.assertIsInstance(
            Date.func('2005-01-13 18:05:10.1313'),
            datetime.date)

    def test_func_str__YYYY_MM_DD(self):
        self.assertEqual(Date.func('2005-01-13'), datetime.date(2005, 1, 13))
        self.assertIsInstance(Date.func('2005-01-13'), datetime.date)

    def test_func_str_bad(self):
        self.assertRaises(ValueError, Date.func, '18:05:10')
        self.assertRaises(ValueError, Date.func, '2005-01-13 bad date')

    def test_func_str_format__DD_MM_YYYY(self):
        self.assertEqual(Date.func('13/01/2005', '%d/%m/%Y'), datetime.date(2005, 1, 13))
        self.assertRaises(ValueError, Date.func, '2005-01-13', '%d/%m/%Y')

    def test_func_typeerror(self):
        self.assertRaises(TypeError, Date.func, 13)


class TimeTests(TestCase):
    def test_func_time(self):
        self.assertEqual(
            Time.func(datetime.time(18, 5, 10)),
            datetime.time(18, 5, 10))

        self.assertIsInstance(
            Time.func(datetime.time(18, 5, 10)),
            datetime.time)

    def test_func_datetime(self):
        self.assertEqual(
            Time.func(datetime.datetime(2005, 1, 13, 18, 5, 10)),
            datetime.time(18, 5, 10))

        self.assertIsInstance(
            Time.func(datetime.datetime(2005, 1, 13, 18, 5, 10)),
            datetime.time)

    def test_func_str__YYYY_MM_DD__hh_mm_ss__mmmm(self):
        self.assertEqual(
            Time.func('2005-01-13 18:05:10.1313'),
            datetime.time(18, 5, 10, 131300))

        self.assertIsInstance(
            Time.func('2005-01-13 18:05:10.1313'),
            datetime.time)

    def test_func_str__YYYY_MM_DD__hh_mm_ss(self):
        self.assertEqual(
            Time.func('2005-01-13 18:05:10'),
            datetime.time(18, 5, 10))

        self.assertIsInstance(
            Time.func('2005-01-13 18:05:10'),
            datetime.time)

    def test_func_str__hh_mm_ss__mmmm(self):
        self.assertEqual(Time.func('18:05:10.1313'), datetime.time(18, 5, 10, 131300))
        self.assertIsInstance(Time.func('18:05:10.1313'), datetime.time)

    def test_func_str__hh_mm_ss(self):
        self.assertEqual(Time.func('18:05:10'), datetime.time(18, 5, 10))
        self.assertIsInstance(Time.func('18:05:10'), datetime.time)

    def test_func_str__hh_mm(self):
        self.assertEqual(Time.func('18:05'), datetime.time(18, 5, 0))
        self.assertIsInstance(Time.func('18:05'), datetime.time)

    def test_func_str_bad(self):
        self.assertRaises(ValueError, Time.func, '2005-01-13')
        self.assertRaises(ValueError, Time.func, '18:05:10 bad time')

    def test_func_str_format(self):
        self.assertEqual(Time.func('18 05 10', '%H %M %S'), datetime.time(18, 5, 10))
        self.assertRaises(ValueError, Time.func, '2005-01-13', '%d/%M/%Y')

    def test_func_typeerror(self):
        self.assertRaises(TypeError, Time.func, 13)


class ComplexTests(TestCase):
    def test_datetime(self):
        class TestClass(Structure):
            a1 = DateTime
            a2 = DateTime(datetime.datetime(2005, 1, 13, 18, 5, 10, 1313))
            a3 = DateTime(format='%d/%m/%Y %H:%M')

        test = TestClass()

        self.assertFalse(hasattr(test, 'a1'))
        self.assertTrue(hasattr(test, 'a2'))
        self.assertFalse(hasattr(test, 'a3'))

        self.assertEqual(test.a2, datetime.datetime(2005, 1, 13, 18, 5, 10, 1313))

        test.a1 = '2005-01-13 18:05'
        self.assertTrue(hasattr(test, 'a1'))
        self.assertEqual(test.a1, datetime.datetime(2005, 1, 13, 18, 5))

        test.a3 = '13/01/2005 18:05'
        self.assertTrue(hasattr(test, 'a3'))
        self.assertEqual(test.a3, datetime.datetime(2005, 1, 13, 18, 5))

    def test_date(self):
        class TestClass(Structure):
            a1 = Date
            a2 = Date(datetime.date(2005, 1, 13))
            a3 = Date(format='%d/%m/%Y')

        test = TestClass()

        self.assertFalse(hasattr(test, 'a1'))
        self.assertTrue(hasattr(test, 'a2'))
        self.assertFalse(hasattr(test, 'a3'))

        self.assertEqual(test.a2, datetime.date(2005, 1, 13))

        test.a1 = '2005-01-13'
        self.assertTrue(hasattr(test, 'a1'))
        self.assertEqual(test.a1, datetime.date(2005, 1, 13))

        test.a3 = '13/01/2005'
        self.assertTrue(hasattr(test, 'a3'))
        self.assertEqual(test.a3, datetime.date(2005, 1, 13))


    def test_time(self):
        class TestClass(Structure):
            a1 = Time
            a2 = Time(datetime.time(18, 5, 10, 1313))
            a3 = Time(format='%H-%M')

        test = TestClass()

        self.assertFalse(hasattr(test, 'a1'))
        self.assertTrue(hasattr(test, 'a2'))
        self.assertFalse(hasattr(test, 'a3'))

        self.assertEqual(test.a2, datetime.time(18, 5, 10, 1313))

        test.a1 = '18:05'
        self.assertTrue(hasattr(test, 'a1'))
        self.assertEqual(test.a1, datetime.time(18, 5))

        test.a3 = '18-05'
        self.assertTrue(hasattr(test, 'a3'))
        self.assertEqual(test.a3, datetime.time(18, 5))
