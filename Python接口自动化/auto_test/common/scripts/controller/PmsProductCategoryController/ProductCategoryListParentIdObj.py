
from common.objects import BaseObj
from Gwe_service.api import *
                

class ProductCategoryListParentIdObj(BaseGwe):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(ProductCategoryListParentIdObj, self).__init__()
        self.info = "分页查询商品分类"
        self.uri = "/productCategory/list/{parentId}"
        self.method = "get"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()
            
    class Body(BaseObj):
        def __init__(self, **kwargs):
            self.parentId = None
            self.pageSize = None
            self.pageNum = None
            BaseObj.__init__(self, **kwargs)
    
    class Resp(object):
        def __init__(self):
            super(ProductCategoryListParentIdObj.Resp, self).__init__()
            self.code = None  # None
            self.data = self.CommonPage«PmsProductCategory»()  # None
            self.message = None  # None
            
        class CommonPage«PmsProductCategory»(object):
            """None"""
            def __init__(self):
                self.list = [self.PmsProductCategory()]  # None
                self.pageNum = None  # None
                self.pageSize = None  # None
                self.total = None  # None
                self.totalPage = None  # None
                
            class PmsProductCategory(object):
                """None"""
                def __init__(self):
    
