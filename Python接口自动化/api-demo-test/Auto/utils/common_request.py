# -*- coding: utf-8 -*-#

# -------------------------------------------------------------------------------
# Name:         common_request
# Description:  
# Author            Dongtian
# Date:         2020-01-05
# -------------------------------------------------------------------------------
import requests
import time


# import urllib3
# urllib3.disable_warnings()

def send_requests(url, data, timeout=10, headers=None, verify=True, retry_time=0.1, method="post", retry_num=3,
                  req=None):
    """
    :param url:  url
    :param data:  数据
    :param method:  方法
    :param timeout:  超时
    :param retry_num:  重试次数
    :param headers:  请求头
    :param req:  请求 (最重要)
    :param verify:  鉴权
    :param retry_time:  重试时间间隔
    :return:
    """
    if type(retry_time) not in [int, float]:
        raise ValueError("retry_time 必须是int 或者float")

    headers = {"content-type": "appalcation/json"} if headers is None else headers

    requests_param = {
        'url': url,
        "json": data,
        "headers": headers,
        'verify': verify,
        'timeout': timeout
    }
    # 登录状态保持
    req = requests.session() if req is None else req

    _retry_num = 0
    _res = None
    while _retry_num < retry_num:
        try:
            if method == "post":
                _res = req.post(**requests_param)
            if method == "get":
                requests_param['params'] = data
                _res = req.get(**requests_param)
            else:
                raise Exception("目前只支持get和post 两种请求！！！")

            break

        except Exception as e:
            if _retry_num == retry_num and _res is None:
                raise Exception(e)
            _retry_num += 1
            print("开始尝试重试。。。。第{}次".format(_retry_num))
            time.sleep(retry_time)
            continue

    return res, req


if __name__ == '__main__':
    res, req = send_requests(url="https://www.baidu91.com/", method="get", data={},timeout=2)

    print(res)
