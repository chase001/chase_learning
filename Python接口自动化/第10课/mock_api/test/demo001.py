# -*- coding: utf-8 -*-#

# -------------------------------------------------------------------------------
# Name:         demo001
# Description:  
# Author            Dongtian
# Date:         2019-12-29
# -------------------------------------------------------------------------------

import unittest


class TestDemo001(unittest.TestCase):
    @classmethod
    def setUpClass(cls):  # 1
        print("每个moudle  setupclass方法")

    @classmethod
    def tearDownClass(cls):  # 5
        print("每个moudle  teardownclass方法")

    def setUp(self):  # 2
        print("每条测试用例都会运行  setup方法")

    def tearDown(self):  # 4
        print("每条测试用例都会运行  teardown方法")

    def test_ademo(self):  # 3
        print("我是测试用例1")

    def test_cdemo2(self):  # 3
        print("我是测试用例2")

    def test_bdemo3(self):
        print("我是测试用例3")
if __name__ == '__main__':
    unittest.main()
