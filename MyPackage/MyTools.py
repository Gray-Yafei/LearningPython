import random,time
def randomChar(upper = True):
    if upper:
        s = chr(random.randint(ord('A'),ord('Z')))
    else:
        s = chr(random.randint(ord('a'),ord('z')))
    return s

def randomString(length):
    s = ''
    for i in range(length):
        s += randomChar(random.choice([True,False]))
    return s

def getTime():
    t = time.localtime()
    return time.strftime("%Y-%m-%d %H:%M:%S", t)



def main():
    a = []
    for i in range(10):
        a.append(randomString(random.randint(3,6)))
    print(a)

