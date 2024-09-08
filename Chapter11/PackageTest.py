class User():
    def __init__(self, name, age):
        self._name = name  # _受保护的变量
        self.__age = age  # __私有的变量
    def _show_info(self):  # 方法也可以用__和_
        print(f"大家好，我是{self._name},我今年{self.__age}")

    '''把函数当作变量去使用
    @property
    def 变量名(self):  # 获取变量
    @get_age.setter
    def 变量名(self, 变量名):  # 修改变量
    '''

    @property  # 装饰器：获取变量的值，加@property之前调用：mia.get_age()，加入之后调用mia.get_age
    def get_age(self):
        return self.__age

    @get_age.setter  # 变量的修改器 修改名.setter
    def set_age(self, age):
        if isinstance(age, int):
            self.__age = age
        else:
            raise Exception("年龄只能是整数")

mia = User('mia', 25)
print(mia._name)
mia._show_info()
# print(mia.__age)
# mia._name = 'tom'
# print(mia._name)
# mia.age = 30
# print(mia.age)

# print(mia.get_age())
# mia.set_age(20)
# print(mia.get_age())

print(mia.get_age)


