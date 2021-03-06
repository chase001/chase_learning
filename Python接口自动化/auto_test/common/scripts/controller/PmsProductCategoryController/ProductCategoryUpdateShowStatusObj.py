
from common.objects import BaseObj
from Gwe_service.api import *
                

class ProductCategoryUpdateShowStatusObj(BaseGwe):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(ProductCategoryUpdateShowStatusObj, self).__init__()
        self.info = "修改显示状态"
        self.uri = "/productCategory/update/showStatus"
        self.method = "post"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()
            
    class Body(BaseObj):
        def __init__(self, **kwargs):
            self.ids = None
            self.showStatus = None
            BaseObj.__init__(self, **kwargs)
    
    class Resp(object):
        def __init__(self):
            super(ProductCategoryUpdateShowStatusObj.Resp, self).__init__()
            self.code = None  # None
            self.data = None  # None
            self.message = None  # None
    
