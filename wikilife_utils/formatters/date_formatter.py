# coding=utf-8

from wikilife_utils.formats import DATETIME_UTC_FMT, DATETIME_UTC_FILENAME_FMT,\
    DATE_FMT, DATETIME_FMT, TIME_FMT

class DateFormatter(object):
    """
    Standard wikilife date formatter
    """
    
    @staticmethod
    def to_datetime_utc(datetime_utc_value):
        return datetime_utc_value.strftime(DATETIME_UTC_FMT)
    
    @staticmethod
    def to_datetime_utc_filename(datetime_utc_value):
        return datetime_utc_value.strftime(DATETIME_UTC_FILENAME_FMT)
    
    @staticmethod
    def to_datetime(datetime_value):
        return datetime_value.strftime(DATETIME_FMT)
    
    @staticmethod
    def to_date(date_value):
        return date_value.strftime(DATE_FMT) 
    
    @staticmethod
    def to_time(time_value):
        return time_value.strftime(TIME_FMT) 
