# -*- coding: utf-8 -*-#

# -------------------------------------------------------------------------------
# Name:         generate_reports
# Description:  
# Author            Dongtian
# Date:         2020-01-05
# -------------------------------------------------------------------------------
import jinja2
from jinja2 import Environment, FileSystemLoader
import os
import time
import random

# self.my_success = []
# self.my_fail = []
# self.my_errors = []
# self.my_skiped = []


# generate_id = random.choice["a","b","c","d"]+
from Auto.utils.tools import generate_len_str


def generate_report(test_result, start_time, duration, Title="XXXX接口自动化测试报告"):
    """
    :param test_result:  测试结果
    :param start_time:  其实时间
    :param duration:  耗时
    :param Title:  标题
    :return:
    """
    test_cases_list = []
    success = getattr(test_result, "my_success")
    error = getattr(test_result, "my_errors")
    failed = getattr(test_result, "my_fail")
    skip = getattr(test_result, "my_skiped")

    def pack_case(res):
        for i in range(len(res)):

            res[i]["id"] = generate_len_str(8)
            try:
                res[i]['casename'] = res[i]['TestService']._testMethodName
                res[i]['desc'] = res[i]['TestService'].shortDescription()
            except Exception as e:
                print(e)
                res[i]['casename'] = str(res[i]['TestService'].__module__)

    for i in [success, failed, error, skip]:
        pack_case(i)
        test_cases_list.extend(i)

    # test_cases_list = [success, error, failed, skip]
    main_path = str(__file__).split("Auto")

    report_path = main_path[0] + os.sep.join(["Auto", "templates"])

    env = Environment(loader=FileSystemLoader(report_path))

    template = env.get_template('report.html')

    res = template.render(Title=Title,
                          start_time=start_time,
                          duration=duration,
                          total_test=len(test_cases_list),
                          success=len(success),
                          failed=len(failed),
                          error=len(error),
                          skip=len(skip),
                          test_cases_list=test_cases_list)

    with open("/Users/dingze/Desktop/api-demo-test/Auto/templates/demo_report.html", 'w', encoding="utf-8") as f:
        f.write(res)
        f.flush()
