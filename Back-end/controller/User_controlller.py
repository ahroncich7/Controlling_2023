from sys import path
path.append("..")
from model.User import User
from model.Database import Database
from Validation import Validator
db = Database()

class User_Controller:
    
    def __init__(self):
        pass 

    def register_user(self,id, mail, password, alias):
        new_user = User(id, mail, password, alias)

        if not Validator.user_is_valid(new_user):
            return {"message": "Fail to create user"}
        
        if (db.insert_user(new_user)):
            return {"message": "User created", "data": new_user}
        else:
            return {"message": "Fail to create user"}

    def get_user(self):
        pass

    def list_users(self):
        pass