
from common.objects import BaseObj
from order_service.api import *
                

class OrderUpdateReceiverInfoObj(BaseOrder):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(OrderUpdateReceiverInfoObj, self).__init__()
        self.info = "修改收货人信息"
        self.uri = "/order/update/receiverInfo"
        self.method = "post"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()
            
    class Body(BaseObj):
        def __init__(self, **kwargs):
            self.orderId = None  # None
            self.receiverCity = None  # None
            self.receiverDetailAddress = None  # None
            self.receiverName = None  # None
            self.receiverPhone = None  # None
            self.receiverPostCode = None  # None
            self.receiverProvince = None  # None
            self.receiverRegion = None  # None
            self.status = None  # None
            BaseObj.__init__(self, **kwargs)
    
    class Resp(object):
        def __init__(self):
            super(OrderUpdateReceiverInfoObj.Resp, self).__init__()
            self.code = None  # None
            self.data = None  # None
            self.message = None  # None
    
