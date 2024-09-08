# -*- coding: utf-8 -*-
# @Time : 2024/9/3 14:36
# @Author : Gray
import pandas as pd
import numpy as np

'''06_Pandas中map(),applymap(),apply()函数的使用方法'''
# https://blog.csdn.net/qq_18351157/article/details/105185224
df = pd.read_csv('C:/Users/81087/Desktop/data/DataFrameTest1.csv')
# 1.指定pandas对象作为NumPy函数的参数
# 1.1元素的应用
# NumPy的通用函数适用于pandas对象的每个元素。
# print(np.sqrt(df))
# print(np.abs(df))
# print(np.log(df))  # 以e为底

# 1.2行/列的应用
# 如果将pandas对象指定为从NumPy数组的所有元素计算值的函数的参数，则默认情况下它将应用于pandas对象的每列。
# 如果参数轴= 1，则将其应用于每行。最大值（max（）），最小值（min（）），平均值（mean（））等。
# print(np.max(df,axis = 0))
# # a    31
# # b    32
# # c    33
# # d    34
# # dtype: int64
#
# print(np.mean(df, axis=1))
# # 0    12.5
# # 1    22.5
# # 2    32.5
# # dtype: float64

# 1.3pandas.DataFrame，pandas.Series方法
# print(df.max())
# # a    31
# # b    32
# # c    33
# # d    34
# # dtype: int64
#
# print(df.max(axis=1))
# # 0    14
# # 1    24
# # 2    34
# # dtype: int64

# 2.Pandas对象方法的函数应用
# 可以使用pandas对象方法将函数应用于元素，行和列。
# 2.1适用于Series的每个元素：map（），apply（）,2个函数功能一样
s = df['a']
# print(s)
# # 0    11
# # 1    21
# # 2    31
# # Name: a, dtype: int64
#
# f_brackets = lambda x: '[{}]'.format(x)
# print(s.map(f_brackets))
#
#
# # 0    [11]
# # 1    [21]
# # 2    [31]
# # Name: a, dtype: object
#
# def f_str(x):
#     return str(x).replace('1', 'One').replace('2', 'Two').replace('3', 'Three').replace('4', 'Four')
#
#
# print(s.map(f_str))
# # 0      OneOne
# # 1      TwoOne
# # 2    ThreeOne
# # Name: a, dtype: object

# 2.2应用于DataFrame的每个元素：applymap（）
# 将Python的内置函数，匿名函数（lambda）或def定义的函数传递为applymap（）的参数。
# f_oddeven = lambda x: 'odd' if x % 2 == 1 else 'even'
# print(df.applymap(f_oddeven))
# #      a     b    c     d
# # 0  odd  even  odd  even
# # 1  odd  even  odd  even
# # 2  odd  even  odd  even

# 2.3应用于DataFrame的每行和每列：apply（）
# 将适用于一维数组的函数传递给apply（）的参数。默认情况下，它应用于每列，如果axis = 1，则应用于每行。
# f_maxmin = lambda x: max(x) - min(x)
# print(df.apply(f_maxmin))
# # a    20
# # b    20
# # c    20
# # d    20
# # dtype: int64
#
# print(df.apply(f_maxmin, axis=1))
# # 0    3
# # 1    3
# # 2    3
# # dtype: int64

# 2.4应用于DataFrame的特定行/列元素
# 由于没有方法仅将功能应用于DataFrame的特定行/列元素，可执行以下方法。
# 选择行/列并应用带有map（）或apply（）的功能
# 覆盖原始行/列
# df['b'] = df['b'].map(f_str)
# print(df)
# #     a         b   c   d
# # 0  11    OneTwo  13  14
# # 1  21    TwoTwo  23  24
# # 2  31  ThreeTwo  33  34
#
# df.iloc[2] = df.iloc[2].map(f_str)
# print(df)
# #           a         b           c          d
# # 0        11    OneTwo          13         14
# # 1        21    TwoTwo          23         24
# # 2  ThreeOne  ThreeTwo  ThreeThree  ThreeFour

'''07_pandas.DataFrame的for循环处理（迭代）'''
# 当使用for语句循环（迭代）pandas.DataFrame时，简单的使用for语句便可以取得返回列名，因此使用重复使用for方法，便可以获取每行的值。
df = pd.DataFrame({'age': [24, 42], 'state': ['NY', 'CA'], 'point': [64, 92]},
                  index=['Alice', 'Bob'])
