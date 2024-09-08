class Player(object):
    numbers = 0  # 类属性
    def __init__(self, name, age, city):  # 初始化函数
        self.name = name  # 实例属性
        self.age = age
        self.city = city
        Player.numbers += 1

tom = Player('tom',24,'上海')  # 类的实例化
print(type(tom))
print(isinstance(tom, Player))

print(tom.name, tom.age, tom.city)
tom.city = '北京'
print(tom.city)
tom.height = 180
tom.age = 18
print(tom.__dict__)  # 获取对象的所有属性，以字典形式保存
print(f'欢迎第{Player.numbers}个玩家注册')
mia = Player('mia',29,'安徽')
print(mia.__dict__)
print(f'欢迎第{Player.numbers}个玩家注册')

class Weapon(object):
    numbers = 0
    max_damage = 10000
    levels = ['青铜','白银','黄金','钻石','王者']
    def __init__(self, name, damage, level):
        self.name = name  # 实例属性
        Weapon.numbers += 1
        if damage > Weapon.max_damage:
            raise Exception("最大伤害为10000，请重试！")
        else:
            self.damage = damage
        if level not in Weapon.levels:
            raise Exception("段位设置错误！")
        else:
            self.level = level
try:
    gun = Weapon('magic',10000,'王者')
    print(gun.__dict__)
    print(Weapon.numbers)
    arrow = Weapon('arrow',450,'青铜')
    print(arrow.__dict__)
    print(Weapon.numbers)
except Exception as e:
    print(e)