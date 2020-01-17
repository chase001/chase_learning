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
from Auto.utils.generate_reports import generate_report
from Auto.utils.myresults import MyResult
import datetime


def start_dir_path(x):
    return os.sep.join([os.getcwd(), x, "cases"])


def suite(x, y):
    return unittest.TestLoader().discover(pattern=x, start_dir=y)


if __name__ == '__main__':
    start_time = datetime.datetime.now()
    suites = suite("test*.py", start_dir_path("Auto"))

    runner = unittest.TextTestRunner(resultclass=MyResult)

    res = runner.run(suites)
    print(vars(res))
    duration = datetime.datetime.now() - start_time
    print(res.my_fail)

    generate_report(start_time=start_time, test_result=res, duration=duration)