# print(df)
#        age state  point
# Alice   24    NY     64
# Bob     42    CA     92
# 1.pandas.DataFrame for循环的应用
# # 当pandas.DataFrame直接使用for循环时，按以下顺序获取列名（列名）。
# for column_name in df:
#     print(type(column_name))  # <class 'str'>
#     print(column_name)  # age  state  point
#     print('======\n')

# 2.逐列检索
# DataFrame.items()
# 使用items（）方法，您可以一一获取列名称和每个列的数据（pandas.Series类型）。
# pandas.Series可以通过指定索引名称等来检索行的值。
# for column_name, item in df.items():
#     print(column_name)
#     print(item)
#     print(item['Alice'])

# 3.逐行检索
# 一次检索一行的方法包括iterrows（）和itertuples（）。 itertuples（）更快。
# 3.1DataFrame.iterrows()
# for index, row in df.iterrows():
#     print(index)  # Alice  Bob
#     print("******")
#     print(row)  # 全部信息
#     print(row['point'])

# 3.2DataFrame.itertuples()
# for row in df.itertuples():
#     print(type(row))  # <class 'pandas.core.frame.Pandas'>
#     print(row)  # Pandas(Index='Alice', age=24, state='NY', point=64)
#     print(row.point)

# 4检索特定列的值
# 如果将pandas.Series应用于for循环，则可以按顺序获取值，因此，如果指定pandas.DataFrame列并将其应用于for循环，则可以按顺序获取该列中的值。
# for age in df['age']:
#     print(age)
# # 24
# # 42

# 如果使用内置函数zip（），则可以一次收集多列值。
# for age, point in zip(df['age'], df['point']):
#     print(age, point)
# # 24 64
# # 42 92
# # 如果要获取索引（行名），使用index属性。
# print(df.index)
# # Index(['Alice', 'Bob'], dtype='object')
#
# print(type(df.index))
# # <class 'pandas.core.indexes.base.Index'>
#
# for index in df.index:
#     print(index)
# # Alice
# # Bob
#
# for index, state in zip(df.index, df['state']):
#     print(index, state)
# # Alice NY
# # Bob CA

# 5.循环更新值

# for index, row in df.iterrows():
#     df.at[index, 'point'] += row['age']
#
# print(df)
# #        age state  point
# # Alice   24    NY     88
# # Bob     42    CA    134

# df['point'] += df['age']
# print(df)
# #        age state  point
# # Alice   24    NY    112
# # Bob     42    CA    176
#
# df['new'] = df['point'] + df['age'] * 2
# print(df)
# #        age state  point  new
# # Alice   24    NY    112  160
# # Bob     42    CA    176  260
#
# df['state_0'] = df['state'].str.lower().str[0]
# print(df)
# #        age state  point  new  age_sqrt state_0
# # Alice   24    NY    112  160  4.898979       n
# # Bob     42    CA    176  260  6.480741       c

'''08_Pandas提取含有指定字符串的行（完全匹配，部分匹配）'''
# 0.数据
dic = {
    'name': ['Alice', 'Bob', 'Charlie'],
    'age': [24, 42, 18],
    'state': ['NY', 'CA', 'CA'],
    'point': [64, 92, 70]
}
df = pd.DataFrame(dic)

# 1.行的提取（选择）方法
# 使用布尔值的布尔列表（数组）或pandas.Series的话，只能提取（选择）True行。
# mask = [True, False, True]
# df_mask = df[mask]
# print(df_mask)
# #       name  age state  point
# # 0    Alice   24    NY     64
# # 2  Charlie   18    CA     70

# 2.完全匹配
# 如果元素与字符串完全匹配，则使用==获取为True的pandas.Series。
# print(df['state'] == 'CA')
# # 0    False
# # 1     True
# # 2     True
# # Name: state, dtype: bool
#
# print(df[df['state'] == 'CA'])
# #       name  age state  point
# # 1      Bob   42    CA     92
# # 2  Charlie   18    CA     70

# 3.部分匹配
# 3.1 str.contains()：包含一个特定的字符串
# print(df['name'].str.contains('li'))
# # 0     True
# # 1    False
# # 2     True
# # Name: name, dtype: bool
#
# print(df[df['name'].str.contains('li')])
# #       name  age state  point
# # 0    Alice   24    NY     64
# # 2  Charlie   18    CA     70

