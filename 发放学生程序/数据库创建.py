# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 08:22:17 2022

@author: lenovo
"""

import sqlite3 
conn = sqlite3.connect("room_data.db")
#connect()函数：用户创建和连接数据库。若room_data.db数据库存在，则打开；否则新建一个数据库文件
cur = conn.cursor() #创建游标对象（指向数据库，便于在数据库上操作）

#创建数据表
create_sql="create table thl(name text,tempvalue real,humvalue real,lightvalue real,nowtime text )"#创建数据表和字段
cur.execute(create_sql)	#执行SQL命令，可以创建数据表，添加、查询、删除更新记录
conn.commit()

cur.close()		#关闭游标对象
conn.close()	#关闭数据库对象conn