
from common.objects import BaseObj
from order_service.api import *
                

class CouponHistoryListObj(Baserder):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(CouponHistoryListObj, self).__init__()
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
            BaseObj.__init__(self, **kwargs)
    
    class Resp(object):
        def __init__(self):
            super(CouponHistoryListObj.Resp, self).__init__()
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
    
