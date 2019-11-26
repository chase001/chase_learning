from common.db.func import generate_where_single, merge_where, generate_update_dict_single
from peewee import *
from common.db.PeeweeUtil import PeeweeUtil
from functools import reduce
import operator

"""
function 说明
:param table 需要查询的表，通过装饰器指定表的集合或者表Model
:param where 通过kwarg转换 & 传入的where = where
:param kwargs index(分表时指定表的序列) /其他and查询参数
"""

"""
调用方式
如果只取query
query = CustomerSql(ShopProduct).conditions(product_id=11111).order_by(a=True, b=False).query
取查询结果
result = CustomerSql(ShopProduct).conditions(product_id=11111).order_by(a=True, b=False).limit(100).exc()
"""


class MyDB(object):
    _METHODS = ("select", "delete", "update")

    def __init__(self, table, index=None, db=None, operation=None):
        """

        :param table: 需要查询的表，通过装饰器指定表的集合或者表Model
        :param index: 如果分表 分表的序号 default不分表
        :param db: 如果分库 分库的序号 default不分库
        :param operation: sql的操作方式，现在具体支持的，见变量 _METHODS
        """
        self.table = table[int(index)] if index is not None else table
        self.operation = operation if operation else "select"
        # self.query = self.table.select()
        self.query = getattr(self.table, self.operation)()
        self.db = db if db else None  # 使用的库名
        self.where = None
        self.total = None  # 需要init_total 初始化
        self.is_pre = None  # 是否还有上一页
        self.is_next = None  # 是否还有下一页

    def __setattr__(self, key, value):
        """
            对操作方法的限制认证
        """
        if key == "operation" and value:
            if value not in self._METHODS:
                raise IndexError()

        object.__setattr__(self, key, value)

    def update_field(self, update_dict=None, **kwargs):
        update_dict = generate_update_dict_single(kwargs, obj=self.table, origin_dict=update_dict)
        self.query = self.table.update(update_dict)
        return self

    def conditions(self, where=None, **kwargs):
        """
        查询条件
        :param where
        :param product_id=1111
        支持以上两种方式
        """
        self.init_where(where=where, **kwargs)
        self.query = self.query.where(self.where)
        return self

    def create_query(self):
        self.query = self.query.where(self.where)
        return self

    def init_where(self, where=None, **kwargs):

        where_list = []
        where_list.extend(generate_where_single(kwargs, self.table))
        if where_list:
            convert_where = reduce(operator.and_, where_list)
        else:
            convert_where = None
        self.where = merge_where([where, convert_where])
        return self

    def order_by(self, order_by=None, **kwargs):
        """
        排序条件
        调用时候可以用order_by(product_id=True, business_product_id=False）
        todo  以上调用方式未实现，自行实现
        """
        if order_by is not None:
            self.query = self.query.order_by(order_by)
        return self

    def limit(self, limit=None):
        """限制条件"""
        if limit:
            self.query = self.query.limit(limit)
        return self

    def offset(self, offset=0, limit=20):
        """
        limit 5 offset 0 从 1 到5 条
        limit 5 offset 5 从 6 到10 条
        """

        self.query = self.query.limit(limit).offset(offset)
        self.init_total()
        # 开始计算是否有上下页面
        self.is_pre = False if offset == 0 else True
        self.is_next = False if (offset + limit) >= self.total else True
        return self

    def offset_v2(self, is_next=True, is_pre=False, total_num=20, start=0):
        from common.db.func import cal_offset_limit
        limit, offset = cal_offset_limit(is_next=is_next,
                                         is_pre=is_pre,
                                         total_num=total_num,
                                         start=start)
        return self.offset(offset=offset,
                           limit=limit)


    def join_left(self, table, on_list=[]):
        """
        如果有自行实现把, 看怎么方便怎么传
        :param table:
        :param on:
        :return:
        """
        on = reduce(operator.and_, on_list)
        self.query = self.query.join(table, join_type=JOIN.LEFT_OUTER, on=on).switch(self.table)
        return self

    def join_inner(self, table, on_list=[]):
        on = reduce(operator.and_, on_list)
        self.query = self.query.join(table, join_type=JOIN.INNER, on=on).switch(self.table)
        return self

    def pagination(self, page, paginate_by=20):
        """
        普通分页查询， 默认会初始化total值
        :param page: 第几页
        :param paginate_by: 页面大小
        :return:
        """
        self.query = self.query.paginate(page=page, paginate_by=paginate_by)
        self.init_total()
        return self

    def init_total(self):
        self.total = len(self.query)

    def exc(self, **kwargs):
        """
        执行sql 同原来的expect_catch()装饰器
        :param is_convert 如果列表只有一个值是否要直接取出来
        :param is_convert_camel 是否要转换成驼峰
        :param is_normal_obj 是否要转换成普通的对象
        :param back 如果为空返回结构返回的结构
        :return:
        """
        is_convert = kwargs.get('is_convert', False)
        is_convert_camel = kwargs.get('is_convert_resp', False)
        is_normal_obj = True if is_convert_camel else kwargs.get('is_normal_obj', True)  # 如果要转换成驼峰，肯定要先转成普通对象
        back = kwargs.get('back', [])
        sql_type = self.operation if kwargs.get('type', None) is None else kwargs.get('type')
        if sql_type == 'select':
            sql_type = 'query'
        if self.query is not None:
            with PeeweeUtil(query=self.query, dbase=self.db) as p_util:
                r = p_util.db_result(is_convert=is_convert,
                                     back=back,
                                     sql_type=sql_type,
                                     is_normal_obj=is_normal_obj,
                                     is_convert_camel=is_convert_camel,
                                     )
        else:
            r = back
        return r
