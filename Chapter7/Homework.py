while True:
    try:
        op = input("请输入一个算式（输入c退出）：")

        if op == "c":
            print("感谢您的使用，再见")
            break

        if "+" in op or "-" in op or "*" in op or "/" in op:
            print(eval(op))
        else:
            raise Exception("输入有误,请重新输入")
    except Exception as e:
        print(e)