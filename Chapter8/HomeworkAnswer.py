cards = [{'name': 'wei', 'tel': '12', 'QQ': '3123', 'mail': '534'},
{'name': 'yang', 'tel': '5', 'QQ': '982', 'mail': '567132'},
         {'name': 'ya', 'tel': '123', 'QQ': '3123123', 'mail': '534567'},
         ]
def menu():
    print("*" * 30)
    print('''欢迎使用【名片管理系统1.0】
    1.新建名片
    2.显示全部
    3.查询名片
    0.退出系统''')
    print("*" * 30)

def newCard(name, tel, QQ, mail):
    user = {
        'name': name,
        'tel': tel,
        'QQ': QQ,
        'mail': mail,
    }
    cards.append(user)
    return True
def show():
    for card in cards:
        print(card)

def queryCard(kw):
    for card in cards:
        for k, v in card.items():
            if v == kw:
                return card
    return False

def exit():
    print("欢迎下次使用【名片管理系统】")

def modifyCard(kw):
    for card in cards:
        for k, v in card.items():
            if k == kw:
                card[k] = input(f"请输入修改的{k}")
                return True

def deleteCard():
    for card in cards:
        for k, v in card.items():
            if v == kw:
                cards.remove(card)
                return True


menu()
while True:
    op = input("请输入你要操作的序号：")
    if op == '1':
        name = input("请输入你的姓名：")
        tel = input("请输入你的电话：")
        QQ = input("请输入你的QQ：")
        mail = input("请输入你的邮箱：")
        result = newCard(name, tel, QQ, mail)
        if result:
            print("成功新建名片")
        else:
            print("请重试")
    elif op == '2':
        show()
    elif op == '3':
        kw = input("请输入查询的关键字：")
        result = queryCard(kw)
        if result:
            print(result)
            op2 = input("输入4修改名片，输入5删除名片：")
            if op2 == '4':
                kw = input("请输入修改的关键字：")
                result = modifyCard(kw)
                if result:
                    print("修改成功")
            elif op2 == '5':
                result = deleteCard()
                if result:
                    print("删除成功")
            else:
                print("输入有误，请重新输入")


        else:
            print("没有查到相关信息")
    elif op == '0':
        quit()
        break
    else:
        print('Invalid input')