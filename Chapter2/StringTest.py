# 创建字符串
s1 = "hello,world"
s2 = 'hello'

s3 = '''
hello
world
'''

s4 = "It's a hat"
s5 = '123"\'23123'



print(s1)
print(s2)
print(s3)
print(s4)
print(s5)

print('------------------------')

print(s1 + str(3))

print(s1 * 3)

print('-'*20)

print(s1[0])

print(s1[-5:-2])

s2 = '123456789'
print(s2[0:9:2])
print(s2[::-1])