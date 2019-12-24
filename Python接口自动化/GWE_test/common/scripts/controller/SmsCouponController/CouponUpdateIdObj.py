
from common.objects import BaseObj
from order_service.api import *
                

class CouponUpdateIdObj(BaseOrder):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(CouponUpdateIdObj, self).__init__()
        self.info = "修改优惠券"
        self.uri = "/coupon/update/{id}"
        self.method = "post"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()
            
    class Body(BaseObj):
        def __init__(self, **kwargs):
            self.id = None
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
                self.couponId = None  # None
                self.id = None  # None
                self.parentCategoryName = None  # 父分类名称
                self.productCategoryId = None  # None
                self.productCategoryName = None  # 产品分类名称
            
        class SmsCouponProductRelation(object):
            """None"""
            def __init__(self):
            BaseObj.__init__(self, **kwargs)
    
    class Resp(object):
        def __init__(self):
            super(CouponUpdateIdObj.Resp, self).__init__()
            self.code = None  # None
            self.data = None  # None
            self.message = None  # None
    
