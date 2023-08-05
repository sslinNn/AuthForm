from web.database import dbController

class User:
    def __init__(self, login, password, email):
        self.login = login
        self.password = password
        self.email = email


    def get_info(self):
        info = {'login': self.login,
                'password': self.password,
                'email': self.email}
        return info


class UserLogin:
    def from_db(self, user_id):
        self.__user = dbController.get_user(user_id)
        return self

    def create(self, user):
        self.__user = user
        return self


    def is_authentificated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.__user[0])

