from functools import partial

def add(x:int,y:int):
    return x + y

add2 = partial(add,y=2)

print(add2(3))