# -*- coding: utf-8 -*-
# @Time : 2024/8/27 10:19
# @Author : Gray
# https://blog.csdn.net/qq_18351157/article/details/106639315
import pandas as pd

'''01_Pandas.DataFrame的行名和列名的修改'''
# https://blog.csdn.net/qq_18351157/article/details/104410294
#
# df = pd.DataFrame({'A': [11, 21, 31],
#                    'B': [12, 22, 32],
#                    'C': [13, 23, 33], }, index=['One', 'Two', 'Three'])
#
# # 1.DataFrame.rename()
# # 函数DataFrame.rename()可以对任意行和列的名称进行修改。
# # DataFrame.rename()的参数有index和columns，使用"{旧值：新值}"字典的形式进行参数的指定。
# # 修改后，返回一个新的DataFrame，原DataFrame并没有被修改。
# # 原DataFrame的修改（参数inplace）这样就不需要赋值了！
# print(df)
# df1 = pd.DataFrame.rename(self = df,columns={'A': 'a'}, index={'Two': '2'})
# # df1 = df.rename(columns={'B': 'b'})
# print(df1)
# print(df)
# # pd.DataFrame.rename(self = df,columns={'A': 'a'}, index={'Two': '2'},inplace=True)
# # *.使用lambda表达式和函数进行批处理
# # rename()的参数index和columns值也可以指定为函数方法。
# print(df.rename(columns=str.lower,index=str.upper))
# # lambda表达式-无名函数的指定。
# print(df.rename(columns = lambda s:s*3,index = lambda s:s+'!!'))
#
# # 2.add_prefix(), add_suffix():只能对列名进行修改
# # 在方法的参数里指定接头词或者结尾词。
# print(df.add_prefix('X_'))
# print(df.add_suffix('_Y'))
#
# # 3.index和columns元素的更新
# # 可以在index，columns属性中指定List，tuple，pandas.Series等。
# df.index = [1, 2, 3]
# df.columns = ['a', 'b', 'c']
# print(df)
# #     a   b   c
# # 1  11  12  13
# # 2  21  22  23
# # 3  31  32  33

'''02_Pandas.concat连接DataFrame,Series'''
# https://blog.csdn.net/qq_18351157/article/details/104557778
# 1.数据
df1 = pd.DataFrame({'A': ['A1', 'A2', 'A3'],
                    'B': ['B1', 'B2', 'B3'],
                    'C': ['C1', 'C2', 'C3']},
                   index=['ONE', 'TWO', 'THREE'])
# print(df1)
#         A   B   C
# ONE    A1  B1  C1
# TWO    A2  B2  C2
# THREE  A3  B3  C3

df2 = pd.DataFrame({'C': ['C2', 'C3', 'C4'],
                    'D': ['D2', 'D3', 'D4']},
                   index=['TWO', 'THREE', 'FOUR'])
# print(df2)
#         C   D
# TWO    C2  D2
# THREE  C3  D3
# FOUR   C4  D4

s1 = pd.Series(['X1', 'X2', 'X3'], index=['ONE', 'TWO', 'THREE'], name='X')
# print(s1)
# ONE      X1
# TWO      X2
# THREE    X3
# Name: X, dtype: object

s2 = pd.Series(['Y2', 'Y3', 'Y4'], index=['TWO', 'THREE', 'FOUR'], name='Y')
# print(s2)
# TWO      Y2
# THREE    Y3
# FOUR     Y4
# Name: Y, dtype: object

# 2.pandas.concat的基本用法（）
# 指定要连接的对象：objs
# 连接方向的指定（垂直/水平）：axis
# 指定连接方法（外部连接/内部连接）：join
# 2.1指定要连接的对象：objs
df_concat = pd.concat([df1, df2], axis=0)  # 垂直或水平方向由axis参数指定。 如果axis = 0，则它们是垂直链接的。
# 默认设置为axis = 0,因此合并的列但是没有合并行,结果是创建了一个新的对象，原始对象保持不变。
# print(df_concat)
#          A    B   C    D
# ONE     A1   B1  C1  NaN
# TWO     A2   B2  C2  NaN
# THREE   A3   B3  C3  NaN
# TWO    NaN  NaN  C2   D2
# THREE  NaN  NaN  C3   D3
# FOUR   NaN  NaN  C4   D4

df_concat_multi = pd.concat([df1, df2, df1])
# print(df_concat_multi)
#          A    B   C    D
# ONE     A1   B1  C1  NaN
# TWO     A2   B2  C2  NaN
# THREE   A3   B3  C3  NaN
# TWO    NaN  NaN  C2   D2
# THREE  NaN  NaN  C3   D3
# FOUR   NaN  NaN  C4   D4
# ONE     A1   B1  C1  NaN
# TWO     A2   B2  C2  NaN
# THREE   A3   B3  C3  NaN

# 2.2连接方向的指定（垂直/水平）：axis
df_h = pd.concat([df1, df2], axis=1)  # 按行(合并行相同的索引)
# print(df_h)
#          A    B    C    C    D
# ONE     A1   B1   C1  NaN  NaN
# TWO     A2   B2   C2   C2   D2
# THREE   A3   B3   C3   C3   D3
# FOUR   NaN  NaN  NaN   C4   D4

# 2.3指定连接方法（外部连接/内部连接）：join
df_v_out = pd.concat([df1, df2], join='outer')  # 并集,默认是外连接
# print(df_v_out)
#          A    B   C    D
# ONE     A1   B1  C1  NaN
# TWO     A2   B2  C2  NaN
# THREE   A3   B3  C3  NaN
# TWO    NaN  NaN  C2   D2
# THREE  NaN  NaN  C3   D3
# FOUR   NaN  NaN  C4   D4

df_v_in = pd.concat([df1, df2], join='inner')  # 交集
# print(df_v_in)
#         C
# ONE    C1
# TWO    C2
# THREE  C3
# TWO    C2
# THREE  C3
# FOUR   C4

