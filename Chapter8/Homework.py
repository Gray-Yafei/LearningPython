def welcome():
    print("*" * 30)
    print("欢迎使用【名片管理系统1.0】")
    print("1.新建名片")
    print("2.显示全部")
    print("3.查询名片")
    print("0.退出系统")
    print("*" * 30)


def newCard():
    dic = {}
    dic['name'] = input("请输入你的姓名：")
    dic['tel'] = input("请输入你的电话：")
    dic['QQ'] = input("请输入你的QQ：")
    dic['mail'] = input("请输入你的邮箱：")
    return dic


def show():
    print(cardList)


def select(opions):
    if opions == 1:
        cardList.append(newCard())
    if opions == 4:
        flag = False
        name = input("请输入你要查询的姓名：")
        for i in range(0, len(cardList)):
            if cardList[i]['name'] == name:
                flag = True
                print(cardList[i])
                break
        if not flag:
            print("未查到相关信息")
    if opions == 2:
        flag = False
        name = input("请输入你要删除的姓名：")
        for i in range(0, len(cardList)):
            if cardList[i]['name'] == name:
                flag = True
                cardList.pop(i)
                break
        if not flag:
            print("未查到相关信息")
    if opions == 3:
        flag = False
        name = input("请输入你要修改人的姓名：")
        for i in range(0, len(cardList)):
            if cardList[i]['name'] == name:
                flag = True
                message = input("请输入你要修改哪项信息：")
                if message == 'name':
                    cardList[i]['name'] = input("请输入你重新修改的姓名：")
                elif message == 'tel':
                    cardList[i]['tel'] = input("请输入你重新修改的电话：")
                elif message == 'QQ':
                    cardList[i]['QQ'] = input("请输入你重新修改的QQ：")
                elif message == 'mail':
                    cardList[i]['mail'] = input("请输入你重新修改的邮箱：")
                else:
                    print("输入有误，请重新输入")
                break
        if not flag:
            print("未查到相关信息")


cardList = []
while True:
    welcome()
    option = int(input("请输入你的选择："))
    if option == 0:
        print("欢迎下次使用，再见")
        break
    elif option == 1:
        cardList.append(newCard())
        print("成功新建账户", cardList[-1]['name'])
    elif option == 2:
        show()
    elif option == 3:
        select(int(input("请输入你的操作(1.Add/2.Delete/3.Update/4.Select):")))
