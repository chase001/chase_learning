

class DevReleaseFinanceConcurrentkey(BaseFinance):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(DevReleaseFinanceConcurrentkey, self).__init__()
        self.info = "删除并发控制的批次"
        self.uri = "/dev/release/finance/concurrentkey"
        self.method = "post"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()

    class Body(BaseObj):
        def __init__(self, **kwargs):
            self.batchCode = None  # None
            BaseObj.__init__(**kwargs)

    class Resp(object):
        def __init__(self):
            super(DevReleaseFinanceConcurrentkey.Resp, self).__init__()
            self.slot = None  # None
            self.dbSuffix = None  # None
            self.tbSuffix = None  # None

