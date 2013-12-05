# coding=utf-8

from wikilife_utils.stats_utils import StatsUtils, PrehistoricalWeekException
import unittest
import datetime


class StatsUtilsTests(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_get_wikilife_week_info(self):
        user_date = "2011-11-24"
        w_week_info = StatsUtils.get_wikilife_week_info(user_date)

        assert w_week_info[0] == 2133
        assert w_week_info[1] == 3

    def test_get_wikilife_week_info_first_week(self):
        user_date = "1971-01-04"
        week, sts_day = StatsUtils.get_wikilife_week_info(user_date)

        assert week == 0
        assert sts_day == 0

    def test_get_wikilife_week_info_prehistorical(self):
        user_date = "1970-11-24"

        try:
            w_week_info = StatsUtils.get_wikilife_week_info(user_date)
            print w_week_info 
            assert False
        except PrehistoricalWeekException, e:
            print e
            assert True
    
    def test_get_stats_dates_array_last_7_days(self):
        user_date = "2011-12-26"
        
        stats_dates = StatsUtils.get_stats_dates_array_last_7_days(user_date) 
        
        assert len(stats_dates) == 7
        assert str(stats_dates[0]) == "2011-12-20"
        assert str(stats_dates[1]) == "2011-12-21"
        assert str(stats_dates[2]) == "2011-12-22"
        assert str(stats_dates[3]) == "2011-12-23"
        assert str(stats_dates[4]) == "2011-12-24"
        assert str(stats_dates[5]) == "2011-12-25"
        assert str(stats_dates[6]) == "2011-12-26"
        
    def test_get_date_from_week_id(self):
        week_id = 0
        day_index = 0
        result_date = StatsUtils.get_date_from_week_id(week_id, day_index)
        print result_date
        assert str(result_date) == "1971-01-04 00:00:00"
        
        user_date = "2011-11-24"
        w_week_info = StatsUtils.get_wikilife_week_info(user_date)
        assert w_week_info[0] == 2133
        assert w_week_info[1] == 3
        
        week_id =  w_week_info[0]
        day_index = w_week_info[1] 
        
        result_date = StatsUtils.get_date_from_week_id(week_id, day_index)
        #print str(result_date) 
        assert str(result_date) == "2011-11-24 00:00:00"
        
        user_date = str(datetime.datetime.now())[:10]
        w_week_info = StatsUtils.get_wikilife_week_info(user_date)
        week_id =  w_week_info[0]
        day_index = w_week_info[1] 
        
        result_date = StatsUtils.get_date_from_week_id(week_id, day_index)
        assert str(result_date)[:10] ==  str(datetime.datetime.now())[:10]
        
        
        