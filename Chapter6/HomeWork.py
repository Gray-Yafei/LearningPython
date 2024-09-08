# users = [{'name': '小红', "password": '123',"status": True},
#          {'name': 'mia', "password": '456',"status": True},
#          {'name': 'Jack', "password": '789',"status": False}
#          ]
#
#
# i = 0
# isflag = False
# while True:
#     name = input("Please enter your name: ")
#     password = input("Please enter your password: ")
#     for user in users:
#         if user['name'] == name:
#             isflag = True
#             if user['status'] == False:
#                 print("您被加入黑名单，请退出")
#                 i = 3
#                 break
#             if user['password'] == password:
#                 print("登录成功")
#                 i = 3
#                 break
#             else:
#                 print("密码有误，请重新输入")
#     if not isflag:
#         print("您未注册，请重新输入")
#
#     i += 1
#     if i >= 3:
#         print("您登录超过3次，或已加入黑名单，程序退出")
#         break

date = input("Enter a date: ")
year = int(date.split('-')[0])
month = int(date.split('-')[1])
day = int(date.split('-')[2])
dates = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    dates[1] += 1

total = sum(dates[:month - 1]) + day
print(total)


