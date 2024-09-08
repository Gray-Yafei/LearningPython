def func(m, n):  # ¹«Ô¼Êý
    maxnum = 1
    for i in range(1, min(m, n)):
        if m % i == 0 and n % i == 0:
            maxnum = i
    return maxnum


def sushu(x):
    flag = False
    for i in range(2, x):
        if x % i == 0:
            return flag
        else:
            continue
    flag = True
    return flag


if __name__ == '__main__':
    for i in range(1, 10):
        if sushu(i):
            print(i)
