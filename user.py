import re
import json

ficher_json='EcoTrack/user.json'

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
        mail=input("mail : ")
        patternmail = r'@[\w\.-]+\.\w+$'
        while re.match(patternmail, mail):
            print("votre mail contient une erreur")
            mail=input("mail : ")

        with open(ficher_json,'r') as file:
            file_data = json.load(file)
            if mail in file_data["user"].keys():
                print("email deja utiliser")
                return False

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

        mdp=input("mot de passe : ")
        while len(mdp)<5:
            print("votre mdp n'est pas assez long")
            mdp=input("mot de passe : ")

        user=User(firstname,ville,departement,mdp,mail)
        self.all.append(user)

        with open(ficher_json,'r+') as file:
            file_data = json.load(file)
            file_data["user"][mail]={"firstname":firstname,"ville":ville,"departement":departement,"mdp":mdp}
            file.seek(0)
            json.dump(file_data,file,indent="\t")
    
    def show_one(self):
        return self.all[-1]
    
    def connexion(self,mail,mdp):
        for elt in self.all:
            if elt.mail == mail :
                if elt.mdp == mdp :
                    return "connecter"
                else :
                    return "erreur mdp"
            else :
                return "mail inconnu"
            
truc=Users()
truc.add_user()