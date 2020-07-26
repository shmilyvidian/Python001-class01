import numpy as np
import pandas as pd


y = pd.DataFrame({'A': [5, 3, None, 5], 'B': [3, None, None, 6], 'C': [
                 None, 1, 2, 5], 'D': [5, 3, None, 5]})

y['A'] + y['D']

y['B'] + 3

y.count() # 非空值的数量
y['B'].sum()
y['B'].mean()
y['B'].max()

