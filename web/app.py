from flask import Flask, render_template, url_for, request, redirect, session, jsonify
from flask_session import Session
import psycopg2
from database import dbController
from class_ import User


app = Flask(__name__)
app.secret_key = 'aOKmc90-ij2n387ch8un1280nx1809m'
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)
db = dbController.dbConn()


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/signup', methods=['POST', 'GET'])
def signup():
    if request.method == 'POST':
        user = User(login=request.form['login'],
                    email=request.form['email'],
                    password=request.form['password'])
        session['user'] = user
        # return redirect(url_for('home'))
        return jsonify(user.get_info())
    else:
        return render_template('signup.html')


@app.route('/login')
def login():
    return render_template('login.html')


if __name__ == "__main__":
    app.run(debug=True)