# 3.2参数na：缺少值NaN处理
# 如果元素是缺失值NaN，则默认情况下它将返回NaN而不是True或False。因此，使用pandas.Series提取该行是错误的。
# df_nan = df.copy()
# df_nan.iloc[2, 0] = float('nan')
# print(df_nan)
# #     name  age state  point
# # 0  Alice   24    NY     64
# # 1    Bob   42    CA     92
# # 2    NaN   18    CA     70
#
# print(df_nan['name'].str.contains('li'))
# # 0     True
# # 1    False
# # 2      NaN
# # Name: name, dtype: object
#
# # print(df_nan[df_nan['name'].str.contains('li')])
# # ValueError: cannot index with vector containing NA / NaN values
# # 可以通过str.contains（）的参数na来指定替换NaN结果的值。
# print(df_nan['name'].str.contains('li', na=False))
# # 0     True
# # 1    False
# # 2    False
# # Name: name, dtype: bool
#
# print(df_nan['name'].str.contains('li', na=True))
# # 0     True
# # 1    False
# # 2     True
# # Name: name, dtype: bool
# 用作条件时，如果na = True，则选择NaN的行，如果na = False，则不选择NaN的行。

# 3.3 参数case：大小写我的处理
# 默认情况下，区分大小写。如果参数case为False，则忽略。
# print(df['name'].str.contains('LI'))
# # 0    False
# # 1    False
# # 2    False
# # Name: name, dtype: bool
#
# print(df['name'].str.contains('LI', case=False))
# # 0     True
# # 1    False
# # 2     True
# # Name: name, dtype: bool

# 3.4 参数regex：使用正则表达式模式  (不清楚正则表达式怎么用)
# print(df['name'].str.contains('i.*e'))
# # 0     True
# # 1    False
# # 2     True
# # Name: name, dtype: bool

# 如果参数ragex为False，则确定是否包含第一个参数的字符串本身.
# print(df['name'].str.contains('i.*e', regex=False))
# # 0    False
# # 1    False
# # 2    False
# # Name: name, dtype: bool

# 3.5 str.endswith（）：以特定字符串结尾
# print(df['name'].str.endswith('e'))
# # 0     True
# # 1    False
# # 2     True
# # Name: name, dtype: bool
#
# print(df[df['name'].str.endswith('e')])
# #       name  age state  point
# # 0    Alice   24    NY     64
# # 2  Charlie   18    CA     70
# str.endswith（）也有一个参数na。如果要选择缺失值NaN的行，则设置na = True；如果不想选择，则将na = False设置。
# 没有参数case，因此它始终区分大小写。

# 3.6 str.startswith（）：以特定的字符串开头
# 获取以特定字符串开头的pandas.Series。同上

# 3.7 str.match（）：匹配正则表达式模式 （看不懂）
# print(df['name'].str.match('.*i.*e'))
# # 0     True
# # 1    False
# # 2     True
# # Name: name, dtype: bool
#
# print(df[df['name'].str.match('.*i.*e')])
# #       name  age state  point
# # 0    Alice   24    NY     64
# # 2  Charlie   18    CA     70

'''09_Pandas从多个条件（AND，OR，NOT）中提取行'''
# 0.准备数据
dic = {
    'name': ['Alice', 'Bob', 'Charlie', 'Dave', 'Ellen', 'Frank'],
    'age': [24, 42, 18, 68, 24, 30],
    'state': ['NY', 'CA', 'CA', 'TX', 'CA', 'NY'],
    'point': [64, 92, 70, 70, 88, 57]
}
df = pd.DataFrame(dic)
# 1.如何提取（选择）行，同上一章内容
# 2.通过AND，OR，NOT多个条件提取（选择）行的代码-示例
# df_and = df[(df['age'] < 35) & ~(df['state'] == 'NY')]
# print(df_and)
# #       name  age state  point
# # 2  Charlie   18    CA     70
# # 4    Ellen   24    CA     88
#
# # 3.3个以上条件的运算符的优先级
# # 运算符的优先级是NOT（〜），AND（＆），OR（|）。因此，结果因顺序而异。
# df_multi_1 = df[(df['age'] < 35) | ~(df['state'] == 'NY') & (df['point'] < 75)]
# print(df_multi_1)
# #       name  age state  point
# # 0    Alice   24    NY     64
# # 2  Charlie   18    CA     70
# # 3     Dave   68    TX     70
# # 4    Ellen   24    CA     88
# # 5    Frank   30    NY     57
# # 结论，加括号。

