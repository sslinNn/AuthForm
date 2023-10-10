from flask import Flask, render_template, url_for, request, redirect, flash
from flask_session import Session
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from database import dbController
from userController import User, UserData


app = Flask(__name__)
login_manager = LoginManager(app)
app.secret_key = 'aOKmc90-ij2n387ch8un1280nx1809m'
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)


@login_manager.user_loader
def load_user(user_id):
    return UserData().from_db(user_id)


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/signup', methods=['POST', 'GET'])
def signup():
    if request.method == 'GET':
        if current_user.is_authenticated:
            return redirect(url_for('profile'))
    if request.method == 'POST':
        user = User(login=request.form['login'],
                    email=request.form['email'],
                    password=request.form['password'])
        password_check = request.form['passwordCheck']

        #            Проверки данных перед сохранением
        if not user.login or not user.password or not password_check:
            flash('Fill all forms!', 'error')
            return render_template('signup.html')
        elif len(user.login) < 4 or len(user.login) > 20:
            flash('Login should be from 4 to 20 symbols!', 'error')
            return render_template('signup.html')
        try:
            if user.login.lower() == dbController.get_user_by_username(user.login.lower())[1]:
                flash('This user is already exist', 'error')
                return render_template('signup.html')
        except:
            pass
        if len(user.password) < 6:
            flash('Pass should be bigger then 6 symbols', 'error')
            return render_template('signup.html')
        elif user.password != password_check:
            flash('Password is not correct!', 'error')
            return render_template('signup.html')
        else:
            #            Хеширование пароля
            password_hash = generate_password_hash(password=request.form['password'])

            #            Сохраняет данные в БД
            dbController.create_user(login=request.form['login'].lower(),
                                     password=password_hash,
                                     email=request.form['email'])
            return redirect(url_for('login'))
    else:
        return render_template('signup.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        if current_user.is_authenticated:
            return redirect(url_for('profile'))
    if request.method == 'POST':
        user = dbController.get_user_by_username(request.form['username'].lower())
        if user and check_password_hash(user[3], request.form['password']):
            user_login = UserData().create(user)
            login_user(user_login)
            return redirect(url_for('profile'))
        else:
            flash(f'Invalid data!', 'error')
    return render_template('login.html')


@app.route('/profile')
@login_required
def profile():
    user = User(login=current_user.get_username(),
                email=current_user.get_email(),
                password=current_user.get_password()).get_info()
    print(user)

    return render_template('profile.html', user=user)

@app.route('/logout/')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.errorhandler(404)
def pageNot(error):
    return render_template('error.html', error=error)


if __name__ == "__main__":
    app.run(debug=True)
