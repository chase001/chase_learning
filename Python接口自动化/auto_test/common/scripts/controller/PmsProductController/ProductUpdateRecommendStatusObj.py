
from common.objects import BaseObj
from order_service.api import *
                

class ProductUpdateRecommendStatusObj(BaseOrder):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(ProductUpdateRecommendStatusObj, self).__init__()
        self.info = "批量推荐商品"
        self.uri = "/product/update/recommendStatus"
        self.method = "post"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()
            
    class Body(BaseObj):
        def __init__(self, **kwargs):
            self.ids = None
            self.recommendStatus = None
            BaseObj.__init__(self, **kwargs)
    
    class Resp(object):
        def __init__(self):
            super(ProductUpdateRecommendStatusObj.Resp, self).__init__()
            self.code = None  # None
            self.data = None  # None
            self.message = None  # None
    
