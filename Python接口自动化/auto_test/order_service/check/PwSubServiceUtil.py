# 查询数据库数据并将结果返回
from common.db.my_db import MyDB
from sub_service_1.db.model import *


class PwSubServiceUtil(object):
    def __init__(self, order_id):
        self.order_id = order_id

    def table_name_1(self):
        # 查询数据库数据并将结果返回 具体写法如下，支持分库，分表
        # return MyDB(table=OrderMaster).conditions(order_id=self.order_id
        #                                           ).exc(is_normal_obj=True)
        return [self.order_id]
