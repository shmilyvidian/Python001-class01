import numpy as np
import pandas as pd

y = pd.DataFrame({'A': [5, 3, None, 5], 'B': [3, None, None, 6], 'C': [
                 None, 1, 2, 5], 'D': [5, 3, None, 5]})

y[['A', 'C']]  # 取出AC两列
y.iloc[:, [0, 2]]  # 取出所有行，和第一列和第三列

y.loc[[0, 2]]  # 取出第一行和第三行
y.loc[0:2]  # 取出第一行到第三行

y[(y['A'] < 4) & y['C'] > 0]
y['A'].replace(5, 50)
y['A'].replace(np.nan, 88)
y.replace([2, 3], 66)
y.replace({2: 20, 6: 60})
y.sort_values(by=['A'], ascending=False)

d = pd.DataFrame([
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
],
    columns=['one', 'two', 'third'],
    index=['first', 'second']
)
d.stack()
d.stack().reset_index()
d.unstack()

y.drop('A', axis=1)

y.T
