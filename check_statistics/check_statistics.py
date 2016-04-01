# -*- coding: utf-8 -*-

from leancloud import Object

CHECK_STATISTICS_DATE = 'date'
CHECK_STATISTICS_TOTAL_COUNT = 'total_count'
CHECK_STATISTICS_RESIDENCE_COUNT = 'residence_count'

CHECK_STATISTICS_TOTAL_AREA = 'total_area'
CHECK_STATISTICS_RESIDENCE_AREA = 'residence_area'


class CheckStatistics(Object):
    def __unicode__(self):
        return u"total_count %d, residence_count %d, total_area %f, residence_area %f, date %s" \
               % (self.get(CHECK_STATISTICS_TOTAL_COUNT), self.get(CHECK_STATISTICS_RESIDENCE_COUNT), self.get(CHECK_STATISTICS_TOTAL_AREA),
                  self.get(CHECK_STATISTICS_RESIDENCE_AREA), self.get(CHECK_STATISTICS_DATE).strftime('%Y-%m-%d'))

    def __str__(self, encoding="utf-8"):
        return self.__unicode__().encode(encoding)
