### 安装问题解决
1. 安装peewee-mssql>=0.1.2 报错
    需要先安装# brew install freetds


=======接口数据继承结构=========
RequestUtil  (所有接口的基础类，主要做sendrequest和mock功能)
    ^
    |
ServiceObj   (接口服务对象: 定义host 等)
    ^
    |
ApiBaseObj   (接口基础类: 直接从swagger上拉取，可做更新)
    ^
    |
TestedApiObj  (实际被用来测试的接口: 有默认值和assert功能)


=======assert部分继承结构=======

pip基本操作
pip freeze > requirements.txt  生成
pip install -r requirements.txt  使用
pip install redis  单个安装
pip list 查看

数据库model文件生成脚本
pg库
python -m pwiz -e postgresql -H 10.10.10.1 -p 5432 -u username -P 'pwd' app > db.py
python -m pwiz -e mysql -H 144.34.200.237  -p 3306 -u root -P 'root' mall -t sms_coupon,sms_coupon_product_category_relation,sms_coupon_product_relation > db.py

本地pg库
python -m pwiz -e postgresql -H localhost  -p 5432 -u root -P 'yinyuting' mall -t sms_coupon,sms_coupon_product_category_relation,sms_coupon_product_relation > db.py

mysql库
echo '{pw}' | python3 -m pwiz -e mysql -H {host}  -p {port} -u {user} -P '{pw}' {db}> {save_file}

#####解决编码问题
修改报告中文unicode,pytest_html包中的plugin.py，TestResult类，修改为
self.test_id = report.nodeid.encode("utf-8").decode("unicode_escape")

修改控制台输出中文用例名
pytest包中的nodes.py， 修改Node类中的name
self.name = name.encode("utf-8").decode("unicode_escape")


/Users/yinyuting/Documents/auto_test/common/scripts/gen_code_swagger.py
/Users/yinyuting/Documents/auto_test/test_case/test_coupon_service/test_coupon_create_api.py
/Users/yinyuting/Documents/auto_test/test_case/conftest.py
/Users/yinyuting/Documents/auto_test/order_service/api/service/coupon_create_api.py
/Users/yinyuting/Documents/auto_test/readme.txt
/Users/yinyuting/Documents/auto_test/common/TestHome.py

11月28号更新内容：
删除/Users/yinyuting/Documents/auto_test/order_service/db/model.py
新增/Users/yinyuting/Documents/auto_test/order_service/db/order_model.py
删除/Users/yinyuting/Documents/auto_test/order_service/check下除了__init__.py以外的所有文件
新增/Users/yinyuting/Documents/auto_test/order_service/check/OrderPWUtil.py
更新/Users/yinyuting/Documents/auto_test/order_service/api/service/coupon_create_api.py
更新/Users/yinyuting/Documents/auto_test/conf/mysql.ini
更新/Users/yinyuting/Documents/auto_test/common/db/my_db.py
更新/Users/yinyuting/Documents/auto_test/common/db/PeeweeUtil.py
