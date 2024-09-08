# -*- coding: utf-8 -*-
# @Time : 2024/8/27 10:18
# @Author : Gray
# https://blog.csdn.net/qq_18351157/article/details/106032849?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522172472503616800188573092%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fblog.%2522%257D&request_id=172472503616800188573092&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~blog~first_rank_ecpm_v1~rank_v31_ecpm-28-106032849-null-null.nonecase&utm_term=Numpy&spm=1018.2226.3001.4450

import numpy as np

'''02_Numpy的One-hot形式的转换（eye，identity）'''
# 1.Numpy.eye()*******************************
# e = np.eye(N = 4,M =5,k = -2,dtype = np.float64)
# # N；行数，M：列数，k非主对角线，dtype指定类型，可以输入字符串'int32'或np.float32等
# print(e)
# print(type(e))
# # e的类型
# print(e.dtype)
# # e中数据的类型
# 2.Numpy.identity()*******************************
# # numpy.identity()是一个可以返回单位矩阵（identity matrix）的函数。
# i = np.identity(4,dtype=np.uint)
# print(i)
# print(i.dtype)
# 3.One-hot的转换*******************************
# # 例子：
# a = [3,0,8,1,9]
# a_onehot = np.identity(10)[a]
# print(a_onehot)
# a = [2,2,0,1,0]
# a_onehot = np.identity(max(a)+1)[a]
# print(a_onehot)

'''03_Numpy的数组各行，各列的求和，平均值，最大值，最小值，最大最小值差，标准差，方差等的计算'''
# a = np.arange(12).reshape(3, 4)
# print(a)
# print(a.shape)
# 1.numpy.sum() 求和 *************************************************
# print(np.sum(a))  # 所有元素求和
# print(a.sum())
# print(np.sum(a, axis=0))  # 按列求和 [12 15 18 21]
# print(a.sum(axis=0))  # [12 15 18 21]
# print(np.sum(a, axis=1))  # 按行求和 [ 6 22 38]
# print(a.sum(axis=1))  # [ 6 22 38]
# 2.numpy.mean() 平均值 *************************************************
# # 方法同上
# print(np.mean(a))
# print(np.mean(a, axis=0))
# print(np.mean(a, axis=1))
# 3.numpy.min() 最小值/numpy.max() 最大值 *************************************************
# # 方法同上
# print(np.min(a))
# print(np.min(a, axis=0))
# print (np.amin(a,0))
# print(np.min(a, axis=1))
# print (np.amin(a,1))
# 4.numpy.ptp() 最大值与最小值的差（最大值-最小值） *************************************************
# # 每列和每行的最大值与最小值的差都相同
# print(a.ptp(axis=0))
# print(np.ptp(a,axis=0))
# print(a.ptp(axis=1))
# print(np.ptp(a,axis=1))
# 5.numpy.std() 标准差/numpy.var() 方差 *************************************************
# print(np.std(a,axis=0))  # 按列
# print(np.var(a))  # 所有数据
# 6.多维数组的参数axis *************************************************
# b = np.arange(24).reshape(2, 3, 4)
# print(b.shape)
# print(b)
# print(b.sum(axis=0))  # 对应元素
# # [[12 14 16 18]
# #  [20 22 24 26]
# #  [28 30 32 34]]
# print(b.sum(axis=1))  # 按列
# # [[12 15 18 21]
# #  [48 51 54 57]]
# print(b.sum(axis=2))  # 按行
# # [[ 6 22 38]
# #  [54 70 86]]
# print(b.sum(axis=(0, 1)))
# # [60 66 72 78]
# print(b.sum(axis=(0, 2)))
# # [ 60  92 124]
# print(b.sum(axis=(1, 2)))
# # [ 66 210]

'''04_Numpy的函数np.where（）—满足条件的处理'''
# 1.Numpy.where()的概要
# Numpy.where(condition,x,y)
# 当条件（condition）满足时为真（True），返回x。当条件（condition）不满足时为假（False），返回y。
a = np.arange(12).reshape(3, 4)
# print(a)
# print(np.where(a < 4, -1, 100))
# # [[ -1  -1  -1  -1]
# #  [100 100 100 100]
# #  [100 100 100 100]]
# print(np.where(a < 4, True, False))
# # [[ True  True  True  True]
# #  [False False False False]
# #  [False False False False]]
# print(a < 4)
# # [[ True  True  True  True]
# #  [False False False False]
# #  [False False False False]]

# 2.多个条件式的使用
# # 多个条件式时，用（）将其分开，条件式与条件式之间可以用 &，| 逻辑运算符进行连接。但不可以使用and，or等关键字链接。
# print(np.where((a > 2) & (a < 6), -1, 100))
# print(np.where((a == 7) | (a > 2) & (a < 6), -1, 100))  # 先&后|
# print((a > 2) & (a < 6))
# # [[False False False  True]
# #  [ True  True False False]
# #  [False False False False]]

# 3.满足条件元素的替换
# # 满足条件的替换
# a[a < 4] = -1  # 2种写法
# print(a)
# print(np.where(a < 4, -1, a))
# # 不满足条件的替换
# print(np.where(a < 4, a, 100))
# # numpy.where()返回一个新的ndarray数组，原数组不变。
# a_new = np.where(a < 4, -1, a)
# print(a_new)
# print(a)

# 4.满足条件元素的处理
# print(np.where(a < 4, a * 10, a))

# 5.满足条件元素的索引
# print(np.where(a < 6))  # 返回行坐标和列坐标，组合起来就是满足条件的坐标
# print(type(np.where(a < 4)))  # <class 'tuple'>
# print(list(zip(*np.where(a < 6))))  # *np表示解包，加*会更好理解，不加*分别返回横纵坐标

a_3d = np.arange(24).reshape(2, 3, 4)
# print(a_3d)
# print(np.where(a_3d < 5))
# print(*np.where(a_3d < 5))  # [0 0 0 0 0] [0 0 0 0 1] [0 1 2 3 0]
# print(list(zip(*np.where(a_3d < 5))))  #[(0, 0, 0), (0, 0, 1), (0, 0, 2), (0, 0, 3), (0, 1, 0)]
a_1d = np.arange(6)
# print(a_1d)
# print(np.where(a_1d < 3))  # (array([0, 1, 2], dtype=int64),)
# print(*np.where(a_1d < 3))  # [0 1 2]
# print(list(zip(*np.where(a_1d < 3))))  # [(0,), (1,), (2,)]
# print(np.where(a_1d < 4)[0].tolist())  # 可以使用tolist()，将其转换成list格式。

'''05_Numpy任意行&列的删除方法（numpy.delete）'''
# 1.Numpy.delete（）基本的使用方法
# Numpy.delete（arr,obj,axis=None）有以下3个参数：
# arr:输入数组
# obj:指定要通过的整数,切片或者列表（数组）删除的行号/列号
# axis:要删除的轴

# a = np.arange(12).reshape(3, 4)
# a = np.delete(a, 2, 0)  # 不对a本身进行修改，而需要用一个新的变量接收。
# # 参数：obj：第几行（列），如果axis=None，则将obj指定的索引处的元素展平到一维后将其删除。由于轴的默认值为"无"
# print(a)
# print(np.delete(a, 1, None))  # print(np.delete(a, 1))  [ 0  2  3  4  5  6  7  8  9 10 11]

# 2.一次删除多行和多列
# 如果在第二个参数obj中指定列表或切片，则可以一次删除多个行或列。
# print(np.delete(a, [0, 1, 3], 1))
#

# print(np.delete(a, slice(2), 1))  # slice(2)意思是生成一个切片对象[0,2) 但是不能print出来
# print(np.delete(a, slice(1, 3), 1))
# print(np.delete(a, slice(None, None, 2), 1))
# print(np.delete(a, np.s_[:2], 1))  # 直接输入[:2]会报错
# print(np.delete(a, np.s_[1:3], 1))
# print(np.delete(a, np.s_[::2], 1))
# 跟正常理解的切片是一样的，不过，要把这些数据给删掉，因此剩下的结果跟切片的结果相反

