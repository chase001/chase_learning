
from common.objects import BaseObj
from Gwe_service.api import *
                

class ProductAttributeCategoryUpdateIdObj(BaseGwe):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(ProductAttributeCategoryUpdateIdObj, self).__init__()
        self.info = "修改商品属性分类"
        self.uri = "/productAttribute/category/update/{id}"
        self.method = "post"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()
            
    class Body(BaseObj):
        def __init__(self, **kwargs):
            self.id = None
            self.name = None
            BaseObj.__init__(self, **kwargs)
    
    class Resp(object):
        def __init__(self):
            super(ProductAttributeCategoryUpdateIdObj.Resp, self).__init__()
            self.code = None  # None
            self.data = None  # None
            self.message = None  # None
    
