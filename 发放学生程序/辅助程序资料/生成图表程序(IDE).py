# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 10:41:17 2022

@author: lenovo
"""
import sqlite3 
import pandas as pd
import matplotlib.pyplot as plt
def tempdata_make_plot():
    # 制作图表
    print("正在制作图表。。。")
    # 链接数据库
    db = sqlite3.connect("room_data.db")
    cur = db.cursor()
    cur.execute("SELECT tempvalue, strftime('%Y-%m-%d',nowtime)  FROM thl") #查询温度、日期  
    data = cur.fetchall() 
     # 关闭游标
    cur.close()
    # 关闭链接
    db.close()
    
    df_data=pd.DataFrame(data)
    df_data.columns = ['温度', '日期']
    df=df_data.groupby("日期",as_index=False).mean() #按照日期分组取温度平均值
    print(df)
    
    # 生成图表
    #解决中文乱码问题
    plt.rcParams["font.sans-serif"]='SimHei'
    #创建画布和坐标系
    plt.figure(figsize=(8,6))
    plt.subplot(1,1,1)
    #创建姓名及借阅册数列表
    x=df["日期"]
    y=df["温度"]  
    #绘图
    plt.plot(x,y,color="y",label="温度（℃）")
    #显示图例
    plt.legend()    
    #设置坐标轴
    plt.xlabel("日期")
    plt.ylabel("温度")  
    #设置标题
    plt.title(label="室内温度折线图")
    plt.xticks(rotation=-120)   # 设置横坐标显示的角度，角度是逆时针
    #设置数据标签
    for a,b in zip(x,y):
        plt.text(a,b,b,ha="center",va="bottom",fontsize=10)
    plt.savefig('static/tempdata.jpg',dpi=300)
    plt.show()
    return render_template('plot.html',url=url)