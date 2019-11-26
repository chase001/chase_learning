

class CouponHistoryList(BaseOrder):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(CouponHistoryList, self).__init__()
        self.info = "根据优惠券id，使用状态，订单编号分页获取领取记录"
        self.uri = "/couponHistory/list"
        self.method = "get"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()

    class Body(BaseObj):
        def __init__(self, **kwargs):
            self.couponId = None
            self.useStatus = None
            self.orderSn = None
            self.pageSize = None
            self.pageNum = None
            BaseObj.__init__(**kwargs)

    class Resp(object):
        def __init__(self):
            super(CouponHistoryList.Resp, self).__init__()
            self.code = None  # None
            self.data = self.CommonPage«SmsCouponHistory»()  # None
            self.message = None  # None

        class CommonPage«SmsCouponHistory»(object):
            """None"""
            def __init__(self):
                self.list = [self.SmsCouponHistory()]  # None
                self.pageNum = None  # None
                self.pageSize = None  # None
                self.total = None  # None
                self.totalPage = None  # None

            class SmsCouponHistory(object):
                """None"""
                def __init__(self):
                    self.couponCode = None  # None
                    self.couponId = None  # None
                    self.createTime = None  # None
                    self.getType = None  # 获取类型：0->后台赠送；1->主动获取
                    self.id = None  # None
                    self.memberId = None  # None
                    self.memberNickname = None  # 领取人昵称
                    self.orderId = None  # 订单编号
                    self.orderSn = None  # 订单号码
                    self.useStatus = None  # 使用状态：0->未使用；1->已使用；2->已过期
                    self.useTime = None  # 使用时间