df_h_out = pd.concat([df1, df2], axis=1, join='outer')
# print(df_h_out)
#          A    B    C    C    D
# FOUR   NaN  NaN  NaN   C4   D4
# ONE     A1   B1   C1  NaN  NaN
# THREE   A3   B3   C3   C3   D3
# TWO     A2   B2   C2   C2   D2

df_h_in = pd.concat([df1, df2], axis=1, join='inner')
# print(df_h_in)
#         A   B   C   C   D
# TWO    A2  B2  C2  C2  D2
# THREE  A3  B3  C3  C3  D3

# 3.pandas.DataFrame的连接  上面举得例子都是DataFrame
# print(type(df_concat))  # <class 'pandas.core.frame.DataFrame'>

# 4.pandas.Series的连接
# 如果是pandas.Series之间的连接，则垂直连接（默认值axis= 0）返回的也是pandas.Series类型的对象。
s_v = pd.concat([s1, s2])  # 默认按列,不合并,和上面DataFrame是一样的
# print(s_v)
# ONE      X1
# TWO      X2
# THREE    X3
# TWO      Y2
# THREE    Y3
# FOUR     Y4
# dtype: object

# print(type(s_v))  # <class 'pandas.core.series.Series'>

s_h = pd.concat([s1, s2], axis=1)
# print(s_h)
#          X    Y
# ONE     X1  NaN
# TWO     X2   Y2
# THREE   X3   Y3
# FOUR   NaN   Y4
# print(type(s_h))  # <class 'pandas.core.frame.DataFrame'>

s_h_in = pd.concat([s1, s2], axis=1, join='inner')
# print(s_h_in)
#         X   Y
# TWO    X2  Y2
# THREE  X3  Y3

# 4.pandas.DataFrame和pandas.Series的连接
df_s_h = pd.concat([df1, s2], axis=1)
# print(df_s_h)
#          A    B    C    Y
# ONE     A1   B1   C1  NaN
# TWO     A2   B2   C2   Y2
# THREE   A3   B3   C3   Y3
# FOUR   NaN  NaN  NaN   Y4
df_s_h_in = pd.concat([df1, s2], axis=1, join='inner')
# print(df_s_h_in)
#         A   B   C   Y
# TWO    A2  B2  C2  Y2
# THREE  A3  B3  C3  Y3
df_s_v = pd.concat([df1, s2])
# print(df_s_v)
#          A    B    C    Y
# ONE     A1   B1   C1  NaN
# TWO     A2   B2   C2  NaN
# THREE   A3   B3   C3  NaN
# TWO    NaN  NaN  NaN   Y2
# THREE  NaN  NaN  NaN   Y3
# FOUR   NaN  NaN  NaN   Y4
# 添加行，可以在.loc中指定新的行名称并分配值的方法。append()方法应该是已经删了
df1.loc['FOUR'] = ['A4', 'B4', 'C4']
# print(df1)
#         A   B   C
# ONE    A1  B1  C1
# TWO    A2  B2  C2
# THREE  A3  B3  C3
# FOUR   A4  B4  C4

'''03_Pandas读取csv/tsv文件（read_csv，read_table）'''
# https://blog.csdn.net/qq_18351157/article/details/104749945

# 1.read_csv()和read_table()之间的区别
# read_table()中，定界符为\t。如果既不是逗号也不是制表符，则可以通过参数（sep或delimiter）设置区分符。

# 2.读取没有标题的CSV
# 如果未设置任何参数，则将第一行识别为标题并将自动分配列名columns。
df = pd.read_csv('C:/Users/81087/Desktop/data/DataFrameTest.csv')
# print(df)
#    11  12  13  14
# 0  21  22  23  24
# 1  31  32  33  34
# print(df.columns)  # Index(['11', '12', '13', '14'], dtype='object')
# 如果header = None，则将为列名列分配一个序号。
df_none = pd.read_csv('C:/Users/81087/Desktop/data/DataFrameTest.csv', header=None)
# print(df_none)
#     0   1   2   3
# 0  11  12  13  14
# 1  21  22  23  24
# 2  31  32  33  34
# 可以将任意值设置为列名，参数为name=（‘A’，‘B’，‘C’，‘D’）。通过列表或元组指定。
df_names = pd.read_csv('C:/Users/81087/Desktop/data/DataFrameTest.csv', names=('A', 'B', 'C', 'D'))
# print(df_names)
#     A   B   C   D
# 0  11  12  13  14
# 1  21  22  23  24
# 2  31  32  33  34

# 3.读取有标题的CSV
# 指定标题的行号从0开始，例如header = 0。由于默认值为header = 0，因此如果第一行是header，则可以获得相同的结果。
df_header = pd.read_csv('C:/Users/81087/Desktop/data/DataFrameTest1.csv')
df_header_0 = pd.read_csv('C:/Users/81087/Desktop/data/DataFrameTest1.csv', header=0)
# print(df_header)
#     a   b   c   d
# 0  11  12  13  14
# 1  21  22  23  24
# 2  31  32  33  34
df_header_2 = pd.read_csv('C:/Users/81087/Desktop/data/DataFrameTest1.csv', header=2)
# 以第2行作为列索引，并且只保存从第2行往后的数据。
# print(df_header_2)
#    21  22  23  24
# 0  31  32  33  34

# 4.读取有index的CSV
# 4.1如果未指定任何内容，则不会识别索引列。
df_header_index = pd.read_csv('C:/Users/81087/Desktop/data/DataFrameTest2.csv')
# print(df_header_index)
#   Unnamed: 0   a   b   c   d
# 0        ONE  11  12  13  14
# 1        TWO  21  22  23  24
# 2      THREE  31  32  33  34
# print(df_header_index.index)  # RangeIndex(start=0, stop=3, step=1)
# 4.2 指定要用作索引的列的列号，从0开始，例如index_col = 0。
df_header_index_col = pd.read_csv('C:/Users/81087/Desktop/data/DataFrameTest2.csv', index_col=0)
# print(df_header_index_col)
#         a   b   c   d
# ONE    11  12  13  14
# TWO    21  22  23  24
# THREE  31  32  33  34
# print(df_header_index_col.index)  # Index(['ONE', 'TWO', 'THREE'], dtype='object')

