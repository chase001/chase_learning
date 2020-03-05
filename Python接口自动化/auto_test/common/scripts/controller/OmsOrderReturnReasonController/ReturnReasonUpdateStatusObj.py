
from common.objects import BaseObj
from Gwe_service.api import *
                

class ReturnReasonUpdateStatusObj(BaseGwe):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(ReturnReasonUpdateStatusObj, self).__init__()
        self.info = "修改退货原因启用状态"
        self.uri = "/returnReason/update/status"
        self.method = "post"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()
            
    class Body(BaseObj):
        def __init__(self, **kwargs):
            self.status = None
            self.ids = None
            BaseObj.__init__(self, **kwargs)
    
    class Resp(object):
        def __init__(self):
            super(ReturnReasonUpdateStatusObj.Resp, self).__init__()
            self.code = None  # None
            self.data = None  # None
            self.message = None  # None
    
