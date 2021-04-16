class View:
    def __init__(self):
        pass

    def changePasswordView(self):
        print("Changement de Password")
        print("Email: ")
        email = input()
        print("Ancien Password: ")
        old_password = input()
        print("Nouveau Password: ")
        print("Attention, le mot de passe doit avoir au moins 8 caractères, une majuscule et un caractère special parmi [@_!#$%^&*()<>?/\|}{~:] ")
        new_password = input()
        print("Verification Nouveau Password: ")
        new_password_verif = input()
        return [email,old_password,new_password,new_password_verif]

    def badCheckPassword(self):
        print("Nouveau Password et Check Nouveau Password different, merci de refaire le process")
        self.changePasswordView()

    def wrongOldPassword(self):
        print("Mauvais email ou ancien Password, merci de recommencer le process")
        self.changePasswordView()
    
    def wrongConformityPasswordView(self):
        print("Pour rappel, le mot de passe doit avoir au moins 8 caractères, une majuscule et un caractère special parmi [@_!#$%^&*()<>?/\|}{~:] ")
        print("Merci de recommencer le process")
        self.changePasswordView()

    def sucessChangePassword(self):
        print("Succes Modification du Password")