'''10_Pandas使用分隔符或正则表达式将字符串拆分为多列'''
# https://blog.csdn.net/qq_18351157/article/details/105506107
# 1.str.split（）：用定界符分割
# 指定split = True作为参数可分为多个列并以pandas.DataFrame的形式获取。默认值为expand = False。
# 1.1pandas.Series
s_org = pd.Series(['aaa@xxx.com', 'bbb@yyy.com', 'ccc@zzz.com', 'ddd'], index=['A', 'B', 'C', 'D'])
# print(s_org)
# print(type(s_org))  # <class 'pandas.core.series.Series'>
# A    aaa@xxx.com
# B    bbb@yyy.com
# C    ccc@zzz.com
# D            ddd
# dtype: object
s = s_org.str.split('@')
# print(s)
# print(type(s))  # <class 'pandas.core.series.Series'>
# A    [aaa, xxx.com]
# B    [bbb, yyy.com]
# C    [ccc, zzz.com]
# D             [ddd]
# dtype: object

# 指定split = True作为参数可分为多个列并以pandas.DataFrame的形式获取。默认值为expand = False。
# 没有足够的行划分的元素为“无(None)”。
df = s_org.str.split('@', expand=True)
# print(df)
# print(type(df))  # <class 'pandas.core.frame.DataFrame'>
#      0        1
# A  aaa  xxx.com
# B  bbb  yyy.com
# C  ccc  zzz.com
# D  ddd     None

# 1.2pandas.DataFrame
df.columns = ['local', 'domain']
# 在特定的列上使用str.split（）获得一个拆分的pandas.DataFrame。
# print(df['domain'].str.split('.', expand=True))
# 第二种方法
# df3 = pd.concat([df['local'], df['domain'].str.split('.', expand=True)], axis=1)
# print(df3)
# 方法一：使用pd.concat（）与原始pandas.DataFrame进行串联（联接），并使用drop（）方法删除原始列。
df = pd.concat([df, df['domain'].str.split('.', expand=True)], axis=1).drop('domain', axis=1)
# print(df)

# 1.3str.extract()：按正则表达式拆分(看不懂，先跳过)

'''11_Pandas.DataFrame中组合多个列的字符串来创建新列'''
# https://blog.csdn.net/qq_18351157/article/details/105642406

dic = {
    'name': ['Alice', 'Bob', 'Charlie'],
    'age': [24, 42, 18],
    'state': ['NY', 'CA', 'CA'],
    'point': [64, 92, 70]
}
df = pd.DataFrame(dic)
# 1.连接字符串
# 1.1 str.cat()
# 可以使用字符串方法str.cat（）连接字符串。
# 调用原pandas.Series和第一个参数中指定的pandas.Series的元素进行串联，返回一个pandas.Series。
# print(df['name'].str.cat(df['state']))
# 0      AliceNY
# 1        BobCA
# 2    CharlieCA
# Name: name, dtype: object
# 如果为参数sep指定了字符串，则会在它们之间插入一个字符串。
# print(df['name'].str.cat(df['state'], sep=' in '))
# 0      Alice in NY
# 1        Bob in CA
# 2    Charlie in CA
# Name: name, dtype: object
# 可以将具有相同数量元素的NumPy数组ndarray或list指定为第一个参数。
# print(df['name'].str.cat(['X', 'Y', 'Z'], sep=' in '))
# 0      Alice in X
# 1        Bob in Y
# 2    Charlie in Z
# Name: name, dtype: object
# 也可以通过指定一个元素为pandas.Series的列表或一个列表作为第一个参数来连接多个字符串。
# print(df['name'].str.cat([df['state'], df['name']], sep='-'))
# 0      Alice-NY-Alice
# 1        Bob-CA-Bob
# 2    Charlie-CA-Charlie
# Name: name, dtype: object

# 1.2+运算符
# 您可以简单地使用+运算符。这可能更直观。
# 相同数量的元素和列表串联的NumPy数组ndarray也是可以的。
# print(df['name'] + ' in ' + df['state'] + ' - ' + ['X', 'Y', 'Z'])
# 0      Alice in NY - X
# 1        Bob in CA - Y
# 2    Charlie in CA - Z
# dtype: object

