from sys import path
from controller.User_controlller import User_Controller


user_controller = User_Controller()

new_user = (None, "ale@gmail.com", "1234", "ale") 
print(user_controller.register_user(None, "ale@gmail.com", "1234", "ale"))