
from common.objects import BaseObj
from order_service.api import *
                

class BrandUpdateShowStatusObj(Baserder):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(BrandUpdateShowStatusObj, self).__init__()
        self.info = "批量更新显示状态"
        self.uri = "/brand/update/showStatus"
        self.method = "post"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()
            
    class Body(BaseObj):
        def __init__(self, **kwargs):
            self.ids = None
            self.showStatus = None
            BaseObj.__init__(self, **kwargs)
    
    class Resp(object):
        def __init__(self):
            super(BrandUpdateShowStatusObj.Resp, self).__init__()
            self.code = None  # None
            self.data = None  # None
            self.message = None  # None
    