# numpy.delete（）无法一次删除多个维度（例如行和列）。要删除多个维度时，请重复使用numpy.delete（）。
# print(np.delete(np.delete(a, 1, 0), 1, 1))  # 删除第1行和第1列(从0计数)

# 3.多维数组的例
# a_3d = np.arange(24).reshape(2, 3, 4)
#
# print(np.delete(a_3d, 1, 0))
# # [[[ 0  1  2  3]
# #   [ 4  5  6  7]
# #   [ 8  9 10 11]]]
#
# print(np.delete(a_3d, 1, 1))
# # [[[ 0  1  2  3]
# #   [ 8  9 10 11]]
# #
# #  [[12 13 14 15]
# #   [20 21 22 23]]]
#
# print(np.delete(a_3d, 1, 2))
# # [[[ 0  2  3]
# #   [ 4  6  7]
# #   [ 8 10 11]]
# #
# #  [[12 14 15]
# #   [16 18 19]
# #   [20 22 23]]]

'''06_Numpy各种随机数组的生成方法'''
# 1.生成均匀分布的随机数
# np.random.seed(0)
# rand = np.random.rand()
# arr = np.random.rand(3)  # [0.71518937 0.60276338 0.54488318]
# arr1 = np.random.rand(3, 4)  # 3行4列
# arr1_sample = np.random.random_sample((3, 4))  # random_sample与rand没区别，就是输入的是元组类型
# arr2 = np.random.rand(3, 4, 5)  # 3页4行5列

# 2.numpy.random.randint()： 均匀分布 任意值范围的整数
# arr = np.random.randint(4, 10, (3, 3))  # 4到10的3 x 3的随机整数数组

# 3.numpy.random.randn(): 正态分布 平均为0，标准差为1
# arr = np.random.randn(3, 4)  # 3行4列，同上

# 4.numpy.random.normal(): 正态分布 任意值的平均和标准差
# arr = np.random.normal(loc=-2, scale=0.5, size=(3, 4))  # 平均值为-2，方差为0.5的3×4矩阵

# 5.numpy.random.binomial(): 二项分布
# 6.numpy.random.beta(): Beta分布
# 7.numpy.random.gamma(): Gamma分布
# 8.numpy.random.chisquare(): 卡方分布

'''07_Numpy渐变图片的生成'''
# 1.np.linspace()
# np.linspace()有开始值(start),结束值(stop),生成个数(num)3个参数，返回的是一个一维数组(等差数列)。
# 和range(),np.arange()不同的是,隔间数将会自动生成。[start, stop]中一共生成num个数字
# print(np.linspace(0, 10, 11))  # [ 0.  1.  2.  3.  4.  5.  6.  7.  8.  9. 10.]
# print(np.linspace(0, 10, 5))  # [ 0.   2.5  5.   7.5 10. ]

# 2.np.tile()
# np.tile()是一个可以横，竖排列的函数。在参数中指定原始数组和重复次数。
# 在二维排列的情况下，重复数为(行的重复数(垂直)，列的重复数(水平))。
# a = np.array([0,1,2,3])
# print(np.tile(a,2))  # [0 1 2 3 0 1 2 3]
# print(np.tile(a,(3,2)))  # 把a当作一个整体，排成3行2列的矩阵
## 原数组是2维的：
# a = np.array([[11, 12], [21, 22]])
# print(np.tile(a,2))
# # [[11 12]      [[11 12 11 12]
# #  [21 22]]      [21 22 21 22]]
# print(np.tile(a,(3,2)))  # 同上当作一个整体

'''08_Numpy初始化生成相同元素值的ndarray数组'''
# 1.numpy.zeros(): 初始值为0
# a = np.zeros(3)  # [0. 0. 0.]
# a = np.zeros((3,4),dtype=np.int32)  # 3行4列都是0，可以指定类型
# print(a)
# 2.numpy.ones(): 初始值为1 同上
# 3.numpy.full(): 任意值的初始化
# print(np.full((2, 3), np.pi,dtype=np.float64))  # 2行3列，值为pi。第一个参数shape表示个数或者行列
# dtype还可以进行类型的强制转换。

# 4.numpy.zeros_like(): 初始值为0
# a = np.arange(10).reshape(2,5)
# a_float = a/10
# print(np.zeros_like(a))  # int
# print(np.zeros_like(a_float))  # float
# print(np.zeros_like(a,dtype=np.float64))  # 也可以类型转换

# 5.numpy.ones_like(): 初始值为1  同上
# 6.numpy.full_like(): 任意值的初始化
# print(np.full_like(a,-10.2,dtype=np.int32))  # 类型根据第一个参数a来，a为整数，则类型转换,也可以dtype指定

'''09_Numpy生成空ndarray数组的方法(empty和empty_like)'''
'''感觉不好用，估计用不太到'''
# 1.Numpy.empty()空数组的生成
# 由于数组是未初始化的，所以其中的值是不确定的。
# 使用 numpy.empty() 时，应该确保你随后会填充数组，或者明确知道未初始化的值不会影响你的计算。
# arr = np.empty((2, 3))
# print(arr)
# print(np.empty(3, dtype=np.int64))
# 2.Numpy.empty_like()空数组的生成
# 同zeros_like

'''10_Numpy图片RGB色彩通道的分离，以及单色化，黑色化和颜色的交换'''
'''跳过，感兴趣自己去看'''

'''11_Numpy含有缺失值ndarray数组的求和，平均值的计算方法'''
# 1.使用函数nansum()，可以对缺失值(nan)以外的其他值进行求和。
arr = np.array([[11., 12., np.nan, 14.],
                [21., np.nan, np.nan, 24.],
                [31., 32., 33., 34.]])
# print(np.sum(arr))  # nan
# print(np.nansum(arr))  # 212.0 除了nan以外的数据求和
# print(np.nansum(arr, axis=0))  # 按列 [63. 44. 33. 72.]
# print(np.nanmean(arr, axis=0))  # [21. 22. 33. 24.]  # 有几个数求和就有几个数求平均
# 平均值，最大值，最小值，标准差，方差等的计算，
# 可以使用函数np.nanmean(), np.nanmax(), np.nanmin(), np.nanstd(), np.nanvar()。

'''12_Numpy数组(ndarray)中缺失值(nan)的替换'''
# 将NumPy数组ndarray的缺失值NaN（例如np.nan）的元素替换为其他值时，
# 可以使用np.nan_to_num（）和np.isnan（）布尔值索引的方法。将其替换为任意值，或替换为不包含缺失值NaN的元素的平均值。
# 1.缺失值NaN的生成和判定
# print(np.nan == np.nan)  # False : "=="不能进行是否为缺失值(nan)的判定
# print(np.isnan(np.nan))  # True : 使用np.isnan（）或math.isnan()（也行）来判定是否为缺少值(nan)。
# print(np.isnan(arr))  # 可以用来判定ndarray中每个元素是否判为缺失值NaN。

# 2.np.nan_to_num（）缺失值NaN的替换
# 使用np.nan_to_num（）会用0替换缺失值NaN，但是一般不会修改原ndarray，而是创建一个新的ndarray。
# 加入copy=False 则会在原ndarray进行修改
# print(np.nan_to_num(arr,copy=False))  # arr也会被修改
# print(np.nan_to_num(arr, nan=-1))  # 指定替换nan的值，默认是0
# print(np.nan_to_num(arr,nan=np.nanmean(arr)))  # 用不缺失值的平均值来填充

# 3.用布尔值索引的方法替换缺失值NaN
# print(np.nanmean(arr))
# print(np.isnan(arr))
# arr[np.isnan(arr)] = np.nanmean(arr)  # 用不缺失值的平均值来填充
# print(arr)

# 扩展numpy读取csv文件的函数
# 使用np.genfromtxt（）在进行读取时，通过参数filling_values来指定用任意值填充缺失的部分。
# a_fill = np.genfromtxt('地址值', delimiter=',', filling_values=0)
# 参数delimiter：表示用什么划分数据，filling_values: 缺失值用什么填充

