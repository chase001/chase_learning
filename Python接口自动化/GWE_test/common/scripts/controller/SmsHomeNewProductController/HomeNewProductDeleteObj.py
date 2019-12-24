
from common.objects import BaseObj
from order_service.api import *
                

class HomeNewProductDeleteObj(Baserder):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(HomeNewProductDeleteObj, self).__init__()
        self.info = "批量删除推荐"
        self.uri = "/home/newProduct/delete"
        self.method = "post"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()
            
    class Body(BaseObj):
        def __init__(self, **kwargs):
            self.ids = None
            BaseObj.__init__(self, **kwargs)
    
    class Resp(object):
        def __init__(self):
            super(HomeNewProductDeleteObj.Resp, self).__init__()
            self.code = None  # None
            self.data = None  # None
            self.message = None  # None
    
