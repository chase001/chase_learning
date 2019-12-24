
from common.objects import BaseObj
from order_service.api import *
                

class BrandListAllObj(BaseOrder):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(BrandListAllObj, self).__init__()
        self.info = "获取全部品牌列表"
        self.uri = "/brand/listAll"
        self.method = "get"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()
            
    class Body(BaseObj):
        def __init__(self, **kwargs):
            BaseObj.__init__(self, **kwargs)
    
    class Resp(object):
        def __init__(self):
            super(BrandListAllObj.Resp, self).__init__()
            self.code = None  # None
            self.data = [self.PmsBrand()]  # None
            self.message = None  # None
            
        class PmsBrand(object):
            """None"""
            def __init__(self):
                self.bigPic = None  # 专区大图
                self.brandStory = None  # 品牌故事
                self.factoryStatus = None  # 是否为品牌制造商：0->不是；1->是
                self.firstLetter = None  # 首字母
                self.id = None  # None
                self.logo = None  # 品牌logo
                self.name = None  # None
                self.productCommentCount = None  # 产品评论数量
                self.productCount = None  # 产品数量
                self.showStatus = None  # None
                self.sort = None  # None
    
