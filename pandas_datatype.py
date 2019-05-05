import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn-darkgrid')

# 两种方法创建Series
ob = pd.Series([8, 7, 6, 5], name='test_data')
print('Name: ', ob.name)
print('Data:\n', ob)
print('Type of Object: ', type(ob))
print('Type of elements:', type(ob.values))
# integers between 5 to 8 (reversed)
ob = pd.Series(np.linspace(5, 8, num=4, dtype=int)[::-1], name='test_data')
print(ob)
print(type(ob))
print("="*40)

# 自己设置Series的index
ob = pd.Series([8, 7, 6, 5], index=['a', 'b', 'c', 'd'])
print(ob['b'])
# select all the values greater than 4 and less than 8
print(ob[(ob > 4) & (ob < 8)])
print("="*40)

# 自己设置Series的index，并更改
states_dict = {'State1': 'Alabama',
               'State2': 'California',
               'State3': 'New Jersey',
               'State4': 'New York'}
ob = pd.Series(states_dict)
print(ob)
print(type(ob))
ob.index = ['AL', 'CA', 'NJ', 'NY']
print(ob)
print(ob.get('CA', np.nan))
print("="*80)

# ===========================
# ===========================
# ===========================

# Dataframe的创造方法1
data = {'one': pd.Series([1., 2., 3.], index=['a', 'b', 'c']),
        'two': pd.Series([1., 2., 3., 4.], index=['a', 'b', 'c', 'd'])}
df = pd.DataFrame(data)
print('Dataframe:\n', df)
print('Type of Object:', type(df))
print('Type of elements:', type(df.values))
print('Index: ', df.index)
print('Columns: ', df.columns)
print('Values of Column one: ', df['one'].values)
print('Values of Column two: ', df['two'].values)
print("="*40)
# Dataframe的创造方法2
df2 = pd.DataFrame([{'a': 1, 'b': 2, 'c': 3, 'd': None},
                    {'a': 2, 'b': 2, 'c': 3, 'd': 4}],
                   index=['one', 'two'])
print('Dataframe: \n', df2)
# Of course you can also transpose the result:
print('Transposed Dataframe: \n', df2.T)
print("="*40)

# 对Dataframe进行处理
df['three'] = None
print('Added third column: \n',df)
# The del keyword can be used delete columns:
del df['three']
# You can also use df.drop(). We shall see that later
print('\nDeleted third column: \n',df)
# 查找元素
print(1 in df.one.values)
print('one' in df.columns)
# ⭐️Reindex in descending order.根据给定索引重排列元素，没有的索引有不同的填充方式
print(df.reindex(['d','c','b','a']))
print(df.reindex(['a','b','c','d','e']))
print(df.reindex(['a','b','c','d','e'], fill_value=0))
print(df.reindex(['a','b','c','d','e'], method='ffill'))
# Drop row c and row a; axis默认为0，即行
print(df.drop(['c', 'a']))
print(df.drop(['two'], axis=1))
# Slicing and selecting only column `one` for row 0 and row 4
print(df['one']['a':'d'])
print(df.loc[['a','c'],['one']])
print(df[df.one > 1])

# ⭐️Dataframe排序
dt = pd.Series(np.random.randint(3, 10, size=7), index=['g','c','a','b','e','d','f'])
print('Original Data: \n', dt, end="\n\n")
print('Sorted by Index: \n', dt.sort_index())
print('Sorted by Values: \n', dt.sort_values())

# Data的计算（包含对齐）
df1 = pd.DataFrame(np.random.randn(10, 4), columns=['A', 'B', 'C', 'D'])
df2 = pd.DataFrame(np.random.randn(7, 3), columns=['A', 'B', 'C'])
print('df1:\n',df1, end="\n\n")
print('df2:\n',df2, end="\n\n")
# 不足的地方用NAN填充
print('Sum:\n',df1.add(df2))
# ⭐️不足的地方用指定数字填充
print('Sum:\n',df1.add(df2, fill_value=0))

# ===========================
# ===========================
# ===========================

# ⭐️DataFrame和Series之间的计算
# 取出一行然后每行减掉
print("Dataframe: \n", df1, end="\n\n")
print("Operand (0th row): \n", df1.loc[0], end="\n\n")
print('Subtraction: \n', df1.sub(df1.loc[0]))
# 在日期等特殊情况下，会按照列进行处理
ind1 = pd.date_range('06/1/2017', periods=10)
print(df1.set_index(ind1))

# ===========================
# ===========================
# ===========================

# 在dataframe上执行numpy的函数
print(np.abs(df1))
# ⭐️⭐️apply函数：对每一列或者每一行执行函数
def fn(x):
    """
    Get max and min of the columns
    """
    return pd.Series([x.min(), x.max()], index=['min', 'max'])
print(df1.apply(fn))
# ⭐⭐️apply️map函数：对每一个元素执行函数
fmt = lambda x: "{:.3f}".format(x)
print(df1.applymap(fmt))