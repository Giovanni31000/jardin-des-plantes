import random
import json
import time

# Classe représentant une plante dans le jardin
class Plante:
    def __init__(self, categorie, nom, besoin_eau, besoin_lumiere, vitesse_croissance, humidite=50, sante=100):
        # Initialisation des propriétés de la plante
        self.categorie = categorie  # Catégorie de la plante (ex : Fleur, Arbre)
        self.nom = nom  # Nom de la plante (ex : "Tulipe")
        self.besoin_eau = besoin_eau  # Besoin en eau de la plante
        self.besoin_lumiere = besoin_lumiere  # Besoin en lumière de la plante
        self.vitesse_croissance = vitesse_croissance  # Vitesse de croissance de la plante
        self.humidite = humidite  # Humidité actuelle de la plante (50 par défaut)
        self.sante = sante  # Santé de la plante (100 par défaut, en pleine forme)
        self.croissance = 0  # Croissance actuelle de la plante (de 0 à 100)

    def arroser(self):
        # Méthode pour arroser la plante, augmentant l'humidité
        self.humidite += 10
        print(f"Vous avez arrosé {self.nom}. Humidité : {self.humidite}%")
        
    def fertiliser(self):
        # Méthode pour fertiliser la plante, augmentant la vitesse de croissance
        self.vitesse_croissance += 1
        print(f"Vous avez fertilisé {self.nom}. Croissance accélérée!")

    def tailler(self):
        # Méthode pour tailler la plante, améliorant sa santé
        self.sante += 5
        print(f"Vous avez taillé {self.nom}. Santé améliorée!")

    def croissance_journaliere(self, saison):
        # Méthode pour gérer la croissance de la plante chaque jour
        if self.humidite >= self.besoin_eau:
            self.croissance += self.vitesse_croissance
        else:
            self.sante -= 5  # Si la plante manque d'eau, sa santé diminue
        
        # Si c'est l'hiver, la croissance est plus lente
        if saison == "hiver":
            self.croissance -= 1  # Réduction de la croissance en hiver

        if self.sante <= 0:
            print(f"{self.nom} est morte...")  # Si la santé atteint 0, la plante meurt
        
        if self.croissance >= 100:
            print(f"{self.nom} est arrivée à maturité!")  # Si la croissance atteint 100, la plante est mature

    def etat(self):
        # Retourne un dictionnaire représentant l'état actuel de la plante
        return {
            "Catégorie": self.categorie,
            "Nom": self.nom,
            "Croissance": self.croissance,
            "Santé": self.sante,
            "Humidité": self.humidite
        }

# Classe représentant le jardin dans lequel on gère les plantes
class Jardin:
    def __init__(self):
        self.plantes = []  # Liste pour stocker toutes les plantes
        self.saison = "printemps"  # Saison par défaut, au début c'est le printemps

    def ajouter_plante(self, plante):
        # Ajoute une nouvelle plante au jardin
        self.plantes.append(plante)
        print(f"{plante.nom} ({plante.categorie}) a été plantée dans votre jardin!")

    def entretenir(self):
        # Appelle la méthode de croissance journalière pour chaque plante
        for plante in self.plantes:
            plante.croissance_journaliere(self.saison)

    def afficher_etat(self):
        # Affiche l'état de chaque plante
        for plante in self.plantes:
            print(plante.etat())

    def sauvegarder(self, fichier="jardin.json"):
        # Sauvegarde l'état actuel du jardin dans un fichier JSON
        with open(fichier, "w") as f:
            json.dump([p.etat() for p in self.plantes], f)
        print("Jardin sauvegardé!")  # Sauvegarde réussie
    
    def charger(self, fichier="jardin.json"):
        # Charge l'état du jardin depuis un fichier JSON
        try:
            with open(fichier, "r") as f:
                data = json.load(f)
                for p in data:
                    # On recrée chaque plante à partir des données sauvegardées
                    self.ajouter_plante(Plante(p["Catégorie"], p["Nom"], 50, 50, 1))
            print("Jardin chargé!")  # Si le fichier est trouvé et chargé
        except FileNotFoundError:
            print("Aucune sauvegarde trouvée.")  # Si le fichier n'existe pas

    def changer_saison(self, nouvelle_saison):
        # Permet de changer la saison du jardin
        if nouvelle_saison in ["printemps", "été", "automne", "hiver"]:
            self.saison = nouvelle_saison
            print(f"La saison a changé pour {nouvelle_saison}!")
        else:
            print("Saison invalide!")  # Si la saison n'est pas valide

