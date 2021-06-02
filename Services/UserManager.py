from Services.IUserManager import IUserManager


class UserManager(IUserManager):
    def logIn(self, userId, password):
        return True

    def SignUp(self, userId, password):
        return True
