from controller.user_controlller import User_Controller


user_controller = User_Controller()



#----------------
#------pruebas---
#----------------

print("#"*50)
print("#"*50)

print("Test register user: ")
print(user_controller.register_user("ale@gmail.com", "123Sdas@4", "ale"))

print("#"*50)
print("#"*50)
print("Test login user: ")
print(user_controller.log_in_user("ale@gmail.com", "123Sdas@4"))