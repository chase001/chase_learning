# -*- coding: UTF-8 -*-
from common.log.Logger import log


class PeeweeUtil(object):
    def __init__(self, query=None, dbase=None, index=None):
        """在这个里面做查询可以修改db配置"""
        self.query = query
        self.dbase = dbase
        self.index = index
        self.origin_table_name = query.model._meta.table_name if query is not None else None  # 原始表名字
        self.origin_database_name = query.model._meta.database if query is not None else None # 原始db名字
        # print("原始配置:" + self.origin_database_name.database + "   " + self.origin_table_name)

    def __enter__(self):
        # 进来修改配置
        if self.dbase:
            print("修改db到:" + self.dbase.database)
            self.query.model._meta.database = self.dbase
            self.query._database = self.dbase
        if self.index:
            print('============开始修改查询前的index拉{}'.format(self.index))
            self.query.model._meta.table_name = self.origin_table_name + "_" + self.index
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        try:
            if self.query:
                self.query.model._meta.database = self.origin_database_name
                self.query.model._meta.table_name = self.origin_table_name
        except:
            pass

    def db_result(self, is_convert=False, back=[], sql_type='query',
                  is_to_list=True, is_normal_obj=False, is_convert_camel=False):
        """
        根据query查询值
        @param is_convert: 如果查询出来是单条数据是否要转换成query[0]
        @param back: 如果查询没有结果返回back
        @param sql_type: 是查询语句还是更新语句
        @param is_to_list: 没想起来也没看懂代码
        @param is_normal_obj: 是否要转换成普通的对象，非pw对象
        @param is_convert_resp: 是否要转换成resp的驼峰形式
        @return:
        """
        # log.step('当前查询DB：{}'.format(self.query.model._meta.database.connect_params))
        db_host = self.query.model._meta.database.connect_params.get('host')
        sql_list = [self.query.sql(), db_host]

        log.mysql(sql_list)

        if sql_type == 'query':
            query_array = [] if is_to_list == True else self.query
            exist = True if self.retry_len(self.query) > 0 else False
            if exist is True:
                # print("query database:{0}".format(result.database.connect_kwargs))
                if is_to_list is True:
                    for q in self.query:
                        if is_normal_obj:  # 假如要转化成普通的类
                            q = self.convert_to_normal_obj(q, is_convert_camel=is_convert_camel)
                        query_array.append(q)
                r = self.deal_query_result(query_array=query_array, is_convert=is_convert)
                return r
            else:
                return back
        elif sql_type == 'update':
            update_result=self.query.execute()  #更新结果是影响行数
            return update_result

    def retry_len(self, query):
        import peewee, time
        for i in range(3):
            try:
                n = len(query)
                return n
            except peewee.OperationalError as e:
                log.error(e)
                time.sleep(2)
                continue

    def deal_query_result(self, query_array, is_convert=False):
        if is_convert:
            return query_array if len(query_array) > 1 else query_array[0]
        else:
            return query_array

    def convert_to_normal_obj(self, obj, is_convert_camel=False):
        """
        将pw对象转换成普通对象
        :param obj:
        :param is_convert_camel: 是否要转换成驼峰
        :return:
        """

        class Temp(CommonBaseObj):
            def __init__(self, **kwargs):
                super(Temp, self).__init__(kwargs)

            def __iter__(self):
                return self

        new_obj = Temp()

        for k, v in obj.__data__.items():
            if k == 'order':
                k = k + '_id'
            if is_convert_camel:
                from hujiang.business.apiCommonTools.common import str_convert_to_camel
                k = str_convert_to_camel(k, "_")
            setattr(new_obj, k, v)
        return new_obj

