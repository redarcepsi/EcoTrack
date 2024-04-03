import json
import matplotlib.pyplot as plt
import numpy as np

from user import Users

ficher_json='EcoTrack/data.json'

with open(ficher_json,'r') as mon_fichier:
    file_data=json.load(mon_fichier)
    utilisateur=file_data["user"]
    donnee=file_data["data"]

truc=Users()
mail=truc.connexion("henri@gmail.com","truc")

user_data=donnee[mail]
print(user_data)