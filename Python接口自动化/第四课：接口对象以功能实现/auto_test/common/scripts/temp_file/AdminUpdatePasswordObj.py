

class AdminUpdatePassword(BaseOrder):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(AdminUpdatePassword, self).__init__()
        self.info = "修改指定用户密码"
        self.uri = "/admin/updatePassword"
        self.method = "post"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()

    class Body(BaseObj):
        def __init__(self, **kwargs):
            self.newPassword = None  # 新密码
            self.oldPassword = None  # 旧密码
            self.username = None  # 用户名
            BaseObj.__init__(**kwargs)

    class Resp(object):
        def __init__(self):
            super(AdminUpdatePassword.Resp, self).__init__()
            self.code = None  # None
            self.data = None  # None
            self.message = None  # None

