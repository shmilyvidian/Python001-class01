import pandas as pd
import numpy as np
import re
pd.Series(['a', 'b', 'c'])

s1 = pd.Series({'a': 11, 'b': 22, 'c': 33})
s2 = pd.Series([11, 22, 33], index=['a', 'b', 'c'])

s1
s2

s1.index
s1.values
# 将pandas类型转为Python列表
s1.values.tolist()

arr = pd.Series([1, 2, 3, 4, 5])
mask = arr.map(lambda x: x > 3)
print(mask)
