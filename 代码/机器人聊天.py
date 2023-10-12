# -*- coding: utf-8 -*-
from flask import Flask, render_template,redirect
from flask_script import Server,Manager 
from flask_wtf import FlaskForm
from flask_moment import Moment
from flask_bootstrap import Bootstrap
from wtforms import StringField,SubmitField,PasswordField
from wtforms.validators import DataRequired

import sys
sys.path.insert(0, "../")

import aiml               
k = aiml.Kernel()	   #创建aiml聊天机器人         
k.learn("cn-startup.xml")   #学习aiml语料库
k.respond("load aiml cn")   #初步交互   
k.respond("start")


app = Flask(__name__)
app.config['SECRET_KEY']='hard to guess string'

manager=Manager(app)
server=Server(host="127.0.0.1",port=80,threaded=True)
manager.add_command("runserver", server)
bootstrap = Bootstrap(app)
moment=Moment(app)

class NameForm(FlaskForm):
    name = StringField('请开始交谈：', validators=[DataRequired()])
    submit = SubmitField('提交')

@app.route('/', methods=['GET', 'POST'])
def index():
    name = ''
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
    return render_template('聊天机器人.html', form=form, name=k.respond(name))


if __name__ == '__main__':
    manager.run()
