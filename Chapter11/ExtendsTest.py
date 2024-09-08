class Player(object):  # 父类
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

class VIP(Player):  # 子类
    def __init__(self, name, age, city, level,coin):
        #  调用父类的构造函数
        super().__init__(name,age,city,level)
        self.coin = coin

    def show(self):  # 实例方法
        print(f'我是第{Player.numbers}个玩家，我的名字是{self.name},来自{self.city},段位是{self.level},余额为{self.coin}')


mia = VIP('mia', 24, '大连', '青铜', 100)
mia.show()