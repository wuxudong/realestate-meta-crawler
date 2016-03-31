# -*- coding: utf-8 -*-

__author__ = 'xudong'

from datetime import datetime

from bs4 import BeautifulSoup

from check.check import *
from check.check_crawler import parse_table


def test_parse_rows():
    with open('tests/check_demo.html', 'r') as f:
        html = f.read()

        rows = parse_table(BeautifulSoup(html, 'html.parser'))
        assert len(rows) == 13
        assert rows[0].get(CHECK_ID) == 1491671
        assert rows[0].get(CHECK_AGENT) == u'北京我爱我家房地产经纪有限公司'
        assert rows[0].get(CHECK_DISTRICT) == u'海淀区'
        assert rows[0].get(CHECK_COMMUNITY) == u'远洋风景'
        assert rows[0].get(CHECK_ROOMS) == u'二室一厅'
        assert rows[0].get(CHECK_AREA) == 67.63
        assert rows[0].get(CHECK_PRICE) == u'526万元'
        assert rows[0].get(CHECK_DATE) == datetime.strptime('2016-03-28', '%Y-%m-%d')

        assert rows[12].get(CHECK_ID) == 1488543

        print(rows)
