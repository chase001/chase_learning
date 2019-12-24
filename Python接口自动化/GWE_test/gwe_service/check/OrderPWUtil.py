# 查询数据库数据并将结果返回
from common.db.my_db import MyDB
from order_service.db.order_model import *


class OrderPWUtil(object):
    def __init__(self):
        pass

    def sms_coupon(self, **kwargs):
        # 查询数据库数据并将结果返回 具体写法如下，支持分库，分表
        return MyDB(table=SmsCoupon).conditions(**kwargs).limit(1).exc(is_normal_obj=True)
        # return [self.order_id]


db = OrderPWUtil()
