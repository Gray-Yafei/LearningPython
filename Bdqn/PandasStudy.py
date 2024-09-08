# -*- coding: utf-8 -*-
# @Time : 2024/8/23 17:11
# @Author : Gray
# https://blog.csdn.net/qq_44921056/article/details/115419404
import pandas as pd
import numpy as np

'''一、series'''
# 1、创建一个series数据（默认索引值）
# s1 = pd.Series([1,3,14,521])
# print(s1)

# 2、创建一个series数据（自定义默认值）
# s2 = pd.Series([1,3,14,521],index=['a','b','c','d'])
# print(s2)

# 3、获取series的数据值
# s3 = pd.Series([1,3,14,521])
# print(s3.values)
# print('-------分割线-------')
# print(s3[:3])

# 4、用字典来构建一个series数据
# dict = {'语文':95,
#         '数学':100,
#         '英语':88,
#         '政治':99
#         }
# s4 = pd.Series(dict)
# print(s4)

'''二、DataFrame'''
# 1、创建一个DataFrame数据
# ①使用pandas.DataFrame函数
# data = {
#     'class':[1,2,3,4],
#     'people':[10,11,32,15]
# }
# df = pd.DataFrame(data)
# print(df)

# ②：利用np.arange()函数，用法可参考np.arange()用法
# df = pd.DataFrame(np.arange(12).reshape(3, 4))
# print(df)

# 2、自定义行和列的值
df = pd.DataFrame(np.arange(8).reshape(2, 4), index=['a', 'b'], columns=['A', 'B', 'C', 'D'])
# print(df)

# 3、获取值、行索引、列索引、转置
# 使用values、index、columns、axes、T
# print(df.values)
# print(df.index)
# print(df.columns)
# print(df.axes)
# print(df.T)

# 4、获取统计变量
# 使用pandas.describe()函数
# print(df.describe())

# 5、根据行、列、值进行排序
# 使用sort_index()、sort_values()
# np.random.seed(0)
# df = pd.DataFrame(np.random.randint(1, 100,size=(2,4)), index=['a', 'b'], columns=['A', 'C', 'B', 'D'])

# df = df.sort_index(ascending=True, axis=1)

# df.loc['a','C'] = 10
# df = df.sort_values(['C','B'], ascending=True)
# print(df)

'''三、pandas选择数据'''
datas = pd.date_range('1/1/2000', periods=4)
np.random.seed(0)
data = pd.DataFrame(np.random.randint(1, 100, size=(4, 5)), index=datas, columns=['A', 'B', 'C', 'D', 'E'])
# print(data)

# 1、获取一列的series数据和行数据
# print(data['B'])
# print(data[0:2])

# 2、通过标签获取数据
# # 使用loc
# print(data.loc[['20000101', '2000-01-02', '2000-01-04'], ['A', 'C']])
# print(data.loc['20000103'])
# # 全行不全列
# print(data.loc[:, ['A','D']])
# # 全列不全行
# print(data.loc[['20000103','20000102'], :])

# 3、通过位置获取数据
# 使用iloc
# print(data.iloc[3])
# print(data.iloc[1:3,2:5])
# print(data.iloc[[1,3],[2,4,1]])

# 4、对某一列的数据进行判断
# print(data.iloc[2])
# print(data.iloc[2]>80)

'''四、pandas赋值及操作'''
# 1、替换原有值
dates = pd.date_range('20210301', periods=6)
df1 = pd.DataFrame(np.arange(24).reshape((6, 4)), index=dates, columns=['A', 'B', 'C', 'D'])
# df1.iloc[1,2] = 100
# df1.loc['20210304','B'] = 200
# df1[df1['D']>10] = 300  # df1['D']>10的作用是找到D列数据大于10的所有行数据
# df1.loc[df1['A'] == 4,'A'] = 400 # 只修改A列的值，不影响其他列的值
# print(df1)

# 2、插入行、列
# ①通过series数据的形式插入
# df1['F'] = pd.Series(['1', '2', '3', '4', '5','6'], index=dates)  # 不加index=dates，F列为Nan
# print(df1)

# ②通过append函数插入（行操作）

# s = pd.Series([1, 2, 3, 4], index=['A', 'B', 'C', 'D'])
# s.name = '2021-03-07'
# s = pd.DataFrame([s],columns=['A', 'B', 'C', 'D'])
# df1 = pd.concat([df1, s],axis=0)
# print(df1)

# ③通过insert函数插入（列操作）
# df1.insert(2, 'E', [7, 7, 7, 7, 7, 7])  # 在第二列的右边插入一个新的E列
# print(df1)

# 3、删除行、列
# ①删除行
# df2 = df1.drop('20210302', axis=0)
# print(df2)

