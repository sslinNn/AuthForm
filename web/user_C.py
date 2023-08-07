from web.database import dbController


class User:
    def __init__(self, login, email, password):
        self.login = login
        self.email = email
        self.password = password

    def get_info(self):
        info = {'login': self.login,
                'password': self.password,
                'email': self.email}
        return info


class UserData:
    def from_db(self, user_id):
        self.__user = dbController.get_user(user_id)
        return self

    def create(self, user):
        self.__user = user
        return self

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.__user[0])

    def get_username(self):
        return str(self.__user[1])

    def get_email(self):
        return str(self.__user[2])

    def get_password(self):
        return str(self.__user[3])

