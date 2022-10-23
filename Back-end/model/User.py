class User:

    users_list = []

    def __init__(self, mail, password, is_registered, alias=None):
        self.mail = mail
        self.password = password
        self.alias = alias
        if is_registered:
            try:
                self.get_user_from_db()
            except Exception as e:
                raise Exception("Error when trying to select user from db.", e)

        else:
            try:
                self.insert_user_from_db()
            except Exception as e:
                print (e)


    def __str__(self):
        return f"User named {self.alias}, has e-mail {self.mail} and password: {self.password}"


    def get_user_from_db(self):  # Simula buscar usuario en base de Datos
        for user in User.users_list:
            if user.mail == self.mail and user.password == self.password:
                self.password = user.password
                self.alias = user.alias
                self.portfolio_id = user.portfolio_id
                return
        raise Exception("Invalid mail/password")


    def insert_user_from_db(self):  # Simula insertar usuario en base de Datos
        User.users_list.append(self)
