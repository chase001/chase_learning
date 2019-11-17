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


pip freeze requirements.txt
