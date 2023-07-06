import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl

# 用errorbar()绘制误差棒图
# 设置中文字体为SimHei
mpl.rcParams['font.sans-serif'] = ['SimHei']


x=np.linspace(0.1,0.6,6)
y=np.exp(x)
plt.errorbar(x,y,fmt="bo:",yerr=0.2,xerr=0.02)
plt.xlim(0,0.7)
plt.title("误差棒图")
plt.show()