# ②删除列
# df3 = df1.drop('B', axis=1)
# print(df3)

'''五、pandas对于空数据的处理'''
dates = pd.date_range('20210301', periods=6)
df1 = pd.DataFrame(np.arange(24).reshape(6,4), index=dates, columns=['A', 'B', 'C', 'D'])
df2 = pd.DataFrame(df1,index=dates, columns=['A', 'B', 'C', 'D','E','F'])
s1 = pd.Series([3,4,6,7],index=dates[:4])
s2 = pd.Series([32,5,2,1],index=dates[2:])
df2['E'] = s1
df2['F'] = s2
# print(df2)
#              A   B   C   D    E     F
# 2021-03-01   0   1   2   3  3.0   NaN
# 2021-03-02   4   5   6   7  4.0   NaN
# 2021-03-03   8   9  10  11  6.0  32.0
# 2021-03-04  12  13  14  15  7.0   5.0
# 2021-03-05  16  17  18  19  NaN   2.0
# 2021-03-06  20  21  22  23  NaN   1.0

# 1、删除空值所在的行或者列
# 使用dropna函数
# axis中的0代表行，1代表列。how中的any表示，含有空值即删除 ，all代表全部为空值才删除
# print(df2.dropna(axis=1, how='any'))

# 2、对空值进行赋值
# 使用fillna函数
# 对空值进行赋值，此处赋值为100
# print(df2.fillna(100))

# 3、判断数据是否为空值
# 使用isnull函数，空值返回True，非空值返回Flase
# print(df2.isnull())  # 如果求和的话，会按列求和

'''七、pandas合并'''
# 1、横向拼接、纵向拼接
# 新建三个dataframe数据
# import pandas as pd
# import numpy as np
# df1 = pd.DataFrame(np.arange(12).reshape((3,4)),columns=['a','b','c','d'])
# df2 = pd.DataFrame(np.arange(12,24).reshape((3,4)),columns=['a','b','c','d'])
# df3 = pd.DataFrame(np.arange(24,36).reshape((3,4)),columns=['a','b','c','d'])
# df = pd.concat([df1,df2,df3],axis=0).reset_index(drop=False)  # ignore_index=True的作用是不考虑表原来的index
# print(df)

# 2、获取两个表的交集和并集
# join参数的属性，如果为’inner’得到的是两表的交集，如果是outer，得到的是两表的并集。
# df1 = pd.DataFrame(np.arange(12).reshape((3, 4)), columns=['a', 'b', 'c', 'f'])
# df2 = pd.DataFrame(np.arange(12, 24).reshape((3, 4)), columns=['a', 'c', 'd', 'e'])
#
# df3 = pd.concat([df1,df2],join='outer',ignore_index=True)
# print(df3)
# df4 = pd.concat([df1,df2],join='inner',ignore_index=True)
# print(df4)

'''八、pandas合并——merge'''

left = pd.DataFrame({'key1':['K0','K0','K1','K2'],
                     'key2':['K0','K1','K0','K1'],
                     'A':['A0','A1','A2','A3'],
                     'B':['B0','B1','B2','B3']})

right = pd.DataFrame({'key1':['K0','K1','K1','K3'],
                      'key2':['K0','K0','K0','K0'],
                     'C':['C0','C1','C2','C3'],
                     'D':['D0','D1','D2','D3']})
# res_1 = pd.merge(left,right,on=['key1','key2'],how='inner')
# res_2 = pd.merge(left,right,on=['key1','key2'],how='outer')
# res_3 = pd.merge(left,right,on=['key1','key2'],how='left')
# res_4 = pd.merge(left,right,on=['key1','key2'],how='right')
# print('-------------------------how的参数取inner的结果--------------------')
# print(res_1)
# print('-------------------------how的参数取outer的结果--------------------')
# print(res_2)
# print('-------------------------how的参数取left的结果---------------------')
# print(res_3)
# print('-------------------------how的参数取right的结果--------------------')
# print(res_4)
# k1 和 k2看作是索引

# 加入indicator参数可以查看merge的详细信息
# res = pd.merge(left,right,on=['key1','key2'],how='outer',indicator=True)
# print(res)

# 以index为链接键需要同时设置left_index= True 和 right_index= True
# res = pd.merge(left,right,left_index=True,right_index=True,how='outer')
# print(res)

# sort对链接的键值进行排序：
# res = pd.merge(left,right,on=['key1','key2'],how='outer',sort=True)
# print(res)

'''九、pandas plot 画图函数'''

# import numpy as np
# import matplotlib.pyplot as plt
# data = pd.DataFrame(np.random.randn(1000,4),index=np.arange(1000),columns=['A','B','C','D'])
# data = data.cumsum()  # 累计求和
# print(data.head())
# data.plot()
# plt.show()
