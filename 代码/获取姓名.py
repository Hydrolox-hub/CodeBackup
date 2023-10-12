from flask import Flask, render_template
from flask_script import Server,Manager 
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY']='hard to guess string'
bootstrap = Bootstrap(app)

class NameForm(FlaskForm):
    name = StringField('你的姓名？', validators=[DataRequired()])
    submit = SubmitField('提交')

@app.route('/', methods=['GET', 'POST'])
def index():
    sname = ''
    myform = NameForm()
    if myform.validate_on_submit():
        sname = myform.name.data
        myform.name.data = ''
    return render_template('获取姓名.html', form=myform, name=sname)

if __name__ == '__main__':
    app.run()