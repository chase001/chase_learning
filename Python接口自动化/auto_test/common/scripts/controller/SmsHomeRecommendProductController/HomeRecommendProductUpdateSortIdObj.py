
from common.objects import BaseObj
from order_service.api import *
                

class HomeRecommendProductUpdateSortIdObj(BaseOrder):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(HomeRecommendProductUpdateSortIdObj, self).__init__()
        self.info = "修改推荐排序"
        self.uri = "/home/recommendProduct/update/sort/{id}"
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
            super(HomeRecommendProductUpdateSortIdObj.Resp, self).__init__()
            self.code = None  # None
            self.data = None  # None
            self.message = None  # None
    
