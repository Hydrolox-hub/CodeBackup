import datetime
import sqlite3 
import pandas as pd
import matplotlib.pyplot as plt
from flask import Flask,render_template,request
ip = "192.168.3.27"  # 服务器绑定本地ip的地址
port = "8080"    # 服务器绑定端口号
url = ip + ':' + port

app = Flask(__name__, static_url_path='')
@app.route('/')

def hello():
    conn = sqlite3.connect("room_data.db")
    cur = conn.cursor() #创建游标对象（指向数据库，便于在数据库上操作）
    #查询所有的记录
    select_sql="select * from thl "
    cur.execute(select_sql)   #不需要commit
    data=cur.fetchall()		#读取游标cur的所有记录，并返回（查询）记录数据	    
   
    cur.close()# 关闭游标
    conn.close() # 关闭链接

    data_now = data[len(data)-1]   # 获取列表中最新记录
    return render_template('thl_data.html',data_now=data_now,data=data,url=url) 

@app.route("/input",methods=['POST','GET'])
def index(): #URL 路由视图
   # http请求方式
    if request.method == 'POST':
        # 从request中取出id
        name = request.form.get('name')
        # 从request中取出val值
        tempvalue = float(request.form.get('tempval'))
        humvalue = float(request.form.get('humval'))
        lightvalue = float(request.form.get('lightval'))
    else:
        name = request.args.get('name') 
        tempvalue = float(request.args.get('tempval'))
        humvalue = float(request.args.get('humval'))
        lightvalue = float(request.args.get('lightval'))     
    
    # 获取本地系统时间
    nowtime = datetime.datetime.now()
    # 格式化系统时间
    nowtime = nowtime.strftime('%Y-%m-%d %H:%M:%S')

    conn = sqlite3.connect("room_data.db")
    cur = conn.cursor() #创建游标对象（指向数据库，便于在数据库上操作）
    
    #插入数据
    insert_sql="insert into thl(name,tempvalue,humvalue,lightvalue,nowtime) values(?,?,?,?,?)"
    cur.execute(insert_sql,(name,tempvalue,humvalue,lightvalue,nowtime))
    conn.commit()		#修改了数据表之后，提交后才生效
    
    # 根据获取的温度（tempvalue）和光照值（lightvalue），设置不同的返回值
    # 情况1.如果温度不在[10,30]和光照<600，返回“T_L_bad”
    # 情况2.如果仅温度不在[10,30]，返回“T_bad”
    # 情况3.如果仅光照<500，返回“L_bad”
    # 情况4.都在正常区间，返回“ok”
    if (tempvalue<10 or tempvalue>30) and lightvalue<600:
        back= "T_L_bad"
    elif tempvalue<10 or tempvalue>30:
        back= "T_bad" 
    elif lightvalue<600:
        back= "L_bad"
    else:
        back= "ok"
    
    return back

# 生成图表（设置路由，以及函数）
@app.route('/plot')
def tempdata_make_plot():
    #生成图表程序(辅助资料程序植入)
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



    return "正在制作图表。。。"

if __name__ == '__main__':
    app.run(host=ip, port=port, debug=True, use_reloader=False)
