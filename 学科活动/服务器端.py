# -*- coding: utf-8 -*-
"""
Created on Sat Apr 16 13:59:42 2022

@author: Administrator
"""

import datetime
import sqlite3 
from flask import Flask,render_template,request
import pandas as pd
import matplotlib.pyplot as plt

ip = "172.20.192.1"  
port = "8080"    
url = ip + ':' + port
app = Flask(__name__)

@app.route('/')
def hello():

    conn = sqlite3.connect("id_DB.db")
    cur = conn.cursor() 
    
    select_sql="select * from id "
    cur.execute(select_sql)   
    data=cur.fetchall()		   
   
    cur.close()
    conn.close() 

    data_now = data[len(data)-1]   
    return render_template('login.html',data_now=data_now,data=data,url=url) 

@app.route('/mainpage2')
def mainpage2():
    
    db = sqlite3.connect("id_DB.db")
    cur = db.cursor()
    cur.execute("SELECT louc FROM id")   
    data_ = cur.fetchall() 
    cur.close()
    db.close()
    x =[]
    for i in data_:
      x.append(i[0]) 
      
    data = {"寝室":x,"举报次数":1}
    df = pd.DataFrame(data)
    s=df.groupby('寝室',as_index=False).sum()
    s = s.sort_values('举报次数',ascending = False)
    plt.rcParams["font.sans-serif"]='SimHei'
    plt.figure(figsize=(8,6))
    plt.subplot(1,1,1)
    x = s['寝室'].head(10)
    y = s['举报次数'].head(10)
    plt.xlabel("寝室")
    plt.ylabel("举报次数")  
    plt.title(label="黑名单")
    plt.bar(x,y,color='b',width=0.5,label = '举报次数') 
    for a,b in zip(x,y):
        plt.text(a,b,b,ha="center",va="bottom",fontsize=10) 
    plt.legend()
    plt.savefig('static/IDdata.jpg',dpi=300)
    return render_template('m2.html',url=url+'/mainpage2')

@app.route('/help')
def help():
    
    return render_template('求救.html',url=url+'/help')

@app.route('/kfz',methods=['post'])
def kfz_():
    weiz = request.form.get("weiz")
    louc = request.form.get("louc")
    print(weiz)
    return render_template('kfz.html',url=url+'/kfz',weiz=weiz,louc=louc)

@app.route('/kfz2',methods=['post'])
def kfz2_():
    jbdx = request.form.get('jbdx')
    jbr= request.form.get('jbr')   

    nowtime = datetime.datetime.now()

    nowtime = nowtime.strftime('%Y-%m-%d %H:%M:%S')

    conn = sqlite3.connect("id_DB.db")
    cur = conn.cursor()

    insert_sql="insert into id(weiz,louc,nowtime) values(?,?,?)"
    cur.execute(insert_sql,(jbdx,jbr,nowtime))
    conn.commit()	
    return render_template('kfz2.html',url=url+'/kfz2')
     
@app.route('/report')
def report_():
    return render_template('举报.html',url=url+'/report')

@app.route('/about')
def about():
    return render_template('about.html',url=url+'/about')
    
if __name__ == '__main__':
    app.run(host=ip, port=port, debug=True, use_reloader=False)
