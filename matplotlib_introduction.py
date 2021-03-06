import matplotlib.pyplot as plt

# 查看可用的绘图样式
print(plt.style.available)
plt.style.use('seaborn-darkgrid')

# 指定高/宽的比例，比如1：2
# fig = plt.figure(figsize=plt.figaspect(0.5))
# plt.plot()
# plt.savefig("1.png")

# Lets manually add axis for x axis
import numpy as np
# fig是画布，axes是坐标系，axis是坐标轴
fig = plt.figure()
ax = fig.add_subplot(111)
theta = np.linspace(-np.pi, np.pi, 100)
# '--'、'-.'、'-'、':'等不同的线样式
plt.plot(theta, np.sin(theta), ls=':')
ax.set_xlim(-np.pi, np.pi/2)  # 设置x轴区间
plt.savefig("1.png")

# Temperature data obtained from NASA: https://data.giss.nasa.gov/gistemp/
surface_temp_change = '-0.29,-0.1,0.11,-0.33,-0.18,-0.64,-0.42,-0.65,-0.42,-0.2,-0.47,-0.46,-0.25,-0.68,-0.55,-0.43,' \
                      '-0.22,-0.22,-0.06,-0.17,-0.39,-0.28,-0.18,-0.27,-0.63,-0.38,-0.3,-0.43,-0.45,-0.69,-0.43,-0.62,' \
                      '-0.26,-0.42,0.02,-0.18,-0.17,-0.46,-0.42,-0.2,-0.14,-0.03,-0.33,-0.25,-0.23,-0.32,0.21,-0.28,' \
                      '-0.02,-0.47,-0.29,-0.1,0.14,-0.34,-0.26,-0.36,-0.28,-0.1,0.0,-0.12,-0.15,0.13,0.26,0.0,0.41,0.13' \
                      ',0.15,-0.13,0.05,0.09,-0.3,-0.35,0.16,0.09,-0.28,0.11,-0.16,-0.14,0.39,0.06,-0.01,0.07,0.08,' \
                      '-0.03,-0.06,-0.09,-0.16,-0.06,-0.23,-0.11,0.09,-0.03,-0.24,0.28,-0.15,0.07,0.0,0.18,0.08,0.14,' \
                      '0.3,0.56,0.09,0.52,0.3,0.21,0.29,0.36,0.56,0.15,0.4,0.42,0.45,0.37,0.3,0.5,0.27,0.32,0.61,0.48,' \
                      '0.26,0.44,0.75,0.73,0.59,0.71,0.58,0.96,0.25,0.62,0.73,0.51,0.46,0.68,0.73,0.82,1.13,0.9'
surface_temp_change_arr = np.fromstring(surface_temp_change, sep=",")
surface_temp_year = np.array(range(1880, 2018))
fig = plt.figure(figsize=plt.figaspect(0.5))
ax = fig.add_subplot(111)
ax.plot(surface_temp_year, surface_temp_change_arr, label='Global Surface Temp Change')
ax.set_ylabel('Temperature (deg C)')
ax.set_xlabel('Month of January')
ax.set_title("A tale of Global Warming")
ax.legend()  # 创建图例

# CO2 data obtained from http://cdiac.ornl.gov/CO2_Emission/timeseries/global
co2_emission_str = '865.412,891.081,938.752,997.424,1008.425,1015.759,1030.427,1081.765,1199.109,1199.109,1305.452,' \
                   '1364.124,1371.458,1356.79,1404.461,1488.802,1536.473,1613.48,1705.155,1859.169,1958.178,2024.184,' \
                   '2075.522,2262.539,2288.208,2431.221,2592.569,2874.928,2750.25,2878.595,3003.273,3065.612,3223.293,' \
                   '3457.981,3116.95,3072.946,3303.967,3501.985,3432.312,2955.602,3417.644,2944.601,3098.615,3556.99,' \
                   '3531.321,3575.325,3604.661,3894.354,3905.355,4198.715,3861.351,3446.98,3105.949,3274.631,3567.991,' \
                   '3766.009,4143.71,4433.403,4187.714,4371.064,4763.433,4891.778,4921.114,5100.797,5071.461,4253.72,' \
                   '4539.746,5104.464,5386.823,5203.473,5977.21,6479.589,6582.265,6750.947,6838.955,7488.014,7983.059,' \
                   '8324.09,8544.11,8998.818,9420.523,9460.86,9849.562,10388.611,10982.665,11477.71,12057.096,12442.131' \
                   ',13076.522,13861.26,14862.351,15430.736,16046.792,16919.538,16952.541,16853.532,17836.288,18393.672' \
                   ',18606.358,19644.119,19438.767,18841.046,18679.698,18610.025,19281.086,19864.139,20472.861,' \
                   '20993.575,21767.312,22244.022,22354.032,22629.057,22405.37,22383.368,22764.736,23263.448,23802.497,' \
                   '24161.863,24095.857,24051.853,24667.909,25250.962,25470.982,27014.789,28364.245,29427.675,30461.769' \
                   ',31125.496,32042.246,31686.547,33505.379,34865.836,35463.557,35848.592'
co2_emissions_arr = np.fromstring(co2_emission_str, sep=",")
# Share x axis，双轴图
ax2 = ax.twinx()
ax2.plot(surface_temp_year[:-4], co2_emissions_arr, label='CO2 emission', color='orange')
ax2.set_ylabel('Million Tons of $CO_2$')
ax.legend(loc="upper left")  # 创建图例
ax2.legend(loc="lower right")
# turn off grids for CO2
ax2.grid(False, which='both')
plt.savefig("2.png")