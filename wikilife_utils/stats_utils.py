# coding=utf-8

from datetime import datetime, timedelta, date
from dateutil.parser import parse
import time
import pytz
import math


class PrehistoricalWeekException(Exception):
    pass


class StatsUtils(object):

    DATE_FORMAT = "%Y-%m-%d"

    @staticmethod
    def user_time_to_user_dateutc(user_time):
        """
        from "2012-02-02 19:15:43 -0300"
        returns "2012-02-02"
        """

        utc = pytz.utc
        fmd = '%Y-%m-%d'
        execute_time_obj = parse(user_time)
        execute_time_utc = utc.normalize(execute_time_obj.astimezone(utc))
        user_date_utc = execute_time_utc.strftime(fmd)

        return user_date_utc

    @staticmethod
    def get_wikilife_week_info(user_date):

        """
        get_wikilife_week_info
        params:
            user_date: UTC date

        return:
            tuple:
                - week_id: ID from 1971-01-04 00:00:00 - Starting in week_id = 0
                - day_of_week: Monday is 0 and Sunday is 6.
        """

        timestring = "1971-01-04"

        user_date = datetime.fromtimestamp(time.mktime(time.strptime(user_date, StatsUtils.DATE_FORMAT)))
        week1 = datetime.fromtimestamp(time.mktime(time.strptime(timestring, StatsUtils.DATE_FORMAT)))

        week = user_date - week1

        week = int(math.floor(week.days / 7.0))

        if week < 0:
            raise PrehistoricalWeekException("Too old date")

        sts_day = user_date.weekday()

        return (week, sts_day)

    @staticmethod
    def get_hour_from_date(user_date):

        """
        get_hour_from_date
        params:
            user_date: local date

        return:
                - hour: 00:00:00
        """

        valid_date = datetime.fromtimestamp(time.mktime(time.strptime(user_date, "%Y-%m-%d %H:%M:%S +0000")))

        str_time = str(valid_date.hour) + ":" + str(valid_date.minute) + ":" + str(valid_date.second)

        return (str_time)

    @staticmethod
    def get_stats_dates_array_last_7_days(user_date_str):

        """
        get_stats_dates_array_last_7_days
        params:
            user_date_str: local datetime. type String. Format yyyy-MM-dd

        return:
            stats_dates: array with dates of last 7 days
        """
        user_date = datetime.fromtimestamp(time.mktime(time.strptime(user_date_str, StatsUtils.DATE_FORMAT)))

        stats_dates = []
        user_date = user_date - timedelta(days=6)
        oneday = timedelta(days=1)
        stdate = date(user_date.year, user_date.month, user_date.day)

        for i in range(7):
            stats_dates.append(stdate)
            stdate = stdate + oneday

        return (stats_dates)

    @staticmethod
    def get_numeric_value(str_value):
        value = -1

        if str_value == "Mild":
            value = 1
        if str_value == "Moderate":
            value = 3
        if str_value == "Severe":
            value = 5

        return value

    @staticmethod
    def get_date_from_week_id(week_id, day_index):
        """
        get_date_from_week_id

        This method returns the execution date from stat.

         Result = 1971-01-01 + the numbers of weeks + the numbers of days in the week.

        params:
            - week_id
            - day_index

        return
            - final_date - datetime object
        """
        timestring = "1971-01-04"
        final_date = datetime.strptime(timestring, "%Y-%m-%d")
        weeks = timedelta(weeks=week_id)
        days = timedelta(days=day_index)
        final_date = final_date + weeks + days
        return final_date