# 1.3NaN缺失值的处理
df['col_NaN'] = ['X', np.nan, 'Z']
# print(df)
#       name  age state  point col_NaN
# 0    Alice   24    NY     64       X
# 1      Bob   42    CA     92     NaN
# 2  Charlie   18    CA     70       Z
# 在str.cat（）和使用+运算符中，包含缺失值NaN的元素默认情况下变为缺失值NaN。
# print(df['name'].str.cat(df['col_NaN'], sep='-'))
# 0      Alice-X
# 1          NaN
# 2    Charlie-Z
# Name: name, dtype: object
# 可以替换为参数na_rep指定的字符串。
# print(df['name'].str.cat(df['col_NaN'], sep='-', na_rep='No Data'))
# 0        Alice-X
# 1    Bob-No Data
# 2      Charlie-Z
# Name: name, dtype: object

# 2.字符串列和数值列的连接
# 当组合字符串列和数字列时，必须通过astype（）方法将数字列转换为字符串类型str。
# print(df['name'].str.cat(df['age'].astype(str),sep='_'))
# print(df['name'] + ' _ ' + df['age'].astype(str))

# 3.将串联的列添加到pandas.DataFrame
# 如果要将字符串连接的字符串作为新列添加到pandas.DataFrame中，请在[列名]中指定一个新列名并替换它。
# df['name_state'] = df['name'].str.cat(df['state'], sep=' in ')
# print(df)
#       name  age state  point col_NaN     name_state
# 0    Alice   24    NY     64       X    Alice in NY
# 1      Bob   42    CA     92     NaN      Bob in CA
# 2  Charlie   18    CA     70       Z  Charlie in CA
# 可以使用drop（）方法删除不再需要的列。
# print(df.drop(columns=['name', 'state']))
#    age  point col_NaN     name_state
# 0   24     64       X    Alice in NY
# 1   42     92     NaN      Bob in CA
# 2   18     70       Z  Charlie in CA
# 还有一种使用assign（）的方法。使用assign（）时，原始对象不会更改，并且会返回一个新对象。
# assign()的功能是新添加一列
# print(df.assign(name_state=df['name'] + ' in ' + df['state']).drop(columns=['name', 'state']))

'''12_Pandas.DataFrame删除指定行和列（drop）'''
# 0. 数据准备
dic = {
    'name': ['Alice', 'Bob', 'Charlie', 'Dave', 'Ellen', 'Frank'],
    'age': [24, 42, 18, 68, 24, 30],
    'state': ['NY', 'CA', 'CA', 'TX', 'CA', 'NY'],
    'point': [64, 92, 70, 70, 88, 57]
}
df = pd.DataFrame(dic)
df.set_index('name', inplace=True)
# 1.DataFrame指定的行删除
# 1.1按行名指定（行标签）  labels填的参数是行索引，如果不是的话会报错。
# 默认情况下，原始DataFrame保持不变，并返回一个新的DataFrame。如果参数inplace设置为True，则将更改原始DataFrame。
# print(df.drop('Charlie', axis=0))
# print(df.drop(labels = ['Bob', 'Dave', 'Frank']))
# print(df.drop(index=['Bob', 'Dave', 'Frank']))
#          age state  point
# name
# Alice     24    NY     64
# Charlie   18    CA     70
# Ellen     24    CA     88

# 1.2按行号指定
# 如果要按行号指定，请使用DataFrame的index属性。
# print(df.drop(df.index[0]))
# print(df.index[[1, 3, 5]])  # Index(['Bob', 'Dave', 'Frank'], dtype='object', name='name')
# print(df.drop(df.index[[1, 3, 5]]))
# #          age state  point
# # name
# # Alice     24    NY     64
# # Charlie   18    CA     70
# # Ellen     24    CA     88

# 1.3 未设置行名的注意事项
# dic = {
#     'name': ['Alice', 'Bob', 'Charlie', 'Dave', 'Ellen', 'Frank'],
#     'age': [24, 42, 18, 68, 24, 30],
#     'state': ['NY', 'CA', 'CA', 'TX', 'CA', 'NY'],
#     'point': [64, 92, 70, 70, 88, 57]
# }
# df = pd.DataFrame(dic)
# print(df.drop([1,3,5]))  # 删除的是索引号，所以我只认1，3，5，排完序还是删这三个数
# print(df.drop(df.index[[1, 3, 5]]))  # 删除的是1，3，5位置，所以说，排完序，我还是删1，3，5位置而不是对应索引

