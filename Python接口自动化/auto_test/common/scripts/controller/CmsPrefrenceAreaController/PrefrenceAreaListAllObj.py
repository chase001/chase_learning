
from common.objects import BaseObj
from order_service.api import *
                

class PrefrenceAreaListAllObj(BaseOrder):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(PrefrenceAreaListAllObj, self).__init__()
        self.info = "获取所有商品优选"
        self.uri = "/prefrenceArea/listAll"
        self.method = "get"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()
            
    class Body(BaseObj):
        def __init__(self, **kwargs):
            BaseObj.__init__(self, **kwargs)
    
    class Resp(object):
        def __init__(self):
            super(PrefrenceAreaListAllObj.Resp, self).__init__()
            self.code = None  # None
            self.data = [self.CmsPrefrenceArea()]  # None
            self.message = None  # None
            
        class CmsPrefrenceArea(object):
            """None"""
            def __init__(self):
                self.id = None  # None
                self.name = None  # None
                self.pic = None  # 展示图片
                self.showStatus = None  # None
                self.sort = None  # None
                self.subTitle = None  # None
    
