
from common.objects import BaseObj
from order_service.api import *
                

class ProductAttributeCategoryDeleteIdObj(Baserder):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(ProductAttributeCategoryDeleteIdObj, self).__init__()
        self.info = "删除单个商品属性分类"
        self.uri = "/productAttribute/category/delete/{id}"
        self.method = "get"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()
            
    class Body(BaseObj):
        def __init__(self, **kwargs):
            self.id = None
            BaseObj.__init__(self, **kwargs)
    
    class Resp(object):
        def __init__(self):
            super(ProductAttributeCategoryDeleteIdObj.Resp, self).__init__()
            self.code = None  # None
            self.data = None  # None
            self.message = None  # None
    
