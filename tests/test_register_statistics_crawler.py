# -*- coding: utf-8 -*-

__author__ = 'xudong'

from register_statistics.register_statistics_crawler import parse_register_statistics
from register_statistics.register_statistics import *
from datetime import datetime

def test_parse_html():
    with open('tests/register_statistics_demo.html', 'r') as f:
        html = f.read()

        statistics = parse_register_statistics(html)

        forward_housing_delivery = statistics[0]

        assert forward_housing_delivery.get(REGISTER_TYPE) == REGISTER_TYPE_FORWARD_HOUSING_DELIVERY
        assert forward_housing_delivery.get(REGISTER_DATE) == datetime.strptime('2016-03-30', '%Y-%m-%d')
        assert forward_housing_delivery.get(REGISTER_TOTAL_COUNT) == 405
        assert forward_housing_delivery.get(REGISTER_TOTAL_AREA) == 37131.9200
        assert forward_housing_delivery.get(REGISTER_RESIDENCE_COUNT) == 123
        assert forward_housing_delivery.get(REGISTER_RESIDENCE_AREA) == 17422.3000

        print(statistics)

