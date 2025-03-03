import json
from plante import Plante

# Classe représentant le jardin
class Jardin:
    def __init__(self):
        self.plantes = []  # Liste pour stocker les plantes
        self.saison = "printemps"  # Saison par défaut

    # Ajouter une plante au jardin
    def ajouter_plante(self, plante):
        self.plantes.append(plante)
        print(f"{plante.nom} ({plante.categorie}) a été plantée dans votre jardin!")

    # Entretenir les plantes du jardin
    def entretenir(self):
        for plante in self.plantes:
            plante.croissance_journaliere(self.saison)

    # Afficher l'état de toutes les plantes
    def afficher_etat(self):
        for plante in self.plantes:
            print(plante.etat())

    # Sauvegarder l'état du jardin dans un fichier JSON
    def sauvegarder(self, fichier="jardin.json"):
        with open(fichier, "w") as f:
            json.dump([p.etat() for p in self.plantes], f)
        print("Jardin sauvegardé!")
    
    # Charger l'état du jardin depuis un fichier JSON
    def charger(self, fichier="jardin.json"):
        try:
            with open(fichier, "r") as f:
                data = json.load(f)
                for p in data:
                    self.ajouter_plante(Plante(p["Catégorie"], p["Nom"], 50, 50, 1))
            print("Jardin chargé!")
        except FileNotFoundError:
            print("Aucune sauvegarde trouvée.")

    # Changer la saison du jardin
    def changer_saison(self, nouvelle_saison):
        if nouvelle_saison in ["printemps", "été", "automne", "hiver"]:
            self.saison = nouvelle_saison
            print(f"La saison a changé pour {nouvelle_saison}!")
        else:
            print("Saison invalide!")