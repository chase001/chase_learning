from common.RequestUtil import RequestUtil
from conf.conf import get_host


class BaseServiceDemo(RequestUtil):
    def __init__(self):
        """域服务对象"""
        super(BaseServiceDemo, self).__init__()
        self.host = get_host('demo_host')
