class Player(object):
    numbers = 0  # 类属性
    levels = ['青铜', '白银', '黄金', '钻石', '王者']

    def __init__(self, name, age, city, level):  # 初始化函数
        self.weapon = None
        self.name = name  # 实例属性
        self.age = age
        self.city = city
        if level not in Player.levels:
            raise Exception("段位设置错误！")
        else:
            self.level = level
        Player.numbers += 1

    def show(self):  # 实例方法
        print(f'我是第{Player.numbers}个玩家，我的名字是{self.name},来自{self.city},段位是{self.level}')

    def level_up(self):
        index = Player.levels.index(self.level)
        if index < len(Player.levels) - 1:
            self.level = Player.levels[index + 1]

    def get_weapon(self, Weapon):
        self.weapon = Weapon

    def show_weapon(self):
        self.weapon.show_weapon()

    @classmethod
    def get_players(cls):  # 类方法
        print(f'用户已经达到了{cls.numbers}人')

    @staticmethod
    def isValid(**kwargs):  # 静态方法
        if kwargs['age'] > 18:
            return True
        else:
            return False

class Weapon(object):
    numbers = 0
    max_damage = 10000
    levels = ['青铜', '白银', '黄金', '钻石', '王者']
    all_weapons = []
    def __init__(self, name, damage, level):
        self.name = name  # 实例属性
        Weapon.numbers += 1
        Weapon.all_weapons.append(self)
        if damage > Weapon.max_damage:
            raise Exception("最大伤害为10000，请重试！")
        else:
            self.damage = damage
        if level not in Weapon.levels:
            raise Exception("段位设置错误！")
        else:
            self.level = level
    def show_weapon(self):
        for k, v in self.__dict__.items():
            print(f'{k}:{v}')

    @classmethod
    def get_max_damage(cls):
        maxDamage = 0
        for w in cls.all_weapons:
            if w.damage > maxDamage:
                maxDamage = w.damage
        return maxDamage


mia = Player('mia', 24, '大连', '青铜')
mia.show()
Player.get_players()

gun = Weapon('magic_gun', 1000, '青铜')
arrow = Weapon('arrow',500,'白银')
sword = Weapon('sword',1334,'黄金')
print(Weapon.get_max_damage())
mia.get_weapon(gun)
mia.show_weapon()

print(gun.all_weapons)
for i in gun.all_weapons:
    print(i.name)

print("*" * 30)
print("静态方法调试：")
Infos = {'name':'mia','age':24,'city':'北京','level':"白银"}
if Player.isValid(**Infos):
    mia = Player('mia', 24, '北京', '白银')
else:
    print("请检查")