# -*- coding: utf-8 -*-

from leancloud import Object

CHECK_ID = 'check_id'
CHECK_DISTRICT = 'district'
CHECK_COMMUNITY = 'community'
CHECK_ROOMS = 'rooms'
CHECK_AREA = 'area'
CHECK_PRICE = 'price'
CHECK_AGENT = 'agent'
CHECK_DATE = 'date'


class Check(Object):
    def __unicode__(self):
        return u"id %i, district %s, community %s, rooms %s, area %f, price %s, agent %s, date %s" \
            % (self.get(CHECK_ID), self.get(CHECK_DISTRICT), self.get(CHECK_COMMUNITY),
               self.get(CHECK_ROOMS), self.get(CHECK_AREA), self.get(CHECK_PRICE),
               self.get(CHECK_AGENT), self.get(CHECK_DATE).strftime('%Y-%m-%d'))
    def __str__(self, encoding="utf-8"):
        return self.__unicode__().encode(encoding)
