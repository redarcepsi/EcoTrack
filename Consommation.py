from tkinter import *


class Conso:

    def __init__(self, transport, surface, chauffage, km):
        self.transport = transport
        self.surface = surface
        self.chauffage = chauffage
        self.km = km
        self.values = []

    def get_transport(self):
         
        if self.transport == "voiture moteur thermique":
            print("Consommation carburant : "f"{0.192 * self.km}kg CO2/km")
            return 0.192 * self.km

        elif self.transport == "voiture moteur électrique":
            print("Consommation carburant : "f"{0.0198 * self.km}kg, CO2/km")
            return 0.0198 * self.km

        elif self.transport == "métro":
            print("Consommation carburant : "f"{0.0042 * self.km}kg, CO2/km")
            return 0.0042 * self.km


        elif self.transport == "vélo et trotinette électrique":
            print("Consommation carburant : "f"{0.00223 * self.km}kg, CO2/km")
            return 0.00223 * self.km


        elif self.transport == "vélo, marche à pied":
            print("Consommation carburant : "f"{0}kg, CO2/km")
            return 0


        elif self.transport == "moto/scooter":
            print("Consommation carburant : "f"{0.0604 * self.km}kg, CO2/km")
            return 0.0604 * self.km

        elif self.transport == "bus":
            print("Consommation carburant : "f"{0.1043 * self.km}kg, CO2/km")
            return 0.1043 * self.km

    
    def get_logement(self):
        
            if self.chauffage == "pompe à chaleur":
                print ("Consommation chauffage : "f"{3.95 * self.surface}kg CO2/m²")
                return 3.95 * self.surface
            
            elif self.chauffage == "poêle à bois" :
                 print ("Consommation chauffage : "f"{9.2 * self.surface}kg CO2/m²")
                 return 9.2 * self.surface
            
            elif self.chauffage == "poêle à granulés" :
                 print ("Consommation chauffage : "f"{5.64 * self.surface}kg CO2/m²")
                 return 5.64 * self.surface
            
            elif self.chauffage == "électrique" :
                 print ("Consommation chauffage : "f"{11.85 * self.surface}kg CO2/m²")
                 return 11.85 * self.surface
            
            elif self.chauffage == "réseau de chaleur" :
                 print ("Consommation chauffage : "f"{18.67 * self.surface}kg CO2/m²")
                 return 18.67 * self.surface
            
            elif self.chauffage == "gaz" :
                 print ("Consommation chauffage : "f"{39 * self.surface}kg CO2/m²")
                 return 39 * self.surface
            
            elif self.chauffage == "fioul" :
                 print ("Consommation chauffage : "f"{57.17 * self.surface}kg CO2/m²")
                 return 57.17 * self.surface

            else :
                return f"le type de logement {type} n'est pas géré"
            




def create_conso():
    transport_choice = transport_var.get()
    surface_value = int(surface_entry.get())
    chauffage_choice = chauffage_var.get()
    km_value = int(km_entry.get())
    
    conso = Conso(transport_choice, surface_value, chauffage_choice, km_value)
    
    transport_result = conso.get_transport()
    logement_result = conso.get_logement()
    
    result_label.config(text=f"Consommation transport : {transport_result}kg CO2\nConsommation chauffage : {logement_result}kg CO2")

gui = Tk()

transport_var = StringVar()
surface_entry = Entry(gui)
chauffage_var = StringVar()
km_entry = Entry(gui)

Label(gui, text="Transport:").pack()
Radiobutton(gui, text="Voiture moteur thermique", variable=transport_var, value="voiture moteur thermique").pack(anchor=W)
Radiobutton(gui, text="Voiture moteur électrique", variable=transport_var, value="voiture moteur électrique").pack(anchor=W)
Radiobutton(gui, text="Métro", variable=transport_var, value="métro").pack(anchor=W)
Radiobutton(gui, text="Vélo et trotinette électrique", variable=transport_var, value="vélo et trotinette électrique").pack(anchor=W)
Radiobutton(gui, text="Vélo, marche à pied", variable=transport_var, value="vélo, marche à pied").pack(anchor=W)
Radiobutton(gui, text="Moto/scooter", variable=transport_var, value="moto/scooter").pack(anchor=W)
Radiobutton(gui, text="Bus", variable=transport_var, value="bus").pack(anchor=W)



Label(gui, text="Nombre de km parcouru:").pack()
km_entry.pack()


Label(gui, text="Chauffage:").pack()
Radiobutton(gui, text="Pompe à chaleur", variable=chauffage_var, value="pompe à chaleur").pack(anchor=W)
Radiobutton(gui, text="Poêle à bois", variable=chauffage_var, value="poêle à bois").pack(anchor=W)
Radiobutton(gui, text="Poêle à granulés", variable=chauffage_var, value="poêle à granulés").pack(anchor=W)
Radiobutton(gui, text="Électrique", variable=chauffage_var, value="électrique").pack(anchor=W)
Radiobutton(gui, text="Réseau de chaleur", variable=chauffage_var, value="réseau de chaleur").pack(anchor=W)
Radiobutton(gui, text="Gaz", variable=chauffage_var, value="gaz").pack(anchor=W)
Radiobutton(gui, text="Fioul", variable=chauffage_var, value="fioul").pack(anchor=W)

Label(gui, text="Surface du logement en m²:").pack()
surface_entry.pack()

Button(gui, text="Valider", command=create_conso).pack()

result_label = Label(gui, text="")
result_label.pack()

gui.mainloop()























# def add_value_to_list(choice):
#     conso.values.append(conso.logement(choice))

# def display_values():
#      total = sum(conso.values)
#      print("Total: ", total)

# conso=Conso(input("transport : "), int(input("surface du logement en m² : ")), input("chauffage : "), int(input("Nombre de km parcouru : ")))
# conso.get_transport()
# conso.get_logement()


# gui = Tk()


# r1 = Radiobutton(gui, text="Pompe à chaleur", value="pompe à chaleur", command=lambda : add_value_to_list("pompe à chaleur"))
# r1.pack(anchor = W)

# r2 = Radiobutton(gui, text="Pôele à bois", value="poêle à bois", command=lambda: add_value_to_list("poêle à bois"))
# r2.pack(anchor = W)

# r3 = Radiobutton(gui, text="Poêle à granulés", value="poêle à granulés", command=lambda: add_value_to_list("poêle à granulés"))
# r3.pack(anchor = W)

# validate_button = Button(gui, text="Valider", command = display_values)
# validate_button.pack()

# label = Label(gui)
# label.pack()
# gui.mainloop()
    
        

# test=Conso(input("transport : "), int(input("surface du logement en m² : ")), input("chauffage : "), int(input("Nombre de km parcouru : ")))