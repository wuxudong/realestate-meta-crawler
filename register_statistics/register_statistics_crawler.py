# -*- coding: utf-8 -*-

__author__ = 'xudong'

import urllib2
from datetime import datetime

from bs4 import BeautifulSoup

from register_statistics import *


def crawl_register_statistics():
    url = 'http://www.bjjs.gov.cn/tabid/2167/default.aspx'

    req = urllib2.Request(url)
    html = urllib2.urlopen(req).read()
    return parse_register_statistics(html)


def parse_register_statistics(html):
    soup = BeautifulSoup(html, 'html.parser', from_encoding="utf-8")

    records = list()

    records.append(parse_forward_housing_delivery(soup.select('div#ess_ctr5115_ModuleContent table:nth-of-type(6)')[0]))
    records.append(parse_complete_apartment(soup.select('div#ess_ctr5115_ModuleContent table:nth-of-type(10)')[0]))
    records.append(parse_second_hand_house(soup.select('div#ess_ctr5112_ModuleContent table:nth-of-type(6)')[0]))

    return records


def parse_forward_housing_delivery(table):
    total_count = int(table.select('#ess_ctr5115_FDCJY_HouseTransactionStatist_totalCount4')[0].string)
    total_area = float(table.select('#ess_ctr5115_FDCJY_HouseTransactionStatist_totalArea4')[0].string)

    residence_count = int(table.select('#ess_ctr5115_FDCJY_HouseTransactionStatist_residenceCount4')[0].string)
    residence_area = float(table.select('#ess_ctr5115_FDCJY_HouseTransactionStatist_residenceArea4')[0].string)

    date = datetime.strptime(table.select("#ess_ctr5115_FDCJY_HouseTransactionStatist_timeMark2")[0].string,
                             "%Y-%m-%d").date()

    register_type = REGISTER_TYPE_FORWARD_HOUSING_DELIVERY

    record = RegisterStatistics()
    record.set(REGISTER_TYPE, register_type)
    record.set(REGISTER_DATE, date)
    record.set(REGISTER_TOTAL_COUNT, total_count)
    record.set(REGISTER_RESIDENCE_COUNT, residence_count)
    record.set(REGISTER_TOTAL_AREA, total_area)
    record.set(REGISTER_RESIDENCE_AREA, residence_area)

    return record


def parse_complete_apartment(table):
    total_count = int(table.select('#ess_ctr5115_FDCJY_HouseTransactionStatist_totalCount8')[0].string)
    total_area = float(table.select('#ess_ctr5115_FDCJY_HouseTransactionStatist_totalArea8')[0].string)

    residence_count = int(table.select('#ess_ctr5115_FDCJY_HouseTransactionStatist_residenceCount8')[0].string)
    residence_area = float(table.select('#ess_ctr5115_FDCJY_HouseTransactionStatist_residenceArea8')[0].string)

    date = datetime.strptime(table.select("#ess_ctr5115_FDCJY_HouseTransactionStatist_timeMark4")[0].string,
                             "%Y-%m-%d").date()

    register_type = REGISTER_TYPE_COMPLETE_APARTMENT

    record = RegisterStatistics()
    record.set(REGISTER_TYPE, register_type)
    record.set(REGISTER_DATE, date)
    record.set(REGISTER_TOTAL_COUNT, total_count)
    record.set(REGISTER_RESIDENCE_COUNT, residence_count)
    record.set(REGISTER_TOTAL_AREA, total_area)
    record.set(REGISTER_RESIDENCE_AREA, residence_area)

    return record


def parse_second_hand_house(table):
    total_count = int(table.select('#ess_ctr5112_FDCJY_SignOnlineStatistics_totalCount4')[0].string)
    total_area = float(table.select('#ess_ctr5112_FDCJY_SignOnlineStatistics_totalArea4')[0].string)

    residence_count = int(table.select('#ess_ctr5112_FDCJY_SignOnlineStatistics_residenceCount4')[0].string)
    residence_area = float(table.select('#ess_ctr5112_FDCJY_SignOnlineStatistics_residenceArea4')[0].string)

    date = datetime.strptime(table.select("#ess_ctr5112_FDCJY_SignOnlineStatistics_timeMark2")[0].string,
                             "%Y-%m-%d").date()
    register_type = REGISTER_TYPE_SECOND_HAND_HOUSE

    record = RegisterStatistics()
    record.set(REGISTER_TYPE, register_type)
    record.set(REGISTER_DATE, date)
    record.set(REGISTER_TOTAL_COUNT, total_count)
    record.set(REGISTER_RESIDENCE_COUNT, residence_count)
    record.set(REGISTER_TOTAL_AREA, total_area)
    record.set(REGISTER_RESIDENCE_AREA, residence_area)

    return record
