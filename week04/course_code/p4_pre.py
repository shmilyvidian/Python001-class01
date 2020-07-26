import numpy as np
import pandas as pd

x = pd.Series([1, 2, 3, 4, np.nan, 6, np.nan])

x.hasnans
x.fillna(value=x.mean())  # 将控制填充为平均值

y = pd.DataFrame({'A': [5, 3, None, 5], 'B': [3, None, None, 6], 'C': [
                 None, 1, 2, 5], 'D': [5, 3, None, 5]})
y.isnull().sum()  # 缺看缺失值汇总
y.ffill()  # 用上一行填充
y.ffill(axis=1)  # 用前一列进行填充
y.info()  # 缺失值删除
y.dropna()  # 删除空值
y.fillna('无')
y.drop_duplicates()  # 删除重复值
