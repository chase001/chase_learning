from order_service.api import *


class CouponCreateApi(OrderManageCreate):
    def __init__(self, status=0, message='成功', **kwargs):
        super(CouponCreateApi, self).__init__()
        self.status = status  # 期望返回结果
        self.message = message
        self.update_default_body(**kwargs)

    def update_default_body(self, **kwargs):
        """原则：必传参数必须给值，非必传参数不给值"""
        self.body.amount = 299.99
        self.body.enableTime = "2019-11-28T16:00:00.000Z"
        self.body.minPoint = 10
        self.body.name = "测试优惠券"
        self.body.note = "备注内容"
        self.body.perLimit = 1
        self.body.platform = 0
        self.body.productCategoryRelationList = []
        self.body.productRelationList = []
        self.body.publishCount = 1000
        self.body.startTime = "2019-11-14T16:00:00.000Z"
        self.body.type = 0
        self.body.useType = 0
        self.body.update_value(**kwargs)

    def check(self):
        """
        1. 检查状态self.status
        2. 检查resp
        3. 检查数据落库
        2. 检查其他内容：redis, mq ,
        :return:
        """
        pass
        # assert self.status == self.resp.status  # 根据业务可做抽取
        # from sub_service_1.check.SubServiceCompare import SubServiceCompare
        # compare = SubServiceCompare(order_id=111111)
        # compare.add_table(table_name_key='table_name_1')
        # compare.do(ex=['id'])
