
from common.objects import BaseObj
from Gwe_service.api import *
                

class OrderUpdateCloseObj(BaseGwe):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(OrderUpdateCloseObj, self).__init__()
        self.info = "批量关闭订单"
        self.uri = "/order/update/close"
        self.method = "post"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()
            
    class Body(BaseObj):
        def __init__(self, **kwargs):
            self.ids = None
            self.note = None
            BaseObj.__init__(self, **kwargs)
    
    class Resp(object):
        def __init__(self):
            super(OrderUpdateCloseObj.Resp, self).__init__()
            self.code = None  # None
            self.data = None  # None
            self.message = None  # None
    
