

class AdminRegister(BaseOrder):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(AdminRegister, self).__init__()
        self.info = "用户注册"
        self.uri = "/admin/register"
        self.method = "post"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()

    class Body(BaseObj):
        def __init__(self, **kwargs):
            self.email = None  # 邮箱
            self.icon = None  # 用户头像
            self.nickName = None  # 用户昵称
            self.note = None  # 备注
            self.password = None  # 密码
            self.username = None  # 用户名
            BaseObj.__init__(**kwargs)

    class Resp(object):
        def __init__(self):
            super(AdminRegister.Resp, self).__init__()
            self.code = None  # None
            self.data = self.UmsAdmin()  # None
            self.message = None  # None

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

