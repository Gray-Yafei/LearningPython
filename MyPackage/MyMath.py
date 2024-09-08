def add(x, y):
    return x + y

def total(*args):
    '''
    参数args:接收一个列表
    结果：返回平方和
    '''
    result = 0
    for i in args:
        result += i ** 2
    return result

author = 'YF'
