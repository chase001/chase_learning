from common.RequestUtil import RequestUtil
from conf.conf import get_host


class Base2ServiceDemo(RequestUtil):
    def __init__(self):
        """域服务对象"""
        super(Base2ServiceDemo, self).__init__()
        self.host = "http://www.origin-api-url.com/"
