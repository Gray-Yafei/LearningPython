# -*- coding: utf-8 -*-
# @Time : 2024/8/23 16:15
# @Author : Gray

# https://blog.csdn.net/qq_44921056/article/details/116309229?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522172440085716800172582777%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fblog.%2522%257D&request_id=172440085716800172582777&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~blog~first_rank_ecpm_v1~rank_v31_ecpm-2-116309229-null-null.nonecase&utm_term=%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90&spm=1018.2226.3001.4450
import numpy as np
'''1.array()：创建一个数组
'''
# arr = np.array([5, 2.1, 'May', 20])
# print(arr)
'''
2.np.eye()
eye(N,M,K)：创建一个对角线为1的二维数组
'''
# arr1 = np.eye(5,4,-2)
# print(arr1)
'''3、np.zeros()
zeros()：创建一个用指定形状用0填充的数组。
zeros(shape, dtype=float, order=‘C’)
shape:形状，也就是几行几列的数组
dtype:可选参数，数据类型，默认numpy.float64
order:可选参数，c代表与c语言类似，行优先；F代表列优先
'''
# arr2 = np.zeros((2,3),dtype=float)
# print(arr2)

'''4、np.ones()
ones()：将创建一个用指定形状用1填充的数组
与ones用法类似'''

'''5、np.arange()
arange()：创建一具有有规律递增值的数组
arange()内的常见参数有三种情况（也可以加dtype参数）：
1）一个参数时，参数值为终点，起点取默认值0，步长取默认值1。
2）两个参数时，第一个参数为起点，第二个参数为终点，步长取默认值1。
3）三个参数时，第一个参数为起点，第二个参数为终点，第三个参数为步长。其中步长支持小数。
'''
# arr3 = np.arange(10)
# arr4 = np.arange(2,8)
# arr5 = np.arange(2,4,0.5)
# print(arr3)
# print(arr4)
# print(arr5)

'''6、np.linspace()
linspace()：将创建具有指定数量元素的数组，并在指定的开始值和结束值之间平均间隔。
np.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None, axis=0)此为默认值

(1、将区间[start, stop]分成等间隔的num个数（包含start和stop两个数），并返回它们组成的数组；

(2、若endpoint=False，就将区间[start, stop]分成等间隔的num个数，但返回的数组中不包括‘stop’项；
(包不包括end)

(3、若retstep=True，返回值格式为 (数组部分, 间隔长度)，即在原有数组部分的基础上，加上间隔长度的数据；

(4、 dtype决定输出数组的数据类型，若是未指定，则根据输入参数决定。

(5、 axis在二维数组上面有着一定的作用
'''
# arr6 = np.linspace(start=0, stop=10, num=50,endpoint=False,retstep=True,dtype=int)
# print(arr6)

'''7、np.indices()
indices():创建一组数组（堆积为一个更高的数组），每个维度一个，每个维度表示该维度中的变化。'''

# print('---------------indices的第一个例子------------')
# print(np.indices((3, 4)))
# print('---------------indices的第2个例子------------')
# print(np.indices((6, 5), dtype=float))
# arr7 = np.indices((5,5))
# print(arr7)
a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])
c = np.eye(4)
d = np.array([False, True, True, False, True])
e = np.array([False, False, False, True, True])


'''三、一些操作'''
'''1、获取数值、修改数值'''
# print('--------读取a索引值为1的数值-------')
# print(a[1])
# print('--------读取c第二行的数值----------')
# print(c[1])
# print('--------读取c第三列的数值----------')
# print(c[:, 2])
# print('--------读取c第一行第一列的数值----')
# print(c[0, 0])
# print('--------修改c第一行第一列的数值----')
# c[0, 0] = 2
# print(c)
'''2、查看维度、维度的长度、数组元素类型'''
# print('-----------查看a和c的维度-------')
# print(a.ndim)
# print(c.ndim)
# print('-----------查看a和c的各维度长度--')
# # 第一个是行，第二个是列
# print(a.shape)
# print(c.shape)
# print('-----------查看a、d数组元素类型--')
# print(a.dtype)
# print(d.dtype)
'''3、四则运算及逻辑运算'''
# print('-----------a与b相加------')
# print(b+a)
# print('-----------a与b相减------')
# print(b-a)
# print('-----------a与b相乘------')
# print(b*a)
# print('-----------a与b相除------')
# print(b/a)
# print('-----------d与e相与------')
# print(np.logical_and(d, e))
# print('-----------d与e相或------')
# print(np.logical_or(d, e))
# print('-----------d取非---------')
# print(np.logical_not(d))
# print('-----------d与e异或------')
# print(np.logical_xor(d, e))

'''4、reshape：更改数组形状'''
# 将一行四列的数组改为两行两列的数组
# print(a.reshape(2, 2))  # 不是在原数组上修改，需要拿新变量接收
# print(a)

# 当reshape中的数字为负数时，则代表未指定具体要求，可用来只获得行或列
# print('---------只获得列------')
# print(a.reshape(-1, 1))
# print('---------只获得行------')
# print(a.reshape(1, -2))
'''5、索引及其一些切片操作'''
# print('----------从索引值0到索引值1的结果------------')
# print(a[0: 2])  # 1 2
# print('----------从索引值0到索引值2的结果------------')
# print(a[: 3])  # 1 2 3
# print('----------从索引值0到索引值2增长的步长为2------')
# print(a[0: 3: 2])  # 1 3
# print('----------从索引值-1到索引值-3的结果-----------')
print(a[-1:-3])  # 4 3 -> []
# print('----------从索引值1到索引值-2的结果------------')
# print(a[1: -1])  # 2 3

# 有一个结果为空，所以，索引是不能以负索引为起始索引。
'''以二维数组c为例'''
# print('----------对应图中的红色区域部分-------------')
# print(c[1, 2:4])  # 0 0
# print('----------对应图中的蓝色区域部分-------------')
# print(c[2:4, 0:2])  # [[0 0] [0 0]]
# print('----------对应图中的绿色区域部分-------------')
# print(c[0, :])  # 1 0 0 0


