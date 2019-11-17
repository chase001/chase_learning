

class MemberLevelList(BaseOrder):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(MemberLevelList, self).__init__()
        self.info = "查询所有会员等级"
        self.uri = "/memberLevel/list"
        self.method = "get"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()

    class Body(BaseObj):
        def __init__(self, **kwargs):
            self.defaultStatus = None
            BaseObj.__init__(**kwargs)

    class Resp(object):
        def __init__(self):
            super(MemberLevelList.Resp, self).__init__()

