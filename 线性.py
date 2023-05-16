import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

f=open('D:\workspace\线性回归\ex1data1.txt', encoding='gbk')
x=[]
y=[]
plt.figure(figsize=(10, 10))  # figsize:确定画布大小
for line in f:
    a=line.split("\n")
    a=a[0].split(",")
    x.append(a[0])
    y.append(a[1])
x=np.array(x)
x=x.astype(float)
y=np.array(y)
y=y.astype(float)
coef=np.polyfit(x,y,1)
poly_fit=np.poly1d(coef)
plt.plot(x,poly_fit(x),'g',label="xianxing")
plt.scatter(x,  # 横坐标
           y,  # 纵坐标
            c='red',  # 点的颜色
            label='function')  # 标签 即为点代表的意思

# 3.展示图形
plt.legend()  # 显示图例

plt.show()  # 显示所绘图形
