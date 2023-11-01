class InvalidPasswordException(BaseException):
    def __init__(self, msg):
        self.msg = msg

class TooOldException(Exception):

    def __init__(self, msg):
        self.msg = msg





try:
    password = input("Enter the password")
    if len(password)<8:
        raise InvalidPasswordException("Password should be min 8 char long")
except InvalidPasswordException("Your password is not following rules and it should be at least 8 char long"):
    print("8 chars")