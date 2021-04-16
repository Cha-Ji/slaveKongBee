import pyupbit
import time
import datetime

import Model.Price
import Model.Key

from unittest import TestCase, main


class DateTests(TestCase):
    ticker = "KRW-GAS"

    def test_date(self):
        now = datetime.datetime.now()
        mid = datetime.datetime(now.year, now.month,
                                now.day) + datetime.timedelta(hours=33)

        self.assertEqual(mid.hour, 9)


if __name__ == '__main__':
    main()
