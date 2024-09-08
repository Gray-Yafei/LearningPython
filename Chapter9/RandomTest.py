import random

# 0-1随机小数
num1 = random.random()
print(num1)

# 随机整数[a,b]
num2 = random.randint(1,2)
print(num2)

# 获取列表中的随机元素
list1 = [6,5,4,3,2,1]
# 方法一
print(list1[random.randint(0,len(list1)-1)])
# 方法二
print(random.choice(list1))
print(random.choice("hello"))

# 打乱列表

random.shuffle(list1)
print(list1)

# 随机生成字母组成的列表

from MyPackage import MyTools
MyTools.main()