'''13_Numpy数组(ndarray)中含有缺失值(nan)行和列的删除方法'''
# 1.删除包含缺失值（NaN）的行
# 要删除包含缺失值NaN的行，可以使用any（）方法，如果NumPy数组行中有一个缺失值则整行返回True。
# 如果参axis= 1，则确定每一行是否有缺失值。
# print(np.isnan(arr).any(axis=1))
# # [True True False]
# print(~np.isnan(arr).any(axis=1))
# # [False False  True]
# print(arr[~np.isnan(arr).any(axis=1), :])
# # [[31. 32. 33. 34.]]
# print(arr[~np.isnan(arr).any(axis=1)])
# # [[31. 32. 33. 34.]]

# 2.删除包含缺失值（NaN）的列
# print(~np.isnan(arr).any(axis=0))
# # [ True False False  True]
# print(arr[:, ~np.isnan(arr).any(axis=0)])
# # [[11. 14.]
# #  [21. 24.]
# #  [31. 34.]]
# arr[2, 2] = np.nan
# print(arr)
# # [[11. 12. nan 14.]
# #  [21. nan nan 24.]
# #  [31. 32. nan 34.]]
# print(arr[:, ~np.isnan(arr).any(axis=0)])
# # [[11. 14.]
# #  [21. 24.]
# #  [31. 34.]]
# print(arr[:, ~np.isnan(arr).all(axis=0)])
# # [[11. 12. 14.]
# #  [21. nan 24.]
# #  [31. 32. 34.]]

'''14_NumPy数组ndarray的显示格式（位数，指数符号，零填充等）的指定'''
# https://blog.csdn.net/qq_18351157/article/details/105093021
# 感觉有点没必要看
# print(np.get_printoptions())
'''系统默认设置
{'edgeitems': 3, 'threshold': 1000, 'floatmode': 'maxprec', 'precision': 8, 'suppress': False,
 'linewidth': 75, 'nanstr': 'nan', 'infstr': 'inf', 'sign': '-', 'formatter': None, 'legacy': False}
 '''
# 3.np.round()
#  在np.round（）中，第一个参数指定目标ndarray，第二个参数指定小数点后的位数。如果对数字位数使用负值，则也可以四舍五入为整数位数。
# a = np.array([12.3456, 0.123456789])
# b = np.round(a, 2)
# print(b)
# # [12.35  0.12]
# b = np.round(a, -1)
# print(b)
# # [10.  0.]
# b = np.round([1234.56, 123456.789], -2)
# print(b)
# # [  1200. 123500.]

'''15_Numpy使用sort和argsort函数进行(行・列）排序'''
# https://blog.csdn.net/qq_18351157/article/details/107049622

# 1.numpy.sort()：获取排序数组ndarray
# 1.1 一维数组
# 对于一维数组，它只是按升序排序。
# 返回一个新的已排序的ndarray，保留原始的ndarray不变。
# a = np.array([3, 4, 2, 0, 1])
# a_sort = np.sort(a)
# print(a)
# print(a_sort)
# # np.sort（）函数没有反向参数。如果要降序使用切片[::-1]。
# a_sort_reverse = np.sort(a)[::-1]
# print(a_sort_reverse)

# 1.2 多维数组
a_2d = np.array([[20, 3, 100], [1, 200, 30], [300, 10, 2]])
# print(a_2d)
# a_2d_sort_col = np.sort(a_2d, axis=0)  # axis = 0在列上排序，而axis = 1在行上排序。每列/行中的值分别进行排序。
# print(a_2d_sort_col)
# a_2d_sort_row = np.sort(a_2d, axis=1)
# print(a_2d_sort_row)
# # 默认值为axis = -1，它沿最后一个轴排序。如果是二维数组，则按行排序。
# # 如果要降序，请对每个轴使用切片[::-1]
# a_2d_sort_col_reverse = np.sort(a_2d, axis=0)[::-1, :]
# print(a_2d_sort_col_reverse)
# a_2d_sort_row_reverse = np.sort(a_2d)[:, ::-1]
# print(a_2d_sort_row_reverse)

# 2.ndarray.sort（）：排序数组ndarray本身，参数同上

# a_2d.sort()  # 默认按行顺序
# print(a_2d)
# a_2d.sort(axis=0)  # 再按列排序
# print(a_2d)
# print(a_2d[::-1])  # 按行逆序打印
# print(a_2d[:,::-1])  # 按列逆序打印

# 3.numpy.argsort（）：获取排序索引的数组ndarray
# a_2d = np.array([[20, 3, 100], [1, 200, 30], [300, 10, 2]])
# print(a_2d)
# # [[ 20   3 100]
# #  [  1 200  30]
# #  [300  10   2]]
#
# a_2d_sort_col_index = np.argsort(a_2d, axis=0)  # 按列排序，输出索引
# print(a_2d_sort_col_index)
# # [[1 0 2]
# #  [0 2 1]
# #  [2 1 0]]
#
# a_2d_sort_row_index = np.argsort(a_2d,axis =1)  # 按行排序，输出索引
# print(a_2d_sort_row_index)
# # [[1 0 2]
# #  [0 2 1]
# #  [2 1 0]]

# 3.1如何按特定的行或列排序
# 使用np.argsort（）获取参考行或列索引。

# 按特定列排序
# # 使用np.argsort（）获取参考行或列索引。
# print(a_2d)
# # [[ 20   3 100]
# #  [  1 200  30]
# #  [300  10   2]]
# col_num = 1  # 按第一列的值进行排序
# print(a_2d[:, col_num])
# # [  3 200  10]
# print(np.argsort(a_2d[:, col_num]))
# # [0 2 1]
# # 根据该索引对行进行排序。
# a_2d_sort_col_num = a_2d[np.argsort(a_2d[:, col_num])]
# print(a_2d_sort_col_num)
# # [[ 20   3 100]
# #  [300  10   2]
# #  [  1 200  30]]
# # 降序：如果要使用降序，请以相反的顺序使用[::-1]以通过np.argsort（）获得索引。
# print(np.argsort(a_2d[:, col_num])[::-1])
# # [1 2 0]
# a_2d_sort_col_num_reverse = a_2d[np.argsort(a_2d[:, col_num])[::-1]]
# print(a_2d_sort_col_num_reverse)
# # [[  1 200  30]
# #  [300  10   2]
# #  [ 20   3 100]]

# 按特定行排序
# row_num = 1
#
# print(a_2d[row_num])
# # [  1 200  30]
#
# print(np.argsort(a_2d[row_num]))
# # [0 2 1]
#
# a_2d_sort_row_num = a_2d[:, np.argsort(a_2d[row_num])]
# print(a_2d_sort_row_num)
# # [[ 20 100   3]
# #  [  1  30 200]
# #  [300   2  10]]
#
# print(np.argsort(a_2d[row_num])[::-1])
# # [1 2 0]
#
# a_2d_sort_row_num_inverse = a_2d[:, np.argsort(a_2d[row_num])[::-1]]
# print(a_2d_sort_row_num_inverse)
# # [[  3 100  20]
# #  [200  30   1]
# #  [ 10   2 300]]

'''16_NumPy数组ndarray以任何顺序排列行和列'''
# https://blog.csdn.net/qq_18351157/article/details/107187726

# a = np.arange(10, 35).reshape(5, 5)
# print(a)
# # [[10 11 12 13 14]
# #  [15 16 17 18 19]
# #  [20 21 22 23 24]
# #  [25 26 27 28 29]
# #  [30 31 32 33 34]]
#
# # 1.以任何顺序对列进行排序
# col_swap = a[:, [3, 2, 4, 0, 1]]
# print(col_swap)
# # [[13 12 14 10 11]
# #  [18 17 19 15 16]
# #  [23 22 24 20 21]
# #  [28 27 29 25 26]
# #  [33 32 34 30 31]]
# col_inverse = a[:, ::-1]
# print(col_inverse)
# # [[14 13 12 11 10]
# #  [19 18 17 16 15]
# #  [24 23 22 21 20]
# #  [29 28 27 26 25]
# #  [34 33 32 31 30]]
#
# # 2. 以任何顺序对行进行排序
# row_swap = a[[3, 2, 4, 0, 1]]
# print(row_swap)
# row_inverse = a[::-1]
# print(row_inverse)
# row_select2 = a[[2, 2, 2]]
# print(row_select2)

