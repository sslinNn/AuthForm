from flask import Flask, render_template, url_for, request, redirect
from flask_session import Session
from flask_login import LoginManager, login_user
from werkzeug.security import generate_password_hash, check_password_hash
from database import dbController
from user_C import User, UserLogin


app = Flask(__name__)
login_manager = LoginManager(app)
app.secret_key = 'aOKmc90-ij2n387ch8un1280nx1809m'
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)


@login_manager.user_loader
def load_user(user_id):
    print('user load')
    return UserLogin().from_db(user_id)


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
            dbController.create_user(login=request.form['login'].lower(),
                                     password=password_hash,
                                     email=request.form['email'])
        return redirect(url_for('login'))
    else:
        return render_template('signup.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = dbController.get_user_by_username(request.form['login'])
        if user and check_password_hash(user[3], request.form['password']):
            user_login = UserLogin().create(user)
            login_user(user_login)
            return f'U are welcome {user[1]}'
        else:
            return f'Fck u!'
    return render_template('login.html')


@app.route('/profile/<int:user_id>')
def profile(user_id):
    return f'User - {user_id}'
    # return render_template('profile.html')

# @app.route('/profile/<int:user_id>')
# def profile(user_id):
#     return f'lsdf {user_id}'


if __name__ == "__main__":
    app.run(debug=True)
