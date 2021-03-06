
from common.objects import BaseObj
from Gwe_service.api import *
                

class BrandCreateObj(BaseGwe):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(BrandCreateObj, self).__init__()
        self.info = "添加品牌"
        self.uri = "/brand/create"
        self.method = "post"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()
            
    class Body(BaseObj):
        def __init__(self, **kwargs):
            self.bigPic = None  # 品牌大图
            self.brandStory = None  # 品牌故事
            self.factoryStatus = None  # 是否为厂家制造商
            self.firstLetter = None  # 品牌首字母
            self.logo = None  # 品牌logo
            self.name = None  # 品牌名称
            self.showStatus = None  # 是否进行显示
            self.sort = None  # 排序字段
            BaseObj.__init__(self, **kwargs)
    
    class Resp(object):
        def __init__(self):
            super(BrandCreateObj.Resp, self).__init__()
            self.code = None  # None
            self.data = None  # None
            self.message = None  # None
    
