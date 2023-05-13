from flask import Flask, render_template, g
from FDataBase import FDataBase
import sqlite3
import os

# Config
DATABASE = '/tmp/site.db'
SECRET_KEY = '23wqe12dcdsv24jgm0=im=K+)((M3102'
DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)
app.config.update(dict(DATABASE=os.path.join(app.root_path, 'site.db')))

# Функция для подключения к БД
def connect_db():
    conn = sqlite3.connect(app.config['DATABASE'])
    conn.row_factory = sqlite3.Row
    return conn

# Функция для создания БД
def create_db():
    db = connect_db()
    with app.open_resource('sq_db.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()
    db.close()

# Функция для поключения БД к WEB
def get_db():
    if not hasattr(g, 'link_db'):
        g.link_db = connect_db()
    return g.link_db



# Функция для закрытия БД
@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'link_db'):
        g.link_db.close()


"""----------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------"""
@app.route('/')
@app.route('/home')
def index():
    db = get_db()
    dbase = FDataBase(db)
    return render_template('home.html', menu=dbase.getMenu())


@app.route('/registration')
def registration():
    return render_template('registration.html')


@app.route('/login')
def login():
    return render_template('login.html')


if __name__ == "__main__":
    app.run()
