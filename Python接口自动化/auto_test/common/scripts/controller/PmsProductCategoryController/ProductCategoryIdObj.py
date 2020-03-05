
from common.objects import BaseObj
from Gwe_service.api import *
                

class ProductCategoryIdObj(BaseGwe):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(ProductCategoryIdObj, self).__init__()
        self.info = "根据id获取商品分类"
        self.uri = "/productCategory/{id}"
        self.method = "get"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()
            
    class Body(BaseObj):
        def __init__(self, **kwargs):
            self.id = None
            BaseObj.__init__(self, **kwargs)
    
    class Resp(object):
        def __init__(self):
            super(ProductCategoryIdObj.Resp, self).__init__()
            self.code = None  # None
            self.data = self.PmsProductCategory()  # None
            self.message = None  # None
            
        class PmsProductCategory(object):
            """None"""
            def __init__(self):
                self.description = None  # 描述
                self.icon = None  # 图标
                self.id = None  # None
                self.keywords = None  # None
                self.level = None  # 分类级别：0->1级；1->2级
                self.name = None  # None
                self.navStatus = None  # 是否显示在导航栏：0->不显示；1->显示
                self.parentId = None  # 上机分类的编号：0表示一级分类
                self.productCount = None  # None
                self.productUnit = None  # None
                self.showStatus = None  # 显示状态：0->不显示；1->显示
                self.sort = None  # None
    
