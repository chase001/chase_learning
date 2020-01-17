# -*- coding: utf-8 -*-#

# -------------------------------------------------------------------------------
# Name:         test_service_modle1
# Description:  
# Author            Dongtian
# Date:         2020-01-05
# -------------------------------------------------------------------------------

import unittest

from Auto.utils.logger import logger


class TestDemo001(unittest.TestCase):

    def test_demo1(self):
        logger.info("测试------")
        self.assertEqual(1, 2)
