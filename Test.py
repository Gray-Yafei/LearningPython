# -*- coding: UTF-8 -*-
import pandas as pd
import numpy as np
# s1 = pd.Series([1, 2, 3, 4, 5], index=["第一", '第二', "第三", '第四', "第五"])
# print(s1[:3])

# d = {"数学":130,
#      "语文":120,
#      "英语":102,}
#
# s2 = pd.Series(d)
# print(s2)

# data = {
#     'class':[1,2,3,4,5],
#     'people':[15,16,17,18,19],
# }
#
# s3 = pd.DataFrame(data)
# print(s3)

import pandas as pd

# s1 = pd.Series([98,69,73,88,100,99,None],index=['a','b','c','d','e','f','g'])
# s2 = pd.Series([71,94,99,92,76,89],index=['g','b','c','d','e','f'])
# # print(s1.index,s1.size)
# # print((s1+s2)/2)
# # print(s1.loc[['a','c']])
# # print(s1.iloc[[0,2]])
# # print(s1[s1>95])
# # print(s2[s2>95])
# #
# # print(s1[s1>s2])
# # s1.sort_values(inplace=True)
# # print(s1.iloc[:3])
# #
# # s2.sort_values(inplace=True)
# # print(s2.iloc[:3])
# print(s1[s1.notnull()].sum())
# print(s1[s1.notnull()].mean())
# print(s1[s1.notnull()].median())
# print(s1[s1.notnull()].max())

# 创建一个Series
# s = pd.Series(['apple', 'banana', 'cherry', 'date'])

# 替换多个值
# # 将'banana'替换为'banana_replaced'，将'cherry'替换为'cherry_replaced'
# result = s.str.replace('a','bbb')  # 模糊匹配
# # result = s.replace('apple','bbb')  # 精准匹配
# result_count = s.str.count('a')  # 结果：1，3，0，1
# result_contains = s.str.contains('a')  # True True False True
# result_split = s.str.split('a')  # 一维列表
# result_split = s.str.split('a',expand=True)  # 二维
#
# print(result)

# high = pd.Series(['188cm','180cm','178cm','189cm','191cm','180cm',np.nan])
# print(high.notnull().sum())
# result_replace = high.str.replace('cm','')
# print(result_replace)
# result_contains_notnull = high[high.notnull()]
# result_contains_notnull_180 = result_contains_notnull.str.contains('180')
# print(sum(result_contains_notnull_180))

# result_replace = high.str.replace('cm','')
# result_replace_notnull_T = result_replace.notnull()
# result_replace_notnull = result_replace[result_replace_notnull_T]
# s_float = pd.to_numeric(result_replace_notnull, errors='coerce')
# print(s_float[s_float>185])
# result = result_replace_notnull.astype(int)
# print(result)
# 创建DataFrame方式1：
# d = [[1,2,3,4],[4,5,6],[7,8,9]]
# data = pd.DataFrame(d, columns=['A', 'B', 'C','D'],index=['A','B','C'])
# print(data)
# 创建DataFrame方式2：
# d = {'name': ['yafei', 'yuxin'],
#      'age': [25, 18],
#      'gender': ['male', 'female'],
#      }
# df = pd.DataFrame(d)

# 创建DataFrame方式3：
# s = pd.Series([1, 2, 3, 4], name='A')
# s1 = pd.Series([1, 2, 3, 4])
# df1 = s1.to_frame()
# # 将Series转换为DataFrame
# df = s.to_frame()
# df = s.to_frame(name='B')
#
# print(df)
# pandas读取
# data = pd.read_csv('C:/Users/81087/Desktop/text.csv')
# data.index = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L']
# d = {'91': [1, 1],
#      '23': [2, 2],
#      '89': [3, 3],
#      '17': [4, 4],
#      "97": [5, 5],
#      '49': [6, 6]}
# data1 = pd.DataFrame(d)
# # print(data1)
# dp = pd.concat([data, data1], axis=0)
# # print(dp)
# dp.drop(['I', 'K'], inplace=True)
# dp.columns = ['Q','W','E','R','T','Y']
# # print(dp['T']<50)
# dp.loc[dp['T']<50,'T'] = 1
# print(dp)
# print(df.sample(1))

