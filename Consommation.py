class conso:
    def transport(self,transport):
        match transport:
            case "voiture":
                return "voiture"
            case "moto":
                return "moto"
            case "camionette":
                return "camionette"
            case "pied":
                return "pied"
            case "velo":
                return "velo"
            case other:
                return "error"
    
    def logement(self,type,taille):
        if type == "appartement":
            if taille <= 30 :
                pass
            elif taille > 31 and taille <= 50 :
                pass
            elif taille > 51 and taille <= 80 :
                pass
            else :
                pass
        elif type == "maison" :
            if taille <= 32 :
                pass
            elif taille > 33 and taille <= 50 :
                pass
            elif taille > 51 and taille <= 80 :
                pass
            else :
                pass
        else :
            return f"le type de logement {type} n'est pas géré"