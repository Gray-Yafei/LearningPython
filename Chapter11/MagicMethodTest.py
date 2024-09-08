class User(object):
    def __init__(self, name):  # 构造函数
        print("__init__被调用")
        self.name = name

    def __str__(self):  # toString
        return f"我的名字是{self.name}"

    def __add__(self, other):  # 运算符重载
        return User(self.name + other.name)

    def __eq__(self, other):
        return self.name == other.name

mia = User("mia")

print(mia)
print(str(mia))
jack = User("jack")
print(mia + jack)