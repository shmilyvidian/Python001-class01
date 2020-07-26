import pandas as pd

df1 = pd.DataFrame(['a', 'b', 'c', 'd'])

df2 = pd.DataFrame([
    ['a', 'b'],
    ['c', 'd']
])

# 自定义列索引
df2.columns = ['one', 'two']

# 自定义行索引
df2.index = ['first', 'second']

# 可以在创建直接指定 DataFrame([],columns='',index='')
# 查看索引
df2.columns, df2.index
type(df2.values)
