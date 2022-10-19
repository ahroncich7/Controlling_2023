class User:
    def __init__(self, mail, password, alias):
        self.mail = mail;
        self.password = password;
        self.alias = alias;

    def show_data(self):
        print(self.password, self.mail, self.alias, sep=", ")

