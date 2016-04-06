# -*- coding: utf-8 -*-

__author__ = 'xudong'

import urllib2
from datetime import datetime

from bs4 import BeautifulSoup
import re

from check_statistics import *


def crawl_register_statistics():
    url = 'http://210.75.213.188/shh/portal/bjjs/index.aspx'

    req = urllib2.Request(url)
    html = urllib2.urlopen(req).read()
    return parse_check_statistics(html)


def parse_check_statistics(html):
    soup = BeautifulSoup(html, 'html.parser', from_encoding="utf-8")

    records = list()

    records.append(
        parse_check_statistics_table(soup.find('table', {'class': 'tjInfo'})))

    return records


def parse_check_statistics_table(table):
    total_count = int(table.select('tbody tr:nth-of-type(1) td')[0].string)
    total_area = float(table.select('tbody tr:nth-of-type(2) td')[0].string)

    residence_count = int(table.select('tbody tr:nth-of-type(3) td')[0].string)
    residence_area = float(table.select('tbody tr:nth-of-type(4) td')[0].string)

    date_content = table.select('thead tr th')[0].string
    date_string = re.search(u"([\d|-]+)核验房源", date_content).group(1)

    date = datetime.strptime(date_string, "%Y-%m-%d").date()

    record = CheckStatistics()
    record.set(CHECK_STATISTICS_DATE, date)
    record.set(CHECK_STATISTICS_TOTAL_COUNT, total_count)
    record.set(CHECK_STATISTICS_RESIDENCE_COUNT, residence_count)
    record.set(CHECK_STATISTICS_TOTAL_AREA, total_area)
    record.set(CHECK_STATISTICS_RESIDENCE_AREA, residence_area)

    return record