# Classe pour générer des événements aléatoires dans le jardin
class EvenementAleatoire:
    @staticmethod
    def generer_evenement(jardin):
        # Choix d'un événement aléatoire parmi une liste d'événements possibles
        evenements = ["tempête", "sécheresse", "parasites", "maladie", None]
        event = random.choice(evenements)
        if event:
            print(f"Un événement s'est produit : {event}!")  # Affichage de l'événement
            # On applique l'effet de l'événement à chaque plante
            for plante in jardin.plantes:
                plante.sante -= 10  # La santé des plantes diminue à cause de l'événement

# Fonction principale qui gère l'interface du programme
def menu():
    jardin = Jardin()  # Création d'un nouveau jardin
    while True:
        # Affichage du menu pour que l'utilisateur choisisse une action
        print("\nMenu du Jardin Virtuel")
        print("1. Planter une plante")
        print("2. Arroser une plante")
        print("3. Fertiliser une plante")
        print("4. Tailler une plante")
        print("5. Afficher l'état du jardin")
        print("6. Sauvegarder et quitter")
        print("7. Changer de saison")
        choix = input("Votre choix : ")
        
        if choix == "1":
            # Planter une nouvelle plante
            categorie = input("Catégorie de la plante (Fleur, Légume, Arbre, etc.) : ")
            nom = input("Nom de la plante : ")
            humidite = int(input("Humidité initiale de la plante (0-100) : "))
            sante = int(input("Santé initiale de la plante (0-100) : "))
            jardin.ajouter_plante(Plante(categorie, nom, 50, 50, 1, humidite, sante))
        elif choix == "2":
            # Arroser une plante existante
            if jardin.plantes:
                for i, plante in enumerate(jardin.plantes):
                    print(f"{i+1}. {plante.nom} ({plante.categorie})")
                idx = int(input("Choisissez une plante à arroser : ")) - 1
                if 0 <= idx < len(jardin.plantes):
                    jardin.plantes[idx].arroser()
                else:
                    print("Index invalide!")  # Si l'index est incorrect
            else:
                print("Aucune plante à arroser!")  # Si le jardin est vide
        elif choix == "3":
            # Fertiliser une plante existante
            if jardin.plantes:
                for i, plante in enumerate(jardin.plantes):
                    print(f"{i+1}. {plante.nom} ({plante.categorie})")
                idx = int(input("Choisissez une plante à fertiliser : ")) - 1
                if 0 <= idx < len(jardin.plantes):
                    jardin.plantes[idx].fertiliser()
                else:
                    print("Index invalide!")
            else:
                print("Aucune plante à fertiliser!")
        elif choix == "4":
            # Tailler une plante existante
            if jardin.plantes:
                for i, plante in enumerate(jardin.plantes):
                    print(f"{i+1}. {plante.nom} ({plante.categorie})")
                idx = int(input("Choisissez une plante à tailler : ")) - 1
                if 0 <= idx < len(jardin.plantes):
                    jardin.plantes[idx].tailler()
                else:
                    print("Index invalide!")
            else:
                print("Aucune plante à tailler!")
        elif choix == "5":
            # Afficher l'état actuel du jardin
            jardin.afficher_etat()
        elif choix == "6":
            # Sauvegarder l'état du jardin et quitter le programme
            jardin.sauvegarder()
            print("Jardin sauvegardé. À bientôt!")
            break
        elif choix == "7":
            # Changer la saison
            saison = input("Entrez la nouvelle saison (printemps, été, automne, hiver) : ").lower()
            jardin.changer_saison(saison)
        else:
            # Si l'utilisateur entre un choix invalide
            print("Choix invalide, veuillez réessayer.")

if __name__ == "__main__":
    menu()  # Exécution du menu principal
