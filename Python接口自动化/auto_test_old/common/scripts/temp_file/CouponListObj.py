

class CouponList(BaseOrder):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(CouponList, self).__init__()
        self.info = "根据优惠券名称和类型分页获取优惠券列表"
        self.uri = "/coupon/list"
        self.method = "get"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()

    class Body(BaseObj):
        def __init__(self, **kwargs):
            self.name = None
            self.type = None
            self.pageSize = None
            self.pageNum = None
            BaseObj.__init__(**kwargs)

    class Resp(object):
        def __init__(self):
            super(CouponList.Resp, self).__init__()
            self.code = None  # None
            self.data = self.CommonPage«SmsCoupon»()  # None
            self.message = None  # None

        class CommonPage«SmsCoupon»(object):
            """None"""
            def __init__(self):
                self.list = [self.SmsCoupon()]  # None
                self.pageNum = None  # None
                self.pageSize = None  # None
                self.total = None  # None
                self.totalPage = None  # None

            class SmsCoupon(object):
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
                    self.publishCount = None  # 发行数量
                    self.receiveCount = None  # 领取数量
                    self.startTime = None  # None
                    self.type = None  # 优惠卷类型；0->全场赠券；1->会员赠券；2->购物赠券；3->注册赠券
                    self.useCount = None  # 已使用数量
                    self.useType = None  # 使用类型：0->全场通用；1->指定分类；2->指定商品

