# -*- coding: utf-8 -*-#

# -------------------------------------------------------------------------------
# Name:         test_service2_m2
# Description:  
# Author            Dongtian
# Date:         2020-01-05
# -------------------------------------------------------------------------------


from Auto.utils.BaseTestCase import BaseTestCase


class TestDemo002(BaseTestCase):

    def test_demo2(self):
        """测试用例---正确---"""
        self.assertEqual(1, 1)

    def test_demo1(self):
        """测试用例------"""
        self.assertEqual(1, 2)

    def test_demo3(self):
        """测试用例------"""
        pass
