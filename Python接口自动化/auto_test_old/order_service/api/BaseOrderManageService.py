from common.RequestUtil import RequestUtil
# from conf.conf import get_host


class BaseOrderManageService(RequestUtil):
    def __init__(self):
        """域服务对象"""
        super(BaseOrderManageService, self).__init__()
        # self.host = get_host('demo_host')  # 这个后面讲
        self.host = "http://144.34.200.237:8080"
        from order_service import auth_token
        self.update_headers(dict(Authorization=auth_token))


