try:
    print("有可能出现的异常")
    n = int(input("请输入一个数字:"))
    n = 5 / n
    print(n)
except ValueError as e:
    print("请输入一个数字")
    print(e)
except ZeroDivisionError as e:
    print("被除数不能为0")
    print(e)
else:
    print("else模块")
    # 没有错误的时候执行
finally:
    print("finally模块")
    # 无论是否出现错误，都会执行

