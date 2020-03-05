
from common.objects import BaseObj
from Gwe_service.api import *
                

class BrandDeleteBatchObj(BaseGwe):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(BrandDeleteBatchObj, self).__init__()
        self.info = "批量删除品牌"
        self.uri = "/brand/delete/batch"
        self.method = "post"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()
            
    class Body(BaseObj):
        def __init__(self, **kwargs):
            self.ids = None
            BaseObj.__init__(self, **kwargs)
    
    class Resp(object):
        def __init__(self):
            super(BrandDeleteBatchObj.Resp, self).__init__()
            self.code = None  # None
            self.data = None  # None
            self.message = None  # None
    
