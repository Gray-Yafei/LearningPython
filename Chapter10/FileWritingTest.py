# 打开文件
f = open('test2', mode='w', encoding='utf-8')
# 写入内容
# 1.
f.write('你好，我是韦亚飞\n')
f.write('你是谁\n')
# 2.1按行写
f.writelines(['你好，我是韦亚飞\n', '你是谁\n'])
# 2.2
context = ['你好，我是韦亚飞', '你是谁']
for i in context:
    f.write(i + '\n')

# 文件关闭前，会一行一行往下写，writelines不会覆盖之前的内容write

# 关闭文件
f.close()

import os
path = os.getcwd()
filename = path + '/test2'
# 打开文件
# f = open('test', encoding='utf-8')  # 相对路径
f = open(filename,encoding='utf-8', mode='r')  # 绝对路径
# f = open('../Chapter9/test2',encoding='utf-8')
# ..退出到上一层
# 读取文件
# 1.按字符数读
context = f.read()
print(context)
# # 2.按行读（1行）
# context = f.readline()
# print(context)
# 2.按行读（每行放入列表中）
# context = f.readlines()
# print(context)
# 关闭文件
f.close()

