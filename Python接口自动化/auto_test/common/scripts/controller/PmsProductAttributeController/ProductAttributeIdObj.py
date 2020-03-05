
from common.objects import BaseObj
from Gwe_service.api import *
                

class ProductAttributeIdObj(BaseGwe):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(ProductAttributeIdObj, self).__init__()
        self.info = "查询单个商品属性"
        self.uri = "/productAttribute/{id}"
        self.method = "get"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()
            
    class Body(BaseObj):
        def __init__(self, **kwargs):
            self.id = None
            BaseObj.__init__(self, **kwargs)
    
    class Resp(object):
        def __init__(self):
            super(ProductAttributeIdObj.Resp, self).__init__()
            self.code = None  # None
            self.data = self.PmsProductAttribute()  # None
            self.message = None  # None
            
        class PmsProductAttribute(object):
            """None"""
            def __init__(self):
                self.filterType = None  # 分类筛选样式：1->普通；1->颜色
                self.handAddStatus = None  # 是否支持手动新增；0->不支持；1->支持
                self.id = None  # None
                self.inputList = None  # 可选值列表，以逗号隔开
                self.inputType = None  # 属性录入方式：0->手工录入；1->从列表中选取
                self.name = None  # None
                self.productAttributeCategoryId = None  # None
                self.relatedStatus = None  # 相同属性产品是否关联；0->不关联；1->关联
                self.searchType = None  # 检索类型；0->不需要进行检索；1->关键字检索；2->范围检索
                self.selectType = None  # 属性选择类型：0->唯一；1->单选；2->多选
                self.sort = None  # 排序字段：最高的可以单独上传图片
                self.type = None  # 属性的类型；0->规格；1->参数
    
