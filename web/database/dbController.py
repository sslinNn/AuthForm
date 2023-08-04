import psycopg2

db_settings = {
    "host": "localhost",
    "database": "fh",
    "user": "postgres",
    "password": "razer1991",
}


def create_user(login, password, email):
    try:
        conn = psycopg2.connect(**db_settings)
        cur = conn.cursor()
        cur.execute("INSERT INTO users (username, password, email) VALUES (%s, %s, %s);",
                    (login, password, email))
        conn.commit()
        cur.close()
        conn.close()
        return True
    except Exception as e:
        print("Error creating user:", e)
        return False

def dbConn():
    # Подключение к базе данных
    conn = psycopg2.connect(
        host="localhost",
        database="fh",
        user="postgres",
        password="razer1991"
    )

    # Создание объекта-курсора
    cur = conn.cursor()

    # Выполнение запроса
    cur.execute("SELECT * FROM users")

    # Получение результатов
    rows = cur.fetchall()

    # Вывод результатов
    for row in rows:
        print(row)

    # Закрытие курсора и соединения с базой данных
    cur.close()
    conn.close()