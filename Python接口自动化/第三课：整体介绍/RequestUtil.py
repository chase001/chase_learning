from wsgiref import headers


class RequestUtil():
    """
    请根据大家各自公司的一个接口写出接口数据相关的4个类以及在基类中实现发送请求的方法，可使用requests或者aiohttp库
    接口基础类
    """
    def __init__(self):
        self.host = None    #域名
        self.uri= None
        self.url= None
        #url host + uri + param
        self.info = None
        self.method = None
        self.body = None
        # 请求参数体 例如
        {"product_id": 123456}
        self.param = None
        #get请求参数例如 product_id = 123456
        self.resp = None
        # 返回结果，例如
        {"product_name":'abc', "price": 5.11}
        self.is_sign = None
        self.key_token = None
        self.headers = headers
        # 请求头例如
        {'Content - Type': 'aaplication/json'}
        self.status = 0
        self.success_status = 0
        self.http_status = 200
        self.timeout = 15
        self.mock_info = BaseObj()  # 如果接口中需要mock的话，存放mock信息


    def Send_request(self):
        """发送请求，使用request库来实现该功能"""
        pass