'''17_NumPy数组ndarray中计算满足条件的元素的个数'''
# https://blog.csdn.net/qq_18351157/article/details/107448247
# 1. 全体ndarray中满足条件的元素数的计算
a = np.arange(12).reshape((3, 4))
# print(a)
# print(a < 4)
# print(a % 2 == 1)
# # [[False  True False  True]
# #  [False  True False  True]
# #  [False  True False  True]]
# 使用np.count_nonzero（）获得True的数量，即满足条件的元素的数量
# print(np.count_nonzero(a < 4))
# print(np.sum(a < 4))
# print(np.count_nonzero(a%2==1))
# print(np.sum(a % 2 == 1))

# # 2.计算ndarray的每一行和每一列满足条件的元素数
# print(np.count_nonzero(a < 4, axis=0))
# # [1 1 1 1]
# print(np.count_nonzero(a < 4, axis=1))
# # [4 0 0]
# print(np.count_nonzero(a % 2 == 1, axis=0))
# # [0 3 0 3]
# print(np.count_nonzero(a % 2 == 1, axis=1))
# # [2 2 2]
#
# # 3.使用numpy.any（）（全体，行/列）检查是否有满足条件的元素
# print(np.any(a < 4))
# # True
# print(np.any(a > 100))
# # False
# print(np.any(a < 4, axis=0))
# # [ True  True  True  True]
# print(np.any(a < 4, axis=1))
# # [ True False False]
#
# # 4.使用numpy.all（）检查所有元素是否都满足条件（全体，行/列）
# print(np.all(a < 4))
# # False
# print(np.all(a < 100))
# # True
# print(np.all(a < 4, axis=0))
# # [False False False False]
# print(np.all(a < 4, axis=1))
# # [ True False False]
#
# # 5.多种条件
# # 如果要组合多个条件，请将每个条件表达式括在（）中，并将其与＆或|连接。
# print((a < 4) | (a % 2 == 1))
# # [[ True  True  True  True]
# #  [False  True False  True]
# #  [False  True False  True]]
# print(np.count_nonzero((a < 4) | (a % 2 == 1)))
# # 8
# print(np.count_nonzero((a < 4) | (a % 2 == 1), axis=0))
# # [1 3 1 3]
# print(np.count_nonzero((a < 4) | (a % 2 == 1), axis=1))
# # [4 2 2]

'''18_NumPy数组ndarray中提取，删除满足条件的元素，行和列'''
# https://blog.csdn.net/qq_18351157/article/details/107628446
# 1.提取符合条件的元素
# print(a < 5)
# print(a[a < 5])
# # 返回一个新的数组ndarray，保留原来的ndarray不变。
# b = a[a < 10]
# # 计算满足条件的元素的总和（sum（），平均均值（），最大值max（），最小值min（）和标准差std（）。
# print(a[a < 5].sum())
# # 10
# print(a[a < 5].mean())
# # 2.0
# print(a[a < 5].max())
# # 4
# print(a[a < 10].min())
# # 0
# print(a[a < 10].std())
# # 2.8722813232690143

# 2.提取符合条件的行和列
# # 2.1使用numpy.all（）提取所有元素均满足条件的行和列
# print(a[np.all(a < 5, axis=1)])  # [[0 1 2 3]] 提取全部小于5的行，且即使只有一行也不会更改维数
# print(a[np.all(a < 10, axis=1),:])  # 提取全部小于10的行
# print(a[:,np.all(a < 10, axis=0)])  # 提取全部小于10的列
# # 如果不满足条件，则返回一个空的ndarray。
# print(a[:, np.all(a < 5, axis=0)])
# # []
#
# # 2.2使用numpy.any（）提取具有至少一个满足条件的元素的行/列
# print(a[:, np.any(a < 5, axis=0)])
# # [[ 0  1  2  3]
# #  [ 4  5  6  7]
# #  [ 8  9 10 11]]
# print(a[np.any(a < 5, axis=1)])
# # [[0 1 2 3]
# #  [4 5 6 7]]
#
# # 3.删除符合条件的元素，行和列
# # 3.1使用否定运算符〜
# # 如果将负运算符〜添加到条件中，则将提取不满足条件的元素，行和列。这等效于删除满足条件的元素/行/列。
# print(a[~(a < 5)])  # [ 5  6  7  8  9 10 11]
# print(a[:, np.all(a < 10, axis=0)])
# # [[0 1]
# #  [4 5]
# #  [8 9]]
# print(a[:, ~np.all(a < 10, axis=0)])
# # [[ 2  3]
# #  [ 6  7]
# #  [10 11]]
# print(a[np.any(a < 5, axis=1)])
# # [[0 1 2 3]
# #  [4 5 6 7]]
# print(a[~np.any(a < 5, axis=1)])
# # [[ 8  9 10 11]]

# 3.2使用numpy.delete（）和numpy.where（）
# np.delete（）将目标ndarray，要删除的索引（行号，列号等）以及目标轴（维）轴设置为参数。
# 在二维数组的情况下，axis = 0删除行，而axis = 1删除列
# print(np.delete(a, [0, 2], axis=0))  # 0表示行，1表示列
# [[4 5 6 7]]
# print(np.delete(a, [0, 2], axis=1))

# np.where（）返回满足条件的元素的索引。
# 对于多维数组，它是满足每个维（行，列）条件的索引（行号，列号）列表的元组。
# print(np.where(a < 2))  # (array([0, 0]), array([0, 1]))
# print(np.where(a < 2)[0])  # [0 0]
# print(np.where(a < 2)[1])  # [0 1]
# print(np.delete(a, np.where(a < 2)[0], axis=0))
# # [[ 4  5  6  7]
# #  [ 8  9 10 11]]
# print(np.delete(a, np.where(a < 2)[1], axis=1))
# # [[ 2  3]
# #  [ 6  7]
# #  [10 11]]
# print(a == 6)
# # [[False False False False]
# #  [False False  True False]
# #  [False False False False]]
# print(np.where(a == 6))
# # (array([1]), array([2]))
# print(np.delete(a, np.where(a == 6)))
# # [ 0  3  4  5  6  7  8  9 10 11]
# print(np.delete(a, np.where(a == 6)[0], axis=0))
# # [[ 0  1  2  3]
# #  [ 8  9 10 11]]
# print(np.delete(a, np.where(a == 6)[1], axis=1))
# # [[ 0  1  3]
# #  [ 4  5  7]
# #  [ 8  9 11]]

# 4.对于多种条件
# print(a[(a < 10) & (a % 2 == 1)])  # [1 3 5 7 9]
# print(a[np.any((a == 2) | (a == 10), axis=1)])
# print(a[:, ~np.any((a == 2) | (a == 10), axis=0)])

'''19_NumPy如何使用insert将元素/行/列插入/添加到数组ndarray'''
# https://blog.csdn.net/qq_18351157/article/details/107831008
# 1.numpy.insert（）
# arr：原始NumPy数组ndarray
# obj：插入值的位置，int，slice，list
# value：要插入的元素/行/列的值
# axis：插入值的轴（尺寸）

# 1.1一维数组
a = np.arange(4)  # [0 1 2 3]
# print(np.insert(a, 2, 100))  # [0 1 100 2 3]
# print(np.insert(a, 1, [100, 101, 102]))  # [  0 100 101 102   1   2   3]
# print(np.insert(a, [0, 2, 4], [100, 101, 102]))  # [100   0   1 101   2   3 102]
# 1.2替换元素
# _a = a.copy()
# _a[1] = 100
# print(_a)  # [  0 100   2   3]
# _a = a.copy()
# _a[1:3] = [100, 101]
# print(_a)  # [  0 100 101   3]
# 在替换前后更改ndarray形状的操作将导致错误。例如，如果要用多个元素替换一个元素。
# _a = a.copy()
# _a[1] = [100, 101, 102]
# print(_a)
# ValueError: setting an array element with a sequence.

# 用np.insert（）插入并用np.delete（）删除不必要的值后，可以获得所需的数组。(实现替换)
# _a = np.insert(a, 1, [100, 101, 102])
# _a = np.delete(_a, 4)
# print(_a)  # [  0 100 101 102   2   3]