# 2.DataFrame指定的列删除
# 2.1按列名指定（列标签）
# print(df.drop(columns=['state', 'point']))
# print(df.drop(['age','state'],axis=1))
# 参数inplace的使用方法与行的相同。在原基础上修改，不需要返回值
# df.drop(['age','state'],axis=1,inplace=True)
# print(df)
# 按列号指定
# print(df.drop(df.columns[[0, 2]], axis=1))

# 3.多行多列的删除
# print(df.drop(columns=['age','point'],index=['Bob','Dave']))
# print(df.drop(index=df.index[[1, 3, 5]],columns=df.columns[[1, 2]]))

'''13_Pandas字符串的替换和空白处删除等方法'''
# https://blog.csdn.net/qq_18351157/article/details/105876906
# 1.替换
# 1.1str.replace():替换字符串
s = pd.Series([' a-a-x ', ' b-x-b ', ' x-c-c '])
# # 0     a-a-x
# # 1     b-x-b
# # 2     x-c-c
# # dtype: object
# s_new = s.str.replace('x', 'z')
# print(s_new)
# # 0     a-a-z
# # 1     b-z-b
# # 2     z-c-c
# # dtype: object
df = pd.DataFrame([[' a-a-x-1 ', ' a-a-x-2 '],
                   [' b-x-b-1 ', ' b-x-b-2 '],
                   [' x-c-c-1 ', ' x-c-c-2 ']],
                  columns=['col1', 'col2'])
# #         col1       col2
# # 0   a-a-x-1    a-a-x-2
# # 1   b-x-b-1    b-x-b-2
# # 2   x-c-c-1    x-c-c-2
# df['col1'] = df['col1'].str.replace('x', 'z')
# print(df)
# #         col1       col2
# # 0   a-a-z-1    a-a-x-2
# # 1   b-z-b-1    b-x-b-2
# # 2   z-c-c-1    x-c-c-2

# 2.空白削除
# 2.1str.strip():删除左右两侧的空白（开始/结束）
# s_new = s.str.strip()
# print(s_new)
# 也可以指定要删除的字符作为参数。指定字符串中包含的字符将被删除。这同样适用于str.lstrip（）和str.rstrip（）。
# s_new = s.str.strip(' x')
# print(s_new)
# 0     a-a-
# 1    b-x-b
# 2     -c-c
# dtype: object
# df['col1'] = df['col1'].str.strip()
# print(df)
# 2.2 str.lstrip():删除左侧空白  用法一样
# 2.3 str.rstrip():删除右侧空白

# 3.大小写変换
# s = pd.Series(['Hello World', 'hello world', 'HELLO WORLD'])
# 0    Hello World
# 1    hello world
# 2    HELLO WORLD
# dtype: object
# 3.1 str.lower():转换为小写
# s_lower = s.str.lower()
# print(s_lower)
# 3.2 str.upper():转换为大写
# 3.3 str.capitalize():将第一个字母转换为大写，将其他字母转换为小写  Hello world
# 3.4 str.title():将单词的首字母转换为大写，其余转换为小写  Hello World

'''14_Pandas.DataFrame行和列的转置'''
# https://blog.csdn.net/qq_18351157/article/details/105931547
# 如果要交换（转置）pandas.DataFrame的行和列，使用T属性或transpose（）方法。
# 1 pandas.DataFrame.T
df = pd.DataFrame({'X': [0, 1, 2], 'Y': [3, 4, 5]}, index=['A', 'B', 'C'])
# print(df)
# #    X  Y
# # A  0  3
# # B  1  4
# # C  2  5
# print(df.T)
# #    A  B  C
# # X  0  1  2
# # Y  3  4  5

# # 2 pandas.DataFrame.transpose()
# print(df.transpose())

# 3 修改原始对象本身
# df = df.T

# 4 当进行类型转换（广播）时
# 结论：如果各列的数据类型不一致，转换会自动数据类型转换为最大的，比如含有int和float，则全转化为float，有object,则全转为object
# 如果类型一致则不会发生变化。

# 5.视图和复制
# 如果所有列都具有相同的数据类型，则T或transpose（）将返回视图。
# 原始对象和视图对象共享内存，因此更改一个元素会更改另一个元素。
# df = pd.DataFrame({'X': [0, 1, 2], 'Y': [3, 4, 5]}, index=['A', 'B', 'C'])
# #    X  Y
# # A  0  3
# # B  1  4
# # C  2  5
# df_T = df.T
# #    A  B  C
# # X  0  1  2
# # Y  3  4  5
# df_transpose = df.transpose()
# #    A  B  C
# # X  0  1  2
# # Y  3  4  5
# df.at['A', 'X'] = 100
# print(df)
# #      X  Y
# # A  100  3
# # B    1  4
# # C    2  5
# print(df_T)
# #      A  B  C
# # X  100  1  2
# # Y    3  4  5
# print(df_transpose)
# #      A  B  C
# # X  100  1  2
# # Y    3  4  5

