class Plante:
    def __init__(self, categorie, nom, besoin_eau, besoin_lumiere, vitesse_croissance, humidite=50, sante=100):
        # Initialisation des attributs de la plante
        self.categorie = categorie
        self.nom = nom
        self.besoin_eau = besoin_eau
        self.besoin_lumiere = besoin_lumiere
        self.vitesse_croissance = vitesse_croissance
        self.humidite = humidite
        self.sante = sante
        self.croissance = 0

    def arroser(self):
        # Augmente l'humidité de la plante
        self.humidite += 10
        print(f"Vous avez arrosé {self.nom}. Humidité : {self.humidite}%")
        
    def fertiliser(self):
        # Augmente la vitesse de croissance
        self.vitesse_croissance += 1
        print(f"Vous avez fertilisé {self.nom}. Croissance accélérée!")

    def tailler(self):
        # Améliore la santé de la plante
        self.sante += 5
        print(f"Vous avez taillé {self.nom}. Santé améliorée!")

    def croissance_journaliere(self, saison):
        # Ajuste l'humidité et la santé en fonction de la saison
        if saison == "été":
            self.humidite -= 10
            self.sante -= 2
        elif saison == "hiver":
            self.humidite -= 5
            self.sante -= 1
        else:
            self.humidite -= 7

        if self.humidite < self.besoin_eau:
            self.sante -= 5

        if self.humidite >= self.besoin_eau:
            self.croissance += self.vitesse_croissance
        else:
            self.croissance -= 1
        
        if self.sante <= 0:
            print(f"{self.nom} est morte...")
        
        if self.croissance >= 100:
            print(f"{self.nom} est arrivée à maturité!")

    def etat(self):
        # Retourne l'état de la plante
        return {
            "Catégorie": self.categorie,
            "Nom": self.nom,
            "Croissance": self.croissance,
            "Santé": self.sante,
            "Humidité": self.humidite
        }