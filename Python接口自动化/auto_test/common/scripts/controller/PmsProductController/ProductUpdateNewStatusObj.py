
from common.objects import BaseObj
from Gwe_service.api import *
                

class ProductUpdateNewStatusObj(BaseGwe):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(ProductUpdateNewStatusObj, self).__init__()
        self.info = "批量设为新品"
        self.uri = "/product/update/newStatus"
        self.method = "post"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()
            
    class Body(BaseObj):
        def __init__(self, **kwargs):
            self.ids = None
            self.newStatus = None
            BaseObj.__init__(self, **kwargs)
    
    class Resp(object):
        def __init__(self):
            super(ProductUpdateNewStatusObj.Resp, self).__init__()
            self.code = None  # None
            self.data = None  # None
            self.message = None  # None
    
