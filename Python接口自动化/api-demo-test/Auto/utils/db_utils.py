# -*- coding: utf-8 -*-#

# -------------------------------------------------------------------------------
# Name:         db_utils
# Description:  
# Author            Dongtian
# Date:         2020-01-05
# -------------------------------------------------------------------------------
from Auto.utils.MyConf import cf
import DBUtils
import pymysql

POOL = DBUtils.PersistentDB(
    creator=pymysql,  # 使用链接数据库的模块
    maxusage=None,  # 一个链接最多被重复使用的次数，None表示无限制
    setsession=[],  # 开始会话前执行的命令列表。如：["set datestyle to ...", "set time zone ..."]
    ping=0,
    # ping MySQL服务端，检查是否服务可用。# 如：0 = None = never, 1 = default = whenever it is requested, 2 = when a cursor is created, 4 = when a query is executed, 7 = always
    closeable=False,
    # 如果为False时， conn.close() 实际上被忽略，供下次使用，再线程关闭时，才会自动关闭链接。如果为True时， conn.close()则关闭链接，那么再次调用pool.connection时就会报错，因为已经真的关闭了连接（pool.steady_connection()可以获取一个新的链接）
    threadlocal=None,  # 本线程独享值得对象，用于保存链接对象，如果链接对象被重置
    host=str(cf.get("db", "host")),
    port=3306,
    user='root',
    password='123',
    database='pooldb',
    charset='utf8',

)
