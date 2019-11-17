

class PermissionList(BaseOrder):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(PermissionList, self).__init__()
        self.info = "获取所有权限列表"
        self.uri = "/permission/list"
        self.method = "get"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()

    class Body(BaseObj):
        def __init__(self, **kwargs):
            BaseObj.__init__(**kwargs)

    class Resp(object):
        def __init__(self):
            super(PermissionList.Resp, self).__init__()

