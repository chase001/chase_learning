
from common.objects import BaseObj
from order_service.api import *
                

class OrderIdObj(BaseOrder):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(OrderIdObj, self).__init__()
        self.info = "获取订单详情:订单信息、商品信息、操作记录"
        self.uri = "/order/{id}"
        self.method = "get"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()
            
    class Body(BaseObj):
        def __init__(self, **kwargs):
            self.id = None
            BaseObj.__init__(self, **kwargs)
    
    class Resp(object):
        def __init__(self):
            super(OrderIdObj.Resp, self).__init__()
            self.code = None  # None
            self.data = self.OmsOrderDetail()  # None
            self.message = None  # None
            
        class OmsOrderDetail(object):
            """None"""
            def __init__(self):
                self.autoConfirmDay = None  # 自动确认时间（天）
                self.billContent = None  # 发票内容
                self.billHeader = None  # 发票抬头
                self.billReceiverEmail = None  # 收票人邮箱
                self.billReceiverPhone = None  # 收票人电话
                self.billType = None  # 发票类型：0->不开发票；1->电子发票；2->纸质发票
                self.commentTime = None  # 评价时间
                self.confirmStatus = None  # 确认收货状态：0->未确认；1->已确认
                self.couponAmount = None  # 优惠券抵扣金额
                self.couponId = None  # None
                self.createTime = None  # 提交时间
                self.deleteStatus = None  # 删除状态：0->未删除；1->已删除
                self.deliveryCompany = None  # 物流公司(配送方式)
                self.deliverySn = None  # 物流单号
                self.deliveryTime = None  # 发货时间
                self.discountAmount = None  # 管理员后台调整订单使用的折扣金额
                self.freightAmount = None  # 运费金额
                self.growth = None  # 可以活动的成长值
                self.historyList = [self.OmsOrderOperateHistory()]  # None
                self.id = None  # 订单id
                self.integration = None  # 可以获得的积分
                self.integrationAmount = None  # 积分抵扣金额
                self.memberId = None  # None
                self.memberUsername = None  # 用户帐号
                self.modifyTime = None  # 修改时间
                self.note = None  # 订单备注
                self.orderItemList = [self.OmsOrderItem()]  # None
                self.orderSn = None  # 订单编号
                self.orderType = None  # 订单类型：0->正常订单；1->秒杀订单
                self.payAmount = None  # 应付金额（实际支付金额）
                self.payType = None  # 支付方式：0->未支付；1->支付宝；2->微信
                self.paymentTime = None  # 支付时间
                self.promotionAmount = None  # 促销优化金额（促销价、满减、阶梯价）
                self.promotionInfo = None  # 活动信息
                self.receiveTime = None  # 确认收货时间
                self.receiverCity = None  # 城市
                self.receiverDetailAddress = None  # 详细地址
                self.receiverName = None  # 收货人姓名
                self.receiverPhone = None  # 收货人电话
                self.receiverPostCode = None  # 收货人邮编
                self.receiverProvince = None  # 省份/直辖市
                self.receiverRegion = None  # 区
                self.sourceType = None  # 订单来源：0->PC订单；1->app订单
                self.status = None  # 订单状态：0->待付款；1->待发货；2->已发货；3->已完成；4->已关闭；5->无效订单
                self.totalAmount = None  # 订单总金额
                self.useIntegration = None  # 下单时使用的积分
                
            class OmsOrderOperateHistory(object):
                """None"""
                def __init__(self):
                
            class OmsOrderItem(object):
                """None"""
                def __init__(self):
    