# 2. 二维数组的行
# 2.1使用numpy.insert（）插入和添加行
a = np.arange(12).reshape((3, 4))
# print(a)
# print(np.insert(a, 2, 100))  # [  0   1 100   2   3   4   5   6   7   8   9  10  11]
# # 如果要将行插入二维数组ndarray中，请设置axis = 0。
# # 如果为参数值指定了标量值，则将插入用该值填充的行。
# print(np.insert(a, 2, 100, axis=0))
# # [[  0   1   2   3]
# #  [  4   5   6   7]
# #  [100 100 100 100]
# #  [  8   9  10  11]]

# 2.2 插入一维数组ndarray
# 可以插入一维数组ndarray或列表
# 指定插入位置的参数obj也可以指定为列表或数组。在这种情况下，同一行将插入到每一行中。
b1 = np.arange(100, 104)
# print(np.insert(a, 2, b1, axis=0))
# print(np.insert(a, 2, [100,101,102,103], axis=0))
# # [[  0   1   2   3]
# #  [  4   5   6   7]
# #  [100 101 102 103]
# #  [  8   9  10  11]]
# print(np.insert(a, [0, 2], b1, axis=0))
# # [[100 101 102 103]
# #  [  0   1   2   3]
# #  [  4   5   6   7]
# #  [100 101 102 103]
# #  [  8   9  10  11]]
#
# # 2.3插入二维数组ndarray
b2 = np.arange(100, 112).reshape((3, 4))
# print(b2)
# # [[100 101 102 103]
# #  [104 105 106 107]
# #  [108 109 110 111]]
# print(np.insert(a, 2, b2, axis=0))
# # [[  0   1   2   3]
# #  [  4   5   6   7]
# #  [100 101 102 103]
# #  [104 105 106 107]
# #  [108 109 110 111]
# #  [  8   9  10  11]]
# print(np.insert(a, 2, b2[2], axis=0))
# # [[  0   1   2   3]
# #  [  4   5   6   7]
# #  [108 109 110 111]
# #  [  8   9  10  11]]
# print(np.insert(a, [0, 2, 3], b2, axis=0))
# # [[100 101 102 103]
# #  [  0   1   2   3]
# #  [  4   5   6   7]
# #  [104 105 106 107]
# #  [  8   9  10  11]
# #  [108 109 110 111]]
# print(np.insert(a, range(3), b2, axis=0))
# # [[100 101 102 103]
# #  [  0   1   2   3]
# #  [104 105 106 107]
# #  [  4   5   6   7]
# #  [108 109 110 111]
# #  [  8   9  10  11]]

# 2.4在numpy.vstack（）的开头和结尾添加行
# print(np.vstack((a, b1)))
# [[  0   1   2   3]
#  [  4   5   6   7]
#  [  8   9  10  11]
#  [100 101 102 103]]
# print(np.vstack((b2, a)))
# [[100 101 102 103]
#  [104 105 106 107]
#  [108 109 110 111]
#  [  0   1   2   3]
#  [  4   5   6   7]
#  [  8   9  10  11]]
# 2.5行的置换
# 如果要替换一行且 如果所选的行数相同，则切片或列表都可以。
# _a = a.copy()
# _a[2] = b1
# print(_a)
# # [[  0   1   2   3]
# #  [  4   5   6   7]
# #  [100 101 102 103]]
# _a = a.copy()
# _a[1] = b2[1]
# print(_a)
# # [[  0   1   2   3]
# #  [104 105 106 107]
# #  [  8   9  10  11]]
# _a = a.copy()
# _a[1:] = b2[[0, 2]]
# print(_a)
# # [[  0   1   2   3]
# #  [100 101 102 103]
# #  [108 109 110 111]]

# 3.二维数组的列
# 3.1使用numpy.insert（）插入和添加列
# print(np.insert(a, 1, 100, axis=1))
c1 = np.arange(100, 103)
# # [100 101 102]
# print(np.insert(a, 1, c1, axis=1))
# print(np.insert(a, 3, c1, axis=1))

# 插入二维数组ndarray时，请注意指定插入位置的参数obj。
# 如果要将obj指定为标量值，除非指定[x]而不是x，否则会发生错误。
c2 = np.arange(100, 106).reshape((3, 2))
# print(c2)
# [[100 101]
#  [102 103]
#  [104 105]]

# print(np.insert(a, 1, c2, axis=1))
# ValueError: could not broadcast input array from shape (2,3) into shape (3,3)

# print(np.insert(a, [1], c2, axis=1))
# # [[  0 100 101   1   2   3]
# #  [  4 102 103   5   6   7]
# #  [  8 104 105   9  10  11]]
#
# print(np.insert(a, [0, 2], c2, axis=1))
# # [[100   0   1 101   2   3]
# #  [102   4   5 103   6   7]
# #  [104   8   9 105  10  11]]
#
# print(c1)
# # [100 101 102]
#
# print(np.insert(a, 1, c1, axis=1))
# # [[  0 100   1   2   3]
# #  [  4 101   5   6   7]
# #  [  8 102   9  10  11]]
#
# print(np.insert(a, [1], c1, axis=1))
# # [[  0 100 101 102   1   2   3]
# #  [  4 100 101 102   5   6   7]
# #  [  8 100 101 102   9  10  11]]
#
# print(np.insert(a, [1, 3, 4], c1, axis=1))
# # [[  0 100   1   2 101   3 102]
# #  [  4 100   5   6 101   7 102]
# #  [  8 100   9  10 101  11 102]]
#
_c1 = c1.reshape((3, 1))
# print(_c1)
# # [[100]
# #  [101]
# #  [102]]
#
# print(np.insert(a, 1, _c1, axis=1))
# # [[  0 100 101 102   1   2   3]
# #  [  4 100 101 102   5   6   7]
# #  [  8 100 101 102   9  10  11]]
#
# print(np.insert(a, [1], _c1, axis=1))
# # [[  0 100   1   2   3]
# #  [  4 101   5   6   7]
# #  [  8 102   9  10  11]]
#
# print(np.insert(a, [1, 3, 4], _c1, axis=1))
# # [[  0 100   1   2 100   3 100]
# #  [  4 101   5   6 101   7 101]
# #  [  8 102   9  10 102  11 102]]


# 3.2 在numpy.hstack（）的开头和结尾添加列
# 如果要在ndarray的开头或结尾而不是在中间添加列，则除了np.insert（）之外，还可以使用竖直连接ndarray的np.hstack（）。
# 请注意，如果原始ndarray和要添加的ndarray的尺寸不匹配，则会发生错误。即使只有一列，也必须使用reshape（）方法将其转换为二维数组。

# print(np.hstack((a, c1)))
# ValueError: all the input arrays must have same number of dimensions
# print(_c1)
# # [[100]
# #  [101]
# #  [102]]
# print(np.hstack((a, _c1)))
# # [[  0   1   2   3 100]
# #  [  4   5   6   7 101]
# #  [  8   9  10  11 102]]
# print(np.hstack((_c1, a)))
# # [[100   0   1   2   3]
# #  [101   4   5   6   7]
# #  [102   8   9  10  11]]
# print(np.hstack((a, c2)))
# # [[  0   1   2   3 100 101]
# #  [  4   5   6   7 102 103]
# #  [  8   9  10  11 104 105]]
# print(np.hstack((c2, a)))
# # [[100 101   0   1   2   3]
# #  [102 103   4   5   6   7]
# #  [104 105   8   9  10  11]]

# 3.3列的置换
# 如果选择的列数相同，则切片或列表确定。
# _a = a.copy()
# _a[:, 1] = c1
# print(_a)
# # [[  0 100   2   3]
# #  [  4 101   6   7]
# #  [  8 102  10  11]]
# _a = a.copy()
# _a[:, :2] = c2
# print(_a)
# # [[100 101   2   3]
# #  [102 103   6   7]
# #  [104 105  10  11]]
# _a = a.copy()
# _a[:, [0, 3]] = c2
# print(_a)
# # [[100   1   2 101]
# #  [102   5   6 103]
# #  [104   9  10 105]]

