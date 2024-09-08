# -*- coding: UTF-8 -*-
n = int(input())  # 数组长度
m = input()
lst = m.replace(' ','')
lst1 = []
for i in lst:
    lst1.append(int(i))

count = 0
x = max(lst1)
y = min(lst1)
while True:
    if count == 0:
        if max(lst1) - min(lst1) == 0:
            break
    else:
        if max(lst1) - min(lst1) == 0 or max(lst1) - min(lst1) == x - y:
            break
        else:
            count += 1
            x = max(lst1)
            y = min(lst1)
            lst1.append(max(lst1)-1)
            lst1.append(min(lst1)+1)
            lst1.remove(x)
            lst1.remove(y)
print(count)