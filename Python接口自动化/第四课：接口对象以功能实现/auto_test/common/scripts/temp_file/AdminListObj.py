

class AdminList(BaseOrder):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(AdminList, self).__init__()
        self.info = "根据用户名或姓名分页获取用户列表"
        self.uri = "/admin/list"
        self.method = "get"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()

    class Body(BaseObj):
        def __init__(self, **kwargs):
            self.name = None
            self.pageSize = None
            self.pageNum = None
            BaseObj.__init__(**kwargs)

    class Resp(object):
        def __init__(self):
            super(AdminList.Resp, self).__init__()
            self.code = None  # None
            self.data = self.CommonPage«UmsAdmin»()  # None
            self.message = None  # None

        class CommonPage«UmsAdmin»(object):
            """None"""
            def __init__(self):
                self.list = [self.UmsAdmin()]  # None
                self.pageNum = None  # None
                self.pageSize = None  # None
                self.total = None  # None
                self.totalPage = None  # None

            class UmsAdmin(object):
                """None"""
                def __init__(self):
                    self.createTime = None  # 创建时间
                    self.email = None  # 邮箱
                    self.icon = None  # 头像
                    self.id = None  # None
                    self.loginTime = None  # 最后登录时间
                    self.nickName = None  # 昵称
                    self.note = None  # 备注信息
                    self.password = None  # None
                    self.status = None  # 帐号启用状态：0->禁用；1->启用
                    self.username = None  # None

