# -*- coding: utf-8 -*-#

# -------------------------------------------------------------------------------
# Name:         BaseTestCase
# Description:  
# Author            Dongtian
# Date:         2020-01-12
# -------------------------------------------------------------------------------
import unittest
import time


class BaseTestCase(unittest.TestCase):


    def setUp(self):
        self.st = time.time()


    def tearDown(self):
        self.total_time = str(time.time() - self.st)[:7]