# 在transpose（）中，当参数copy设置为True时，将生成一个副本。
# print(df)
# #    X  Y
# # A  0  3
# # B  1  4
# # C  2  5
# df_T_copy = df.T.copy()
# print(df_T_copy)
# #    A  B  C
# # X  0  1  2
# # Y  3  4  5
# df_transpose_copy = df.transpose(copy=True)
# print(df_transpose_copy)
# #    A  B  C
# # X  0  1  2
# # Y  3  4  5
# df.at['A', 'X'] = 100
# print(df)
# #      X  Y
# # A  100  3
# # B    1  4
# # C    2  5
# print(df_T_copy)
# #    A  B  C
# # X  0  1  2
# # Y  3  4  5
# print(df_transpose_copy)
# #    A  B  C
# # X  0  1  2
# # Y  3  4  5

'''15_Pandas计算元素的数量和频率（出现的次数）'''
# https://blog.csdn.net/qq_18351157/article/details/105993752
# pandas.Series.unique(): 返回NumPy数组ndarray中唯一元素值的列表
# pandas.Series.value_counts(): 返回唯一元素的值及其在出现的次数。
# pandas.Series.nunique(), pandas.DataFrame.nunique(): 返回int，pandas.Series中唯一元素的数量。

dic = {
    'name': ['Alice', 'Bob', 'Charlie', 'Dave', 'Ellen', 'Frank'],
    'age': [24, 42, 18, 68, 24, 30],
    'state': ['NY', 'CA', 'CA', 'TX', 'CA', 'NY'],
    'point': [64, 92, 70, 70, 88, 57]
}
df = pd.DataFrame(dic)
df.iloc[1] = np.nan
# print(df)
#       name   age state  point
# 0    Alice  24.0    NY   64.0
# 1      NaN   NaN   NaN    NaN
# 2  Charlie  18.0    CA   70.0
# 3     Dave  68.0    TX   70.0
# 4    Ellen  24.0    CA   88.0
# 5    Frank  30.0    NY   57.0

# 1. pandas.Series.unique():返回NumPy数组ndarray中唯一元素值的列表
# unique（）返回唯一元素值的列表。还包括缺失值NaN。
u = df['state'].unique()
# print(u)  # ['NY' nan 'CA' 'TX']
# print(type(u))  # <class 'numpy.ndarray'>

# 2. pandas.Series.value_counts():返回唯一元素的值及其在出现的次数。
# 默认情况下，它按出现次数的降序排序，但是如果参数ascending = True，则以升序排序，如果参数sort = False，则不进行排序，ascending参数失效。
# 默认情况下，NaN被排除，但如果参数dropna = False，则也计入NaN。
# 如果指定了参数normalize = True，则将值归一化，以使总数变为1。
vc = df['state'].value_counts(ascending = False)
# print(vc)
# # state
# # NY    2
# # CA    2
# # TX    1
# # Name: count, dtype: int64
# print(type(vc))  # <class 'pandas.core.series.Series'>

# 3.pandas.Series.nunique(), pandas.DataFrame.nunique():返回int，pandas.Series中唯一元素的数量。
# 3.1 pandas.Series.nunique()
# 默认情况下，不包含NaN，并且如果指定了参数dropna = False，则结果还将包含NaN。
nu = df['state'].nunique()
# print(nu)  # 3
# print(type(nu))  # <class 'int'>
# print(df['state'].nunique(dropna=False))  # 4

# 3.2 pandas.DataFrame.nunique()
# 计算每列的唯一元素数。返回pandas.Series类型。
# 默认情况下，不包含NaN，并且如果指定了参数dropna = False，则结果还将包含NaN。
# 默认情况下，该值为每列，但是如果参数axis = 1或axis =‘columns’，则返回每行的值。
nu_col = df.nunique()
# print(nu_col)
# print(type(nu_col))  # <class 'pandas.core.series.Series'>
# # name     5
# # age      4
# # state    3
# # point    4
# # dtype: int64
# print(df.nunique(dropna=False))
# # name     6
# # age      5
# # state    4
# # point    5
# # dtype: int64
# print(df.nunique(dropna=False, axis='columns'))
# # 0    4
# # 1    1
# # 2    4
# # 3    4
# # 4    4
# # 5    4
# # dtype: int64

