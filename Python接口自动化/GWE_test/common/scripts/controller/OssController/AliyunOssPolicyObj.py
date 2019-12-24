
from common.objects import BaseObj
from order_service.api import *
                

class AliyunOssPolicyObj(Baserder):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(AliyunOssPolicyObj, self).__init__()
        self.info = "oss上传签名生成"
        self.uri = "/aliyun/oss/policy"
        self.method = "get"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()
            
    class Body(BaseObj):
        def __init__(self, **kwargs):
            BaseObj.__init__(self, **kwargs)
    
    class Resp(object):
        def __init__(self):
            super(AliyunOssPolicyObj.Resp, self).__init__()
            self.code = None  # None
            self.data = self.OssPolicyResult()  # None
            self.message = None  # None
            
        class OssPolicyResult(object):
            """None"""
            def __init__(self):
                self.accessKeyId = None  # 访问身份验证中用到用户标识
                self.callback = None  # 上传成功后的回调设置
                self.dir = None  # 上传文件夹路径前缀
                self.host = None  # oss对外服务的访问域名
                self.policy = None  # 用户表单上传的策略,经过base64编码过的字符串
                self.signature = None  # 对policy签名后的字符串
    
