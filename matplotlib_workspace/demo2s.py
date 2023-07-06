import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl

# 用scatter绘制气泡图
a=np.random.randn(100)
b=np.random.randn(100)
# a和b：这是两个数组，分别表示散点图中每个点的x和y坐标。它们用于确定每个散点的位置。

# s：这是一个数组，用于指定每个散点的大小。在给定代码中，s的值通过对a和b进行一些计算来确定，具体为np.power(10*a+20*b,2)。这意味着每个散点的大小由计算得到，并与其对应的a和b值相关。

# c：这是一个数组，用于指定每个散点的颜色。在给定代码中，c的值为np.random.rand(100)，即一个长度为100的随机值数组。这些随机值将被映射到cmap=mpl.cm.RdYlBu所定义的颜色映射中，以决定每个散点的颜色。

# cmap：这是颜色映射（Color Map），用于将c的值映射到相应的颜色。在给定代码中，使用的颜色映射是mpl.cm.RdYlBu，表示从红色（Red）到黄色（Yellow）再到蓝色（Blue）的渐变色系。

# marker：这是散点图中每个点的标记样式。在给定代码中，使用的标记样式是"o"，表示使用圆圈作为散点的标记。
plt.scatter(a,b,s=np.power(10*a+20*b,2),c=np.random.rand(100),cmap=mpl.cm.RdYlBu,marker="o")

plt.show()