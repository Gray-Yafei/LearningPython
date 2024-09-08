# n = 0
# sum = 0
# while n <= 100:
#     sum += n
#     n += 1
# print(sum)

# n = 4
# result = 1
# sum = 0
# for i in range(1, n+1):
#     result *= i
#     sum += result
# print(sum)


# n = 5
# result = 1
# i = 1
# sum = 0
# while i <= n:
#     result *= i
#     sum += result
#     i += 1
# print(sum)

# 判断一个数字n是否是质数

# n = 11
# i = 2
# # flag = True
# while i < n:
#     if n % i == 0:
# #       flag = False
#         print("%d不是质数" % n)
#         break
#     i += 1
# else:
#     print("%d是质数" % n)
# # if flag:
# #     print("%d是质数" % n)


# n = 11
# for i in range(2, n):
#     if n % i == 0:
#         print("%d不是质数" % n)
#         break
# else:
#     print("%d是质数" % n)
#
# # 若没有执行break，则执行else

# for i in range(5):
#     if i == 3:
#         continue
#     print(i)
# ***************************************
# n = 0.1
# for i in range(50):
#     n *= 2
# print(n)

# ****************************************

# g = 1
# total = 0
# num = 100
#
# for i in range(1, num + 1):
#     total += g
#     g *= 2
# print(total)


# m = 3
# n = 5
#
# for i in range(m):
#     for j in range(n):
#         print("*", end='')
#     print()

# n = 7
# for i in range(1, n+1):
#     print(' '*(n-i),'*'*(2*i-1))


# peach = 1
#
# while True:
#     d1 = peach // 2 - 1
#     d2 = d1 // 2 - 1
#     d3 = d2 // 2 - 1
#     if d3 == 1:
#         print(peach)
#         break
#     peach += 1

# n = 12
# for i in range(1, n + 1):
#     for j in range(1,i+1):
#         print("%d × %d = %d\t" % (j,i,i*j), end='')
#     print()


apple = 1
while True:
    d = apple
    for i in range(3):
        d = d // 2 - 1

    if d == 1:
        print(apple)
        break
    apple += 1