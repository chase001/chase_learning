# -*- coding: utf-8 -*-#

# -------------------------------------------------------------------------------
# Name:         demo00_request
# Description:  
# Author            Dongtian
# Date:         2019-12-29
# -------------------------------------------------------------------------------


import requests

# r = requests.get("https://www.baidu.com/")
#
# # get 请求传参  ?id=3&name=ddd
# print(r.content)  # 返回的二进制内容

r = requests.get('https://www.baidu.com/',params={"wd":"request","id":99})

print(r.url)