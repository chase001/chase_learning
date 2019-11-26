# 通用mock工具类
import uuid


class MockUtil(object):
    """
    mock工具类
    """
    def __init__(self, origin_api):
        self.origin_api = origin_api

    def mock_confirm(self, *args, **kwargs):
        """
        :param args: 可以传入指定的self.mock_info的属性名字， 例如mock_rule_calculate等
        不传则默认确认所有的mock数据
        :param kwargs: 可以传入其他需要使用到的参数
        :return:
        """
        # mock_headers = dict(hj_mock_tag='y',
        #                     hj_mock_src_url='',
        #                     hj_mock_target_url='')
        mock_key = str(uuid.uuid1().int >> 64)
        mock_headers = {'Mock-Key': mock_key}
        if args:
            # todo ... 谁需要用到谁添加下吧
            pass
        else:
            for mock_api_name, mock_api_obj in vars(self.origin_api.mock_info).items():
                """
                1. 拼接header
                2. request body 存入redis
                3. 生成期望结果
                4. response 存入redis
                """
                mock_api_obj.archive_exp_mock_body(self.origin_api)  # 这里传self,不传入body 确保信息的完整
                # mock_api_obj.set_exp_body_to_redis()  # 将request_body存入redis中
                mock_api_obj.set_redis(mock_key)  # 将response信息存入redis中
                # 此时生成了request和response两个key
                # mock_keys = self.convert_mock_key(mock_api_obj.mock_key)
                # mock_body_keys = self.convert_mock_key(mock_api_obj.mock_body_key)
                # hj_mock_src_url = mock_api_obj.compose_url()  #  原始的url
                # from conf.conf import get_host
                # hj_mock_target_url = get_host('mock') + str(mock_api_obj.uri)
                # hj_mock_target_url += '?mock_key=' + "__".join(mock_keys) + '&mock_body_key=' + "__".join(mock_body_keys)
                # mock_headers['hj_mock_src_url'] += hj_mock_src_url + ';'

                print('==========mock_key==============')
                print(mock_headers)
                self.origin_api.update_headers(add_headers=mock_headers)

    def convert_mock_key(self, mock_key):
        if isinstance(mock_key, list):
            mock_keys = mock_key
        else:
            mock_keys = [mock_key]
        return mock_keys

    class MockInfo():
        def __init__(self):
            pass

