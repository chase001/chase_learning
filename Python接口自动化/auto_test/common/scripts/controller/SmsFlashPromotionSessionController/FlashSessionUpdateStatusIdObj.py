
from common.objects import BaseObj
from Gwe_service.api import *
                

class FlashSessionUpdateStatusIdObj(BaseGwe):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(FlashSessionUpdateStatusIdObj, self).__init__()
        self.info = "修改启用状态"
        self.uri = "/flashSession/update/status/{id}"
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
            super(FlashSessionUpdateStatusIdObj.Resp, self).__init__()
            self.code = None  # None
            self.data = None  # None
            self.message = None  # None
    