# 5.指定（选择）要读取的列
# 要仅读取特定的列，请使用usecols参数。 指定要在列表中读取的列号。即使只有一列，也要使用列表。
df_none_usecols = pd.read_csv('C:/Users/81087/Desktop/data/DataFrameTest.csv', header=None, usecols=[1, 3])
# print(df_none_usecols)
#     1   3
# 0  12  14
# 1  22  24
# 2  32  34
df_none_usecols = pd.read_csv('C:/Users/81087/Desktop/data/DataFrameTest.csv', header=None, usecols=[2])
# print(df_none_usecols)
#     2
# 0  13
# 1  23
# 2  33
# 也可以按列名而不是列号指定。
df_header_usecols = pd.read_csv('C:/Users/81087/Desktop/data/DataFrameTest1.csv', usecols=['a', 'c'])
# print(df_header_usecols)
#     a   c
# 0  11  13
# 1  21  23
# 2  31  33
# 在没有特定列的情况下时，使用匿名函数（lambda表达式）很方便。
# 尤其是当您要从具有许多列的文件中排除少量列并读取它们时，比指定要读取的大量列号要容易得多。
df_header_usecols = pd.read_csv('C:/Users/81087/Desktop/data/DataFrameTest1.csv', usecols=lambda x: x != 'b')
# print(df_header_usecols)
#     a   c   d
# 0  11  13  14
# 1  21  23  24
# 2  31  33  34
df_header_usecols = pd.read_csv('C:/Users/81087/Desktop/data/DataFrameTest1.csv', usecols=lambda x: x not in ['a', 'c'])
# print(df_header_usecols)
#     b   d
# 0  12  14
# 1  22  24
# 2  32  34
# 当与index_col一起使用时，由index_col指定的列也必须由usecols指定。(因为index_col列是索引列)
df_index_usecols = pd.read_csv('C:/Users/81087/Desktop/data/DataFrameTest2.csv', index_col=0, usecols=[0, 1, 3])
# print(df_index_usecols)
#         a   c
# ONE    11  13
# TWO    21  23
# THREE  31  33

# 6.跳过（排除）行的读取
# 6.1 skipprows
# 要跳过（排除）特定行并读取它们，使用参数skipprows。 如果将整数传递给skipprows，那么将跳过skipprows行（不删除列索引）。
df_none = pd.read_csv('C:/Users/81087/Desktop/data/DataFrameTest.csv', header=None)
# print(df_none)
#     0   1   2   3
# 0  11  12  13  14
# 1  21  22  23  24
# 2  31  32  33  34
df_none = pd.read_csv('C:/Users/81087/Desktop/data/DataFrameTest.csv', header=None, skiprows=2)
# print(df_none)
#     0   1   2   3
# 0  31  32  33  34
# 可以指定要跳过的行号列表。即使在一行中也要使用列表。
df_none_skiprows = pd.read_csv('C:/Users/81087/Desktop/data/DataFrameTest.csv',
                               header=None, skiprows=[0, 2])
# print(df_none_skiprows)
#     0   1   2   3
# 0  21  22  23  24

df_none_skiprows = pd.read_csv('C:/Users/81087/Desktop/data/DataFrameTest.csv',
                               header=None, skiprows=[1])
# print(df_none_skiprows)
#     0   1   2   3
# 0  11  12  13  14
# 1  31  32  33  34

# 仅读取特定行时，使用匿名函数（lambda表达式）会很方便。特别是当您只想从文件中读取多行的特定行时，比指定要跳过的行数要容易得多。
df_none_skiprows = pd.read_csv('C:/Users/81087/Desktop/data/DataFrameTest.csv', header=None,
                               skiprows=lambda x: x not in [0, 2])
# print(df_none_skiprows)
#     0   1   2   3
# 0  11  12  13  14
# 1  31  32  33  34
# 如果文件具有标题，则还需要考虑标题行。
df_header_skiprows = pd.read_csv('C:/Users/81087/Desktop/data/DataFrameTest1.csv', skiprows=[1])
# print(df_header_skiprows)
#     a   b   c   d
# 0  21  22  23  24
# 1  31  32  33  34

df_header_skiprows = pd.read_csv('C:/Users/81087/Desktop/data/DataFrameTest1.csv', skiprows=[0, 3])
# print(df_header_skiprows)  # 把标题行给删了
#    11  12  13  14
# 0  21  22  23  24

# 6.2 skipfooter
# 要跳过文件的末尾，请使用skipfooter参数。将要跳过的行数指定为整数。根据环境的不同，会出现以下警告，因此请指定参数engine =‘python’。
df_none_skipfooter = pd.read_csv('C:/Users/81087/Desktop/data/DataFrameTest.csv', header=None,
                                 skipfooter=1, engine='python')
# print(df_none_skipfooter)
#     0   1   2   3
# 0  11  12  13  14
# 1  21  22  23  24

# 6.3nrows
df_none_nrows = pd.read_csv('C:/Users/81087/Desktop/data/DataFrameTest.csv', header=None, nrows=2)
# print(df_none_nrows)  # 需要注意，df_none_nrows只读取了前2行的数据，因此文件其他数据就没办法用到了
#     0   1   2   3
# 0  11  12  13  14
# 1  21  22  23  24

# 7.通过指定类型dtype进行读取
# 7.1 原始数据
# ,a,b,c,d
# ONE,1,"001",100,x
# TWO,2,"020",,y
# THREE,3,"300",300,z
# 7.2默认情况下，以0开头的数字序列（无论是否带引号）都被视为数字，而不是字符串，并且省略前导零。
df_default = pd.read_csv('C:/Users/81087/Desktop/data/DataFrameTest3.csv', index_col=0)
# print(df_default)
#        a    b      c  d
# ONE    1    1  100.0  x
# TWO    2   20    NaN  y
# THREE  3  300  300.0  z

# print(df_default.dtypes)
# a      int64
# b      int64
# c    float64
# d     object
# dtype: object

