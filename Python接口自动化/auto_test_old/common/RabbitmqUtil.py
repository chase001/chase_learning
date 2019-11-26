# -*- coding:utf8 -*-

import pika, uuid
from .func import *
from .log.Logger import log


class RabbitMQ(object):
    def __init__(self, mq_name=None):
        """
        :param mq_name:服务名称
        """
        self.conf = MQConfig(mq_name)
        self.s_conn = self.__init_connect()

    def __init_connect(self):
        """
        初始化RabbitMQ连接
        :return:
        """
        user_pwd = pika.PlainCredentials(self.conf.username, self.conf.pwd)
        s_conn = pika.BlockingConnection(pika.ConnectionParameters(host=self.conf.host,
                                                                   port=self.conf.port,
                                                                   virtual_host=self.conf.virtual_host,
                                                                   credentials=user_pwd,
                                                                   ))
        log.info('Mq连接成功')
        return s_conn

    def callback(self, ch, method, properties, body):
        """
            回调方法
        :param ch:
        :param method:
        :param properties:
        :param body:
        :return:
        """
        body = body.decode("utf-8")
        print("接收消息 ==> {body}".format(body=body))
        self.msg_list.append(body)

    def send(self, message):
        message = self.deal_message(message)
        chan = self.s_conn.channel()  # 在连接上创建一个频道
        chan.queue_declare(queue=self.conf.queue,
                           durable=self.conf.durable)  # 声明一个队列，生产者和消费者都要声明一个相同的队列，用来防止万一某一方挂了，另一方能正常运行
        chan.basic_publish(exchange=self.conf.exchange,  # 交换机
                           routing_key=self.conf.routing_key,  # 路由键，写明将消息发往哪个队列，本例是将消息发往队列hello
                           body=message,
                           properties=self.conf.properties)  # 生产者要发送的消息
        # log.formmat_info(title="消息发送", content=message)
        log.step("通知退款消息发送")

    def deal_message(self, message):
        common = {"MessageHeader": {"SendDateTime": now(format="%Y-%m-%dT%H:%M:%S+0800"),
                                    "MessageId": str(uuid.uuid1()),
                                    "MessageTypeFullname": "ShoppingPlatform.ChangeOrder.Entities.Message.PayFinishedEventedMessage",
                                    "SendMachineIp": "127.0.0.1"},
                  "MessageBody": message}
        return json.dumps(common)

    def subscribe(self, is_ack=False):
        """
            订阅消息
        :param is_ack:是否将消息消费
        :param is_clear:是否直接清空消息
        :return:消息队列
        """
        msg_list = list()
        channel = self.s_conn.channel()  # 创建频道
        queue = channel.queue_declare(queue=self.conf.queue, durable=True)  # 声明队列
        queue_num = queue.method.message_count  # 获取队列数量
        log.info("获取消息Success，队列长度为【{num}】".format(num=queue_num))
        for i in range(queue_num):
            # no_ack=True 开启自动确认，不然消费后的消息会一直留在队列里面
            # no_ack = no_manual_ack = auto_ack；不手动应答，开启自动应答模式
            r = channel.basic_get(queue=self.conf.queue, no_ack=is_ack)  # 取出数据
            if r:
                body = json.loads(r[2])
                msg_list.append(body)
        return msg_list

    def clear_msg(self, msg_limit=100):
        """
        清空消息（待消费的消息太多，会卡住脚本）
        :param msg_limit 限制待消费msg的数量,>该数量，则清空，<则不做任何操作
        :return:
        """
        log.info("准备清空mq消息。。。")
        channel = self.s_conn.channel()  # 创建频道
        queue = channel.queue_declare(queue=self.conf.queue, durable=True)  # 声明队列
        queue_num = queue.method.message_count  # 获取队列数量
        if queue_num <= msg_limit:
            log.info("跳过队列清空任务：当前队列消息数量为{queue_num},小于清空上限{msg_limit}".format(queue_num=queue_num, msg_limit=msg_limit))
        else:
            queue = channel.queue_purge(queue=self.conf.queue)  # 清空队列消息
            log.info(
                "队列清空结束，状态【{state}】,清空数量【{num}】+\n".format(state=queue.method.NAME, num=queue.method.message_count))

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(exc_val)
        self.s_conn.close()
        print('断开连接')


