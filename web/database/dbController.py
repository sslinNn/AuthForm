import psycopg2

db_settings = {
    "host": "localhost",
    "database": "fh",
    "user": "postgres",
    "password": "admin",
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


def get_user(user_id):
    try:
        conn = psycopg2.connect(**db_settings)
        cur = conn.cursor()
        cur.execute(f'SELECT * FROM users WHERE user_id = {user_id} LIMIT 1')
        res = cur.fetchone()
        cur.close()
        conn.close()
        if not res:
            print('Пользователь не найден!')
            return False
        else:
            return res
    except Exception as e:
        print("Error:", e)
        return False


def get_user_by_username(username):
    try:
        conn = psycopg2.connect(**db_settings)
        cur = conn.cursor()
        cur.execute(f"SELECT * FROM users WHERE username = '{username}' LIMIT 1")
        res = cur.fetchone()
        cur.close()
        conn.close()
        if not res:
            print('Пользователь не найден!')
            return False
        else:
            return res
    except Exception as e:
        print("Error:", e)
        return False
