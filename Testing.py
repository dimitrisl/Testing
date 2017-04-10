import sqlite3
from flask import Flask,g,request
from flask.helpers import url_for
from flask.templating import render_template
from flask import abort

app = Flask(__name__)

def connect_db():
    return sqlite3.connect("C:\Users\Dimitrisl\Desktop\Testing\\test.db")

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html",x=None)

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


if __name__ == '__main__':
    app.run()
