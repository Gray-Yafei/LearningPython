score = 68

if score >= 90:
    print('A')
elif score >= 80:
    print('B')
elif score >= 70:
    print('C')
elif score >= 60:
    print('D')
else:
    print('F')

w = float(input("请输入你的体重，单位kg："))
h = float(input("请输入你的身高，单位m："))
bmi = w / (h * h)
print(bmi)
if bmi < 18.5:
    print("太瘦了")
elif bmi < 23.9:
    print("非常健康")
else:
    print("太胖了")