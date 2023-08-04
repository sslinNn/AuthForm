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