# print(df)
# df['age'] = df['age'].astype(float)
# print(df.dtypes)
# df.index = ['1','2']
# df.rename(index={0: "第一个", 1: "第二个"},inplace=True)
# print(df)
# print(df['age'].shape)
# print(data)
# data.columns = range(len(data.columns))
# data_float = data.astype(float)
# print(data_float)
# print((data_float+0.516).round(2))
# print(data.sort_values(ascending=False,by=2,axis=1))

# l = [1,2,3,4,5,6,5,4,3,7,9,2,2]
# s = pd.Series(l)
# print(s.unique())
# print(s.nunique())
# print(s.value_counts())

# data.columns = ['A','B','C','D','E','F']
# print(data)
# print(data.query('A > 10 & B < 80'))
# d = {
#     'age': [18, 19, 21, 121, np.nan, 19, 5, 5, -3],
#     'gender': ['F', 'M', 'F', 'X', 'F', None, 'F', 'F', 'M'],
#     'score': [78, -89, 93, np.nan, 64, np.nan, 23, 23, 79]
# }
# data = pd.DataFrame(d)
# age = [18,19,21,121,np.nan,19,5,5,-3]
# gender = ['F','M','F','X','F','','F','F','M']
# score = [78,-89,93,np.nan,64,np.nan,23,23,79]
# s = pd.Series(score)
# print(s.isnull())

# print(data.dropna(how='any',subset=['score']))
# print(data)

# print(data.ffill())
# data.fillna(value={'age': 18, 'gender': 'X', 'score': data['score'].max()}, inplace=True)
# print(data)
# query_str = "score >= 0"
# filtered_df = data.query(query_str)
# print(filtered_df)
# da = data.drop_duplicates(keep = False)
# print(da)

# df = data.replace([18,19,21],[78,79,80])
#
# print(df)

# df = pd.DataFrame({
#     'A': [1, 2, 3, 4],
#     'B': [5, 6, 7, 8]
# })
#
#
# df['A^2'] = df['A'].apply(lambda x: x**2)
# print(df)
# df['A+B'] = df.apply(lambda row: row.sum(), axis=1)
# df['A_gt_2'] = df['A'].apply(lambda x: x > 2)
# def custom_func(row):
#     # 假设我们想要根据列'A'和'B'的值来生成一个新的值
#     return row['A'] * row['B']
# # 对每一行应用自定义函数
# df['A_times_B'] = df.apply(custom_func, axis=1)
# print(df)
# def func(x):
#     if x > 3:
#         return x*10
#     else:
#         return x/10
# lst = [1,2,3,4,5,6]
# df = pd.Series(lst)
# s_custom = df.apply(func)
# print(df)
# print(s_custom )
#
# df = pd.DataFrame({
#     'A': [1, 2, 3, 4],
#     'B': [5, 6, 7, 8]
# })
#
# def func1(x):
#     return x.loc['A']+x.loc['B']
#
#
# # df = df.apply(lambda x: x.astype(object))
# df.loc[len(df.index)] = df.apply(lambda x:x.dtype)
# print(df)

# s = pd.Series([1, 2, 3, 4, 5])
# s = s.map(pd.Series([0,10,20,30,40],index=[1,2,5,3,4]))
# print(s)

# s = pd.Series([1, 2, 3, 4, 5])
# s = pd.cut(s, [1,2,3,4.5], labels=['a', 'b', 'c'])
# 只包含区间[1,2,3,4.5]内小于1和大于4.5未NaN
# print(s)

# s = pd.Series([1, 2, 3, 4, 5])
# s = pd.qcut(s, q=5, labels=False)
# # 分组，返回分组后的标签
# print(s)

#
# df = pd.DataFrame({
#     'A': [1, 2, 3, 4],
#     'B': [5, 6, 7, 8]
# })
# print(df.rolling(3, center=True).mean())
df = pd.DataFrame(np.arange(30).reshape(6, 5),columns=['A','B','C','D','E'])


data4 = df.loc[ 1:3, "B":"D"]
print(data4)
