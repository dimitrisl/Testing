from flask import Flask, request, redirect, session
from flask.helpers import url_for
from flask.templating import render_template
from forms import RegisterForm, LoginForm, Otp
import os
import MySQLdb

app = Flask(__name__)

app.config.from_object('config')

DATABASE = os.path.join(app.root_path, 'test.db')


def connect_db():
    db = MySQLdb.connect(host="localhost",  # your host, usually localhost
                         user="root",  # your username
                         passwd="root",  # your password
                         db="flask")  # name of the data base

    return db, db.cursor()


@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")


@app.route('/welcome')
def welcome():
    return render_template("welcome.html")


@app.route('/database')
def show_me_the_data():
    _, cursor = connect_db()
    cursor.execute("select * from user;")
    data = [dict(id=row[0], username=row[1], email=row[2], authecticated=row[3], password=row[4]) for row in cursor.fetchall()]
    return render_template("database.html", x=data)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if request.method == "POST":
        if form.validate():
            connection, db_connection = connect_db()
            db_connection.execute("select * from user where username='{0}';".format(form.username.data))
            user = db_connection.fetchall()
            if user:
                return render_template('register.html', form=form, error="Account already exists!")
            else:
                db_connection.execute("Insert into user (username,password,authenticated,email) VALUES ('{0}','{1}',{2},'{3}');".\
                    format(form.username.data, form.password.data, 0, form.email.data)) # set to not authenticated at first
                connection.commit()
                return redirect('/database')
    return render_template("register.html", form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # mysql query
        _, db_connection = connect_db()
        print type('{0}'.format(form.username.data)),form.username.data
        db_connection.execute("select * from user where username='{0}';".format(form.username.data))
        user = db_connection.fetchall()
        print user
        if user:
            user = user[0]
            user = dict(id=user[0], username=user[1], email=user[2], authecticated=user[3], password=user[4])
            if user['password'] == form.password.data:
                session['username'] = user['username']
                session['authenticated'] = 0
                return redirect("/intermediate")
            elif user['password'] != form.password.data:
                return render_template('login.html',  form=form, error="Invalid credentials")
        else:
            return render_template('login.html', form=form, error="Invalid credentials")
    return render_template('login.html', form=form)


@app.route('/intermediate', methods=['GET','POST'])
def authority():
    form = Otp()
    if form.validate_on_submit():
        whateva = 123131
        if str(form.key.data) == str(whateva):
            session['authenticated'] = 1
            return "this is succesfull!"
    return render_template('intermediate.html',form=form)


@app.route('/logout')
def logout():
    print "we destroy", session
    session.pop('username', None)
    session.pop('authenticated', None)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
