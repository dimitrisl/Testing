import sqlite3
from flask import Flask,g,request,flash,redirect
from flask.helpers import url_for
from flask.templating import render_template
from flask import abort
from forms import RegisterForm,LoginForm
import os

app = Flask(__name__)

app.config.from_object('config')

DATABASE=os.path.join(app.root_path, 'test.db')

def connect_db():
    return sqlite3.connect(DATABASE)

@app.route('/')
@app.route('/index')
def index(x=None):
    return render_template("index.html",x=x)

@app.route('/database')
def hello_world():
    db_connection = connect_db()
    cursor = db_connection.execute("select * from user;")
    records = [dict(id=row[0],username=row[1],email=row[2],authecticated=row[3]) for row in cursor.fetchall()]
    print records[0]["username"]
    return render_template("index.html",x=records)


@app.route('/register')
def noaccount():
    return render_template("register.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # mysql query
        db_connection = connect_db()
        user = db_connection.execute("select * from user where username='{}';".format(form.username.data)).fetchall()
        if user:
            print user
            user = dict(id=user[0][0], username=user[0][1], email=user[0][2], authecticated=user[0][3])
            print type(form.password.data), form.password.data
            print type(user['id'])

            if user['id'] == int(form.password.data):
                return "mpikes kariolare"
    return render_template('login.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
