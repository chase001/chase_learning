
from common.objects import BaseObj
from Gwe_service.api import *
                

class ProductAttributeAttrInfoProductCategoryIdObj(BaseGwe):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(ProductAttributeAttrInfoProductCategoryIdObj, self).__init__()
        self.info = "根据商品分类的id获取商品属性及属性分类"
        self.uri = "/productAttribute/attrInfo/{productCategoryId}"
        self.method = "get"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()
            
    class Body(BaseObj):
        def __init__(self, **kwargs):
            self.productCategoryId = None
            BaseObj.__init__(self, **kwargs)
    
    class Resp(object):
        def __init__(self):
            super(ProductAttributeAttrInfoProductCategoryIdObj.Resp, self).__init__()
            self.code = None  # None
            self.data = [self.ProductAttrInfo()]  # None
            self.message = None  # None
            
        class ProductAttrInfo(object):
            """None"""
            def __init__(self):
                self.attributeCategoryId = None  # None
                self.attributeId = None  # None
    
