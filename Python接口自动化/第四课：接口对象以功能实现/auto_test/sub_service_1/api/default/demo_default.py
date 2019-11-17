from ..base.demo_base import MyServiceBaseDemoApi


class MyServiceDemoApi(MyServiceBaseDemoApi):
    def __init__(self, **kwargs):
        super(MyServiceDemoApi, self).__init__(**kwargs)
        self.status = 0  # 期望返回结果
        self.update_default_body()

    def update_default_body(self):
        self.body.args_1 = 111
        self.body.args_2 = 2222

    def check(self):
        """
        1. 检查状态self.status
        2. 检查resp
        3. 检查数据落库
        2. 检查其他内容：redis, mq ,
        :return:
        """
        assert self.status == self.resp.status  # 根据业务可做抽取
        from sub_service_1.check.SubServiceCompare import SubServiceCompare
        compare = SubServiceCompare(order_id=111111)
        compare.add_table(table_name_key='table_name_1')
        compare.do(ex=['id'])