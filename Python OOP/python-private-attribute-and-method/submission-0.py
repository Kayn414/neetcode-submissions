class PasswordManager:
    def __init__(self, pswd: str):
        self.__pswd = pswd 
    
    # TODO: Implement the verify_password method
    def verify_password(self, user_pswd: str):
        if user_pswd == self.__pswd:
            return True
        return False


# Don't modify the code below this line
my_password = PasswordManager("secret123")
print(my_password.verify_password("secret123"))  # Should print: True
print(my_password.verify_password("wrong"))      # Should print: False
