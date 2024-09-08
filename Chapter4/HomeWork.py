# age = input("Enter your age: ")
# if age.isdigit():  # 判断输入是否是阿拉伯数字
#     age = int(age)
#     if age >= 0 and age <= 100:
#         print("Your age is %d" % age)
#     else:
#         print("Sorry, your age is invalid")
# else:
#     print("Sorry, your age is invalid")



pythonScore = input("Enter your python score: ")
cScore = input("Enter your c-score: ")
if pythonScore.isdigit() and cScore.isdigit():
    pythonScore = int(pythonScore)
    cScore = int(cScore)
    if pythonScore >= 60 or cScore >= 60:
        print("成绩合格")
    else:
        print("重修")
else:
    if not pythonScore.isdigit():
        print("py输入有误，请重新输入")
    if not cScore.isdigit():
        print("c输入有误，请重新输入")


