import re

class User:
    def __init__(self,firstname,ville,departement,mdp,mail):
        self.firstname = firstname
        self.ville = ville
        self.departement = departement
        self.mdp = mdp
        self.mail = mail
    
    def get_firstname(self):
        return self.firstname
    def get_ville(self):
        return self.ville
    def get_departement(self):
        return self.departement
    def get_mdp(self):
        return self.mdp
    def get_mail(self):
        return self.mail

class Users:
    def __init__(self):
        self.all=[]

    def add_user(self):

        firstname=input("prenom : ")
        while not re.match("^[a-zA-Z]+$", firstname):
            print("votre prenom contient une erreur")
            firstname=input("prenom : ")

        ville=input("ville : ")
        while not re.match("^[a-zA-Z]+$", ville):
            print("votre ville contient une erreur")
            ville=input("ville : ")

        departement=input("numero de departement : ")
        while True:
            try:
                int(departement)
            except ValueError:
                print("votre numero de departement doit etre un nombre")
                departement=input("numero de departement : ")
            break

        mail=input("mail : ")
        while "@" not in mail:
            print("votre mail contient une erreur")
            mail=input("mail : ")

        mdp=input("mot de passe : ")

        user=User(firstname,ville,departement,mdp,mail)
        self.all.append(user)
    
    def show_one(self):
        return self.all[-1]

truc=Users()
truc.add_user()
print(truc.show_one())