# 如果在参数dtype中指定了任意数据类型，则包括index_col指定的列在内的所有列都将转换为该类型并读取。
# 例如，如果dtype = str，则所有列都强制转换为字符串。但是，同样在这种情况下，缺少的值是浮点类型。
# dtype = str 和 dtype = object效果一样
# 在参数dtype中指定无法转换的类型将导致错误。比如dtype = int
df_str = pd.read_csv('C:/Users/81087/Desktop/data/DataFrameTest3.csv', index_col=0, dtype=str)
# print(df_str)
#        a    b    c  d
# ONE    1    1  100  x
# TWO    2   20  NaN  y
# THREE  3  300  300  z

# print(df_str.dtypes)
# a    object
# b    object
# c    object
# d    object
# dtype: object

# print(df_str.map(type))
#                    a              b                c              d
# ONE    <class 'str'>  <class 'str'>    <class 'str'>  <class 'str'>
# TWO    <class 'str'>  <class 'str'>  <class 'float'>  <class 'str'>
# THREE  <class 'str'>  <class 'str'>    <class 'str'>  <class 'str'>

df_str_col = pd.read_csv('C:/Users/81087/Desktop/data/DataFrameTest3.csv',
                         index_col=0, dtype={'b': str, 'c': str})
df_str_col_num = pd.read_csv('C:/Users/81087/Desktop/data/DataFrameTest3.csv',
                             index_col=0, dtype={2: str, 3: str})  # 2，3分别对应b和c，因为行索引列对应的是0
# print(df_str_col)
#        a    b    c  d
# ONE    1  001  100  x
# TWO    2  020  NaN  y
# THREE  3  300  300  z

# print(df_str_col.dtypes)
# print(df_str_col_num.dtypes)
# a     int64
# b    object
# c    object
# d    object
# dtype: object

# 7.3要在读取后转换pandas.DataFrame的列类型，请在astype（）方法中以字典格式指定它。
df_str_cast = df_str.astype({'a': int})
# print(df_str_cast)
#        a    b    c  d
# ONE    1  001  100  x
# TWO    2  020  NaN  y
# THREE  3  300  300  z

# print(df_str_cast.dtypes)
# a     int64
# b    object
# c    object
# d    object
# dtype: object

# 8.NaN缺失值的处理
# 8.1默认情况下，可能的值（例如空字符串”，字符串“ NaN”，“ nan”和null）通常默认为缺少NaN
# By default the following values are interpreted as NaN: ‘’, ‘#N/A’, ‘#N/A N/A’, ‘#NA’, ‘-1.#IND’,
# ‘-1.#QNAN’, ‘-NaN’, ‘-nan’, ‘1.#IND’, ‘1.#QNAN’, ‘N/A’, ‘NA’, ‘NULL’, ‘NaN’, ‘n/a’, ‘nan’, ‘null’.

df_nan = pd.read_csv("C:/Users/81087/Desktop/data/DataFrameTest4.csv", index_col=0)
# print(df_nan)
#          a   b
# ONE    NaN NaN
# TWO      - NaN
# THREE  NaN NaN

# print(df_nan.isnull())
#            a     b
# ONE     True  True
# TWO    False  True
# THREE   True  True

# 8.2要指定默认值以外的值，将其视为缺失值，使用参数na_values。例：na_values='-'表示'-'也当作是Nan
df_nan_set_na = pd.read_csv("C:/Users/81087/Desktop/data/DataFrameTest4.csv", index_col=0, na_values='-')
# print(df_nan_set_na)
#         a   b
# ONE   NaN NaN
# TWO   NaN NaN
# THREE NaN NaN
# print(df_nan_set_na.isnull())
#           a     b
# ONE    True  True
# TWO    True  True
# THREE  True  True

# 8.3keep_default_na设置为False之后,只将na_values中的值设置为Nan，而其余默认值不再当作Nan处理，参考465行左右的内容
df_nan_set_na_no_keep = pd.read_csv('C:/Users/81087/Desktop/data/DataFrameTest4.csv', index_col=0,
                                    na_values=['-', 'NaN', 'null'], keep_default_na=False)

# print(df_nan_set_na_no_keep)
#          a    b
# ONE         NaN
# TWO    NaN  nan
# THREE  NaN  N/A
# print(df_nan_set_na_no_keep.isnull())
#            a      b
# ONE    False   True
# TWO     True  False
# THREE   True  False

# 8.4如果参数na_filter设置为False，则无论参数na_values和keep_default_na的规格如何，所有值都将按原样读取，并且不会被视为缺失值。
df_nan_no_filter = pd.read_csv('C:/Users/81087/Desktop/data/DataFrameTest4.csv',
                               index_col=0, na_filter=False)

# print(df_nan_no_filter)
#           a    b
# ONE          NaN
# TWO       -  nan
# THREE  null  N/A

# print(df_nan_no_filter.isnull())
#            a      b
# ONE    False  False
# TWO    False  False
# THREE  False  False

# 9.tsv的读取
# df_tsv_sep = pd.read_csv('./data/03/sample_header_index.tsv',
# 							index_col=0, sep='\t')
# print(df_tsv_sep)
# #         a   b   c   d
# # ONE    11  12  13  14
# # TWO    21  22  23  24
# # THREE  31  32  33  34

'''04_Pandas获取和修改任意位置的值（at,iat,loc,iloc）'''
# https://blog.csdn.net/qq_18351157/article/details/104838924

df = pd.read_csv('C:/Users/81087/Desktop/data/Pandas4Test.csv', index_col=0)
# 行标签（索引）和列标签（列）的值如下。
# print(df.index.values)  # ['Alice' 'Bob' 'Charlie' 'Dave' 'Ellen' 'Frank']
# print(df.columns.values)  # ['age' 'state' 'point']

# 1.at，iat：选择，获取和更改单个元素的值
# at通过行标签和列标签指定位置。除了获取数据之外，还可以在该位置设置（替换）新值。
# print(df.at['Bob', 'age'])  # 42
# print(df.at['Dave', 'state'])  # TX
# df.at['Bob', 'age'] = 60
# print(df.at['Bob', 'age'])  # 60

# 2.iat通过行号和列号指定位置。行号和列号以0开头。  使用方法同at
# print(df.iat[1, 0])  # 42 或 60

