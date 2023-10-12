# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 08:37:57 2022

@author: Administrator
"""

from flask import Flask
app=Flask(__name__)
@app.route('/')
def index():
    return'<html><body><h1>主页</h1></body></html>'
if __name__ == '__main__':
    app.run()
