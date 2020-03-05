
from common.objects import BaseObj
from Gwe_service.api import *
                

class ProductUpdateVerifyStatusObj(BaseGwe):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(ProductUpdateVerifyStatusObj, self).__init__()
        self.info = "批量修改审核状态"
        self.uri = "/product/update/verifyStatus"
        self.method = "post"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()
            
    class Body(BaseObj):
        def __init__(self, **kwargs):
            self.ids = None
            self.verifyStatus = None
            self.detail = None
            BaseObj.__init__(self, **kwargs)
    
    class Resp(object):
        def __init__(self):
            super(ProductUpdateVerifyStatusObj.Resp, self).__init__()
            self.code = None  # None
            self.data = None  # None
            self.message = None  # None
    