# 3.loc，iloc：选择，获取和更改单个和多个元素的值
# 3.1 选择单个元素的值
# 访问单个值时，它与at和iat相同。 但at和iat的处理速度更快。
# print(df.loc['Bob', 'age'])  # 42
# print(df.loc['Dave', 'state'])  # TX
# df.iloc[1, 0] = 44  # 修改Bob的年龄
# print(df.iloc[1, 0])

# 3.2选择多个元素值
# 要访问多个值，在列表[x，y]或切片[start:stop:step]中指定数据的范围和位置。引用的值将是pandas.Series或pandas.DataFrame。
# 切片的写入方式与普通切片相同。step可以省略。
# print(df.loc['Bob':'Dave', 'age'])
# print(type(df.loc['Bob':'Dave', 'age']))  # <class 'pandas.core.series.Series'>
# # name
# # Bob        42
# # Charlie    18
# # Dave       68
# # Name: age, dtype: int64
#
# print(df.loc[:'Dave', ['age', 'point']])
# print(type(df.loc[:'Dave', 'age':'point']))  # <class 'pandas.core.frame.DataFrame'>
# #          age  point
# # name
# # Alice     24     64
# # Bob       42     92
# # Charlie   18     70
# # Dave      68     70
#
# print(df.iloc[:3, [0, 2]])
# print(type(df.iloc[:3, [0, 2]]))  # <class 'pandas.core.frame.DataFrame'>
# #          age  point
# # name
# # Alice     24     64
# # Bob       42     92
# # Charlie   18     70
#
# # 切片
# print(df.iloc[::2, 0])
# print(type(df.iloc[::2, 0]))  # <class 'pandas.core.series.Series'>
# # name
# # Alice      24
# # Charlie    18
# # Ellen      24
# # Name: age, dtype: int64

# 3.3选择行/列
# 行选择：行名和行号的切片
# 列选择：列名称或列名称列表
# print(df['Bob':'Ellen'])  # Bob Charlie Dave
# print(df[:3])  # 前3行
# print(df['age'])  # age列
# print(df[['age', 'point']])  # age和point列
#
# # 当使用loc和iloc选择行或列时，可以比索引参考df []更灵活地指定它。
# # 在loc和iloc中省略该列，则它将是行引用。也可以选择列表中的多行。
# print(df.loc['Bob'])
# print(type(df.loc['Bob']))  # <class 'pandas.core.series.Series'>
# # age      20
# # state    CA
# # point    92
# # Name: Bob, dtype: object
#
# print(df.iloc[[1, 4]])
# print(type(df.iloc[[1, 4]]))  # <class 'pandas.core.frame.DataFrame'>
# #        age state  point
# # name
# # Bob     20    CA     92
# # Ellen   24    CA     88
#
# # 可以通过将行规范设置为loc和iloc中的（整个切片）来引用列。可以使用索引引用无法完成的切片。也可以在iloc中使用列号。
# print(df.loc[:, 'age':'point'])
# print(type(df.loc[:, 'age':'point']))  # <class 'pandas.core.frame.DataFrame'>
# #          age state  point
# # name
# # Alice     24    NY     64
# # Bob       20    CA     92
# # Charlie   30    CA     70
# # Dave      40    TX     70
# # Ellen     24    CA     88
# # Frank     30    NY     57
#
# print(df.iloc[:, [0, 2]])
# print(type(df.iloc[:, [0, 2]]))  # <class 'pandas.core.frame.DataFrame'>
# #          age  point
# # name
# # Alice     24     64
# # Bob       20     92
# # Charlie   30     70
# # Dave      40     70
# # Ellen     24     88
# # Frank     30     57

# 4.当行名和列名具有重复值时
df_state = pd.read_csv('C:/Users/81087/Desktop/data/Pandas4Test.csv', index_col=2)
# print(df_state)
#           name  age  point
# state
# NY       Alice   24     64
# CA         Bob   42     92
# CA     Charlie   18     70
# TX        Dave   68     70
# CA       Ellen   24     88
# NY       Frank   30     57
# print(df_state.index.values)  # ['NY' 'CA' 'CA' 'TX' 'CA' 'NY']

# 4.1如果在中指定重复的列名，则numpy.ndarray中将返回多个值。
# print(df_state.at['NY', 'age'])  # [24 30]
# print(type(df_state.at['NY', 'age']))  # <class 'numpy.ndarray'>

# 4.2如果在loc中指定重复的列名，则它将在pandas.DataFrame或pandas.Series中返回。
# print(df_state.loc['NY', 'age'])
# print(type(df_state.loc['NY', 'age']))  # <class 'pandas.core.series.Series'>
# # state
# # NY    24
# # NY    30
# # Name: age, dtype: int64
#
# print(df_state.loc['NY', ['age', 'point']])
# print(type(df_state.loc['NY', ['age', 'point']]))  # <class 'pandas.core.frame.DataFrame'>
# #        age  point
# # state
# # NY      24     64
# # NY      30     57

# 4.3可以使用index.is_unique和column.is_unique检查列标签和行标签是否具有唯一值（不重复）。
# print(df_state.index.is_unique)  # False
# print(df_state.columns.is_unique)  # True

# 5.通过数字和标签指定位置
# print(df.index[2])  # Charlie
# print(df.columns[1])  # state
# # 使用at或loc，可以通过数字和标签的组合来指定位置。
# print(df.at[df.index[2], 'age'])  # 18
# print(df.loc[['Alice', 'Dave'], df.columns[1]])
# # name
# # Alice    NY
# # Dave     TX
# # Name: state, dtype: object

