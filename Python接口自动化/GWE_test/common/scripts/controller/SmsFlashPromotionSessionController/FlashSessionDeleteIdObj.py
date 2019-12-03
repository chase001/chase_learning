
from common.objects import BaseObj
from order_service.api import *
                

class FlashSessionDeleteIdObj(BaseOrder):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(FlashSessionDeleteIdObj, self).__init__()
        self.info = "删除场次"
        self.uri = "/flashSession/delete/{id}"
        self.method = "post"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()
            
    class Body(BaseObj):
        def __init__(self, **kwargs):
            self.id = None
            BaseObj.__init__(self, **kwargs)
    
    class Resp(object):
        def __init__(self):
            super(FlashSessionDeleteIdObj.Resp, self).__init__()
            self.code = None  # None
            self.data = None  # None
            self.message = None  # None
    
