import re
mail_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
passwor_regex = r"^(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$"

class Validator:

    @classmethod
    def user_is_valid(self, new_user):
        if re.match(mail_regex, new_user.mail) and \
           re.match(passwor_regex, new_user.password):
            return True
        else:
            return False
        

