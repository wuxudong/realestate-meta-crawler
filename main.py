import leancloud
from leancloud import Query
from leancloud import LeanCloudError

from check.check import *
from check import check_crawler

from register_statistics.register_statistics import *
from register_statistics import register_statistics_crawler


leancloud.init('30WAnGl011OU88WAGBH5dmuz-gzGzoHsz', 'eBxQv0goJVso11f6zx6lbRJm')


def main():

    try:
        query = Query(Check)
        query.count()
    except LeanCloudError as e:
        empty = Check()
        empty.save()

    for check in check_crawler.crawl_check():
        query = Query(Check)
        query.equal_to(CHECK_ID, check.get(CHECK_ID))
        if not query.find():
            check.save()

    try:
        query = Query(RegisterStatistics)
        query.count()
    except LeanCloudError as e:
        empty = RegisterStatistics()
        empty.save()

    for statistics in register_statistics_crawler.crawl_register_statistics():
        query = Query(RegisterStatistics)
        query.equal_to(REGISTER_TYPE, statistics.get(REGISTER_TYPE))
        query.equal_to(REGISTER_DATE, statistics.get(REGISTER_DATE))

        if not query.find():
            statistics.save()


if __name__ == '__main__':
    main()
