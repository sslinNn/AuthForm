from flask import Flask, render_template, url_for
import psycopg2

app = Flask(__name__)
DEBUG = True

@app.route('/')
@app.route('/home')
def index():
    return render_template('home.html')


@app.route('/registration')
def registration():
    return render_template('registration.html')


if __name__ == "__main__":
    app.run(debug=True)
