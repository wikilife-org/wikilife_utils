# coding=utf-8

import unittest
from datetime import datetime
from wikilife_utils.date_utils import DateUtils
from wikilife_utils.parsers.date_parser import DateParser

class DateUtilsTests(unittest.TestCase):
    
    def setUp(self):
        pass
    
    def tearDown(self):
        pass
    
    def test_get_datetime_utc(self):
        dr = DateUtils.get_datetime_utc()
        assert dr != None

    def test_get_date_utc(self):
        dr = DateUtils.get_date_utc()
        print dr
        assert dr != None
    
    def test_to_datetime_utc(self):
        local_datetime = DateParser.from_datetime("2012-06-15 10:30:45 -0300")
        utc_datetime = DateUtils.to_datetime_utc(local_datetime)
        #print local_datetime
        #print utc_datetime
        assert local_datetime.hour+3 == utc_datetime.hour
        assert local_datetime.year == utc_datetime.year
        assert local_datetime.month == utc_datetime.month
        assert local_datetime.day == utc_datetime.day
        assert local_datetime.minute == utc_datetime.minute
        assert local_datetime.second == utc_datetime.second

    def test_get_utc_offset_str(self):
        assert DateUtils.get_utc_offset_str("America/Argentina/San_Luis") == "-0300"
        assert DateUtils.get_utc_offset_str("America/Argentina/Buenos_Aires") == "-0300"
        #assert DateUtils.get_utc_offset_str("US/Eastern") == "-0400"
        #assert DateUtils.get_utc_offset_str("US/Central") == "-0500"
        #assert DateUtils.get_utc_offset_str("US/Pacific") == "-0700"

    def test_get_datetime_local(self):
        tz_name = "US/Central"

        utc_dt = DateUtils.get_datetime_utc()
        local_dt = DateUtils.get_datetime_local(tz_name)

        #assert local_dt.hour+5 == utc_dt.hour
        assert local_dt.year == utc_dt.year
        assert local_dt.month == utc_dt.month
        assert local_dt.day == utc_dt.day
        assert local_dt.minute == utc_dt.minute
        assert local_dt.second == utc_dt.second

    def test_create_datetime(self):
        d = DateUtils.create_datetime(2001, 1, 15)
        assert d != None
        assert d.year == 2001
        assert d.month == 1
        assert d.day == 15
        assert d.hour == 0
        assert d.minute == 0
        assert d.second == 0
    
    def test_get_zero_datetime(self):
        d = DateUtils.get_zero_datetime()
        assert d != None
        assert d.year == 1
        assert d.month == 1
        assert d.day == 1
        assert d.hour == 0
        assert d.minute == 0
        assert d.second == 0
    
    def test_add_seconds(self):
        d = datetime(2012, 3, 6, 15, 30, 45)
        seconds_offset = 7
        dr = DateUtils.add_seconds(d, seconds_offset)
        
        assert dr != None
        assert dr.year == 2012
        assert dr.month == 3
        assert dr.day == 6
        assert dr.hour == 15
        assert dr.minute == 30
        assert dr.second == 52
    
    def test_add_seconds_returns_copy(self):
        d = datetime(2012, 3, 6, 15, 30, 45)
        seconds_offset = 60*60*24
        dr = DateUtils.add_seconds(d, seconds_offset)
        
        assert dr != None
        assert dr.day == 7
        assert dr != d
        assert d.day == 6

    def test_add_seconds_neg(self):
        d = datetime(2012, 3, 6, 15, 30, 45)
        seconds_offset = -7
        dr = DateUtils.add_seconds(d, seconds_offset)
        
        assert dr != None
        assert dr.year == 2012
        assert dr.month == 3
        assert dr.day == 6
        assert dr.hour == 15
        assert dr.minute == 30
        assert dr.second == 38
        
    def test_add_seconds_change_day(self):
        d = datetime(2012, 3, 6, 15, 30, 45)
        seconds_offset = 8*60*60 + 29*60 + 15
        dr = DateUtils.add_seconds(d, seconds_offset)
        
        assert dr != None
        assert dr.year == 2012
        assert dr.month == 3
        assert dr.day == 7
        assert dr.hour == 0
        assert dr.minute == 0
        assert dr.second == 0
        
    def test_add_days(self):
        d = datetime(2012, 3, 6, 15, 30, 45)
        days_offset = 10
        dr = DateUtils.add_days(d, days_offset)
        
        assert dr != None
        assert dr.year == 2012
        assert dr.month == 3
        assert dr.day == 16
        assert dr.hour == 15
        assert dr.minute == 30
        assert dr.second == 45

    def test_add_months(self):
        d = datetime(2012, 3, 6, 15, 30, 45)
        months_offset = 1
        dr = DateUtils.add_months(d, months_offset)
        
        assert dr != None
        assert dr.year == 2012
        assert dr.month == 4
        assert dr.day == 6
        assert dr.hour == 15
        assert dr.minute == 30
        assert dr.second == 45

    def test_equals_datetime(self):
        d1 = DateUtils.get_datetime_utc()
        d2 = DateUtils.get_datetime_utc()
        
        assert DateUtils.equals_datetime(d1, d2, 5) == True

    def test_equals_datetime2(self):
        d1 = DateUtils.get_datetime_utc()
        d2 = DateUtils.get_datetime_utc()
        d2 = DateUtils.add_seconds(d2, 1)

        assert DateUtils.equals_datetime(d1, d2, 5) == True
        assert DateUtils.equals_datetime(d1, d2, 1.1) == True
        assert DateUtils.equals_datetime(d1, d2, 0.9) == False
        assert DateUtils.equals_datetime(d1, d2) == False
    
    """
    def test_add_seconds_to_utc(self):
        local_datetime = DateParser.from_datetime("2012-06-15 10:30:45 -0300")
        utc_datetime = DateUtils.to_datetime_utc(local_datetime)
        dr = DateUtils.add_seconds(utc_datetime, 30)
        
        assert dr > local_datetime
        assert dr != None
        assert dr.year == 2012
        assert dr.month == 6
        assert dr.day == 15
        assert dr.hour == 10
        assert dr.minute == 31
        assert dr.second == 15
    """
