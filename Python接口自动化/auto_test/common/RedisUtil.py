import redis
import uuid
from .func import *


connecting_kwargs = {
    'host': '127.0.0.1',
    'port': 6379,
    'db': 0
}

r = None


def connect_redis():
    pool = redis.ConnectionPool(**connecting_kwargs)
    try:
        global r
        r = redis.Redis(connection_pool=pool)
    except Exception as e:
        raise e
    return r


def set_value(name='', value=None, ex=86400, value_standard=True, constant_key=False, absolute_name=None):
    # if absolute_name:
    #     new_name = absolute_name
    # else:
    #     if constant_key is False:
    #         uuid_sign = uuid.uuid1()
    #         new_name = 'test_mock:{}:{}'.format(name, uuid_sign)
    #     else:
    #         new_name = 'test_mock:{}'.format(name)
    #         ex = 1314000
    # if isinstance(value, list):
    #     value = obj_convert_json(value)
    #     value = json.dumps(dict(data=value, status=0))
    # if is_custom_object(value) is True:
    #     value = obj_convert_json(value)
    #     if value.get('error_list', None) is not None:
    #         value.pop('error_list')
    #     if value_standard is True:
    #         # 讲塞进redis的值拼接成基础返回结构，加入data前缀
    #         value = json.dumps(dict(data=value, status=0))
    #     else:
    #         value = json.dumps(value)
    if isinstance(value, dict):
        value = json.dumps(value)

    global r
    r.set(name=name, value=value, ex=ex, nx=True)
    return name


def get_value(name):
    try:
        global r
        result = r.get(name)
        if result is None:
            assert False, "mock接口返回为空，可能key错误，也可能key已过期，请重置。"
        else:
            return result
    except Exception as e:
        raise e


def del_value(name):
    try:
        global r
        r.delete(name)
    except:
        assert False, "删除失败，可能因为key{}不存在".format(name)

def md5_str(source_str):
    h = hashlib.md5()
    h.update(str(source_str).encode())
    return h.hexdigest()

connect_redis()


if __name__ == '__main__':
    # set_value(absolute_name="test22222", value="2222", ex=60)
    key = "test_mock:expire_mock:e15a05ea-3653-11e9-8de7-acde48001122"
    msg = get_value(key)
    msg = json.dumps(json.loads(msg), ensure_ascii=False, indent=2)
    # msg = json.dumps(msg, ensure_ascii=False, indent=2)
    print(msg)
