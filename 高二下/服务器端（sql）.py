import datetime
import sqlite3 
from flask import Flask,render_template,request
ip = "192.168.31.123"  # 服务器绑定本地ip的地址
port = "8080"    # 服务器绑定端口号
url = ip + ':' + port

app = Flask(__name__, static_url_path='')
@app.route("/input",methods=['POST','GET'])
def index(): #URL 路由视图
   # http请求方式
    if request.method == 'POST':
        # 从request中取出id
        name = request.form.get('name')
        sensorid = int(request.form.get('id'))
        tempvalue = float(request.form.get('tempval'))
        humvalue = float(request.form.get('humval'))
        
    else:
        name = request.args.get('name')
        sensorid = int(request.args.get('id')) 
        tempvalue = float(request.args.get('tempval'))
        humvalue = float(request.args.get('humval'))
        
    # 获取本地系统时间
    nowtime = datetime.datetime.now()
    # 格式化系统时间
    nowtime = nowtime.strftime('%Y-%m-%d %H:%M:%S')

    conn = sqlite3.connect("cgq.db")
    #connect()函数：用户创建和连接数据库。若stu.db数据库存在，则打开；否则新建一个数据库文件
    cur = conn.cursor() #创建游标对象（指向数据库，便于在数据库上操作）
    
    # #创建数据表
    #create_sql="create table wenshi(name text,sensorid integer,tempvalue real,hemvalue real,nowtime text )"#创建数据表和字段
    #cur.execute(create_sql)	#执行SQL命令，可以创建数据表，添加、查询、删除更新记录
    #conn.commit()
    
    #插入数据
    insert_sql="insert into wenshi(name,sensorid,tempvalue,humvalue,nowtime) values(?,?,?,?,?)"
    cur.execute(insert_sql,(name,sensorid,tempvalue,humvalue,nowtime))
    conn.commit()		#修改了数据表之后，提交后才生效
    
    #再次查询自己提交的所有记录
    select_sql="select * from wenshi where name='"+name+"'"
    cur.execute(select_sql)   #不需要commit
    data=cur.fetchall()		#读取游标cur的所有记录，并返回（查询）记录数据	
    
    return str(data[-1])  
if __name__ == '__main__':
    app.run(host=ip, port=port, debug=True, use_reloader=False)
