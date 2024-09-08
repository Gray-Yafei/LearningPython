tuple1 = (1, 2, 3, 4, True, 'hello')
print(tuple1)
print(type(tuple1))

list1 = [1]
print(list1)

tuple2 = (1,)
print(tuple2)
print(type(tuple2))

tuple3 = ()
print(tuple3)
print(type(tuple3))

tuple5 = tuple('hello')
print(tuple5)

tuple6 = tuple(list(range(1, 10)))
print(tuple6)

list1 = list(tuple6)
print(list1)

str1 = str(tuple6)
print(str1)

print("-"*30)
print(tuple1[-1])

print(tuple1[::-1])

print(max(tuple6), min(tuple6), sum(tuple6))
print(len(tuple6))

print(tuple1+tuple6)

print(tuple1*3)

print(1 in tuple1)

# 元组的常用方法
a = tuple1.count('helasd alo')
print(a)

a = tuple1.index(2)
print(a)
print("-"*30)
for i in tuple1:
    print(i)
for index, value in enumerate(tuple1):
    print(index, value)