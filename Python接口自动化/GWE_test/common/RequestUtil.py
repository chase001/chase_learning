import base64
import hmac
import requests
import urllib.request, urllib.parse, urllib.error
from .func import *
from .log.Logger import log
from .objects import BaseObj
from retrying import retry

headers = {'Content-Type': 'application/json',
           'Accept': 'application/json',
           "User-Agent": "tester-pc"
           }
retry_num = 3


class RequestUtil(object):
    """
    接口基础类
    """
    def __init__(self):
        self.host = None  # 域名
        self.uri = None  # uri
        self.url = None  # url host+uri+param
        self.info = None  # 描述
        self.method = None  # 请求方式 post get
        self.body = None  # 请求参数体
        self.param = None  # get请求参数
        self.resp = None  # 返回结果
        self.is_sign = None
        self.key_token = None
        self.headers = headers
        self.return_original = False  # 是否要返回dict格式的resp  功能未加进来
        # self.status_map = dict()  # status的转换 todo 这个放到check里面做应该不用了
        self.status = 0  # 期望的status值  # todo 这个走装饰器才生效
        self.success_status = 0  # 接口成功的status值
        self.http_status = 200  # http返回码
        self.timeout = 15  # 最大超时时间
        self.mock_info = BaseObj()  # mock信息

    def send_request(self,):
        log.api(type='desc', msg=self.info)  # 记录接口的中文描述
        # region 请求参数对象转换成json格式(后续发送请求使用)
        json_body = obj_to_json(self.body) if self.body else None
        json_param = obj_to_json(self.param) if self.param else None
        # endregion
        self.url = self.compose_url(json_param=json_param)  # 更新url
        # # region 处理签名
        # try:
        #     if self.is_sign:
        #         sign = _genBodySign(json_body)
        #         json_body["sign"] = sign
        #         self.body.sign = sign
        # except Exception as e:
        #     log.api(type='Request Data', msg=self.body + '\n' + self.param)
        #     log.error(msg=e)
        #     raise NameError("处理接口签名出错!!!!")
        # # endregion
        resp_act = self.base_send_request(data=json_body)  # 发送请求三次重试
        self.resp = json_to_obj(resp_act)
        # self.generate_resp_obj(resp_act=resp_act)  # 这个比较傻的写法

        # region 转换json格式的返回值response为对象

        return self

    def update_headers(self, add_headers={}):
        self.headers.update(add_headers)

    def compose_url(self, json_param=None):
        """拼接完成的url=host+uri+params"""
        url = self.host.rstrip('/') + '/' + self.uri.lstrip('/')
        if json_param and isinstance(json_param, dict):
            para_value = urllib.parse.urlencode(json_param) if json_param else ''
        else:
            para_value = None
        para_str = ('?' + para_value) if para_value else ''
        url += para_str
        return url

    # def encode_url_params(self, params, needencode=True):
    #     """
    #     encode request parameters dict to query string, like: param1=value1&param2=value2
    #     eg: {"param1": "value1", "param2": None, "param3": ""} => param1=value1&param3=
    #     :param params: dict, request query parameters.
    #     :return string, like "param1=&param3=value3"
    #     """
    #     if params:
    #         # if not needencode:
    #         #     params_str_list = []
    #         #     for (key, value) in list(params.items()):
    #         #         if value is None:
    #         #             params.pop(key)
    #         #             continue
    #         #         params_str_list.append(key + "=" + str(value))
    #         #     return '&'.join(params_str_list)
    #         return urllib.parse.urlencode(params)
    #     else:
    #         return ''

    # def generate_resp_obj(self, resp_act):
    #     try:
    #         self.resp = self._generate_resp_obj(self.resp, resp_act)  # 生成resp对象
    #     except Exception as e:
    #         log.error(msg=e)
    #         raise NameError("转换json格式的返回值response为对象出错!!!")
    #
    # def _generate_resp_obj(self, obj, resp_act):
    #     """
    #     接口返回的格式如为list，目标对象需要给最外层的list命名为root，dict无所谓
    #     :param obj: 目标对象
    #     :param resp_act: 接口返回值，外层结构为list或dict
    #     :return:
    #     """
    #     if obj is None:
    #         raise NameError("亲，未定义接口返回对象")
    #
    #     if isinstance(resp_act, list):
    #         # 如果接口返回是个list，则获取接口对象中定义的外层列表属性名，获取不到则报错
    #         count = len(resp_act)
    #         root_name = None
    #         for name in dir(obj):
    #             if isinstance(getattr(obj, name), list) and name != "error_list":
    #                 root_name = name
    #         if root_name is None:
    #             log.error("接口返回结构设置错误！！！！返回值直接为列表，请设置一个空属性包含具体返回对象！！！！")
    #             assert False
    #         if len(resp_act) > 0:
    #             # 如果接口返回的list长度大于0，则遍历返回，按接口生成返回对象
    #             if isinstance(resp_act[0], (int, float)) is False:
    #                 for i in range(0, count):
    #                     if i > 0:
    #                         getattr(obj, root_name).append(copy.deepcopy(getattr(obj, root_name)[0]))
    #                     self._generate_resp_obj(getattr(obj, root_name)[i], resp_act[i])
    #             else:
    #                 setattr(obj, root_name, resp_act)
    #         else:
    #             setattr(obj, root_name, resp_act)
    #             log.info("return empty list")
    #     elif isinstance(resp_act, dict):
    #         for k, v in list(dict(resp_act).items()):
    #             if isinstance(v, dict):
    #                 self._generate_resp_obj(getattr(obj, k), v)
    #                 continue
    #             # 条件：1.是个list，2.resp_object中k对应的每一项均为dict，3.返回list不为空
    #             if isinstance(v, list) and len(getattr(obj, k)) and len(v) > 0:
    #                 # 如果是个列表，则先取出第一项作为基准，再删除，然后每次遍历的时候deepcopy一个，再赋值
    #                 count = len(v)
    #                 base_obj = getattr(obj, k)[0]
    #                 if isinstance(base_obj, type) is True:
    #                     base_obj = copy.deepcopy(base_obj)()
    #                 getattr(obj, k).pop()
    #                 for i in range(0, count):
    #                     getattr(obj, k).append(copy.deepcopy(base_obj))
    #                     self._generate_resp_obj(getattr(obj, k)[i], v[i])
    #                 continue
    #             if hasattr(obj, k) is True:
    #                 pass
    #             else:
    #                 log.warning("接口结构{}定义中不包含属性{}，不影响结果，但建议补一下！！！！！！".format(obj, k))
    #             setattr(obj, k, v)
    #     elif isinstance(resp_act, (int, str, bool)):
    #         setattr(obj, "data", resp_act)
    #     return obj if resp_act is not None else None

    # def send_request_then_check(self, status_exp=0, return_all=False, do_check_whatever=False):
    #     class_name = self.__class__.__name__
    #     # 判断是否有pre check
    #     if getattr(self, "pre_check", None) is not None:
    #         log.info("Execute pre_check before send_request")
    #         pre_func = getattr(self, "pre_check")
    #         pre_func()
    #     log.info("Send_request, {}".format(class_name))
    #     req_func = getattr(self, "send_request")
    #     req_func(status_exp=status_exp, return_all=return_all)
    #     log.info("Finish send_request, {}".format(class_name))
    #     if status_exp == self.success_status or do_check_whatever is True:
    #         log.info("Check, {}".format(class_name))
    #         check_func = getattr(self, "check")
    #         check_func()
    #         log.info("Finish check, {}".format(class_name))
    #     return self

    @retry(stop_max_attempt_number=retry_num)
    def base_send_request(self, data=None):
        """
        发送请求并判断r.status_code == 200
        :param data: json_body
        :return:
        """
        request_id = random.randint(100000, 999999)
        log.info("Send Json request and check the http status to '%s', then return dict" % self.http_status)
        log.api(type='url', msg=self.uri)
        log.info(msg="Header: {}".format(self.headers))
        log.api(type='Request Data', msg=data, deal_key=request_id)
        # if self.headers.get("Content-Type") == "application/json":
        #     data = json.dumps(data)
        # elif self.headers.get("Content-Type") == "multipart/form-data":
        #     data = MultipartEncoder(fields=self.data)
        # else:
        #     data = encodeUrlParams(self, self.data)

        r = None
        common_condition = dict(url=self.url, headers=self.headers, timeout=self.timeout)
        if self.method == "get":
            r = requests.get(**common_condition)
        elif self.method == "post":
            r = requests.post(**common_condition, data=data, allow_redirects=False)
        elif self.method == "put":
            r = requests.put(**common_condition, data=data)
        elif self.method == "delete":
            r = requests.delete(**common_condition, data=data)

        act_http_status = r.status_code
        if self.http_status != act_http_status:
            assert False, "当前请求返回状态码{}".format(act_http_status)
        elif self.http_status == 200:
            log.api(type="Response", msg=r.text, deal_key=request_id)
            return r.json()
        else:
            return None

    def mock(self, mock_api):
        """

        :param mock_api: 需要mock的接口对象
        :param mock_name: 指定的mock名称，不传则默认为接口对象名字
        :return:
        """
        from common.mock.MockUtil import MockUtil
        mock_name = getattr(mock_api, 'mock_name', 'mock_name')
        setattr(self.mock_info, mock_name, mock_api)
        mock_tools = MockUtil(self)
        mock_tools.mock_confirm()

