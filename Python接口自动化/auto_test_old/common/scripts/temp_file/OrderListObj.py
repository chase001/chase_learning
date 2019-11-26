

class OrderList(BaseOrder):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(OrderList, self).__init__()
        self.info = "查询订单"
        self.uri = "/order/list"
        self.method = "get"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()

    class Body(BaseObj):
        def __init__(self, **kwargs):
            self.orderSn = None
            self.receiverKeyword = None
            self.status = None
            self.orderType = None
            self.sourceType = None
            self.createTime = None
            self.pageSize = None
            self.pageNum = None
            BaseObj.__init__(**kwargs)

    class Resp(object):
        def __init__(self):
            super(OrderList.Resp, self).__init__()