class MQConfig(object):
    """
    MQ配置信息
    """

    def __init__(self, mq_name=None):
        if mq_name == 'project':
            self.init_project()
        elif mq_name == 'notice_refund':
            """cc阶梯价拼团break后通知公共方退款"""
            self.group_to_refund()
        elif mq_name == "deliver":
            """订阅【配送】消息"""
            self.deliver_mq()

    def init_project(self):
        """
        项目管理MQ配置
        :return:
        """
        self.username = 'ha_user'  # 指定远程rabbitmq的用户名密码
        self.pwd = 'ha_user'
        self.host = '192.168.36.75'
        self.port = 5672
        self.virtual_host = 'ecommon'
        self.queue = 'yinyuting'
        self.exchange = "projectManage.TopicExchange"
        # self.exchange = None
        self.routing_key = 'projectManage.project.OnChangeEvented'
        headers = dict(MachineName='test', FailedCount=0)
        self.properties = pika.BasicProperties(content_encoding='UTF-8',
                                               priority=0,
                                               delivery_mode=2,
                                               headers=headers,
                                               content_type='application/json')
        self.durable = False

    def group_to_refund(self):
        """
        拼团cc发消息通知公共退款
        :return:
        """
        self.username = 'ha_user'  # 指定远程rabbitmq的用户名密码
        self.pwd = 'ha_user'
        self.host = '192.168.36.75'
        self.port = 5672
        self.virtual_host = 'ecommon'
        # self.queue = 'yinyuting'
        self.queue = "common.groupon.external.q"
        self.exchange = "groupon.TopicExchange"
        # self.exchange = None
        self.routing_key = 'ccweb.trade.Groupon.BreakRefundEvented'
        header = dict(FailedCount=0,
                      MachineName='test',
                      CreatedDateTime=now(format="%Y/%m/%d %H:%M:%S"))
        self.properties = pika.BasicProperties(content_encoding='utf-8',
                                               priority=0,
                                               delivery_mode=2,
                                               headers=header,
                                               content_type='application/json',
                                               message_id=str(uuid.uuid1()),
                                               type="YesHJ.Framework.MessagingAvailability.MessageDeclare.Message",
                                               app_id="autotest.soa.yeshj.com"
                                               )

        self.durable = True
        # self.properties = None

    def deliver_mq(self):
        """
         订阅【配送】消息
        :return:
        """
        self.username = 'ha_user'  # 指定远程rabbitmq的用户名密码
        self.pwd = 'ha_user'
        self.host = '192.168.36.75'
        self.port = 5672
        self.virtual_host = 'ecommon'
        self.queue = "common.order.on-deliver-event.for-test"
        self.exchange = "Order.TopicExchange"
        # self.routing_key = 'order.Delivery.OnDeliveryEvent'
        header = dict(FailedCount=0,
                      MachineName='localhost',
                      CreatedDateTime=now(format="%Y/%m/%d %H:%M:%S"))
        self.properties = pika.BasicProperties(content_encoding='utf-8',
                                               priority=0,
                                               delivery_mode=2,
                                               headers=header,
                                               content_type='application/json',
                                               # message_id=str(uuid.uuid1()),
                                               type="YesHJ.Framework.MessagingAvailability.MessageDeclare.Message",
                                               app_id="delivery-order.soa.yeshj.com"
                                               )
        log.info("配送服务mq参数初始化完毕")


#
# message = {"activityId": 2726,
#             # "groupCodeList": ["ss","sss"]
# }
# # message = 'test001'
#
# with RabbitMQ('notice_refund') as mq:
#     mq.send(message)

# with RabbitMQ('project') as mq:
#     mq.send('test')


def callback(ch, method, properties, body):
    body = body.decode("utf-8")
    print("接收消息 ==> {body}".format(body=body))
    return body


# with RabbitMQ('notice_refund') as mq:
#     mq.send(message)
