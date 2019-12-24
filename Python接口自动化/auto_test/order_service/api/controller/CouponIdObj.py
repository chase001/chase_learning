
from common.objects import BaseObj
from order_service.api import *


class CouponIdObj(BaseOrderManageService):
    """api controller obj"""
    def __init__(self, coupon_id, **kwargs):
        super(CouponIdObj, self).__init__()
        self.info = "获取单个优惠券的详细信息"
        self.uri = "/coupon/{coupon_id}".format(coupon_id=coupon_id)
        self.method = "get"
        self.body = self.Body(coupon_id)
        self.resp = self.Resp()

    class Body(BaseObj):
        def __init__(self,coupon_id):
            self.id = coupon_id
            BaseObj.__init__(self)

    class Resp(object):
        def __init__(self):
            super(CouponIdObj.Resp, self).__init__()
            self.code = None  # None
            self.data = self.SmsCouponParam()  # None
            self.message = None  # None

        class SmsCouponParam(object):
            """None"""
            def __init__(self):
                self.amount = None  # 金额
                self.code = None  # 优惠码
                self.count = None  # 数量
                self.enableTime = None  # 可以领取的日期
                self.endTime = None  # None
                self.id = None  # None
                self.memberLevel = None  # 可领取的会员类型：0->无限时
                self.minPoint = None  # 使用门槛；0表示无门槛
                self.name = None  # None
                self.note = None  # 备注
                self.perLimit = None  # 每人限领张数
                self.platform = None  # 使用平台：0->全部；1->移动；2->PC
                self.productCategoryRelationList = [self.SmsCouponProductCategoryRelation()]  # None
                self.productRelationList = [self.SmsCouponProductRelation()]  # None
                self.publishCount = None  # 发行数量
                self.receiveCount = None  # 领取数量
                self.startTime = None  # None
                self.type = None  # 优惠卷类型；0->全场赠券；1->会员赠券；2->购物赠券；3->注册赠券
                self.useCount = None  # 已使用数量
                self.useType = None  # 使用类型：0->全场通用；1->指定分类；2->指定商品

            class SmsCouponProductCategoryRelation(object):
                """None"""
                def __init__(self):
                    pass

            class SmsCouponProductRelation(object):
                """None"""
                def __init__(self):
                    pass

