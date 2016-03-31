# -*- coding: utf-8 -*-

from leancloud import Object

REGISTER_DATE = 'date'
REGISTER_TYPE = 'type'
REGISTER_TOTAL_COUNT = 'total_count'
REGISTER_RESIDENCE_COUNT = 'residence_count'

REGISTER_TOTAL_AREA = 'total_area'
REGISTER_RESIDENCE_AREA = 'residence_area'

REGISTER_TYPE_FORWARD_HOUSING_DELIVERY = 'forward_housing_delivery'
REGISTER_TYPE_COMPLETE_APARTMENT = 'complete_apartment'
REGISTER_TYPE_SECOND_HAND_HOUSE = 'second_hand_house'


class RegisterStatistics(Object):
    def __unicode__(self):
        return u"type %s, total_count %d, residence_count %d, total_area %f, residence_area %f, date %s" \
               % (self.get(REGISTER_TYPE),
                  self.get(REGISTER_TOTAL_COUNT), self.get(REGISTER_RESIDENCE_COUNT), self.get(REGISTER_TOTAL_AREA),
                  self.get(REGISTER_RESIDENCE_AREA), self.get(REGISTER_DATE).strftime('%Y-%m-%d'))

    def __str__(self, encoding="utf-8"):
        return self.__unicode__().encode(encoding)
