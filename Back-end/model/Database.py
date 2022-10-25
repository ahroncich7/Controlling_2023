class Database:
    users = []
    def __init__(self):
        pass

    def insert_user(self, new_user):
        try:
            Database.users.append(new_user)
            return True
        except Exception as e:
            print(e)
            