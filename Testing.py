import sqlite3
from flask import Flask, g, request, flash, redirect
from flask.helpers import url_for
from flask.templating import render_template
from flask import abort
from forms import RegisterForm,LoginForm
import os
import MySQLdb


app = Flask(__name__)

app.config.from_object('config')

DATABASE=os.path.join(app.root_path, 'test.db')


def connect_db():
    db = MySQLdb.connect(host="localhost",  # your host, usually localhost
                         user="root",  # your username
                         passwd="root",  # your password
                         db="flask")  # name of the data base

    return db.cursor()


@app.route('/')
@app.route('/index')
def index(x=None,error=None):
    return render_template("index.html", x=x,error=error)


@app.route('/database')
def hello_world():
    cursor = connect_db()
    cursor.execute("select * from user;")
    data = [dict(id=row[0], username=row[1], email=row[2], authecticated=row[3],password=row [4]) for row in cursor.fetchall()]
    return render_template("index.html",x=data)


@app.route('/register')
def noaccount():
    return render_template("register.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # mysql query
        db_connection = connect_db()
        db_connection.execute("select * from user where username='{0}';".format(form.username.data))
        user = db_connection.fetchall()
        if user:
            user = user[0]
            user = dict(id=user[0], username=user[1], email=user[2], authecticated=user[3], password=user[4])
            if user['password'] == form.password.data:
                return render_template("welcome.html")
            elif user['password'] != form.password.data :
                return render_template('login.html',  form=form, error="Invalid credentials")
        else:
            return render_template('login.html', form=form, error="Invalid credentials")
    return render_template('login.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
