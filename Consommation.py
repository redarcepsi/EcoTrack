class Conso:

    def __init__(self, transport, surface, chauffage, km):
        self.transport = transport
        self.surface = surface
        self.chauffage = chauffage
        self.km = km

    def get_transport(self):
         
        if self.transport == "voiture moteur thermique":
            print("Consommation carburant : "f"{0.192 * self.km}kg CO2/km")

        elif self.transport == "voiture moteur électrique":
            print("Consommation carburant : "f"{0.0198 * self.km}kg, CO2/km")

        elif self.transport == "métro":
            print("Consommation carburant : "f"{0.0042 * self.km}kg, CO2/km")

        elif self.transport == "vélo/trotinette électrique":
            print("Consommation carburant : "f"{0.00223 * self.km}kg, CO2/km")

        elif self.transport == "moto/scooter":
            print("Consommation carburant : "f"{0.0604 * self.km}kg, CO2/km")

        elif self.transport == "bus":
            print("Consommation carburant : "f"{0.1043 * self.km}kg, CO2/km")
    
    def logement(self):
        
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
        

test=Conso(input("transport : "), int(input("surface du logement en m² : ")), input("chauffage : "), int(input("Nombre de km parcouru : ")))
test.get_transport()
test.logement()