# 6.在pandas.Series中选择行时的隐式类型转换
# 如果原始pandas.DataFrame的每一列的数据类型不同，则会执行隐式类型转换。
df_mix = pd.DataFrame({'col_int': [0, 1, 2], 'col_float': [0.1, 0.2, 0.3]}, index=['A', 'B', 'C'])
# print(df_mix)
# #    col_int  col_float
# # A        0        0.1
# # B        1        0.2
# # C        2        0.3
# print(df_mix.dtypes)
# # col_int        int64
# # col_float    float64
# # dtype: object
# 使用loc或iloc提取一行将导致float pandas.Series。 int列中的元素将转换为float。
# print(df_mix.loc['B'])
# # col_int      1.0
# # col_float    0.2
# # Name: B, dtype: float64
# print(type(df_mix.loc['B']))  # <class 'pandas.core.series.Series'>
# # 如果按如下所示编写[]，则将pandas.Series元素转换为float。请注意，元素的值将以与原始类型不同的类型获得。
# print(df_mix.loc['B']['col_int'])  # 1.0
# print(type(df_mix.loc['B']['col_int']))  # <class 'numpy.float64'>
# # 如上所述，最好使用at和iat而不是重复编写[]，loc和iloc。如果是at或iat，则可以获取原始类型的元素。
# print(df_mix.at['B', 'col_int'])  # 1
# print(type(df_mix.at['B', 'col_int']))  # <class 'numpy.int64'>
# # 如果在loc或iloc中指定一个包含1个元素的列表，它将是一行的pandas.DataFrame而不是pandas.Series。
# # 当然，在这种情况下，将保留原始数据类型dtype。
# print(df_mix.loc[['B']])
# #    col_int  col_float
# # B        1        0.2
# print(type(df_mix.loc[['B']]))  # <class 'pandas.core.frame.DataFrame'>
# print(df_mix.loc[['B']].dtypes)
# # col_int        int64
# # col_float    float64
# # dtype: object

'''05_Pandas删除，替换并提取其中的缺失值NaN(dropna,fillna,isnull)'''
# https://blog.csdn.net/qq_18351157/article/details/104993254
import numpy as np
import math
data = {
    'name': ['Alice', np.nan, 'Charlie', 'Dave', 'Ellen', 'Frank'],
    'age': [24.0, np.nan, np.nan, 68.0, np.nan, 30.0],
    'state': ['NY', np.nan, 'CA', 'TX', 'CA', np.nan],
    'point': [np.nan, np.nan, np.nan, 70.0, 88.0, np.nan],
    'other': [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan]
}
df = pd.DataFrame(data)
# 1.Pandas中缺少值NaN的介绍
# 如果列包含任何缺失值NaN，则即使所有其他值均为整数int，该列的dtype也将被视为浮点。
# print(df.dtypes)
# name      object
# age      float64
# state     object
# point    float64
# other    float64
# dtype: object
# 对象类型列的缺失值是内置的float，而浮点类型列的缺失值是NumPy的numpy.float64。数字可能会因环境而异）。
# print(df.at[1, 'name'])  # nan
# print(type(df.at[1, 'name']))  # <class 'float'>
# print(df.at[0, 'point'])  # nan
# print(type(df.at[0, 'point']))  # <class 'numpy.float64'>
# 1.1 检查缺失值
# 使用pandas.isnull（）检查缺失的值。也可以使用numpy.isnan（）和math.isnan（）
# print(pd.isnull(df.at[0, 'point']))
# print(np.isnan(df.at[0, 'point']))
# print(math.isnan(df.at[0, 'point']))
# # True

# 2.将缺失值作为Pandas中的缺少值NaN
# 在Pandas中，将None，np.nan，math.nan视为缺失值NaN.在numpy.float64中，None也转换为nan。
s_nan = pd.Series([None, np.nan, math.nan])
# print(s_nan)
# # 0   NaN
# # 1   NaN
# # 2   NaN
# # dtype: float64
#
# print(s_nan[0])
# print(type(s_nan[0]))
# # nan
# # <class 'numpy.float64'>
#
# print(s_nan.isnull())
# # 0    True
# # 1    True
# # 2    True
# # dtype: bool

# 如上所述，如果包含缺失值，则将整数int类型值强制转换为浮点浮点类型。
# s_nan_int = pd.Series([None, np.nan, 0, 1])
# print(s_nan_int)
# # 0    NaN
# # 1    NaN
# # 2    0.0
# # 3    1.0
# # dtype: float64
#
# print(s_nan_int.isnull())
# # 0     True
# # 1     True
# # 2    False
# # 3    False
# # dtype: bool

# 如果包含字符串str值，则其pandas.Series（和pandas.DataFrame列）数据类型将为object。
# None不会转换为numpy.float64的nan并保持为None
s_nan_str = pd.Series([None, np.nan, 'NaN', 'nan'])
# print(s_nan_str)
# # 0    None
# # 1     NaN
# # 2     NaN
# # 3     nan
# # dtype: object
#
# print(s_nan_str[0])
# print(type(s_nan_str[0]))
# # None
# # <class 'NoneType'>
#
# print(s_nan_str.isnull())
# # 0     True
# # 1     True
# # 2    False
# # 3    False
# # dtype: bool

# 如果有一个您想当作缺失值的值，例如字符串“ NaN”，则可以使用replace（）方法将其替换为缺失值。
# s_nan_str_replace = s_nan_str.replace({'NaN': np.nan, 'nan': np.nan})
# print(s_nan_str_replace)
# # 0   NaN
# # 1   NaN
# # 2   NaN
# # 3   NaN
# # dtype: float64
#
# print(s_nan_str_replace.isnull())
# # 0    True
# # 1    True
# # 2    True
# # 3    True
# # dtype: bool

# 3.缺少值NaN的删除方法
# 3.1使用dropna（）方法删除缺失值。
# 默认情况下，将返回新对象，并且不会更改原始对象，但是参数inplace = True会更改原始对象本身。
# print(df)

# 3.2删除所有值均缺失的行/列
# 如果指定了参数how =‘all’，则将删除所有缺少值的行。
# print(df.dropna(how='all'))
# 如果设置axis = 1，则将删除所有缺少值的列。
# print(df.dropna(how='all',axis=1))
# 如果要同时应用于行和列，则可以重复应用dropna（）
# print(df.dropna(how='all',axis=0).dropna(how='all',axis=1))

# 3.3删除至少包含一个缺失值的行/列
# 如果指定了参数how =‘any’，则将删除至少包含一个缺失值的行。默认值为how =‘any’。
df2 = df.dropna(how='all',axis=0).dropna(how='all',axis=1)  # 删除所有行和列都为空的值
# print(df2.dropna(axis=1, how='any'))
# print(df2.dropna(axis=0, how='any'))

