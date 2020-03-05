
from common.objects import BaseObj
from Gwe_service.api import *
                

class ProductAttributeCategoryCreateObj(BaseGwe):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(ProductAttributeCategoryCreateObj, self).__init__()
        self.info = "添加商品属性分类"
        self.uri = "/productAttribute/category/create"
        self.method = "post"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()
            
    class Body(BaseObj):
        def __init__(self, **kwargs):
            self.name = None
            BaseObj.__init__(self, **kwargs)
    
    class Resp(object):
        def __init__(self):
            super(ProductAttributeCategoryCreateObj.Resp, self).__init__()
            self.code = None  # None
            self.data = None  # None
            self.message = None  # None
    
