
from common.objects import BaseObj
from Gwe_service.api import *
                

class ProductAttributeUpdateIdObj(BaseGwe):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(ProductAttributeUpdateIdObj, self).__init__()
        self.info = "修改商品属性信息"
        self.uri = "/productAttribute/update/{id}"
        self.method = "post"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()
            
    class Body(BaseObj):
        def __init__(self, **kwargs):
            self.id = None
            self.filterType = None  # 分类筛选样式：0->普通；1->颜色
            self.handAddStatus = None  # 是否支持手动新增；0->不支持；1->支持
            self.inputList = None  # 可选值列表，以逗号隔开
            self.inputType = None  # 属性录入方式：0->手工录入；1->从列表中选取
            self.name = None  # 属性名称
            self.productAttributeCategoryId = None  # 属性分类ID
            self.relatedStatus = None  # 相同属性产品是否关联；0->不关联；1->关联
            self.searchType = None  # 检索类型；0->不需要进行检索；1->关键字检索；2->范围检索
            self.selectType = None  # 属性选择类型：0->唯一；1->单选；2->多选
            self.sort = None  # None
            self.type = None  # 属性的类型；0->规格；1->参数
            BaseObj.__init__(self, **kwargs)
    
    class Resp(object):
        def __init__(self):
            super(ProductAttributeUpdateIdObj.Resp, self).__init__()
            self.code = None  # None
            self.data = None  # None
            self.message = None  # None
    
