# -*- coding: utf-8 -*-

__author__ = 'xudong'

from check_statistics.check_statistics_crawler import parse_check_statistics
from check_statistics.check_statistics import *
from datetime import datetime


def test_parse_html():
    with open('tests/check_statistics_demo.html', 'r') as f:
        html = f.read()

        statistics = parse_check_statistics(html)[0]

        assert statistics.get(CHECK_STATISTICS_DATE) == datetime.strptime('2016-03-31', '%Y-%m-%d')
        assert statistics.get(CHECK_STATISTICS_TOTAL_COUNT) == 633
        assert statistics.get(CHECK_STATISTICS_TOTAL_AREA) == 53808.56
        assert statistics.get(CHECK_STATISTICS_RESIDENCE_COUNT) == 567
        assert statistics.get(CHECK_STATISTICS_RESIDENCE_AREA) == 48156.27

        print(statistics)

