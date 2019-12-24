
from common.objects import BaseObj
from order_service.api import *
                

class ProductCategoryCreateObj(Baserder):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(ProductCategoryCreateObj, self).__init__()
        self.info = "添加产品分类"
        self.uri = "/productCategory/create"
        self.method = "post"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()
            
    class Body(BaseObj):
        def __init__(self, **kwargs):
            self.description = None  # 描述
            self.icon = None  # 图标
            self.keywords = None  # 关键字
            self.name = None  # 商品分类名称
            self.navStatus = None  # 是否在导航栏显示
            self.parentId = None  # 父分类的编号
            self.productAttributeIdList = []  # 产品相关筛选属性集合
            self.productUnit = None  # 分类单位
            self.showStatus = None  # 是否进行显示
            self.sort = None  # 排序
            BaseObj.__init__(self, **kwargs)
    
    class Resp(object):
        def __init__(self):
            super(ProductCategoryCreateObj.Resp, self).__init__()
            self.code = None  # None
            self.data = None  # None
            self.message = None  # None
    
