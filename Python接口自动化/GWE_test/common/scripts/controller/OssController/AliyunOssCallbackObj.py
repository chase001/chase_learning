
from common.objects import BaseObj
from order_service.api import *
                

class AliyunOssCallbackObj(Baserder):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(AliyunOssCallbackObj, self).__init__()
        self.info = "oss上传成功回调"
        self.uri = "/aliyun/oss/callback"
        self.method = "post"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()
            
    class Body(BaseObj):
        def __init__(self, **kwargs):
            BaseObj.__init__(self, **kwargs)
    
    class Resp(object):
        def __init__(self):
            super(AliyunOssCallbackObj.Resp, self).__init__()
            self.code = None  # None
            self.data = self.OssCallbackResult()  # None
            self.message = None  # None
            
        class OssCallbackResult(object):
            """None"""
            def __init__(self):
                self.filename = None  # 文件名称
                self.height = None  # 图片文件的高
                self.mimeType = None  # 文件的mimeType
                self.size = None  # 文件大小
                self.width = None  # 图片文件的宽
    