'''20_NumPy数组ndarray和Python标准列表相互转换'''
# https://blog.csdn.net/qq_18351157/article/details/107936965
# 1.将列表类型列表转换为NumPy数组ndarray：numpy.array（）
# l_1d = [0, 1, 2]
# arr_1d = np.array(l_1d)
# print(arr_1d)  # [0 1 2]
# print(type(arr_1d))  # <class 'numpy.ndarray'>
#
# l_2d = [[0, 1, 2], [3, 4, 5]]
# arr_2d = np.array(l_2d,dtype=float)
# print(arr_2d)
# # [[0 1 2]
# #  [3 4 5]]

# l_2d_error = [[0, 1, 2], [3, 4]]
# arr_2d_error = np.array(l_2d_error)  # ValueError: setting an array element with a sequence.

# 2.将NumPy数组ndarray转换为列表类型列表：tolist（）
# 2.1 一维
# arr_1d = np.arange(3)  # [0 1 2]
# l_1d = arr_1d.tolist()  # [0, 1, 2]
# # 2.2 二维
# arr_2d = np.arange(6).reshape((2, 3))
# # [[0 1 2]
# #  [3 4 5]]
# l_2d = arr_2d.tolist()
# # [[0, 1, 2], [3, 4, 5]]
# # 2.3 三维
# arr_3d = np.arange(24).reshape((2, 3, 4))
# l_3d = arr_3d.tolist()
# print(l_3d)  # [[[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11]], [[12, 13, 14, 15], [16, 17, 18, 19], [20, 21, 22, 23]]]
# print(l_3d[0])  # [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11]]
# print(l_3d[0][0])  # [0, 1, 2, 3]
# print(l_3d[0][0][0])  # 0

'''21_Numpy进行矩阵运算（逆矩阵，行列式，特征值等）'''
# https://blog.csdn.net/qq_18351157/article/details/108058962
# 1.创建矩阵对象：Python列表，numpy.array（），numpy.matrix()
l_2d = [[0, 1, 2], [3, 4, 5]]
arr = np.array(l_2d)
# print(type(arr))  # <class 'numpy.ndarray'>
mat = np.matrix(l_2d)  # 必须是小于等于2维，如果是1维也会转化为2维
# print(type(mat))  # <class 'numpy.matrix'>
mat_1d = np.matrix([0, 1, 2])
# print(mat_1d)  # [[0 1 2]]

# 2.获取和更改（分配）矩阵元素
# 可以使list[行号] [列号]访问Python"列表"类型二维数组的元素的值。
# print(l_2d)  # [[0, 1, 2], [3, 4, 5]]
# print(l_2d[0][1])  # 1
# l_2d[0][1] = 100
# print(l_2d)  # [[0, 100, 2], [3, 4, 5]]
# numpy.ndarray，numpy.matrix可以通过arr [行号，列号]访问。
# print(mat)
# # [[0 1 2]
# #  [3 4 5]]
# print(mat[0, 1])  # 1
# mat[0, 1] = 100
# print(mat)
# # [[  0 100   2]
# #  [  3   4   5]]

# 3.转置矩阵：.T属性
# # 3.1 "列表"的转置
l_2d = [[0, 1, 2], [3, 4, 5]]
# print(l_2d)
# # [[0, 1, 2], [3, 4, 5]]
# print([list(x) for x in zip(*l_2d)])
# *l_2d 是一个解包操作，它将 l_2d 中的元素（即子列表）作为独立的参数传递给 zip 函数。
# 因此，zip 函数接收到的参数实际上是 [0, 1, 2] 和 [3, 4, 5] 这两个列表。
# zip 函数将这两个列表作为输入，并返回一个迭代器，该迭代器中的每个元素都是一个元组，包含来自每个输入列表的对应元素。
# 在这个例子中，返回的迭代器将包含元组 (0, 3), (1, 4), (2, 5)。
# # [[0, 3], [1, 4], [2, 5]]

# # 3.2 numpy.ndarray和numpy.matrix可以使用.T获得转置矩阵。
# print(mat)
# print(mat.T)

# 4.矩阵总和与差：+运算符，-运算符
# 4.1 列表
# 在Python列表类型中，+运算符是列表串联，-并未定义操作符的操作，从而导致错误TypeError
l_2d_1 = [[0, 1, 2], [3, 4, 5]]
l_2d_2 = [[0, 2, 4], [6, 8, 10]]
# print(l_2d_1 + l_2d_2)  # [[0, 1, 2], [3, 4, 5], [0, 2, 4], [6, 8, 10]]
# print(l_2d_1 - l_2d_2)  # TypeError: unsupported operand type(s) for -: 'list' and 'list'

# 4.2 在numpy.ndarray和numpy.matrix中，每个元素都由+运算符和-运算符进行加减。
arr1 = np.arange(6).reshape((2, 3))
# print(arr1)
# # [[0 1 2]
# #  [3 4 5]]
arr2 = np.arange(0, 12, 2).reshape((2, 3))
# print(arr2)
# # [[ 0  2  4]
# #  [ 6  8 10]]
# print(arr1 + arr2)
# # [[ 0  3  6]
# #  [ 9 12 15]]
# print(arr1 - arr2)
# # [[ 0 -1 -2]
# #  [-3 -4 -5]]
mat1 = np.matrix(arr1)
mat2 = np.matrix(arr2)
# print(mat1 + mat2)
# # [[ 0  3  6]
# #  [ 9 12 15]]
# print(mat1 - mat2)
# # [[ 0 -1 -2]
# #  [-3 -4 -5]]

# 5. 标量乘法和按元素乘积：*运算符，numpy.multiply（）
# # 5.1 列表
# # 带数字的运算是重复的数组，并且由于未定义列表之间的运算而发生错误。
# print(l_2d_1 * 2)  # [[0, 1, 2], [3, 4, 5], [0, 1, 2], [3, 4, 5]]
# # print(l_2d_1 * l_2d_2)  # TypeError: can't multiply sequence by non-int of type 'list'
# # 5.2 在numpy.ndarray和numpy.matrix中，带有数字值（标量值）的*运算是每个元素的标量倍数。
# print(arr1 * 2)
# print(mat1 * 2)
# # [[ 0  2  4]
# #  [ 6  8 10]]
# # 5.2使用numpy.multiply（）获取矩阵之间的按元素乘积（Hadamard乘积）。
# print(np.multiply(arr1, arr2))
# print(np.multiply(mat1, mat2))
# # [[ 0  2  8]
# #  [18 32 50]]

# 6.矩阵乘法：numpy.dot（），numpy.matmul（），@运算符，*运算符
arr1 = np.arange(4).reshape((2, 2))
# print(arr1)
# # [[0 1]
# #  [2 3]]
arr2 = np.arange(6).reshape((2, 3))
# print(arr2)
# # [[0 1 2]
# #  [3 4 5]]
# print(np.dot(arr1, arr2))
# print(arr1.dot(arr2))
# print(np.matmul(arr1, arr2))
# print(arr1 @ arr2)
# # [[ 3  4  5]
# #  [ 9 14 19]]

# 在numpy.matrix中，*运算符还会计算矩阵乘积。
mat1 = np.matrix(arr1)
mat2 = np.matrix(arr2)
# print(np.dot(mat1, mat2))
# print(mat1.dot(mat2))
# print(np.matmul(mat1, mat2))
# print(mat1 @ mat2)
# print(mat1 * mat2)
# # [[ 3  4  5]
# #  [ 9 14 19]]

# 7. 求幂：**运算符
# numpy.ndarray对每个元素执行幂运算
arr = np.arange(1, 5).reshape(2, 2)
# print(arr)
# # [[1 2]
# #  [3 4]]
# print(arr**2)
# # [[ 1  4]
# #  [ 9 16]]
# 并且numpy.matrix重复矩阵乘法。
mat = np.matrix(arr)
# print(mat)
# # [[1 2]
# #  [3 4]]
# print(mat**2)
# # [[ 7 10]
# #  [15 22]]
# print(mat**2 == mat * mat)
# # [[ True  True]
# #  [ True  True]]
# print(mat**3 == mat * mat * mat)
# # [[ True  True]
# #  [ True  True]]

# 关于负值的幂运算，numpy.ndarray还会对每个元素执行幂运算。
# 此时，如果原始数组的数据类型dtype为int，则会发生错误。如果数据类型为预先浮动，则可以。
# print(arr**-1)
# ValueError: Integers to negative integer powers are not allowed.

