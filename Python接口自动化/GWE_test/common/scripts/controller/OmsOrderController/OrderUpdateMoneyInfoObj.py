
from common.objects import BaseObj
from order_service.api import *
                

class OrderUpdateMoneyInfoObj(Baserder):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(OrderUpdateMoneyInfoObj, self).__init__()
        self.info = "修改订单费用信息"
        self.uri = "/order/update/moneyInfo"
        self.method = "post"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()
            
    class Body(BaseObj):
        def __init__(self, **kwargs):
            self.discountAmount = None  # None
            self.freightAmount = None  # None
            self.orderId = None  # None
            self.status = None  # None
            BaseObj.__init__(self, **kwargs)
    
    class Resp(object):
        def __init__(self):
            super(OrderUpdateMoneyInfoObj.Resp, self).__init__()
            self.code = None  # None
            self.data = None  # None
            self.message = None  # None
    
