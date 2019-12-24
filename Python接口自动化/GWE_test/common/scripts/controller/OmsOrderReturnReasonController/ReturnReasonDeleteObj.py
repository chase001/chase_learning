
from common.objects import BaseObj
from order_service.api import *
                

class ReturnReasonDeleteObj(BaseOrder):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(ReturnReasonDeleteObj, self).__init__()
        self.info = "批量删除退货原因"
        self.uri = "/returnReason/delete"
        self.method = "post"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()
            
    class Body(BaseObj):
        def __init__(self, **kwargs):
            self.ids = None
            BaseObj.__init__(self, **kwargs)
    
    class Resp(object):
        def __init__(self):
            super(ReturnReasonDeleteObj.Resp, self).__init__()
            self.code = None  # None
            self.data = None  # None
            self.message = None  # None
    
