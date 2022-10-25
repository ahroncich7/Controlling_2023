class User:

    def __init__(self, id, mail, password, alias):
        self.id  = id 
        self.mail = mail
        self.password = password
        self.alias = alias

    def __str__(self):
        return f"User id: {self.id} with mail: {self.mail}, has password: {self.password}, and named {self.alias}"