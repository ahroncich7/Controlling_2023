from sys import path
path.append('..\\')
from model.User import User


class User_Controller:

    @classmethod
    def login(self, user_mail, user_pass):
        try:
            return User(user_mail, user_pass, True)
        except Exception:
            raise

