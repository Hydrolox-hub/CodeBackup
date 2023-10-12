# -*- coding: utf-8 -*-
from flask import Flask, render_template,redirect
from flask_script import Server,Manager 
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap
from wtforms import StringField,SubmitField,PasswordField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY']='hard to guess string'
bootstrap = Bootstrap(app)

class LoginForm(FlaskForm):
    user = StringField('请输入用户名：', validators=[DataRequired()])
    psw = PasswordField('请输入密码：', validators=[DataRequired()])
    submit = SubmitField('登录')

@app.route('/login', methods=['GET', 'POST'])
def login():
    sname=""
    myform = LoginForm()
    if myform.validate_on_submit():
        if myform.user.data == 'admin' and myform.psw.data == '123456':
            sname = '登录成功！'
            #return redirect("http://www.baidu.com")
        else:
            sname = '用户名或密码错误！'
    return render_template('登录验证.html', form=myform, name=sname)

if __name__ == '__main__':
    app.run()