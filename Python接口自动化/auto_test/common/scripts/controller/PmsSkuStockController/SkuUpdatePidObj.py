
from common.objects import BaseObj
from Gwe_service.api import *
                

class SkuUpdatePidObj(BaseGwe):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(SkuUpdatePidObj, self).__init__()
        self.info = "批量更新库存信息"
        self.uri = "/sku/update/{pid}"
        self.method = "post"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()
            
    class Body(BaseObj):
        def __init__(self, **kwargs):
            self.pid = None
            BaseObj.__init__(self, **kwargs)
    
    class Resp(object):
        def __init__(self):
            super(SkuUpdatePidObj.Resp, self).__init__()
            self.code = None  # None
            self.data = None  # None
            self.message = None  # None
    
