# -*- coding: utf-8 -*-#

# -------------------------------------------------------------------------------
# Name:         test_service_modle1
# Description:  
# Author            Dongtian
# Date:         2020-01-05
# -------------------------------------------------------------------------------

import unittest
import time

from Auto.utils.BaseTestCase import BaseTestCase
from Auto.utils.logger import logger


class TestDemo001(BaseTestCase):

    def setUp(self):
        self.st = time.time()

    def tearDown(self):
        self.total_time = str(time.time() - self.st)[:7]
        print(self.total_time)

    def test_demo1(self):
        """测试demo1001"""
        logger.info("测试------")
        self.assertEqual(1, 2)


if __name__ == '__main__':
    unittest.main()
