# -*- coding: UTF-8 -*-
import pandas as pd
import datetime
import numpy as np
import warnings

warnings.filterwarnings('ignore')
data = {
    '姓名': ['张三', '李四', '王五', '赵六'],
    '年龄': [28, 34, 29, 32],
    '生日': [datetime.date(1994, 3, 15), datetime.date(1988, 9, 20), datetime.date(1993, 4, 1),
             datetime.date(1990, 8, 18)],
    '身高': [175.5, 180.2, 168.0, 172.3],
    '体重': [70.0, 80.5, 65.0, 72.0]
}
df = pd.DataFrame(data)
df['生日'] = pd.to_datetime(df['生日'])

# df.set_index(['姓名', '年龄'], inplace=True, drop=True, append=False)
# 设置索引，可以设置多个，
# inplace表示是否在原数据修改，drop表示姓名和年龄作为索引后需要丢弃吗？默认True
# append表示是否以追加的方式进行（保留原来的索引，默认的有0，1，2，3），默认False

# df.reset_index(['姓名'], drop =False ,inplace=True)
# 删除索引，只能在已有索引上进行删除
# drop表示丢弃后的索引还要作为数据保存吗？默认False保存
# level表示丢弃的索引名字，默认全丢
# print(df)


# ********************************************************************
# numpy.random.randint()
# 1, 4,(20,20):1-3, 20 行 20 列
# np.random.seed(0)
# arr = np.random.randint(1, 5, (3, 2))
# print(arr)

'''
高维索引
创建方法1：MultiIndex
'''
# 定义行索引
# 上下半年 和 AB组
years = pd.MultiIndex.from_product([['上半年', '下半年'], ['A组', 'B组']])

# 定义列索引
# 一二区 和 苹果/橘子销量
columns = pd.MultiIndex.from_product([['一区', '二区'], ['苹果', '橘子']])

# 生成随机数据
# 这里我们假设每个组在每个时间段，每个区域的每种水果的销量都是随机生成的
# 数据范围从0到1000
data = np.random.randint(0, 1001, size=(len(years), len(columns)))

# 创建DataFrame
df = pd.DataFrame(data, index=years, columns=columns)
#
# # 打印DataFrame查看结果
# print(df)
'''方法二：set_index'''
# 创建一个DataFrame
# data = {'时间': ['上半年', '上半年', '下半年', '下半年'],
#         '组别': ['A组', 'B组', 'A组', 'B组'],
#         '销量': [100, 200, 150, 250]}
# df = pd.DataFrame(data)
#
# # 将'时间'和'组别'列设置为索引
# df.set_index(['时间', '组别'], inplace=True)

# 现在df的索引就是一个多级索引了
# print(df)


'''获取高维索引的值'''
# print(df.loc[('上半年'),:])
# print()
# print(df.loc[('上半年','A组'),:])
# print()
# print(df.loc[('上半年'),('二区','橘子')])
# print()
# print(df.loc[('上半年','A组'),('二区','橘子')])

'''交换索引'''
# df.swaplevel(索引层级，索引层级，axis) axis=0 行索引
# df = df.swaplevel(0,1)  # 默认对最后2个索引进行交换，一般也就2层，所以0，1可省略
# print(df)

'''索引排序'''
# df.sort_index(level,axis) 指定按照哪一层索引（根据索引名字的顺序）进行排序，默认最外层，level=0,axis = 0行，1列
# df = df.sort_index(level=1,axis=1)
# print(df)

'''索引堆叠'''
# df.stack(level) 可以理解为将指定层级的列转换为行 level 默认-1
# 对比
# print(df,)
# df = df.stack()
# print(df)

'''取消索引堆叠'''
# df.unstack(level) 可以理解为将指定层级的行转换为列 level 默认-1
# df = df.unstack()
# print(df)

'''获取主键索引'''
# df.xs(key,level,axis) 0行1列
# print(df)
# # df = df.xs("苹果",level=1,axis=1)  # 获取苹果一二区的数据
# df = df.xs("B组",level=1,axis=0)  # 获取B组上下半年数据
# print(df)

'''获取某一级别的索引值'''
# df.index.get_level_values(level) level:索引层级  返回列索引都是什么
# df = df.index.get_level_values(1)
# print(df)

# ****************************************************************************************
'''分组和聚合'''
# df.groupby(by,level,axis)
# by:分组标准key，可以是单独列名，也可以是索引列名
# level:如果是索引列名，应根据level分组，默认level = 0 最高维
# axis:默认按照行分组
dic = {'a': [1, 1, 1, 2, 2, 2],
       'b': [2, 5, 2, 10, 5, 5],
       'c': [3, 6, 6, 9, 9, 8]
       }
data = pd.DataFrame(dic)
'''按照a分组'''
# data1 = data.groupby('a')
'''按照a,b分组'''
# data2 = data.groupby(['a', 'b'])
# print(data)
'''迭代输出分组对象'''
# 按照a分组，a = 1时，有三个数据，a = 2 时，有另外三个数据
# for i,groupdata in data1:
#     print(i)
#     print(groupdata)
# 按照a，b分组，a = 1, b = 2时 有2个数据，a = 1,b=5时，a = 2, b=5时
# for i, groupdata in data2:
#     print(i)
#     print(groupdata)

