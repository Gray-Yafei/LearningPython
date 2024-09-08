print(list(range(1, 11, 2)))

for i in range(100,1000):
    # ge = i % 10
    # shi = i // 10 % 10
    # bai = i // 100
    t = str(i)

    if int(t[0]) ** 3 + int(t[1]) ** 3 + int(t[2]) ** 3 == i:
        print(i)
