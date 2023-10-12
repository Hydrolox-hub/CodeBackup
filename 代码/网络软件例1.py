# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 12:22:20 2021

@author: lenovo
"""

from flask import Flask
from flask_script import Server,Manager 

app = Flask(__name__)
'''
#默认地址及端口号
@app.route('/')
def index():
    return '<html><body><center><h1>我的第一个Web程序!</h1><center></body></html>'
if __name__ == '__main__':
    app.run()
'''

#修改访问地址以及端口号（cmd运行）
manager=Manager(app)
server=Server(host="127.0.0.1",port=80,threaded=True)
manager.add_command("runserver", server)
@app.route('/two/<name>')
def hello(name):
    return '<html><body><center><h1> %s的Web程序!</h1><center></body></html>'%name
if __name__ == '__main__':
    manager.run()
