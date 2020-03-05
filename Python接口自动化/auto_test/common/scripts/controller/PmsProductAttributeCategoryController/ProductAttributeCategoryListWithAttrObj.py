
from common.objects import BaseObj
from Gwe_service.api import *
                

class ProductAttributeCategoryListWithAttrObj(BaseGwe):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(ProductAttributeCategoryListWithAttrObj, self).__init__()
        self.info = "获取所有商品属性分类及其下属性"
        self.uri = "/productAttribute/category/list/withAttr"
        self.method = "get"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()
            
    class Body(BaseObj):
        def __init__(self, **kwargs):
            BaseObj.__init__(self, **kwargs)
    
    class Resp(object):
        def __init__(self):
            super(ProductAttributeCategoryListWithAttrObj.Resp, self).__init__()
            self.code = None  # None
            self.data = [self.PmsProductAttributeCategoryItem()]  # None
            self.message = None  # None
            
        class PmsProductAttributeCategoryItem(object):
            """None"""
            def __init__(self):
                self.attributeCount = None  # 属性数量
                self.id = None  # None
                self.name = None  # None
                self.paramCount = None  # 参数数量
                self.productAttributeList = [self.PmsProductAttribute()]  # None
                
            class PmsProductAttribute(object):
                """None"""
                def __init__(self):
    
