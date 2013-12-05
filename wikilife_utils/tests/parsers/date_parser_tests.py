# coding=utf-8

import unittest
from wikilife_utils.parsers.date_parser import DateParser

class DateParserTests(unittest.TestCase):
    
    def setUp(self):
        pass
    
    def tearDown(self):
        pass
    
    def test_from_datetime_utc(self):
        str_value = "2012-03-30 19:15:10"
        date_value = DateParser.from_datetime_utc(str_value)
        assert date_value != None
        assert date_value.year == 2012
        assert date_value.month == 3
        assert date_value.day == 30
        assert date_value.hour == 19
        assert date_value.minute == 15
        assert date_value.second == 10
    
    def test_from_datetime_utc_ugly_format(self):
        str_value = "Tue, 30 Mar 2012 19:15:10"
        date_value = DateParser.from_datetime_utc(str_value)
        assert date_value != None
        assert date_value.year == 2012
        assert date_value.month == 3
        assert date_value.day == 30
        assert date_value.hour == 19
        assert date_value.minute == 15
        assert date_value.second == 10

    def test_from_datetime(self):
        str_value = "2012-03-30 19:15:10 +0300"
        date_value = DateParser.from_datetime(str_value)
        assert date_value != None
        assert date_value.year == 2012
        assert date_value.month == 3
        assert date_value.day == 30
        assert date_value.hour == 19
        assert date_value.minute == 15
        assert date_value.second == 10
        assert date_value.utcoffset().total_seconds() == 10800.0

    def test_from_datetime_arg(self):
        str_value = "2013-01-05 22:00:00 -0300"
        date_value = DateParser.from_datetime(str_value)
        assert date_value != None
        assert date_value.year == 2013
        assert date_value.month == 1
        assert date_value.day == 5
        assert date_value.hour == 22
        assert date_value.minute == 00
        assert date_value.second == 00
        print date_value

    def test_from_timestamp(self):
        #2012-05-29 21:00:00
        str_value = "1338336000"
        date_value = DateParser.from_timestamp(str_value)
        assert date_value != None
        assert date_value.year == 2012
        assert date_value.month == 5
        assert date_value.day == 29
        assert date_value.hour == 21
        assert date_value.minute == 0
        assert date_value.second == 0
