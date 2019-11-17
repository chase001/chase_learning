# -*- coding:utf8 -*-

class ApiClassCodeMode(object):

    def generate_import(self):
        """接口类导入的模块"""
        code = """
from common.objects import BaseObj
from ..__init__ import *
                """
        return code

    def generate_base_class(self, base_class, host):
        """基础类代码模版,暂时不用了"""
        code = """
class Base{base_class}(SendRequest):
    def __init__(self, info=None, uri=None, method=\"POST\", body=None, param=None, resp=None):
        super(Base{base_class}, self).__init__()
        self.info = info
        self.uri = uri
        self.method = method
        self.body = body
        self.param = param
        self.resp = resp
        self.host = \"http://{host}\"
        


        """.format(base_class=base_class,host=host)
        return code

    def generate_api_class(self, class_name, base_name, api_desc, uri, method):
        code = """

class {api_class_name}({base_name}):
    \"\"\"api controller obj\"\"\"
    def __init__(self, **kwargs):
        super({api_class_name}, self).__init__()
        self.info = \"{api_desc}\"
        self.uri = \"{uri}\"
        self.method = \"{method}\"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()
        """.format(api_class_name=class_name,
                   base_name=base_name,
                   api_desc=api_desc,
                   uri=uri,
                   method=method
                   )
        return code

class TestCaseCodeMode(object):
    def code_model_header(self, uri,api_class_name):
        code = """
# 开始打印接口{uri}的用例====================================
from hujiang.testcase1.apiPlaceOrderV2.__init__ import *
from hujiang.business.apiCommonTools.Logger import log
# 通用log，parameterized是通用模块，已经在common.__init__导入，用例层不需要导入
from nose_parameterized import parameterized



class TestApiTestCaseName(object):

    @classmethod
    def setupclass(cls):
        pass

    @classmethod
    def teardownclass(cls):
        pass

    def setup(self):
        self.api_obj = {api_class_name}()


    def teardown(self):
        pass
    """.format(uri=uri,
               api_class_name=api_class_name)
        return code

class DBCodeModel(object):
    def __init__(self):
        pass

    def import_code(self):
        import_str = """
from hujiang.business.apiPeewee.customerFields import MyBitField, MyDateTimeField
from hujiang.conf.ecm_config import get_database

        """
        return import_str

    def db_code(self, db_name):
        db_str = """
database = get_database('{db_name}')
        """.format(db_name=db_name)
        return db_str


api_obj_code_model = ApiClassCodeMode()
test_case_code_model = TestCaseCodeMode()
db_code_model = DBCodeModel()

