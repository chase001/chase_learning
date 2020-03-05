
from common.objects import BaseObj
from Gwe_service.api import *
                

class ProductUpdateDeleteStatusObj(BaseGwe):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(ProductUpdateDeleteStatusObj, self).__init__()
        self.info = "批量修改删除状态"
        self.uri = "/product/update/deleteStatus"
        self.method = "post"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()
            
    class Body(BaseObj):
        def __init__(self, **kwargs):
            self.ids = None
            self.deleteStatus = None
            BaseObj.__init__(self, **kwargs)
    
    class Resp(object):
        def __init__(self):
            super(ProductUpdateDeleteStatusObj.Resp, self).__init__()
            self.code = None  # None
            self.data = None  # None
            self.message = None  # None
    