arr_f = np.array(arr, dtype=float)
# print(arr_f**-1)
# # [[1.         0.5       ]
# #  [0.33333333 0.25      ]]

# numpy.matrix的**-1是逆矩阵运算。负幂是逆矩阵乘积的重复。
# print(mat**-1)
# # [[-2.   1. ]
# #  [ 1.5 -0.5]]
# print(mat**-2)
# # [[ 5.5  -2.5 ]
# #  [-3.75  1.75]]
# print(mat**-2 == mat**-1 * mat**-1)
# # [[ True  True]
# #  [ True  True]]
# print(mat**-3 == mat**-1 * mat**-1 * mat**-1)
# # [[ True  True]
# #  [ True  True]]

# 8.矢量点积：numpy.inner（）
# 使用numpy.inner（）计算向量（一维数组）的内积。返回值是标量值。
v = np.array([0, 1, 2])
# print(v)  # [0 1 2]
# print(v.shape)  # (3,)
# # 都表示内积
# print(np.dot(v, v))
# print(np.matmul(v, v))
# print(v @ v)
# print(np.inner(v, v))
# # 5
# print(type(np.inner(v, v)))  # <class 'numpy.int64'>
# 使用numpy.dot（），numpy.matmul（），@运算符计算一维数组和二维数组的乘积时，
# 如果第一个参数（左侧）是一维数组，则行向量，
# 第二个参数（右侧））是一维数组，它作为列向量计算，结果作为一维数组返回。
arr = np.arange(9).reshape(3, 3)
arr_row = np.arange(3).reshape(1, 3)
arr_col = np.arange(3).reshape(3, 1)
# print(arr)
# # [[0 1 2]
# #  [3 4 5]
# #  [6 7 8]]
# print(v @ arr)
# # [15 18 21]
# print(arr_row @ arr)
# # [[15 18 21]]
# print(arr @ v)
# # [ 5 14 23]
# print(arr @ arr_col)
# # [[ 5]
# #  [14]
# #  [23]]

# 9.逆矩阵：numpy.linalg.inv（），**-1，.I属性
# 使用numpy.linalg.inv（）计算逆矩阵。
# ndarray,matrix都能用
arr = np.array([[2, 5], [1, 3]])
arr_inv = np.linalg.inv(arr)
mat = np.matrix([[2, 5], [1, 3]])
mat_inv = np.linalg.inv(mat)
# print(mat_inv)
# [[ 3. -5.]
#  [-1.  2.]]
# 在numpy.matrix中，即使使用**-1（-1幂），也可以计算逆矩阵。
mat_inv = mat ** -1
# 还可以使用I属性获得逆矩阵。
mat_inv = mat.I
# print(mat_inv)  # 结果同上
# 在numpy.matrix中，可以使用*运算符来计算矩阵的乘积，因此，例如，您可以通过以下简单的书写来确定原始矩阵和逆矩阵的乘积是单位矩阵。
# result = mat * mat.I
# print(result)
# # [[1. 0.]
# #  [0. 1.]]
# numpy.ndarray没有I属性。
# print(arr.I)  # AttributeError: 'numpy.ndarray' object has no attribute 'I'
# 逆矩阵不存在（奇异），则numpy.linalg.inv（）将生成错误。可以使用numpy.linalg.pinv（）计算Moore-Penrose伪逆矩阵。
arr_s = np.array([[0, 0], [1, 3]])
# print(np.linalg.inv(arr_s))  # LinAlgError: Singular matrix
arr_pinv = np.linalg.pinv(arr_s)  # 伪逆矩阵
# print(arr_pinv)
# # [[0.  0.1]
# #  [0.  0.3]]
# # 奇异矩阵与其伪逆矩阵的矩阵乘积不成为单位矩阵，但是伪逆矩阵的伪逆矩阵具有与原始矩阵相等
# print(arr_s @ arr_pinv)
# # [[0. 0.]
# #  [0. 1.]]
# print(np.linalg.pinv(arr_pinv))
# # [[0. 0.]
# #  [1. 3.]]
# # 可逆的矩阵，伪逆矩阵和逆矩阵结果相同
# print(np.linalg.inv(arr))
# print(np.linalg.pinv(arr))
# # [[ 3. -5.]
# #  [-1.  2.]]

# 10. 行列式：numpy.linalg.det（）
# arr = np.array([[0, 1], [2, 3]])
# det = np.linalg.det(arr)
# print(det)  # -2.0

# 11.特征值和特征向量：numpy.linalg.eig（）
arr = np.array([[8, 1], [4, 5]])
w, v = np.linalg.eig(arr)
# print(w)
# # [9. 4.]
# print(v)
# # [[ 0.70710678 -0.24253563]
# #  [ 0.70710678  0.9701425 ]]
# print('value: ', w[0])
# print('vector: ', v[:, 0])
# # value:  9.0
# # vector: [0.70710678 0.70710678]
# # 如果要查找最大特征值，请使用numpy.argmax（），它返回最大值的索引
# print(w[np.argmax(w)])
# print(v[:, np.argmax(w)])
# # 9.0
# # [0.70710678 0.70710678]

# 11.numpy.ndarray和numpy.matrix之间的差异摘要
# 最后，我将总结numpy.ndarray和numpy.matrix之间的区别。
#
#         numpy.ndarray	         numpy.matrix
# 维度数	       任意	                  2D
# *运算符	各要素的乘积	            矩阵乘法
# **运算符	每个元素的幂	          重复矩阵乘积
# **-1	   每个元素的-1幂	            逆矩阵
# **-n	   每个元素的-n幂	         重复逆矩阵的乘积
# .I属性	       没有	                逆矩阵

'''22_NumPy检查版本（np.version）'''
# https://blog.csdn.net/qq_18351157/article/details/108391640
# print(np.__version__)

'''23_Python列表和数组以及numpy.ndarray的区别和正确使用'''
# https://blog.csdn.net/qq_18351157/article/details/109469790
# 列表 - list
# 数组 - array
# 多维数组 - numpy.ndarray

# 列表与数组和numpy.ndarray之间的区别
# 1. 列表 - list
# 内置式:无需导入即可使用
# 可以存储不同类型:也可以通过列表表示多维数组
# 尽管从狭义上讲它可能不同于数组，但列表通常足以进行简单的类似数组的处理。
# l = ['apple', 100, 0.123]
# l_2d = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
# # 提取元素
# print(l[1])  # 100
# print(l_2d[1])  # [3, 4, 5]
# print(l_2d[1][1])  # 4
# # 切片
# print(l[:2])  # ['apple', 100]
# l_num = [0, 10, 20, 30]
# # 使用内置函数max（），min（），sum（），len（）计算最大值，最小值，总计，平均值
# print(min(l_num))  # 0
# print(max(l_num))  # 30
# print(sum(l_num))  # 60
# print(sum(l_num) / len(l_num))  # 15.0
# # for语句进行循环
# l_str = ['apple', 'orange', 'banana']
# for s in l_str:
#     print(s)  # apple  # orange  # banana

# 2.数组 - array
# 导入并使用标准库的数组模块
# 只能存储相同类型
# 仅一维数组
# 可以使用与列表相同的方式来处理它，但对类型有限制。
# 与类型代码不匹配的类型的元素无法存储。
# import array
# arr_int = array.array('i', [0, 1, 2])  # 'i'应该表示的是整型的意思，'f'表示float
# print(arr_int)  # array('i', [0, 1, 2])
# arr_float = array.array('f', [0.0, 0.1, 0.2])
# print(arr_float)  # array('f', [0.0, 0.10000000149011612, 0.20000000298023224])
# # arr_int = array.array('i', [0, 0.1, 2])
# # TypeError: integer argument expected, got float
# print(arr_int[1])  # 1
# print(sum(arr_int))  # 3

