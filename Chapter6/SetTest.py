# 集合的创建

s = set()
print(s)
print(type(s))

s = {1, 2, 3, 4}
print(s)
print(type(s))

s = set([1, 2, 3, 4, 1])
print(s)

s = set((1, 2, 3, 3))
print(s)

s = set('123')
print(s)

print("*" * 30)

s = set({1: 'a', 2: 'b', 3: 'c', 'a': 4})
print(s)

print('1' in s)
print(len(s))

# print(max(s))
print("*" * 30)

for i in s:
    print(i)

# 常用的方法
print(s)
s.remove(1)
print(s)

s.update([2, 3, 4, 3, 1, 5, 8, 9, 4, 8])
print(s)

s.add(10)
print(s)

# 交集并集
s2 = {10, 20, 30, 0, 1, 2, 3}
print(s)
print(s2)
print(s & s2)  # 交集
print(s | s2)  # 并集

score = [8,7,6,5,4,3,2,1,1,2,3,4,2,3,1]
s = set(score)
print(s)
d = {}
for i in s:
    d[i] = score.count(i)

for k, v in d.items():
    print(k, v)

