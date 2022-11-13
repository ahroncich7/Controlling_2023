from sys import path
path.append("..\\")
from model.user_connection import Dao
from controller.Validation import Validator


db = Dao("localhost", "3306", "root", "", "controlling")

class User_Controller:
    
    def __init__(self):
        pass 

    def register_user(self, mail, password, alias, nationality):
        
        if not Validator.user_is_valid(mail, password):
            return {"status":"fail","message": "User/Password not valid"}


        try:
            db.insert_user([mail, password, alias, nationality])

        except Exception as e:
            return {"status":"fail","message": f"Fail to create user, {e}"}


        return {"status":"ok", "message": "User created", "data": ""}



    def log_in_user(self, mail, password):
        if not (Validator.user_is_valid(mail, password)):
            return {"status":"fail","message": "User/Password not valid"}

        try:
            user_data = db.select_user(mail)

        except Exception as e:
            return {"status":"fail","message": f"{e}"}

        if not user_data:
            return {"status":"fail","message": "User doesnt exist"}
        
       
        if not (user_data[1] == password):
            return {"status":"fail","message": "Invalid Password"}

        return  {"status":"ok", "message": "Allowed acces", "data": f"{user_data}"}

    
    
    def update_user_data(self, mail, password, values):
        
        if not (Validator.user_is_valid(mail, password)):
            return {"status":"fail","message": "User/Password not valid"}

        try:
            user_data = db.select_user(mail)

        except Exception as e:
            return {"status":"fail","message": f"{e}"}

        if not user_data:
            return {"status":"fail","message": "User doesnt exist"}
        
       
        if not (user_data[1] == password):
            return {"status":"fail","message": "Invalid Password"}

        try:
            db.update_user(mail, values)
        
        except Exception as e:
            return {"status":"fail","message": f"{e}"}

        return  {"status":"ok", "message": "Changes done", "data": f"{user_data}"}


    
    def delete_user(self, mail, password):

        # if not (Validator.user_is_valid(mail, password)):
        #     return {"status":"fail","message": "User/Password not valid"}

        try:
            user_data = db.select_user(mail)

        except Exception as e:
            return {"status":"fail","message": f"{e}"}

        if not user_data:
            return {"status":"fail","message": "User doesnt exist"}
        
       
        if not (user_data[1] == password):
            return {"status":"fail","message": "Invalid Password"}

        try:
            db.delete_user(mail)

        except Exception as e:
            return {"status":"fail","message": f"{e}"}

        return  {"status":"ok", "message": "User deleted", "data": ""}


    def count_users_by_country(self):
        
        return f"{db.count_users_by_country()}"



user = User_Controller()

print(user.count_users_by_country())