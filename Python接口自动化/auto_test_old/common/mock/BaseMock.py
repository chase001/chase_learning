# 需要被mock的对象需要继承的基类

from common.RedisUtil import *
from common.RequestUtil import *


class BaseMock(object):
    def __init__(self, ex=1800, **kwargs):
        """
        :param key_name: 服务名称可能是放在header的那个key里面的
        例如 demo_mock 'test_mock:demo_mock:cdc19a26-721b-11e9-beac-acde48001122
        :param ex:
        :param value_standard:
        :param cons_mock_obj:
        :param kwargs:
        """
        self.http_code = 200
        self.service_name = None
        # self.key_name = key_name
        self.ex = ex
        # self.mock_body_key = None
        # self.cons_mock_obj = cons_mock_obj
        # self.value_standard = value_standard
        self.mock_key = kwargs.get('mock_key', None)
        if self.mock_key:  # 这里直接获取处理长期存放的key值
            self.get_cons_value()  # 通过key获取到期望mock的resp内容
            # self.resp = getattr(mock_data, self.mock_key, None)
            # self.mock_key = 'test_mock:{}'.format(self.mock_key)

    def archive_exp_mock_body(self, obj=None):
        """
        该方法在各个需要mock接口的对象中会被重写
        :param order_obj:
        :return:
        """
        pass

    def set_redis(self, key, ex=86400):
        """将期望的mock接口返回结果存入redis中"""
        self.mock_key = key if key else self.mock_key  # trace_id
        http_code = self.http_code
        service_name = self.service_name
        uri = self.uri
        body = obj_convert_json(self.body)  # 这个转换方式不好
        resp = obj_convert_json(self.resp)
        value = dict(http_code=http_code,
                     service_name=service_name,
                     uri=uri,
                     body=body,
                     response=resp)
        set_value(name=self.mock_key, value=value, ex=ex)
        return self

    # def set_exp_body_to_redis(self):
    #     """将期望的mock接口请求参数存入redis中并生成对应的key"""
    #     self.mock_body_key = set_value(name=self.key_name,
    #                                    value=self.body,
    #                                    ex=self.ex,
    #                                    value_standard=False)
    #     return self

    def get_cons_value(self):
        """通过key检查redis中是否有值，如果没有则set进去"""
        try:
            get_value('test_mock:{}'.format(self.mock_key))
        except:
            log.info("获取mock名：{} 失败，重新set".format(self.mock_key))
            # value = getattr(mock_data, self.mock_key, None)
            # set_value(name=self.mock_key, value=value, constant_key=True, value_standard=False)