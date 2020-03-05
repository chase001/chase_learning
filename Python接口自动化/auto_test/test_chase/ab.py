#ab.py
import sys
sys.path.append('E:\chase_Learning\chase_learning\Python接口自动化\auto_test')
sys.path.append('E:\chase_Learning\chase_learning\Python接口自动化\auto_test\test_chase')

# c.py
from test_chase.a import  data

# 由于是直接import a 所以都是从源模块a里面拿出来的，所以这里的改变都会影响源模块a
# 可以理解为有着作用域 a.的限制
a.data[0] = 5
print(a.data)  # 输出[5,2,3]
a.run()  # 输出[5,2,3]

a.data = 100  # 因为这里影响的是a里面的data
print(a.data)  # 输出100
