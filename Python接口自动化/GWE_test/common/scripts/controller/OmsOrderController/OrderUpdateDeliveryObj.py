
from common.objects import BaseObj
from order_service.api import *
                

class OrderUpdateDeliveryObj(BaseOrder):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(OrderUpdateDeliveryObj, self).__init__()
        self.info = "批量发货"
        self.uri = "/order/update/delivery"
        self.method = "post"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()
            
    class Body(BaseObj):
        def __init__(self, **kwargs):
            BaseObj.__init__(self, **kwargs)
    
    class Resp(object):
        def __init__(self):
            super(OrderUpdateDeliveryObj.Resp, self).__init__()
            self.code = None  # None
            self.data = None  # None
            self.message = None  # None
    
