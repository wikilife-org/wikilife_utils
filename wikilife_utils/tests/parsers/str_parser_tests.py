# coding=utf-8

import unittest
from wikilife_utils.parsers.str_parser import StrParser
import datetime

class StrParserTests(unittest.TestCase):
    
    def setUp(self):
        pass
    
    def tearDown(self):
        pass
    
    def test_parse_int(self):
        assert StrParser.parse_int("1")  == 1
        assert StrParser.parse_int("01")  == 1
        assert StrParser.parse_int(None)  == None

    def test_parse_list(self):
        assert StrParser.parse_list("a, b, c")  == ["a", "b", "c"]
        assert StrParser.parse_list(None)  == None

    def test_parse_date(self):
        r = StrParser.parse_date("2012-01-15")
        assert isinstance(r, datetime.datetime)
        
        r = StrParser.parse_date("2012-1-15")
        assert isinstance(r, datetime.datetime)
        
        assert StrParser.parse_date(None) == None
        
        