# 3.多维数组 - numpy.ndarray
# 安装和使用Numpy
# 只能存储相同类型
# 可以表示多维数组
# 丰富的数值计算方法和功能，可实现高速计算
# arr = np.array([0, 1, 2])
# print(arr)  # [0 1 2]
# arr_2d = np.array([[0, 1, 2], [3, 4, 5]])
# print(arr_2d)
# # [[0 1 2]
# #  [3 4 5]]
# # 多维数组，请指定以逗号分隔的位置（索引）。也可以使用切片。
# print(arr[1])  # 1
# print(arr_2d[1, 1])  # 4
# print(arr_2d[0, 1:])  # [1 2]
# # 可以对每个元素（例如，平方根）执行操作或查找矩阵乘积。
# print(np.sqrt(arr_2d))
# # [[0.         1.         1.41421356]
# #  [1.73205081 2.         2.23606798]]
# arr_1 = np.array([[1, 2], [3, 4]])
# arr_2 = np.array([[1, 2, 3], [4, 5, 6]])
# print(np.dot(arr_1, arr_2))
# # [[ 9 12 15]
# #  [19 26 33]]

'''24_Numpy数组通过切片选择和分配子数组'''
# https://blog.csdn.net/qq_18351157/article/details/111146506
# 1.切片的基础
# l = list(range(10))
# print(l)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(l[4:8])  # [4, 5, 6, 7]
# print(l[-5:-2])  # [5, 6, 7]
# print(l[::-1])  # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

# 2.切片一维NumPy数组ndarray
# 2.1选择
a = np.arange(10)
# print(a)  # [0 1 2 3 4 5 6 7 8 9]
# print(a[4:8])  # [4 5 6 7]
# print(a[-5:-2])  # [5 6 7]
# print(a[::-1])  # [9 8 7 6 5 4 3 2 1 0]
# # 2.2代入
# a[3:6] = 100
# print(a)  # [  0   1   2 100 100 100   6   7   8   9]
# a[3:6] = [100, 200, 300]
# print(a)  # [  0   1   2 100 200 300   6   7   8   9]
# print(a[2:8:2])  # [2 4 6]
# a[2:8:2] = 100
# print(a)  # [  0   1 100   3 100   5 100   7   8   9]
# a[2:8:2] = [100, 200, 300]
# print(a)  # [  0   1 100   3 200   5 300   7   8   9]

# 3.切片多维NumPy数组ndarray
# 3.1选择
a = np.arange(12).reshape((3, 4))
# print(a[1:, 1:3])
# # [[ 5  6]
# #  [ 9 10]]
# # 3.2行的选择
# # 整个切片[：]选择一行。在这种情况下，可以省略结尾的[,:]。
# print(a[1:, :])
# # [[ 4  5  6  7]
# #  [ 8  9 10 11]]
# print(a[1:])
# # [[ 4  5  6  7]
# #  [ 8  9 10 11]]
# # 选择一行时，如果通过标量值而不是切片来指定索引，则它将成为一维数组，但是，如果在切片中选择一行，则它将成为与原始数组类似的二维数组。
# print(a[1])# [4 5 6 7]
# print(a[1].shape)# (4,)
# print(a[1:2])# [[4 5 6 7]]
# print(a[1:2].shape)# (1, 4)
# # 3.3 列的选择
# print(a[:, 1:3])
# # [[ 1  2]
# #  [ 5  6]
# #  [ 9 10]]
# # 与行一样，选择一列时，如果通过标量值而不是切片来指定索引，则它将成为一维数组，
# # 但是如果在切片中选择一列，则它将成为与原始数组类似的二维数组。
# print(a[:, 1])# [1 5 9]
# print(a[:, 1].shape)# (3,)
# print(a[:, 1:2])
# # [[1]
# #  [5]
# #  [9]]
# print(a[:, 1:2].shape)# (3, 1)
# 3.4代入
# 至于对多维NumPy数组ndarray的分配，与一维的情况一样，广播并分配右侧的值。
# 分配数组时，请注意，如果要分配的数组中的元素数量与切片选择的区域中的对应元素数量不匹配，则会发生错误ValueError。
a = np.arange(12).reshape((3, 4))
# print(a)
# # [[ 0  1  2  3]
# #  [ 4  5  6  7]
# #  [ 8  9 10 11]]
# print(a[1:, 1:3])
# # [[ 5  6]
# #  [ 9 10]]
# a[1:, 1:3] = 100
# print(a)
# # [[  0   1   2   3]
# #  [  4 100 100   7]
# #  [  8 100 100  11]]
# a[1:, 1:3] = [100, 200]
# print(a)
# # [[  0   1   2   3]
# #  [  4 100 200   7]
# #  [  8 100 200  11]]
# a[1:, 1:3] = [[100, 200], [300, 400]]
# print(a)
# # [[  0   1   2   3]
# #  [  4 100 200   7]
# #  [  8 300 400  11]]
# a = np.arange(12).reshape((3, 4))
# print(a)
# # [[ 0  1  2  3]
# #  [ 4  5  6  7]
# #  [ 8  9 10 11]]
# print(a[1:, ::2])
# # [[ 4  6]
# #  [ 8 10]]
# a[1:, ::2] = 100
# print(a)
# # [[  0   1   2   3]
# #  [100   5 100   7]
# #  [100   9 100  11]]
# a[1:, ::2] = [100, 200]
# print(a)
# # [[  0   1   2   3]
# #  [100   5 200   7]
# #  [100   9 200  11]]
# a[1:, ::2] = [[100, 200], [300, 400]]
# print(a)
# # [[  0   1   2   3]
# #  [100   5 200   7]
# #  [300   9 400  11]]

# 4.查看（参考）并复制
# 通过切片提取的子数组是原始数组的视图（参考），并且更改子数组的元素也会更改原始数组的元素。
a = np.arange(12).reshape((3, 4))
# print(a)
# # [[ 0  1  2  3]
# #  [ 4  5  6  7]
# #  [ 8  9 10 11]]
# a_slice = a[1:, 1:3]
# print(a_slice)
# # [[ 5  6]
# #  [ 9 10]]
# a_slice[0, 0] = 100
# print(a_slice)
# # [[100   6]
# #  [  9  10]]
# print(a)
# # [[  0   1   2   3]
# #  [  4 100   6   7]
# #  [  8   9  10  11]]
# 如果要复制通过切片提取的部分数组，请使用copy（）方法。更改副本的元素不会更改原始数组的元素。
a = np.arange(12).reshape((3, 4))
# print(a)
# # [[ 0  1  2  3]
# #  [ 4  5  6  7]
# #  [ 8  9 10 11]]
# a_slice_copy = a[1:, 1:3].copy()
# print(a_slice_copy)
# # [[ 5  6]
# #  [ 9 10]]
# a_slice_copy[0, 0] = 100
# print(a_slice_copy)
# # [[100   6]
# #  [  9  10]]
# print(a)
# # [[ 0  1  2  3]
# #  [ 4  5  6  7]
# #  [ 8  9 10 11]]

# 5.与花式索引组合（按列表选择）
# NumPy具有一种称为花式索引的机制，该机制通过索引列表从numpy.ndarray中选择一个子数组。
# 通过将其与切片组合，可以选择并获取部分阵列。
a = np.arange(12).reshape((3, 4))
# print(a)
# # [[ 0  1  2  3]
# #  [ 4  5  6  7]
# #  [ 8  9 10 11]]
# print(a[[0, 2], 1:3])
# # [[ 1  2]
# #  [ 9 10]]
# a[[0, 2], 1:3] = 100
# print(a)
# # [[  0 100 100   3]
# #  [  4   5   6   7]
# #  [  8 100 100  11]]
# a[[0, 2], 1:3] = [100, 200]
# print(a)
# # [[  0 100 200   3]
# #  [  4   5   6   7]
# #  [  8 100 200  11]]
# a[[0, 2], 1:3] = [[100, 200], [300, 400]]
# print(a)
# # [[  0 100 200   3]
# #  [  4   5   6   7]
# #  [  8 300 400  11]]
#
# 通过花式索引提取的部分数组是副本，而不是视图。
# a_subset = a[[0, 2], 1:3]
# print(a_subset)
# # [[100 200]
# #  [300 400]]
# a_subset[0, 0] = -1
# print(a_subset)
# # [[ -1 200]
# #  [300 400]]
# print(a)
# # [[  0 100 200   3]
# #  [  4   5   6   7]
# #  [  8 300 400  11]]


