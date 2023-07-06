import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl

x=np.random.randn(1000)
#boxplot()用于绘制箱线图
plt.boxplot(x)
plt.xticks([1],["随机数生成器rm"])
plt.ylabel("随机数值")
plt.title("随机数抗干扰的稳定性")
plt.show()