# 4 唯一元素的数量（不包括重复项的）
# print(df['state'].unique().tolist())  # ['NY', nan, 'CA', 'TX']
# print(type(df['state'].unique().tolist()))  # <class 'list'>
#
# print(df['state'].value_counts().index.tolist())  # ['NY', 'CA', 'TX']
# print(type(df['state'].value_counts().index.tolist()))  # <class 'list'>
#
# print(df['state'].value_counts(dropna=False).index.values)  # ['NY' 'CA' 'TX' nan]
# print(type(df['state'].value_counts().index.values))  # <class 'numpy.ndarray'>
# # 如上所述，在unique（）的情况下，始终包含NaN，但是value_counts（）可以指定参数dropna是否包含NaN。

# 5. 唯一元素的频率（出现次数）
# print(df['state'].value_counts()['NY'])  # 2
# 使用iteritems（）方法检索for循环中的元素值和频率（出现次数）。
# for index, value in df['state'].value_counts().items():  # 文档里有错误
#     print(index, ': ', value)
# # NY :  2
# # CA :  2
# # TX :  1

# 6 独特元素及其出现的字典
# 也可以将to_dict（）方法应用于value_counts（）获得的pandas.Series使其成为字典。
# d = df['state'].value_counts().to_dict()
# print(d)  # {'NY': 2, 'CA': 2, 'TX': 1}
# print(type(d))  # <class 'dict'>
# print(d['NY'])  # 2
# # 使用items（）方法在for循环中检索元素值和频率（出现次数）。
# for key, value in d.items():
#     print(key, ': ', value)

# 7. 模式及其频率
# 7.1
# 默认情况下，value_counts（）返回pandas.Series，它以出现次数的降序排列，因此顶部是最频繁出现的值及其频率。
# print(df['state'].value_counts())
# # NY    2
# # CA    2
# # TX    1
# # Name: state, dtype: int64
# print(df['state'].value_counts().index[0])  # NY
# print(df['state'].value_counts().iat[0])  # 2

# 使用apply（）方法将其应用于pandas.DataFrame的每一列。
# print(df.apply(lambda x: x.value_counts().index[0]))
# # name     Frank
# # age         24
# # state       NY
# # point       70
# # dtype: object
#
# print(df.apply(lambda x: x.value_counts().iat[0]))
# # name     1
# # age      2
# # state    2
# # point    2
# # dtype: int64

# 7.2 mode()  众数
# pandas.Series的mode（）方法将模式值返回为pandas.Series，表示众数的意思
# 如果使用tolist（）列出此结果，则可以将模式值作为列表获取。请注意，即使只有一种模式，也将是一个列表。

# print(df['state'].mode())
# # 0    CA
# # 1    NY
# # Name: state, dtype: object
# print(df['age'].mode().tolist())  # [24.0]

# s_mode = df.apply(lambda x: x.mode().tolist())
# print(s_mode)
# # name     [Alice, Charlie, Dave, Ellen, Frank]
# # age                                    [24.0]
# # state                                [CA, NY]
# # point                                  [70.0]
# # dtype: object
# print(type(s_mode))  # <class 'pandas.core.series.Series'>
# print(s_mode['name'])  # ['Alice', 'Charlie', 'Dave', 'Ellen', 'Frank']
# print(type(s_mode['name']))  # <class 'list'>

# 计算众数数
# 可以使用count（）方法获得每列中的模式数，该方法对不缺少值NaN的元素数进行计数。
# print(df.mode().count())

# # 7.3describe():describe（）方法可用于共同计算每一列的唯一元素的数量，模式值及其频率（出现的次数）。每个项目都可以使用loc []获得。
# print(df.describe())
# # 在describe（）中，由列类型dtype计算出的项是不同的，因此使用astype（）进行类型转换（转换）。
# print(df.astype(str).describe())
# print(df.astype('str').describe().loc['top'])
#
# # 8.归一化频率
# print(df['state'].value_counts(dropna=False, normalize=True))
# # NY     0.333333
# # CA     0.333333
# # TX     0.166667
# # NaN    0.166667
# # Name: state, dtype: float64










