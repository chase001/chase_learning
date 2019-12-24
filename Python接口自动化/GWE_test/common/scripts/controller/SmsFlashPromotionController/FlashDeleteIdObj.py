
from common.objects import BaseObj
from order_service.api import *
                

class FlashDeleteIdObj(Baserder):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(FlashDeleteIdObj, self).__init__()
        self.info = "删除活动信息"
        self.uri = "/flash/delete/{id}"
        self.method = "post"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()
            
    class Body(BaseObj):
        def __init__(self, **kwargs):
            self.id = None
            BaseObj.__init__(self, **kwargs)
    
    class Resp(object):
        def __init__(self):
            super(FlashDeleteIdObj.Resp, self).__init__()
            pass
    
