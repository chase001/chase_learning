
from common.objects import BaseObj
from Gwe_service.api import *
                

class SkuPidObj(BaseGwe):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(SkuPidObj, self).__init__()
        self.info = "根据商品编号及编号模糊搜索sku库存"
        self.uri = "/sku/{pid}"
        self.method = "get"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()
            
    class Body(BaseObj):
        def __init__(self, **kwargs):
            self.pid = None
            self.keyword = None
            BaseObj.__init__(self, **kwargs)
    
    class Resp(object):
        def __init__(self):
            super(SkuPidObj.Resp, self).__init__()
            self.code = None  # None
            self.data = [self.PmsSkuStock()]  # None
            self.message = None  # None
            
        class PmsSkuStock(object):
            """None"""
            def __init__(self):
                self.id = None  # None
                self.lockStock = None  # 锁定库存
                self.lowStock = None  # 预警库存
                self.pic = None  # 展示图片
                self.price = None  # None
                self.productId = None  # None
                self.promotionPrice = None  # 单品促销价格
                self.sale = None  # 销量
                self.skuCode = None  # sku编码
                self.sp1 = None  # 销售属性1
                self.sp2 = None  # None
                self.sp3 = None  # None
                self.stock = None  # 库存
    
