import matplotlib.pyplot as plt
plt.style.use('seaborn-darkgrid')
import numpy as np
import pandas as pd

global_co2_emission = pd.read_csv('global_co2_emission.csv')
print(global_co2_emission)

fig = plt.figure()
ax = fig.add_subplot(111)
theta = np.linspace(-np.pi, np.pi, 50)
plt.scatter(theta, np.sin(theta), marker="p")

N = 50
x = np.random.rand(N)
y = np.random.rand(N)
colors = np.random.rand(N)
area = np.pi * (15 * np.random.rand(N))**2  # 0 to 15 point radii，散点覆盖的区域大小
fig = plt.figure()
plt.scatter(x, y, s=area, c=colors, alpha=0.5, cmap='gist_earth')
plt.colorbar()  # 图例，色彩条

fig, ax = plt.subplots(figsize=(15,7))
ax.bar(global_co2_emission['Year'], global_co2_emission['Total'],
        width=0.5, align='center', color='#34495e')  # RGBA：color = (1.0, 0.0, 0.0, 1.0)，最后一个参数是alpha（透明度）
'''
查看所有颜色对应的色号
import matplotlib
for name, hex in matplotlib.colors.cnames.items():
    print(name, hex)
'''
ax.set_xticks(global_co2_emission['Year'][::10])  # 将X轴每10位标记出一个
ax.set_xlabel('Year')
ax.set_ylabel('Million Tons of $CO_2$')
ax.set_title('Global $CO_2$ emissions')

bars = plt.bar([1, 2, 3, 4], [10, 12, 15, 17])
# add hatches to the first bar
plt.setp(bars[0], hatch='x-',)  # setp是对已经画好的内容进行再加工的方法

# 饼图
labels = ['Samsung', 'Apple', 'Huawei', 'Oppo', 'Vivo', 'Others']
market_share = [21, 12.5, 9.3, 7.1, 5.9, 44.2]
explode = [0.2, 0, 0, 0, 0, 0]  # 每块饼区域是否要离开圆心
fig, ax = plt.subplots()
ax.pie(market_share, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
# Equal aspect ratio so that we get a circle
ax.axis('equal')

# 直方图
# Random numbers from normal distribution
data = np.random.randn(1000)
print("Max: ", data.max())
print("Min: ", data.min())
fig, ax = plt.subplots()
ax.hist(data, bins=30, normed=True, alpha=0.8,
         histtype='barstacked', color='lightcoral',
         edgecolor='none')

# ⭐️用matpotlib进行图像分析
import scipy.misc
racoon = scipy.misc.face()
fig, ax = plt.subplots()
ax.imshow(racoon)
# disable the grid lines and axis
ax.grid(False)
ax.axis('off')
plt.savefig("racoon.png")
# The image is a 3-D numpy array.. 3D = Red, Green, Blue，查看图像的RGB值特性及分布
print('Type: ', type(racoon))
# An RGB image should have a shape of rows x cols x 3
print("Shape: ", racoon.shape)
# Lets check the dtype，dype of uint8 means a range of 0 - 255
print("Dtype: ", racoon.dtype)
# Great, now lets plot the red, green and blue color channels
fig, axes = plt.subplots(nrows=3, ncols=2, figsize=(15, 15))
colors = ['red', 'green', 'dodgerblue']
for i in range(3):
    axes[i][0].imshow(racoon[:,:,i])
    axes[i][1].hist(racoon[:,:,i].ravel(), bins=255, alpha=0.3, color=colors[i])
plt.savefig("racoon_rgb.png")
# For Red channel
counts, bins = np.histogram(racoon[:,:,0], bins=255)
print("Counts: ", counts)