class User:
    def __init__(self,id, first_name,last_name,email,password):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password

    def getPassword(self,email):
        if (email == self.email):
            return self.password

    def changePassword(self,email, old_password,new_password):
        if(email == self.email and old_password == self.password):
            self.password = new_password