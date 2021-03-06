
from common.objects import BaseObj
from order_service.api import *
                

class HomeBrandUpdateSortIdObj(BaseOrder):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(HomeBrandUpdateSortIdObj, self).__init__()
        self.info = "修改品牌排序"
        self.uri = "/home/brand/update/sort/{id}"
        self.method = "post"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()
            
    class Body(BaseObj):
        def __init__(self, **kwargs):
            self.id = None
            self.sort = None
            BaseObj.__init__(self, **kwargs)
    
    class Resp(object):
        def __init__(self):
            super(HomeBrandUpdateSortIdObj.Resp, self).__init__()
            self.code = None  # None
            self.data = None  # None
            self.message = None  # None
    
