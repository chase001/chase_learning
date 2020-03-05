
from common.objects import BaseObj
from Gwe_service.api import *
                

class SubjectListAllObj(BaseGwe):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(SubjectListAllObj, self).__init__()
        self.info = "获取全部商品专题"
        self.uri = "/subject/listAll"
        self.method = "get"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()
            
    class Body(BaseObj):
        def __init__(self, **kwargs):
            BaseObj.__init__(self, **kwargs)
    
    class Resp(object):
        def __init__(self):
            super(SubjectListAllObj.Resp, self).__init__()
            self.code = None  # None
            self.data = [self.CmsSubject()]  # None
            self.message = None  # None
            
        class CmsSubject(object):
            """None"""
            def __init__(self):
                self.albumPics = None  # 画册图片用逗号分割
                self.categoryId = None  # None
                self.categoryName = None  # 专题分类名称
                self.collectCount = None  # None
                self.commentCount = None  # None
                self.content = None  # None
                self.createTime = None  # None
                self.description = None  # None
                self.forwardCount = None  # 转发数
                self.id = None  # None
                self.pic = None  # 专题主图
                self.productCount = None  # 关联产品数量
                self.readCount = None  # None
                self.recommendStatus = None  # None
                self.showStatus = None  # 显示状态：0->不显示；1->显示
                self.title = None  # None
    
