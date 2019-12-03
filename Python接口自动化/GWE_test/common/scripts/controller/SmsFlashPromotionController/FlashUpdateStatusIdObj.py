
from common.objects import BaseObj
from order_service.api import *
                

class FlashUpdateStatusIdObj(BaseOrder):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(FlashUpdateStatusIdObj, self).__init__()
        self.info = "修改上下线状态"
        self.uri = "/flash/update/status/{id}"
        self.method = "post"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()
            
    class Body(BaseObj):
        def __init__(self, **kwargs):
            self.id = None
            self.status = None
            BaseObj.__init__(self, **kwargs)
    
    class Resp(object):
        def __init__(self):
            super(FlashUpdateStatusIdObj.Resp, self).__init__()
            pass
    
