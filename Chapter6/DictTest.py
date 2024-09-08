# 字典的创建
d = {
    "name": 'mia',
    'gender': False,
}
print(d)
print(type(d))

# d = {}
# print(d)
# print(type(d))
#
# d = dict()
# print(d)
# print(type(d))

# 字典添加键值对
d['height'] = 170
print(d)

print(d['name'])

d['gender'] = True
print(d)

print('name' in d)
print("*"*40)
# 字典的遍历
# for i in d:
#     print(i,d[i])

for k,v in d.items():
    print(k,v)

for k in d.keys():
    print(k)

for v in d.values():
    print(v)


print("*"*40)
# 字典的常用方法

print(d.get('gender'))
print(d)
d.popitem()
print(d)
d.update({'age': 23})
print(d)