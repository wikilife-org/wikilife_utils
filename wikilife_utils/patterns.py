# coding=utf-8

"""
Wikilife Standard Patterns
"""

import re

TIME_PATTERN = "(\d{2}:\d{2}:\d{2})"
TIME_PATTERN_C = re.compile(TIME_PATTERN)
"""
hh24:mm:ss
"""

DATE_PATTERN = "(\d{4})-(\d{2})-(\d{2})"
DATE_PATTERN_C = re.compile(DATE_PATTERN)
"""
yyyy-MM-dd
"""

DATETIME_PATTERN = "%s %s" % (DATE_PATTERN, TIME_PATTERN)
DATETIME_PATTERN_C = re.compile(DATETIME_PATTERN)
"""
yyyy-MM-dd hh24:mm:ss
"""

TZ_PATTERN = "(-|\+)(\d{4})"
"""
-zzzz
+zzzz
"""

DATETIMETZ_PATTERN = "%s %s %s" % (DATE_PATTERN, TIME_PATTERN, TZ_PATTERN)
DATETIMETZ_PATTERN_C = re.compile(DATETIMETZ_PATTERN)
"""
yyyy-MM-dd hh24:mm:ss -zzzz
"""

USERNAME_PATTERN = "^[a-zA-Z0-9_.-]+$"
USERNAME_PATTERN_C = re.compile(USERNAME_PATTERN)
"""
"""

PIN_PATTERN = "^[a-zA-Z0-9]+$"
PIN_PATTERN_C = re.compile(PIN_PATTERN)
"""
"""
