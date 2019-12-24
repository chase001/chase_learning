
from common.objects import BaseObj
from order_service.api import *
                

class ProductUpdatePublishStatusObj(Baserder):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(ProductUpdatePublishStatusObj, self).__init__()
        self.info = "批量上下架"
        self.uri = "/product/update/publishStatus"
        self.method = "post"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()
            
    class Body(BaseObj):
        def __init__(self, **kwargs):
            self.ids = None
            self.publishStatus = None
            BaseObj.__init__(self, **kwargs)
    
    class Resp(object):
        def __init__(self):
            super(ProductUpdatePublishStatusObj.Resp, self).__init__()
            self.code = None  # None
            self.data = None  # None
            self.message = None  # None
    
