# -*- coding: UTF-8 -*-
import pandas as pd
# 常用时间函数
# import pandas as pd
# print(pd.Timestamp.min,pd.Timestamp.max)  # Timestamp类时间是有限制的
# ************************************************************************************************************

# to_datetime()函数
# print(pd.to_datetime('today'))  # 今天时间

d = {'name': ['Tom', 'Jack', 'Xin'],
     'dates_str': ['2023-04-01', '2023-04-02', '2023-04-03']}
df = pd.DataFrame(d)
df['dates_str'] = pd.to_datetime(df['dates_str'])
# print(df.dtypes)

# 计算
df['day'] = (pd.to_datetime('today') - df['dates_str']).dt.days
# print(df)

# strftime() 日期格式化
# .dt访问器允许你访问这些日期时间数据或时间差数据的各种属性和方法，比如年份、月份、小时等，或者进行格式化。
# df['dates_str'] = df['dates_str'].dt.strftime('%Y-%m-%d %H:%M:%S')
# print(df)

# 时间列设置为索引列
# 切片
# 1.推荐
# df.set_index('dates_str', inplace=True)
# start_date = pd.to_datetime('2023-04-01',format='%Y-%m-%d')
# end_date = pd.to_datetime('2023-04-02',format='%Y-%m-%d')
# sliced_df = df.loc[start_date:end_date]
# print(sliced_df)
# 2.
# print(df['2023-04-01':'2023-04-02'])
# 3.
# sliced_df = df.iloc[0:2]
# print(sliced_df)
# 取值
# value = df.loc['2023-04-01 00:00:00', 'name']
# print(value)


