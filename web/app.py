from flask import Flask, render_template, url_for, request, redirect
from flask_session import Session
from werkzeug.security import generate_password_hash           #, check_password_hash
from database import dbController
from class_ import User


app = Flask(__name__)
app.secret_key = 'aOKmc90-ij2n387ch8un1280nx1809m'
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)


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
        password_check = request.form['passwordCheck']
        if user.password != password_check:
            return f"The password is not correct"
        else:
            password_hash = generate_password_hash(password=request.form['password'])
            dbController.create_user(login=request.form['login'],
                                     password=password_hash,
                                     email=request.form['email'])
        return redirect(url_for('login'))
    else:
        return render_template('signup.html')


@app.route('/login')
def login():
    return render_template('login.html')


if __name__ == "__main__":
    app.run(debug=True)
