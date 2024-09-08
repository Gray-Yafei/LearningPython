import re
# 需要的话百度吧

result = re.match(r'^\d{17}(\d|X)$','12345678901234567X')
print(result)

