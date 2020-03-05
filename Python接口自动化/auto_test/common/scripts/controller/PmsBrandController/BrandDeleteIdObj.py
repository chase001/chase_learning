
from common.objects import BaseObj
from Gwe_service.api import *
                

class BrandDeleteIdObj(BaseGwe):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(BrandDeleteIdObj, self).__init__()
        self.info = "删除品牌"
        self.uri = "/brand/delete/{id}"
        self.method = "get"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()
            
    class Body(BaseObj):
        def __init__(self, **kwargs):
            self.id = None
            BaseObj.__init__(self, **kwargs)
    
    class Resp(object):
        def __init__(self):
            super(BrandDeleteIdObj.Resp, self).__init__()
            self.code = None  # None
            self.data = None  # None
            self.message = None  # None
    
