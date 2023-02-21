from unittest import TestCase

import datetime
import localnow


class Test(TestCase):
    def test_now(self):
        a = localnow.now()
        b = datetime.datetime.now(localnow.tz)
        self.assertLess((b - a).total_seconds(), 1)
