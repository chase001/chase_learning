
from common.objects import BaseObj
from Gwe_service.api import *
                

class ProductAttributeCategoryIdObj(BaseGwe):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(ProductAttributeCategoryIdObj, self).__init__()
        self.info = "获取单个商品属性分类信息"
        self.uri = "/productAttribute/category/{id}"
        self.method = "get"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()
            
    class Body(BaseObj):
        def __init__(self, **kwargs):
            self.id = None
            BaseObj.__init__(self, **kwargs)
    
    class Resp(object):
        def __init__(self):
            super(ProductAttributeCategoryIdObj.Resp, self).__init__()
            self.code = None  # None
            self.data = self.PmsProductAttributeCategory()  # None
            self.message = None  # None
            
        class PmsProductAttributeCategory(object):
            """None"""
            def __init__(self):
                self.attributeCount = None  # 属性数量
                self.id = None  # None
                self.name = None  # None
                self.paramCount = None  # 参数数量
    
