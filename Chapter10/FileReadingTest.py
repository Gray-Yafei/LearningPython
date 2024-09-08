import os
path = os.getcwd()
filename = path + '/test'
# 打开文件
# f = open('test', encoding='utf-8')  # 相对路径
f = open(filename,encoding='utf-8', mode='r')  # 绝对路径
# f = open('../Chapter9/test2',encoding='utf-8')
# ..退出到上一层
# 读取文件
# 1.按字符数读
# context = f.read(5)
# print(context)
# # 2.按行读（1行）
# context = f.readline()
# print(context)
# 2.按行读（每行放入列表中）
context = f.readlines()
print(context)
# 关闭文件
f.close()

