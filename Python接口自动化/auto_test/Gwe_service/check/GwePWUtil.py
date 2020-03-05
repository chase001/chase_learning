# 查询数据库数据并将结果返回
from common.db.my_db import MyDB
from Gwe_service.db.Gwe_model import *


class GwePWUtil(object):
    def __init__(self,):
        pass

    def sms_coupon(self, like_name=None, **kwargs):
        # 查询数据库数据并将结果返回 具体写法如下，支持分库，分表
        where = SmsCoupon.name.contains(like_name) if like_name else None # name like "%测试%"
        return MyDB(table=SmsCoupon).conditions(where=where,
                                                **kwargs).exc(is_normal_obj=True)
        # return MyDB(table=SmsCoupon).conditions(**kwargs).limit(1).exc(is_normal_obj=True)



db = GwePWUtil()
