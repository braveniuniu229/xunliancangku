import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl

mpl.rcParams["font.sans-serif"]=["SimHei"]
mpl.rcParams["axes.unicode_minus"]=False

# x=[1,2,3,4,5,6,7]
# y=[3,4,3,5,7,3,2]
# bar（）绘制柱状图
# plt.bar(x,y,align="center",color="c",tick_label=["q","a","c","e","h","t","w"],hatch="/")
# barh（）绘制条形柱状图，这里的xlabel与ylabel就变成相反的了
# plt.barh(x,y,align="center",color="c",tick_label=["q","a","c","e","h","t","w"],hatch="/")


# hist（）绘制直方图,bins参数表示要绘制多少个箱体，如果给个整数就代表数量，如果是序列则代表每个箱体的边界
boxWeight=np.random.randint(0,10,50)
x=boxWeight
bins=range(0,10,1)

plt.xlim(0, max(x))  # 设置x轴的范围从0到最大值
plt.ylim(0, max(bins))  # 设置y轴的范围从0到最大值
plt.hist(x,bins=bins,color="g",histtype='bar',edgecolor="#000",rwidth=1,alpha=0.5)

# 绘制饼状图，pie()
kinds=["1","2","3","4"]
colors=["#e41a1c","#377eb8","#4daf4a","#98433e"]
soldnums=[0.2,0.2,0.5,0.1]
plt.pie(soldnums,labels=kinds,autopct="%3.1f%%",startangle=60,colors=colors)

# 绘制极坐标系下的图
barslices=12
theta=np.linspace(0.0,2*np.pi,barslices)
r=30*np.random.rand(barslices)
plt.polar(theta,r,color="chartreuse",linewidth=2,marker="*",mfc="b",ms=10)


plt.xlabel("编号")
plt.ylabel("大小")
plt.legend()
plt.title("demo2")
plt.show()