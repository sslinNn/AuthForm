from flask import Flask, render_template
import psycopg2

# Подключение к базе данных
conn = psycopg2.connect(
    host="your_host",
    database="your_database",
    user="your_user",
    password="your_password"
)


app = Flask(__name__)
DEBUG = True

@app.route('/')
@app.route('/home')
def index():
    return render_template('home.html')


if __name__ == "__main__":
    app.run(debug=True)
