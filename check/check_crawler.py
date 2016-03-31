# -*- coding: utf-8 -*-
from check import *

__author__ = 'xudong'

import urllib2
from bs4 import BeautifulSoup
import re
from datetime import datetime


def crawl_check():
    url = 'http://210.75.213.188/shh/portal/newbjjs/list.aspx'

    req = urllib2.Request(url)
    html = urllib2.urlopen(req).read()

    soup = BeautifulSoup(html, 'html.parser', from_encoding="utf-8")

    records_desc = soup.select('table')[-1].tr.find_all('td')[0].string
    records_count = re.search(u"共有(\d+)条记录", records_desc).group(1)
    print(u'条数:' + records_count)

    page_desc = soup.select('table')[-1].tr.find_all('td')[5].string
    pages_count = re.search(u"页次：\d+/(\d+)页", page_desc).group(1)

    print(u'页数:' + pages_count)

    records = []

    for i in xrange(1, int(pages_count)):
        page_url = url + '?pagenumber=' + str(i)
        page_req = urllib2.Request(page_url)
        page_html = urllib2.urlopen(page_req).read()
        page_soup = BeautifulSoup(page_html, 'html.parser')
        table_html = page_soup.select('table')[1]

        records = records + parse_table(table_html)

    return records


def parse_table(table):
    rows = []
    for tr in table.find_all('tr')[1:]:
        tds = tr.find_all('td')
        check_id = int(tds[0].string)
        check_district = tds[1].string
        check_community = tds[2].string
        check_rooms = tds[3].string
        check_area = float(tds[4].string)
        check_price = tds[5].string
        check_agent = tds[6].string.strip()
        check_date = datetime.strptime(tds[7].string, '%Y-%m-%d')

        check = Check()
        check.set(CHECK_ID, check_id)
        check.set(CHECK_DISTRICT, check_district)
        check.set(CHECK_COMMUNITY, check_community)
        check.set(CHECK_ROOMS, check_rooms)
        check.set(CHECK_AREA, check_area)
        check.set(CHECK_PRICE, check_price)
        check.set(CHECK_AGENT, check_agent)
        check.set(CHECK_DATE, check_date)

        rows.append(check)

    return rows