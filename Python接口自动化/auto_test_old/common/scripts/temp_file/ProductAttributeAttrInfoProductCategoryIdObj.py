

class ProductAttributeAttrInfoProductCategoryId(BaseOrder):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(ProductAttributeAttrInfoProductCategoryId, self).__init__()
        self.info = "根据商品分类的id获取商品属性及属性分类"
        self.uri = "/productAttribute/attrInfo/{productCategoryId}"
        self.method = "get"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()

    class Body(BaseObj):
        def __init__(self, **kwargs):
            self.productCategoryId = None
            BaseObj.__init__(**kwargs)

    class Resp(object):
        def __init__(self):
            super(ProductAttributeAttrInfoProductCategoryId.Resp, self).__init__()

