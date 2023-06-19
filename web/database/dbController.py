import psycopg2


def dbConn():
    # Подключение к базе данных
    conn = psycopg2.connect(
        host="localhost",
        database="finance_helper",
        user="postgres",
        password="admin"
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