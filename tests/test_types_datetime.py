# coding: utf8

import datetime
from nose.tools import *
from structures import *


def test_Datetime_func():
    eq_(DateTime.func(datetime.datetime(2005, 1, 13, 18, 5, 10)),
        datetime.datetime(2005, 1, 13, 18, 5, 10))
    assert type(DateTime.func(datetime.datetime(2005, 1, 13, 18, 5, 10))) \
           is datetime.datetime

    eq_(DateTime.func(datetime.date(2005, 1, 13)),
        datetime.datetime(2005, 1, 13, 0, 0, 0))
    assert type(DateTime.func(datetime.date(2005, 1, 13))) is datetime.datetime

    eq_(DateTime.func('2005-01-13 18:05:10.1313'),
        datetime.datetime(2005, 1, 13, 18, 5, 10, 131300))
    assert type(DateTime.func('2005-01-13 18:05:10.1313')) is datetime.datetime

    eq_(DateTime.func('2005-01-13 18:05:10'),
        datetime.datetime(2005, 1, 13, 18, 5, 10))
    assert type(DateTime.func('2005-01-13 18:05:10')) is datetime.datetime

    eq_(DateTime.func('2005-01-13 18:05'),
        datetime.datetime(2005, 1, 13, 18, 5))
    assert type(DateTime.func('2005-01-13 18:05')) is datetime.datetime

    eq_(DateTime.func('2005-01-13'), datetime.datetime(2005, 1, 13))
    assert type(DateTime.func('2005-01-13')) is datetime.datetime

    assert_raises(ValueError, DateTime.func, '18:05:10')
    assert_raises(ValueError, DateTime.func, '2005-01-13 18:05:10 bad datetime')

    eq_(DateTime.func('13/01/2005', '%d/%m/%Y'), datetime.datetime(2005, 1, 13))
    assert_raises(ValueError, DateTime.func, '2005-01-13', '%d/%m/%Y')

    eq_(DateTime.func('13/01/2005 18:05:10', '%d/%m/%Y %H:%M:%S'),
        datetime.datetime(2005, 1, 13, 18, 5, 10))
    assert_raises(ValueError, DateTime.func, '2005-01-13 18:05:10',
                                             '%d/%m/%Y %H:%M:%S')

    assert_raises(TypeError, DateTime.func, 13)


def test_Date_func():
    eq_(Date.func(datetime.date(2005, 1, 13)), datetime.date(2005, 1, 13))
    assert type(Date.func(datetime.date(2005, 1, 13))) is datetime.date

    eq_(Date.func(datetime.datetime(2005, 1, 13, 18, 5, 10)),
        datetime.date(2005, 1, 13))
    assert type(Date.func(datetime.datetime(2005, 1, 13, 18, 5, 10))) \
           is datetime.date

    eq_(Date.func('2005-01-13 18:05:10.1313'), datetime.date(2005, 1, 13))
    assert type(Date.func('2005-01-13 18:05:10.1313')) is datetime.date

    eq_(Date.func('2005-01-13'), datetime.date(2005, 1, 13))
    assert type(Date.func('2005-01-13')) is datetime.date

    assert_raises(ValueError, Date.func, '18:05:10')
    assert_raises(ValueError, Date.func, '2005-01-13 bad date')

    eq_(Date.func('13/01/2005', '%d/%m/%Y'), datetime.date(2005, 1, 13))
    assert_raises(ValueError, Date.func, '2005-01-13', '%d/%m/%Y')

    assert_raises(TypeError, Date.func, 13)


def test_Time_func():
    eq_(Time.func(datetime.time(18, 5, 10)), datetime.time(18, 5, 10))
    assert type(Time.func(datetime.time(18, 5, 10))) is datetime.time

    eq_(Time.func(datetime.datetime(2005, 1, 13, 18, 5, 10)),
        datetime.time(18, 5, 10))
    assert type(Time.func(datetime.datetime(2005, 1, 13, 18, 5, 10))) \
           is datetime.time

    eq_(Time.func('2005-01-13 18:05:10.1313'), datetime.time(18, 5, 10, 131300))
    assert type(Time.func('2005-01-13 18:05:10.1313')) is datetime.time

    eq_(Time.func('2005-01-13 18:05:10'), datetime.time(18, 5, 10))
    assert type(Time.func('2005-01-13 18:05:10')) is datetime.time

    eq_(Time.func('18:05:10.1313'), datetime.time(18, 5, 10, 131300))
    assert type(Time.func('18:05:10.1313')) is datetime.time

    eq_(Time.func('18:05:10'), datetime.time(18, 5, 10))
    assert type(Time.func('18:05:10')) is datetime.time

    eq_(Time.func('18:05'), datetime.time(18, 5, 0))
    assert type(Time.func('18:05')) is datetime.time

    assert_raises(ValueError, Time.func, '2005-01-13')
    assert_raises(ValueError, Time.func, '18:05:10 bad time')

    eq_(Time.func('18 05 10', '%H %M %S'), datetime.time(18, 5, 10))
    assert_raises(ValueError, Time.func, '2005-01-13', '%d/%M/%Y')

    assert_raises(TypeError, Time.func, 13)


def test_DateTime():
    from datetime import datetime

    class TestClass(Structure):
        a1 = DateTime
        a2 = DateTime(datetime(2005, 1, 13, 18, 5, 10, 1313))
        a3 = DateTime(format='%d/%m/%Y %H:%M')

    test = TestClass()

    assert not hasattr(test, 'a1')
    assert hasattr(test, 'a2')
    assert not hasattr(test, 'a3')

    eq_(test.a2, datetime(2005, 1, 13, 18, 5, 10, 1313))

    test.a1 = '2005-01-13 18:05'
    assert hasattr(test, 'a1')
    eq_(test.a1, datetime(2005, 1, 13, 18, 5))

    test.a3 = '13/01/2005 18:05'
    assert hasattr(test, 'a3')
    eq_(test.a3, datetime(2005, 1, 13, 18, 5))


def test_Date():
    from datetime import date

    class TestClass(Structure):
        a1 = Date
        a2 = Date(date(2005, 1, 13))
        a3 = Date(format='%d/%m/%Y')

    test = TestClass()

    assert not hasattr(test, 'a1')
    assert hasattr(test, 'a2')
    assert not hasattr(test, 'a3')

    eq_(test.a2, date(2005, 1, 13))

    test.a1 = '2005-01-13'
    assert hasattr(test, 'a1')
    eq_(test.a1, date(2005, 1, 13))

    test.a3 = '13/01/2005'
    assert hasattr(test, 'a3')
    eq_(test.a3, date(2005, 1, 13))


def test_Time():
    from datetime import time

    class TestClass(Structure):
        a1 = Time
        a2 = Time(time(18, 5, 10, 1313))
        a3 = Time(format='%H-%M')

    test = TestClass()

    assert not hasattr(test, 'a1')
    assert hasattr(test, 'a2')
    assert not hasattr(test, 'a3')

    eq_(test.a2, time(18, 5, 10, 1313))

    test.a1 = '18:05'
    assert hasattr(test, 'a1')
    eq_(test.a1, time(18, 5))

    test.a3 = '18-05'
    assert hasattr(test, 'a3')
    eq_(test.a3, time(18, 5))
