'''In this is module defined types for working with **datetime**.'''

__all__ = ['DateTime', 'Date', 'Time']

import re
import datetime

from .types import Type, NoDefault

RE_datetime_ISO = re.compile(
    r'^(\d\d\d\d)-(\d\d)-(\d\d)[\sTt](\d\d):(\d\d)(?::(\d\d))?(?:\.(\d+))?$')
RE_date_ISO = re.compile(r'^(\d\d\d\d)-(\d\d)-(\d\d)$')
RE_time_ISO = re.compile(r'^(\d\d):(\d\d)(?::(\d\d))?(?:\.(\d+))?$')


def parse_ISO(string):
    '''It returns datetime.date, datetime.time or datetime.datetime
       from date in ISO format.'''
    r = RE_datetime_ISO.match(string)
    if r:
        tt = [int(i) for i in r.groups(0)]
        tt[-1] = tt[-1] * (10 ** (6 - len(str(tt[-1]))))
        return datetime.datetime(*tt)

    r = RE_date_ISO.match(string)
    if r:
        tt = [int(i) for i in r.groups(0)]
        return datetime.date(*tt)

    r = RE_time_ISO.match(string)
    if r:
        tt = [int(i) for i in r.groups(0)]
        tt[-1] = tt[-1] * (10 ** (6 - len(str(tt[-1]))))
        return datetime.time(*tt)

    raise ValueError('The bad ISO datetime string: %r' % string)


class _DateTimeType(Type):
    func = lambda x: x
    format = None

    def __init__(self, default=NoDefault, format=None):
        self.format = format
        if format is not None:
            func = lambda dt, format=format: self.__class__.func(dt, format)
        else:
            func = self.__class__.func
        super(_DateTimeType, self).__init__(func, default)


class DateTime(_DateTimeType):
    @staticmethod
    def func(dt, format=None):
        if type(dt) is datetime.datetime:
            return dt
        elif type(dt) is datetime.date:
            return datetime.datetime(*dt.timetuple()[:3])
        elif isinstance(dt, str):
            if format is None:
                dt = parse_ISO(dt)
                if type(dt) is datetime.datetime:
                    return dt
                elif type(dt) is datetime.date:
                    return datetime.datetime(*dt.timetuple()[:3])
                else:
                    raise ValueError('Bad ISO date or datetime: %r' % dt)
            else:
                return datetime.datetime.strptime(dt, format)
        else:
            raise TypeError('First value must be datetime,'
                            ' date or string, but %r' % type(dt))


class Date(_DateTimeType):
    @staticmethod
    def func(date, format=None):
        if type(date) is datetime.date:
            return date
        elif type(date) is datetime.datetime:
            return date.date()
        elif isinstance(date, str):
            if format is None:
                dt = parse_ISO(date)
                if type(dt) is datetime.datetime:
                    return dt.date()
                elif type(dt) is datetime.date:
                    return dt
                else:
                    raise ValueError('Bad ISO date or datetime: %r' % date)
            else:
                return datetime.datetime.strptime(date, format).date()
        else:
            raise TypeError('First value must be date,'
                            ' datetime or string, but %r' % type(date))


class Time(_DateTimeType):
    @staticmethod
    def func(time, format=None):
        if type(time) is datetime.time:
            return time
        elif type(time) is datetime.datetime:
            return time.time()
        elif isinstance(time, str):
            if format is None:
                dt = parse_ISO(time)
                if type(dt) is datetime.datetime:
                    return dt.time()
                elif type(dt) is datetime.time:
                    return dt
                else:
                    raise ValueError('Bad ISO time or datetime: %r' % time)
            else:
                return datetime.datetime.strptime(time, format).time()
        else:
            raise TypeError('First value must be time,'
                            ' datetime or string, but %r' % type(time))
