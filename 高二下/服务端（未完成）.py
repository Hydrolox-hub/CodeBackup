# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 08:42:25 2022

@author: Administrator
"""

from flask import Flask
from flask_script import Server,Manager

app=Flask(__name__)
manager=Manager(app)
server=Server(host='127.0.0.1',port=225,threaded=True)
manager.add_command('runserver',server)

@app.route('/')
def index():
    return '<html><body><h1>主页</h1></body></html>'
@app.route('/two/<name>')
def hello(name):
    return '<html><body>'