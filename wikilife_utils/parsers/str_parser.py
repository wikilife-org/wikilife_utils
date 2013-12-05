# coding=utf-8

import dateutil.parser

class StrParser(object):
    """
    Common String Parser 
    """
    
    @staticmethod
    def parse_int(str):
        """
        from '1' returns 1
        from '01' returns 1
        
        Returns: Integer or None
        """
        try:
            return int(str)
        except:
            return None    
    
    @staticmethod
    def parse_list(str, separator=","):
        """
        from 'a, b, c'
        returns ['a', 'b', 'c']
        
        str: raw string
        separator=",": list delimiter
        
        Returns: List or None
        """
        try:
            r = [item.strip() for item in str.split(separator)]
            return r
        except:
            return None
        
    @staticmethod
    def parse_date(str, format="%Y-%m-%d"):
        """
        from "2012-01-15"
        returns Date(2012, 1, 15)
        
        str: raw string with format
        format="%Y-%m-%s": String
        
        Returns: Date or None
        """
        
        try:
            r = dateutil.parser.parse(str)
            return r
        except:
            return None
