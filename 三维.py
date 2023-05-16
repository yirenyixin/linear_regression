import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import *
from mpl_toolkits.mplot3d import Axes3D
f=open('D:\workspace\线性回归\ex1data2.txt', encoding='gbk')
x=[]
y=[]
z=[]
for line in f:
    a=line.split("\n")
    a=a[0].split(",")
    x.append(a[0])
    y.append(a[1])
    z.append(a[2])
x=np.array(x)
x=x.astype(float)
y=np.array(y)
y=y.astype(float)
z=np.array(z)
z=z.astype(float)


ax = plt.subplot(projection = '3d')  # 创建一个三维的绘图工程
ax.set_title('3d_image_show')  # 设置本图名称
ax.scatter(x, y, z, c = 'r')   # 绘制数据点 c: 'r'红色，'y'黄色，等颜色

ax.set_xlabel('X')  # 设置x坐标轴
ax.set_ylabel('Y')  # 设置y坐标轴
ax.set_zlabel('Z')  # 设置z坐标轴
plt.show()