import hashlib
#
# md5 = hashlib.md5()
# md5.update("how to use md5 in python hashlib?".encode("utf-8"))
# print(md5.hexdigest())
#
# sha1 = hashlib.sha1()
# sha1.update("how to use md5 in python hashlib?".encode("utf-8"))
# print(sha1.hexdigest())
#
# def calc_md5(password):
#     pass
# 设计一个验证用户登录的函数，根据用户输入的口令是否正确，返回True或False：
# -*- coding: utf-8 -*-
db = {
    'michael': 'e10adc3949ba59abbe56e057f20f883e',
    'bob': '878ef96e86145580c38c87f0410ad153',
    'alice': '99b1c2188db85afee403b1536010c2c9'
}


def login(user,password):
    md5 = hashlib.md5()
    md5.update(password.encode("utf-8"))
    if md5.hexdigest() == db[user]:
        return True
    else:
        return False


# 测试:
assert login('michael', '123456')
assert login('bob', 'abc999')
assert login('alice', 'alice2008')
assert not login('michael', '1234567')
assert not login('bob', '123456')
assert not login('alice', 'Alice2008')
print('ok')

# 根据用户输入的登录名和口令模拟用户注册，计算更安全的MD5：
db = {}

def register(username, password):
    db[username] = get_md5(password + username + 'the-Salt')

# 然后，根据修改后的MD5算法实现用户登录的验证：
# -*- coding: utf-8 -*-
import hashlib, random

def get_md5(s):
    return hashlib.md5(s.encode('utf-8')).hexdigest()

class User(object):
    def __init__(self, username, password):
        self.username = username
        self.salt = ''.join([chr(random.randint(48, 122)) for i in range(20)])
        self.password = get_md5(password + self.salt)
db = {
    'michael': User('michael', '123456'),
    'bob': User('bob', 'abc999'),
    'alice': User('alice', 'alice2008')
}

def login(username, password):
    user = db[username]
    return user.password == get_md5(password)


# 测试:
assert login('michael', '123456')
assert login('bob', 'abc999')
assert login('alice', 'alice2008')
assert not login('michael', '1234567')
assert not login('bob', '123456')
assert not login('alice', 'Alice2008')
print('ok')

