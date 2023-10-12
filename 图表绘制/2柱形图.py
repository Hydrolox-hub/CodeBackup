import pandas as pd
import matplotlib.pyplot as plt

#解决中文乱码问题
plt.rcParams["font.sans-serif"]='SimHei'

#创建画布和坐标系
plt.figure()
plt.subplot(1,1,1)

#创建DataFrame
df=pd.read_excel("2柱形图.xls")


#创建姓名及借阅册数列表
x=df["姓名"]
y=df["借阅册数"]

#绘图
plt.bar(x,y,color="b",width=0.5,align="center",label="借阅册数")

#显示图例
plt.legend()

#设置坐标轴
plt.xlabel("姓名")
plt.ylabel("借阅册数")

#设置标题
plt.title(label="部分同学图书借阅情况对比图")

#设置数据标签
for a,b in zip(x,y):
    plt.text(a,b,b,ha="center",va="bottom",fontsize=10)

plt.show()

