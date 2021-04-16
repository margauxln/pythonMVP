from model import User
from view import View

import re

class Presenter:
    user = User(1,"Margaux","Lenne","margaux.lenne@hotmail.fr","azerty1234")
    view = View()

    def __init__(self):
        pass

    def launchChangePassword(self):
        return self.view.changePasswordView()

    def checkConformityPassword(self,password):
        result = False
        if (len(password) >= 8):
            """print("le password est bien sup a 8 caracteres")"""
            if(any(x.isupper() for x in password)):
                """print("le password a bien une majuscule")"""
                if(re.compile('[@_!#$%^&*()<>?/\|}{~:]').search(password)):
                    """print("le password contient un caractere special")"""
                    result = True
        return result


    def checkAndChangePassword(self):
        infoChangePasswordAttempt = self.launchChangePassword()
        email = infoChangePasswordAttempt[0]
        old_password = infoChangePasswordAttempt[1]
        new_password = infoChangePasswordAttempt[2]
        new_password_verif = infoChangePasswordAttempt[3]
        if (self.user.getPassword(email) == old_password):
            """print("Les anciens passwords coincident")"""
            if(self.checkConformityPassword(new_password)):
                """print("Le nouveau password est conforme")"""
                if(new_password == new_password_verif):
                    """print("Le nouveau password et le password verif coincident")"""
                    self.user.changePassword(email,old_password,new_password)
                    self.view.sucessChangePassword()
                else:
                    """print("Le nouveau password et le password verif ne coincident pas")"""
                    self.view.badCheckPassword()
            else:
                """print("Le nouveau password n'est pas conforme")"""
                self.view.wrongConformityPasswordView()
        else:
            """print("Les anciens passwords ne coincident pas")"""
            self.view.wrongOldPassword()

changePassword = Presenter()
if __name__ == "__main__":
    changePassword.checkAndChangePassword()