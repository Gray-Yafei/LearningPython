total = 10
a = 2
b = 4
c = total - a - b
print("小A和小B一共拿走了%d个苹果" % (a+b))
print(c)


total = 100
print("支付宝余额：%d" % total)
total += 10
print("支付宝余额：%d" % total)
total -= 20
print("支付宝余额：%d" % total)
total -= total
print("支付宝余额：%d" % total)