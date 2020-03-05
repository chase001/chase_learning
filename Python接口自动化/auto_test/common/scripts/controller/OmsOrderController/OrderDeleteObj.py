
from common.objects import BaseObj
from Gwe_service.api import *
                

class OrderDeleteObj(BaseGwe):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(OrderDeleteObj, self).__init__()
        self.info = "批量删除订单"
        self.uri = "/order/delete"
        self.method = "post"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()
            
    class Body(BaseObj):
        def __init__(self, **kwargs):
            self.ids = None
            BaseObj.__init__(self, **kwargs)
    
    class Resp(object):
        def __init__(self):
            super(OrderDeleteObj.Resp, self).__init__()
            self.code = None  # None
            self.data = None  # None
            self.message = None  # None
    
