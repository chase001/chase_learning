
from common.objects import BaseObj
from Gwe_service.api import *
                

class ReturnApplyIdObj(BaseGwe):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(ReturnApplyIdObj, self).__init__()
        self.info = "获取退货申请详情"
        self.uri = "/returnApply/{id}"
        self.method = "get"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()
            
    class Body(BaseObj):
        def __init__(self, **kwargs):
            self.id = None
            BaseObj.__init__(self, **kwargs)
    
    class Resp(object):
        def __init__(self):
            super(ReturnApplyIdObj.Resp, self).__init__()
            self.code = None  # None
            self.data = None  # None
            self.message = None  # None
    
