from model.fakedb import users_list
class User:

    def __init__(self, mail, password, is_registered, alias=None):

        if is_registered:
            try:
                self.get_user_from_db(mail, password)
            except Exception as e:
                raise Exception("Error when trying to select user from db.", e)

        else:
            try:
                self.insert_user_to_db(mail, password, alias)
            except Exception as e:
                print (e)


    def __str__(self):
        return f"User named {self.alias}, has e-mail {self.mail} and password: {self.password}"


    def get_user_from_db(self, mail, password):  # Simula buscar usuario en base de Datos
        for user in users_list:
            user = user
            if user["mail"] == mail and user["password"] == password:
                self.mail = user["mail"]
                self.password = user["password"]
                self.alias = user["alias"]
                return
        raise Exception("Invalid mail/password")


    def insert_user_to_db(self, mail, password, alias):  # Simula insertar usuario en base de Datos
        self.mail = mail
        self.password = password
        self.alias = alias
        users_list.append(self.__dict__)
