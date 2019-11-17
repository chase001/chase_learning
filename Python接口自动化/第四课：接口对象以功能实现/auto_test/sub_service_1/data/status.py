# 该文件存放接口状态数据


class ConsStatusCode(object):
    """response 状态码"""
    OK = 0
    ServiceWrong = -50000  # 服务错误
    TypeWrong = -40400  # 类型错误
    TypeWrong9449474 = -9449474  # 类型错误
    RepeatActivity = -9502003  # '同一商品不可重复创建活动'
    Unknow = -1  # 无错误码的报错

    CouponNotExist = -2138035159  # 卡券不存在
    CouponExpire = -2138035134  # 卡券已过期
    CouponNotDispatch = -2138035136  # 卡券尚未发放
    CouponHadUsed = -2138035164  # 卡券已使用
    CouponWrongPlateForm = -2138035141  # 卡券不能用于当前平台
    CouponBindUser = -2138035162  # 卡券绑定其他用户
    CouponCantUse = -2138035163  # 卡券不能用于当前订单
    DiscountInfoError = -2138034160  # 折扣信息不合法