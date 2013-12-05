# coding=utf-8

from datetime import datetime
from wikilife_utils.formatters.date_formatter import DateFormatter
import unittest
from wikilife_utils.date_utils import DateUtils

class DateFormatterTests(unittest.TestCase):
    
    def setUp(self):
        pass
    
    def tearDown(self):
        pass
    
    def test_to_datetime_utc(self):
        d = datetime.utcnow()
        expected_str_value = "%s-%02d-%02d %02d:%02d:%02d" %(d.year, d.month, d.day, d.hour, d.minute, d.second)
        str_value = DateFormatter.to_datetime_utc(d)
        
        print expected_str_value
        print str_value
        
        assert str_value != None
        assert str_value == expected_str_value

    def test_to_datetime(self):
        tz_name = "US/Central" 
        dt = DateUtils.get_datetime_local(tz_name)
        expected_str_value = "%s-%02d-%02d %02d:%02d:%02d %s" %(dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second, DateUtils.get_utc_offset_str(tz_name))
        str_value = DateFormatter.to_datetime(dt)

        print expected_str_value
        print str_value

        assert str_value != None
        assert str_value == expected_str_value

    def test_to_date(self):
        d = datetime.utcnow()
        expected_str_value = "%s-%02d-%02d" %(d.year, d.month, d.day)
        str_value = DateFormatter.to_date(d)
        
        print expected_str_value
        print str_value
        
        assert str_value != None
        assert str_value == expected_str_value
