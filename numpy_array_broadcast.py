import numpy as np
arr1 = np.random.randint(1, 40, 5)
num = 5
print("Arr1: \n{}".format(arr1), end="\n\n")
print("num : \n{}".format(num), end="\n\n")
print("Sum : \n{}".format(arr1+num), end="\n\n")

# broadcast允许不同维度的array进行维度扩展后的算数运算，但是维度匹配上必须遵循三个规则
# 1.If the two arrays differ in their number of dimensions, the shape of the one with fewer dimensions is
#   padded with ones on its leading (left) side.
# 2.If the shape of the two arrays does not match in any dimension, the array with shape equal to 1 in that
#   dimension is stretched to match the other shape.
# 3.If in any dimension the sizes disagree and neither is equal to 1, an error is raised.
arr1 = np.ones((3, 4))
arr2 = np.arange(4)
print("Arr1: \n{}".format(arr1), end="\n\n")
print("Arr2: \n{}".format(arr2), end="\n\n")
print("Arr1 + Arr2: \n{}".format(arr1 + arr2), end="\n\n")

# 矩阵转置
print("Arr1: \n{}".format(arr1))
print("arr1.shape: {}".format(arr1.shape), end="\n\n")
print("Arr1 Transpose: \n{}".format(arr1.T))
print("arr1.T.shape: {}".format(arr1.T.shape))

# aggregation统计特性
arr = np.random.randint(1, 700, 10000)
print("Sum of 1D: {}".format(np.sum(arr)))

arr2d = np.random.uniform(1, 700, (3, 4))
print("Sum of 2D: {}".format(np.sum(arr2d)))

print("Max of 1D arr: {}".format(np.max(arr)))
print("Min of 1D arr: {}".format(np.min(arr)))
print("Max of 2D arr: {}".format(np.max(arr2d)))
print("Min of 2D arr: {}".format(np.min(arr2d)))

# ⭐️axis = 0输出一行，每个元素表示每列中的选定值，axis = 1输出一列，每个元素表示每行中的选定值
print("2D Array: \n{}".format(arr2d), end="\n\n")
print("Max of 2D arr along axis 0: {}".format(np.amax(arr2d, axis=0)))
print("Min of 2D arr along axis 0: {}".format(np.amin(arr2d, axis=0)))

print("2D Array: \n{}".format(arr2d), end="\n\n")
print("Std along axis 0: \n{}".format(np.std(arr2d, axis=0)))
print("Std along axis 1: \n{}".format(np.std(arr2d, axis=1)))