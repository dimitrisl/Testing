import sqlite3
from flask import Flask,g,request,flash,redirect
from flask.helpers import url_for
from flask.templating import render_template
from flask import abort

from flask_wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired

app = Flask(__name__)

app.config.from_object('config')

class LoginForm(Form):
    name = StringField('name', validators=[DataRequired()])
    surname = StringField('surname', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired()])


def connect_db():
    return sqlite3.connect("C:\Users\Dimitrisl\Desktop\Testing\\test.db")

@app.route('/')
@app.route('/index')
def index(x=None):
    return render_template("index.html",x=x)

@app.route('/database')
def hello_world():
    db_connection = connect_db()
    cursor = db_connection.execute("select * from user;")
    print type(cursor)
    records = [dict(id=row[0],username=row[1],email=row[2],authecticated=row[3]) for row in cursor.fetchall()]
    print records[0]["username"]
    return render_template("index.html",x=records)

@app.route('/register')
def noaccount():
    return render_template("register.html")

@app.route('/list')
def skata():
    lista = ["apples","oranges"]
    #abort(404)
    return render_template("index.html",x=lista)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for name="%s", surname=%s ,e mail = %s' %(form.name.data, form.surname.data,form.email.data))
        return redirect('/')
    return render_template('form.html',title='Sign In',form=form)

if __name__ == '__main__':
    app.run()
