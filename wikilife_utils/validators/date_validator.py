# coding=utf-8

from wikilife_utils.patterns import DATETIME_PATTERN_C, DATE_PATTERN_C, \
    TIME_PATTERN_C, DATETIMETZ_PATTERN_C

class DateValidator(object):
    #TODO emprove validation currently 2012-15-50 is valid
    
    @staticmethod
    def validate_datetimetz(datetimetz_str):
        return DATETIMETZ_PATTERN_C.match(datetimetz_str) != None
    
    @staticmethod
    def validate_datetime(datetime_str):
        return DATETIME_PATTERN_C.match(datetime_str) != None

    @staticmethod
    def validate_date(date_str):
        return DATE_PATTERN_C.match(date_str) != None
    
    @staticmethod
    def validate_time(time_str):
        return TIME_PATTERN_C.match(time_str) != None
    