"""
调用此脚本生成数据库对象和期望结果对象 脚本文件
"""

import os
from conf.conf import db_conf

from common.scripts.lib.CodeMode import db_code_model as code_model

# 执行pw生成pw_model的命令
db_config_name = "db_hot"  # from conf/mysql.ini中的section name
db_config = db_conf()
cmd_model = "echo '{pw}' | python3 -m pwiz -e mysql -H {host}  -p {port} -u {user} -P '{pw}' {db}> {save_file}"

pwd = os.getcwd()
pw_model_file = pwd + "/temp_db_file/db.py"
convert_db_file = pwd + "/temp_db_file/xj_recon_model.py"
expect_obj_file = pwd + "/temp_db_file/ExpectXjReconTable.py"
pw_util_file = pwd + "/temp_db_file/PeeweeUtil.py"
cmd_str = cmd_model.format(save_file=pw_model_file,
                           pw=db_config.get(db_config_name, 'pw'),
                           host=db_config.get(db_config_name, 'host'),
                           port=db_config.get(db_config_name, 'port'),
                           user=db_config.get(db_config_name, 'user'),
                           db=db_config.get(db_config_name, 'db'),
                           )
print("准备执行命令:" + cmd_str)

try:
    print("执行命令...")
    resp = os.popen(cmd_str).readlines()
    print("执行结果如下:")
    print(resp)
except Exception as e:
    print("执行失败！！！！！！原因如下:...")
    print(e)

import re
# 开始操作文件生成pw_model

expect_dict = dict()
with open(file=convert_db_file, mode='w+', encoding='utf-8') as w_f:

        with open(file=pw_model_file, encoding='utf-8') as r_f:
            tables = list()  # 存储所有表名
            w_f.write("""from common.db.MyFields import * \n from common.db.func import init_database \n""")
            line_num = 0  # 记录行数
            for line in r_f:
                if "table_name" in line:
                    table_name = line.split("=")[-1][2:-2]
                    tables.append(table_name)
                write_data = ''
                search_database = re.search(r'database = MySQLDatabase(.*)', line)
                search_column_id = re.search(r'column_name=\'(.*)_id\'', line)
                if search_database:
                    write_data = code_model.db_code(db_name=db_config_name)
                elif search_column_id:
                    column_name, column_define = line.split('=', maxsplit=1)
                    column_name = column_name.replace(' ', '') + "_id"
                    write_data = column_name + " =" + column_define
                else:
                    write_data = line

                write_data = write_data.replace("DateTimeField", "MyDateTimeField")
                if "# bit" in write_data:
                    write_data = write_data.replace("UnknownField", "MyBitField")
                if "# json" in write_data:
                    write_data = write_data.replace("UnknownField", "MyJsonField")

                if line != write_data:
                    print("原始line: {}".format(line))
                    print("替换成: {}".format(write_data))
                w_f.write(write_data)
print(tables)

# 开始生成期望结果
start = False
with open(file=convert_db_file, mode='r', encoding='utf-8') as r_f:
    with open(file=expect_obj_file, mode='w+', encoding='utf-8') as w_f:
        for line in r_f:
            start_class_name = re.search(r'class (.*)(BaseModel)', line)
            end_class_name = re.search(r'class Meta:', line)
            if start_class_name:
                start = True
                class_name = start_class_name.group(1)[:-1]
                w_f.write("\n\nclass " + class_name + "(object):\n")
                w_f.write("    def __init__(self):\n")
            if end_class_name:
                start = False
            if start and "=" in line:
                w_f.write("        self." + line.split("=")[0].replace(' ', '') + " = None\n")
