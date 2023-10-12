# -*- coding: utf-8 -*-
"""
Created on Wed Dec 29 14:19:29 2021

@author: cnhhdn
"""
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei']
df=pd.read_excel("global.xls",header=1)
df["累计确诊"]=df["新增确诊"]+df["现有确诊"]
df_s=df.sort_values("累计确诊",ascending=False).head()  
print("累计确诊数最多的五个国家")
print(df_s)
df1=df[df["新增确诊"]==0]
print("新增确诊数为0的国家数:", len(df1))
# print("新增确诊数为0的国家数:", df1["新增确诊"].count())

df_g=df.groupby("洲别").sum()
print(df_g)
plt.figure(figsize=(8,4))
x=df_g["死亡数"]
y=df_g.index
plt.title("各洲别死亡数",fontsize=20)
plt.barh(y,x,label="死亡数",height=0.5,color=['c','orange','b','y','r','g'])
for a,b in zip(y,x):
    plt.text(b,a,b,va='center',fontsize=13)
plt.xlim(10,1800000)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.legend(handlelength=1,fontsize=14,shadow=True)
plt.show()

#①x=df_g.values  ②x=df_g["死亡数"]  ③y=df_g.index  ④y=df_g["洲别"]