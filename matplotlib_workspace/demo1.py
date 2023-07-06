import matplotlib.pyplot as plt
import numpy as np

# linesapce产生一个区间内均匀的点
# 在这里的画图中无法画出完美连续的函数图像，只能是取尽可能多得点模拟更加平滑的效果，这里就取的1000个点
x=np.linspace(0.05,10,1000 )
y=np.cos(x)
y1=np.random.randn(1000)


#plot和scatter都是绘图函数，线和点，参数顺序为xyz轴
plt.plot(x,y,ls='-',lw=2,label='sin')
plt.scatter(x,y1,label="scatterpot")

# 设置绘图中轴的显示范围
plt.xlim(0.05,1)
plt.ylim(0,2)

# 设置轴的标签
plt.xlabel("x")
plt.ylabel("y")

#绘制带刻度线的网格 ls=linestyle color=r
plt.grid(ls=":",c='g')


# 绘制水平/垂直参考线 axhline,属性值也可以传入变量
plt.axhline(y=1.33,c='r',ls='-',lw=2)
plt.axvline(x=0.23,c='r',ls='-',lw=2)

#绘制水平/垂直的参考区域
plt.axvspan(xmin=0.2,xmax=0.6,facecolor="y",alpha=0.2)
plt.axhspan(ymin=1.2,ymax=1.6,facecolor="y",alpha=0.2)

# 可以添加具体到某个点的指向性注释
plt.annotate("maximum",xy=(np.pi/4,0.5),xytext=(np.pi/4+0.1,.5),weight="bold",c="b",arrowprops=dict(arrowstyle="->",connectionstyle="arc3",color="b"))
#无指向性的注释
plt.text(0.3,0.3,"wojiushishi",weight="bold",c="g")

# 给整幅图添加标题
plt.title("demo1")

# legend()函数的作用是获取绘图中各个函数画出东西的标签，还可以设置函数标签的位置
plt.legend()
plt.show()