# 3.4根据不缺少值的元素数量删除行/列
# 通过在参数thresh中指定数字，可以根据不缺少值的元素数量删除行和列。当非NaN的值多于3个时,数据就会被保留.而不是看NaN的数量!
# print(df.dropna(thresh=3))  # NaN大于3个就删除整行
# #     name   age state  point  other
# # 0  Alice  24.0    NY    NaN    NaN
# # 3   Dave  68.0    TX   70.0    NaN
# # 4  Ellen   NaN    CA   88.0    NaN
# print(df.dropna(thresh=3,axis=1))
# #       name   age state
# # 0    Alice  24.0    NY
# # 1      NaN   NaN   NaN
# # 2  Charlie   NaN    CA
# # 3     Dave  68.0    TX
# # 4    Ellen   NaN    CA
# # 5    Frank  30.0   NaN

# 3.5删除特定行/列中缺少值的列/行
# 如果要基于特定的行/列删除，请在列表的参数子集中指定要定位的行/列标签。由于它必须是列表，因此请至少指定一个目标.
# 例如subset = [‘name’]。 默认情况下，子集指定的列中缺少值的行将被删除。
# print(df.dropna(subset=['age']))  # 针对age列,如果为NaN,则删除该行
# #     name   age state  point  other
# # 0  Alice  24.0    NY    NaN    NaN
# # 3   Dave  68.0    TX   70.0    NaN
# # 5  Frank  30.0   NaN    NaN    NaN
#
# # 如果指定了多列，则默认为删除所有缺少指定值的行。
# print(df.dropna(subset=['age', 'state']))
# #     name   age state  point  other
# # 0  Alice  24.0    NY    NaN    NaN
# # 3   Dave  68.0    TX   70.0    NaN
# # 如果参数how =‘all’，则仅删除所有指定列均缺少值的行。
# print(df.dropna(subset=['age', 'state'], how='all'))
# #       name   age state  point  other
# # 0    Alice  24.0    NY    NaN    NaN
# # 2  Charlie   NaN    CA    NaN    NaN
# # 3     Dave  68.0    TX   70.0    NaN
# # 4    Ellen   NaN    CA   88.0    NaN
# # 5    Frank  30.0   NaN    NaN    NaN

# 如果axis = 1，则删除子集指定的行中缺少值的列。参数how也可以使用。
# print(df.dropna(subset=[0, 4], axis=1))  # 看0行和4行,如果这2行中有列是NaN的,那么就删除这一列,例如第4行的age列为NaN,所以没有age列
#       name state
# 0    Alice    NY
# 1      NaN   NaN
# 2  Charlie    CA
# 3     Dave    TX
# 4    Ellen    CA
# 5    Frank   NaN

# print(df.dropna(subset=[0, 4], axis=1, how='all'))  # 看0行和4行,如果这2行中所有列都是NaN,那么就删除这一列
#       name   age state  point
# 0    Alice  24.0    NY    NaN
# 1      NaN   NaN   NaN    NaN
# 2  Charlie   NaN    CA    NaN
# 3     Dave  68.0    TX   70.0
# 4    Ellen   NaN    CA   88.0
# 5    Frank  30.0   NaN    NaN

# 3.6pandas.Series
# 如果数据是一维pandas.Series，则只需调用dropna（）。缺少的值将被删除。
# s = df['age']
# print(s)
# # 0    24.0
# # 1     NaN
# # 2     NaN
# # 3    68.0
# # 4     NaN
# # 5    30.0
# # Name: age, dtype: float64
#
# print(s.dropna())
# # 0    24.0
# # 3    68.0
# # 5    30.0
# # Name: age, dtype: float64

# 4.替换（填充）缺失值
# 可以使用fillna（）方法将缺失值替换为任意值。
# 默认情况下，将返回新对象，并且不会更改原始对象，但是参数inplace = True会更改原始对象本身。

# 4.1用通用值统一替换
# 如果指定要用参数替换的值，则所有缺少的值NaN都将替换为该值。
# print(df.fillna(0))
#       name   age state  point  other
# 0    Alice  24.0    NY    0.0    0.0
# 1        0   0.0     0    0.0    0.0
# 2  Charlie   0.0    CA    0.0    0.0
# 3     Dave  68.0    TX   70.0    0.0
# 4    Ellen   0.0    CA   88.0    0.0
# 5    Frank  30.0     0    0.0    0.0

# 4.2为每列替换不同的值
# 将字典指定为参数时，每列将替换一个不同的值。字典键是列标签（列名），而值是要替换的值。未指定的列仍缺少值NaN。
# print(df.fillna({'name': 'XXX', 'age': 20, 'point': 0}))
#       name   age state  point  other
# 0    Alice  24.0    NY    0.0    NaN
# 1      XXX  20.0   NaN    0.0    NaN
# 2  Charlie  20.0    CA    0.0    NaN
# 3     Dave  68.0    TX   70.0    NaN
# 4    Ellen  20.0    CA   88.0    NaN
# 5    Frank  30.0   NaN    0.0    NaN

# 不仅可以指定字典，还可以指定pandas.Series。具有与pandas.Series中的标签匹配的列标签（列名）的列中缺少的值将替换为pandas.Series值。
# 与pandas.Series标签不对应的列仍然缺少值。
# s_for_fill = pd.Series(['ZZZ', 100], index=['name', 'age'])
# print(s_for_fill)
# # name    ZZZ
# # age     100
# # dtype: object
#
# print(df.fillna(s_for_fill))
# #       name    age state  point  other
# # 0    Alice   24.0    NY    NaN    NaN
# # 1      ZZZ  100.0   NaN    NaN    NaN
# # 2  Charlie  100.0    CA    NaN    NaN
# # 3     Dave   68.0    TX   70.0    NaN
# # 4    Ellen  100.0    CA   88.0    NaN
# # 5    Frank   30.0   NaN    NaN    NaN

