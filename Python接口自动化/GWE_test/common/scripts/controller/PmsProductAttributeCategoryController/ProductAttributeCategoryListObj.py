
from common.objects import BaseObj
from order_service.api import *
                

class ProductAttributeCategoryListObj(Baserder):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(ProductAttributeCategoryListObj, self).__init__()
        self.info = "分页获取所有商品属性分类"
        self.uri = "/productAttribute/category/list"
        self.method = "get"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()
            
    class Body(BaseObj):
        def __init__(self, **kwargs):
            self.pageSize = None
            self.pageNum = None
            BaseObj.__init__(self, **kwargs)
    
    class Resp(object):
        def __init__(self):
            super(ProductAttributeCategoryListObj.Resp, self).__init__()
            self.code = None  # None
            self.data = self.CommonPage«PmsProductAttributeCategory»()  # None
            self.message = None  # None
            
        class CommonPage«PmsProductAttributeCategory»(object):
            """None"""
            def __init__(self):
                self.list = [self.PmsProductAttributeCategory()]  # None
                self.pageNum = None  # None
                self.pageSize = None  # None
                self.total = None  # None
                self.totalPage = None  # None
                
            class PmsProductAttributeCategory(object):
                """None"""
                def __init__(self):
    
