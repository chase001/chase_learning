# -*- coding: utf-8 -*-#

# -------------------------------------------------------------------------------
# Name:         Myconf
# Description:  
# Author            Dongtian
# Date:         2020-01-05
# -------------------------------------------------------------------------------
import configparser

import os


class MyConf(object):
    """读取配置文件"""

    def __init__(self, path):
        """
        :param path:  配置文件的路径
        """
        if os.path.exists(path):
            self.confFile = path
            self.cf = configparser.ConfigParser()
            self.cf.read(self.confFile)

    # def __call__(self, *args, **kwargs):
    #     return self.cf


path_list = str(__file__).split("Auto")
conf_path = path_list[0] + os.sep.join(['Auto', 'config.ini'])
cf = MyConf(conf_path).cf

if __name__ == '__main__':
    host = cf.get("db", "host")

    print(host)

# /Users/dingze/Desktop/api-demo-test/Auto/config.ini
