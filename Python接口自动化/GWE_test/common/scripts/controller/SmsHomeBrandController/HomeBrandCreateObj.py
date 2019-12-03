
from common.objects import BaseObj
from order_service.api import *
                

class HomeBrandCreateObj(BaseOrder):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(HomeBrandCreateObj, self).__init__()
        self.info = "添加首页推荐品牌"
        self.uri = "/home/brand/create"
        self.method = "post"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()
            
    class Body(BaseObj):
        def __init__(self, **kwargs):
            BaseObj.__init__(self, **kwargs)
    
    class Resp(object):
        def __init__(self):
            super(HomeBrandCreateObj.Resp, self).__init__()
            self.code = None  # None
            self.data = None  # None
            self.message = None  # None
    
