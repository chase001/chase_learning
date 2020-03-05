
from common.objects import BaseObj
from Gwe_service.api import *
                

class ProductCategoryUpdateNavStatusObj(BaseGwe):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(ProductCategoryUpdateNavStatusObj, self).__init__()
        self.info = "修改导航栏显示状态"
        self.uri = "/productCategory/update/navStatus"
        self.method = "post"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()
            
    class Body(BaseObj):
        def __init__(self, **kwargs):
            self.ids = None
            self.navStatus = None
            BaseObj.__init__(self, **kwargs)
    
    class Resp(object):
        def __init__(self):
            super(ProductCategoryUpdateNavStatusObj.Resp, self).__init__()
            self.code = None  # None
            self.data = None  # None
            self.message = None  # None
    