# 4.3用每列的平均值，中位数，众数等替换
# 将相应列中的缺失值替换为平均值。
# print(df.fillna(df.mean(numeric_only = True)))  # numeric_only只考虑数字列
#       name        age state  point  other
# 0    Alice  24.000000    NY   79.0    NaN
# 1      NaN  40.666667   NaN   79.0    NaN
# 2  Charlie  40.666667    CA   79.0    NaN
# 3     Dave  68.000000    TX   70.0    NaN
# 4    Ellen  40.666667    CA   88.0    NaN
# 5    Frank  30.000000   NaN   79.0    NaN
# 替换中位数
# print(df.fillna(df.median()))
# 众数,如果数量相同,返回第一个非NaN的值
# print(df.fillna(df.mode().iloc[0]))
# print(df.mode().iloc[0])
# # name     Alice
# # age       24.0
# # state       CA
# # point     70.0
# # other      NaN
# # Name: 0, dtype: object

# 4.4替换为上一个或下一个值
#  如果method =‘ffill’，它将被以前的值替换；如果method =‘bfill’，将被后面的值替换。对于时间序列数据很有用。
# print(df.fillna(method='ffill'))
# #       name   age state  point  other
# # 0    Alice  24.0    NY    NaN    NaN
# # 1    Alice  24.0    NY    NaN    NaN
# # 2  Charlie  24.0    CA    NaN    NaN
# # 3     Dave  68.0    TX   70.0    NaN
# # 4    Ellen  68.0    CA   88.0    NaN
# # 5    Frank  30.0    CA   88.0    NaN
#
# print(df.fillna(method='bfill'))
# #       name   age state  point  other
# # 0    Alice  24.0    NY   70.0    NaN
# # 1  Charlie  68.0    CA   70.0    NaN
# # 2  Charlie  68.0    CA   70.0    NaN
# # 3     Dave  68.0    TX   70.0    NaN
# # 4    Ellen  30.0    CA   88.0    NaN
# # 5    Frank  30.0   NaN    NaN    NaN

# 4.5指定连续更换的最大数量
# 使用参数limit，可以指定连续替换的最大数量。
# print(df.bfill(limit=1))  # 只有最近的1行才能填充
#       name   age state  point  other
# 0    Alice  24.0    NY    NaN    NaN
# 1  Charlie   NaN    CA    NaN    NaN
# 2  Charlie  68.0    CA   70.0    NaN
# 3     Dave  68.0    TX   70.0    NaN
# 4    Ellen  30.0    CA   88.0    NaN
# 5    Frank  30.0   NaN    NaN    NaN

# 4.6pandas.Series
# s = df['age']
# print(s)
# # 0    24.0
# # 1     NaN
# # 2     NaN
# # 3    68.0
# # 4     NaN
# # 5    30.0
# # Name: age, dtype: float64
#
# print(s.fillna(100))
# # 0     24.0
# # 1    100.0
# # 2    100.0
# # 3     68.0
# # 4    100.0
# # 5     30.0
# # Name: age, dtype: float64
#
# print(s.fillna({1: 100, 4: 0}))
# # 0     24.0
# # 1    100.0
# # 2      NaN
# # 3     68.0
# # 4      0.0
# # 5     30.0
# # Name: age, dtype: float64
#
# print(s.fillna(method='bfill', limit=1))
# # 0    24.0
# # 1     NaN
# # 2    68.0
# # 3    68.0
# # 4    30.0
# # 5    30.0
# # Name: age, dtype: float64

# 5.提取缺失值
# 5.1提取特定行/列中缺少值的列/行

# print(df['point'].isnull())
# # 0     True
# # 1     True
# # 2     True
# # 3    False
# # 4    False
# # 5     True
# # Name: point, dtype: bool
#
# print(df[df['point'].isnull()])
# #       name   age state  point  other
# # 0    Alice  24.0    NY    NaN    NaN
# # 1      NaN   NaN   NaN    NaN    NaN
# # 2  Charlie   NaN    CA    NaN    NaN
# # 5    Frank  30.0   NaN    NaN    NaN

# 选择在特定行中包含缺失值的列时，想法是相同的。使用loc []按行名（行标签）选择，并使用iloc []按位置选择。
# print(df.iloc[2].isnull())
# # name     False
# # age       True
# # state    False
# # point     True
# # other     True
# # Name: 2, dtype: bool
#
# print(df.loc[:, df.iloc[2].isnull()])
# #     age  point  other
# # 0  24.0    NaN    NaN
# # 1   NaN    NaN    NaN
# # 2   NaN    NaN    NaN
# # 3  68.0   70.0    NaN
# # 4   NaN   88.0    NaN
# # 5  30.0    NaN    NaN

# 6.提取至少包含一个缺失值的行/列
# pandas.DataFrame isnull（）方法确定每个元素是否为缺失值，并返回为True或False的pandas.DataFrame。
# print(df2.isnull())
# #     name    age  state  point
# # 0  False  False  False   True
# # 2  False   True  False   True
# # 3  False  False  False  False
# # 4  False   True  False  False
# # 5  False  False   True   True
# # 如果任何行或列包含True，则any方法将返回True。如果参数axis= 1，则在该行上执行处理。
# print(df2.isnull().any(axis=1))
# # 0     True
# # 2     True
# # 3    False
# # 4     True
# # 5     True
# # dtype: bool
#
# print(df2[df2.isnull().any(axis=1)])
# #       name   age state  point
# # 0    Alice  24.0    NY    NaN
# # 2  Charlie   NaN    CA    NaN
# # 4    Ellen   NaN    CA   88.0
# # 5    Frank  30.0   NaN    NaN
# # 提取列时也是如此。如果any（）的参数轴设置为0，则对列执行处理。可以省略，因为默认值为axis = 0。
# print(df2.isnull().any())
# # name     False
# # age       True
# # state     True
# # point     True
# # dtype: bool
#
# print(df2.loc[:, df2.isnull().any()])
# #     age state  point
# # 0  24.0    NY    NaN
# # 2   NaN    CA    NaN
# # 3  68.0    TX   70.0
# # 4   NaN    CA   88.0
# # 5  30.0   NaN    NaN


