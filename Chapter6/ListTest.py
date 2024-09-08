# list1 = []
#
list2 = [1, 2, 3, True, False, 'hello']
#
# print(list1)
#
# print(type(list1))
#
# print(list2[:2])
#
# list3 = list('hello')
# print(list3)
#
# list4 = list3 + list2
# print(list4)
#
# list5 = list2 * 2
# print(list5)
#
# print('1' in list2)
#
#
# print(len(list1))
# list1 = [1, 2, 3, 4, 5]
#
# print(max(list1))
#
# list2 = list('12345')
# print(list2)
# print(min(list2))

# for i in list2:
#     print(i)
# for i,j in enumerate(list2):
#     print(i,j)

# for i in range(len(list2)):
#     print(i,list2[i])

# list2.append(66)
# # 添加元素
# print(list2)
#
# list2.extend(['hello', 'world'])
# # 添加列表，类似+
# print(list2)

list2.insert(3, "hello")
print(list2)

list2.pop(2)
print(list2)

list2.remove("hello")
print(list2)

list3 = list2.copy()
print("*" * 20)
print(list3)

list1 = [1,2,3,4,5,6,7,8,9,1,1,1]

print(sum(list1)/len(list1))