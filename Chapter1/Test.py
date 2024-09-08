year = 2024  # 年
month = 2  # 月
day = 2  # 日
week = "一"  # 星期
weather = "晴"
temp = 19.5

print("我是mia")
print(year, "年，我要减肥", sep='')  # sep：设置打印多个内容的分隔符
print(end='*')
# 设置print执行结束后的操作
print(year, "年，我要读100本书", sep='')
print()
print(year, "年，我要去10个城市旅游", sep='*')
print()

print('今天是%d年%d月%d日'%(year, month, day))

print("今天是 %d 年 0%d 月 %02d 日，星期%s，天气%s，温度%.2f度" % (year, month, day, week, weather, temp))


