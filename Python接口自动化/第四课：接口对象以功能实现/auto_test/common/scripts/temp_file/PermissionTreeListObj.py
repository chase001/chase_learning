

class PermissionTreeList(BaseOrder):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(PermissionTreeList, self).__init__()
        self.info = "以层级结构返回所有权限"
        self.uri = "/permission/treeList"
        self.method = "get"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()

    class Body(BaseObj):
        def __init__(self, **kwargs):
            BaseObj.__init__(**kwargs)

    class Resp(object):
        def __init__(self):
            super(PermissionTreeList.Resp, self).__init__()

