from sys import path
path.append('..\\')
from model.User import User


class User_Controller:

    def __init__(self):
        pass

        User

    @classmethod
    def login(self, user_mail, user_pass):
        try:
            return User(user_mail, user_pass, True)
        except Exception:
            raise




# Simula que llegan datos del login
# try:
#     test_user_mail = input("Ingrese dirección de correo registrado: ")
#     test_user_pass = input("Ingrese contraseña del usuario registrado: ")
#     test_user = User_Controller.login(test_user_mail, test_user_pass)
#     print(test_user)
# except Exception as e:
#     print(e)

