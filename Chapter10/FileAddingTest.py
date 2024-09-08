# 打开文件
f = open('test3', mode='a', encoding='utf-8')

# 写入文件
f.write('hello world\n')

s = ['hello\n', 'world\n']
f.write(''.join(s))

# 关闭文件
f.close()