class Demo(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def my_print(self,):
        print("a = ", self.a, "b = ", self.b)

    # def __call__(self, *args, **kwargs):
    #     self.a = args[0]
    #     self.b = args[1]
    #     print("call: a = ", self.a, "b = ", self.b)

if __name__ == "__main__":
    demo = Demo(10, 20)
    demo.my_print()

    demo(50, 60)