'''高维索引按二级索引（level=1）分组情况展示'''
# print(df)
# df = df.groupby(level=1)
# for i,group in df:
#     print(i)
#     print(group)

'''分组函数的属性和函数'''

# 1.df.groupby().groups  返回分组情况(以字典类型数据表示)，key值为b可能取到的值，value为对应行数
# data1 = data.groupby('b').groups
# print(data1)

# 2.data1 = data.groupby('b').get_group(2)
# #按照b进行分组了，get_group(key):key中只能输入b中的取值（2，5，10）返回b=key的所有结果
# data1 = data.groupby('b').get_group(2)
# print(data1)

# groupby().get_group()使用举例
# data = {
#     'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
#     'department': ['HR', 'IT', 'IT', 'HR', 'Finance'],
#     'salary': [50000, 60000, 65000, 55000, 70000]
# }
# df = pd.DataFrame(data)
# # 按照部门分组
# grouped = df.groupby('department')
# # 获取 IT 部门的所有员工信息
# it_department = grouped.get_group('IT')
# print(it_department)

# 3.data1 = data.groupby('b').first()/last() 返回分组后每组的第一/最后一条数据
# data1 = data.groupby('b').first()
# print(data1)

# 4.data1 = data.groupby('b').size() 统计分组后，每组数据的个数,例如b=2时有2个，b=5时有3个，b=10时有1个
# data1 = data.groupby('b').size()
# print(data1)

# 5.data1 = data.groupby('b').nunique()
# 统计分组后，每组指定列(或各列)唯一值(不重复元素)的数量
# 例如当b = 5 时,a取1或2或2,c取6或9或9,因此是2和2
# print(data)
# data1 = data.groupby('b').nunique()
# print(data1)

# 6.data1 = data.groupby('b').value_counts()  先以b进行分组,然后每组的计数
# print(data)
# data1 = data.groupby('b').value_counts()
# print(data1)

# 举例:计算每个部门中不同名字的出现次数。
# data = {
#     'name': ['Alice', 'Bob', 'Charlie', 'Alice', 'David', 'Eve', 'Bob'],
#     'department': ['HR', 'IT', 'IT', 'HR', 'Finance', 'Finance', 'IT'],
#     'salary': [50000, 60000, 65000, 50000, 70000, 75000, 62000]
# }
# # 创建 DataFrame
# df = pd.DataFrame(data)
# # 按照部门分组，然后对每个部门中的名字进行计数
# name_counts_by_department = df.groupby('department')['name'].value_counts()
# print(name_counts_by_department)
# # 注意：上面的操作返回的是一个 Series，其索引是元组，包含部门和名字
# # 如果需要更清晰的格式，可以将其重置索引或转换为 DataFrame
# name_counts_by_department_df = name_counts_by_department.reset_index(name='count')
# name_counts_by_department_df.columns = ['department', 'name', 'count']
# print(name_counts_by_department_df)

'''高维索引下分组操作(不明白)'''
# import pandas as pd
# import numpy as np
#
# # 创建MultiIndex的索引和列
# years = pd.MultiIndex.from_product([['上半年', '下半年'], ['A组', 'B组']])
# columns = pd.MultiIndex.from_product([['一区', '二区'], ['苹果', '橘子']])
# data = np.random.randint(0, 1001, size=(len(years), len(columns)))
# df = pd.DataFrame(data, index=years, columns=columns)
#
# # 选择“一区”下的“苹果”列
# apple_sales_in_area1 = df[('一区', '苹果')]
#
# # 现在apple_sales_in_area1是一个Series，其索引是MultiIndex（由年份和组别组成）
# # 我们可以直接对这个Series进行分组求和
# grouped_apple_sales = apple_sales_in_area1.groupby(level=[0, 1]).sum()  # level=[0, 1]分别代表年份和组别
#
# # 如果想要得到DataFrame格式的结果
# grouped_apple_sales_df = grouped_apple_sales.reset_index()
# print(grouped_apple_sales_df)

'''聚合'''
# 1.sum()  先分组,再聚合
# data1 = data.groupby('a')
# for i,group in data1:
#     print(i)
#     print(group)
# print(data1.sum())
# 单独取某列 print(data1.sum()['b']) 或 print(data1.c.sum())   <-(推荐第二种)

'''分组滚动聚合'''
# 2.groupby().transform() 分组后将其他变量进行统计,可以求max, min, mean
# d1 = {'id':[1,2,3,4,5],
#       'age':[18,19,18,19,17],
#       'score':[78,89,93,59,99]}
# data1 = pd.DataFrame(d1)
# data1 = data1.groupby('age').transform('max')
# print(data1)

# print(data.groupby("a").transform('mean'))

# 3.groupby().apply(函数/lambda表达式)
# print(data)
# data = data.groupby("a").apply(lambda x: x - x.mean())
# print(data)

# 4.groupby().agg/aggregate(函数)
# 实现多个聚合操作,可以输入:
# ①函数名: 例:'mean'
# ②聚合函数对象: 例:np.mean
# ③多个函数对象: 例:[np.mean, np.max, np.min, np.median]
# ④字典:针对不同列实现不同的聚合方式 例:{'b':np.max, 'c':np.min}
# 举例:
print(data)
data = data.groupby("a").agg({'b':np.max, 'c':np.min})
print(data)
