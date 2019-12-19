from flask import Flask, url_for, render_template, flash, redirect
from flask_sqlalchemy import SQLAlchemy

import config
from forms import LoginForm



app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)



@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/index')
def index():
    user = {'nickname':'zhou'}
    posts = [
        {
        'author':{'nickname':'mike'},
        'body':'今天周一要发周报'
         },
        {
        'author':{'nickname':'amy'},
        'body':'周二没课上体验课',
        }
    ]
    return render_template('index.html',user = user,title = 'zhouying',posts = posts)

@app.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('opendid = '+form.openid.data+' remember me =  '+ str(form.remember_me.data))
        return redirect('/index')
    return render_template('login.html',form = form,title = 'sign in',
                           providers = app.config['OPENID_PROVIDERS'])

if __name__ == '__main__':
    app.run()
