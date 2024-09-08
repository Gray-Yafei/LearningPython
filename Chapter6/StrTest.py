s1 = "Hello World"

print(s1+'hi')
print(s1*3)
print(len(s1))
print(max(s1),min(s1))
print(ord('w'))

print('s' in s1)


for index, value in enumerate(s1):
    print(index, value)

for i in range(len(s1)):
    print(i, s1[i])

print("*"*30)
print(s1.split(' '))
print('*'.join(['111','1112','3333']))

print(s1.replace('o','a'))

print("*"*30)


s = input("请输入一篇文章")
a, b, c = 0, 0, 0
for i in s:
    if i.isdigit():
        a+=1
    elif i.isalpha():
        b+=1
    else:
        c+=1
print(a, b, c)