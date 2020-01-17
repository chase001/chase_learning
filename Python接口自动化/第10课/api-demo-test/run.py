# -*- coding: utf-8 -*-#

# -------------------------------------------------------------------------------
# Name:         run
# Description:  
# Author            Dongtian
# Date:         2020-01-05
# -------------------------------------------------------------------------------


import os
import unittest


# start_dir_path = lambda x: os.sep.join([os.getcwd(), x, "cases"])
#
# suite = lambda x, y: unittest.TestLoader().discover(pattern=x, start_dir=y)

def start_dir_path(x):
    return os.sep.join([os.getcwd(), x, "cases"])


def suite(x, y):
    return unittest.TestLoader().discover(pattern=x, start_dir=y)


if __name__ == '__main__':
    suites = suite("test*.py", start_dir_path("Auto"))
    runner = unittest.TextTestRunner()
    res = runner.run(suites)
    # print(vars(res))
