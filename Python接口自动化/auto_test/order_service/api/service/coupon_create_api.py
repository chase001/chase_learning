from order_service.api import *


class CouponCreateApi(OrderManageCreate):
    def __init__(self, status=200, message='操作成功', **kwargs):
        super(CouponCreateApi, self).__init__()
        self.status = status  # 期望返回结果
        self.message = message
        self.update_default_body(**kwargs)

    def get_coupon_info(self):
        self.coupon_info = None  # 从数据库中查询结果

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
        self.body.productRelationList = []
        self.body.productCategoryRelationList = []
        self.body.update_value(**kwargs)

    def add_cate_relation(self, **kwargs):
        """
        新增优惠券所属类目
        :param kwargs:
        :return:
        """
        cate = OrderManageCreate.Body.SmsCouponProductCategoryRelation
        add_item = cate(**kwargs)
        self.body.productCategoryRelationList.append(add_item)

    def check(self):
        """
        1. 检查状态self.status
        2. 检查resp
        3. 检查数据落库
        2. 检查其他内容：redis, mq ,
        :return:
        """
        # 新增类check
        from order_service.data.status import ConsStatusCode
        from order_service.check.ExpectObj import ExpectSmsCoupon
        from common.func import fill_in_obj_from_obj
        assert str(self.status) == str(self.resp.code)  # 根据业务可做抽取
        if self.status == ConsStatusCode.OK:
            from order_service.check.OrderPWUtil import db
            # r = db.sms_coupon(name="测试优惠券")
            r = db.sms_coupon(like_name="测试")[0]
            exp_obj = ExpectSmsCoupon()
            fill_in_obj_from_obj(exp_obj, self.body)
            from common.ObjAssert import ObjAssert
            ObjAssert().is_equal(exp_obj=exp_obj, act_obj=r)
            # compare = SubServiceCompare(order_id=111111)
            # compare.add_table(table_name_key='table_name_1')
            # compare.do(ex=['id'])

        # 修改类接口
        exp_obj = self.coupon_info
        exp_obj.status = 0
        act_obj = db.sms_coupon(id=self.body.id)[0]  # 接口已被调用之后数据库中优惠券的信息
        # 好处： 检查该接口修改了它该修改的地方同时保证它没有修改它不修改的地方
        ObjAssert().is_equal(exp_obj=exp_obj, act_obj=act_obj)
