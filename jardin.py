import json
from plante import Plante

class Jardin:
    def __init__(self):
        self.plantes = []
        self.saison = "printemps"

    def ajouter_plante(self, plante):
        self.plantes.append(plante)
        print(f"{plante.nom} ({plante.categorie}) a été plantée dans votre jardin!")

    def entretenir(self):
        for plante in self.plantes:
            plante.croissance_journaliere(self.saison)

    def afficher_etat(self):
        for plante in self.plantes:
            print(plante.etat())

    def sauvegarder(self, fichier="jardin.json"):
        with open(fichier, "w") as f:
            json.dump([p.etat() for p in self.plantes], f)
        print("Jardin sauvegardé!")
    
    def charger(self, fichier="jardin.json"):
        try:
            with open(fichier, "r") as f:
                data = json.load(f)
                for p in data:
                    self.ajouter_plante(Plante(p["Catégorie"], p["Nom"], 50, 50, 1))
            print("Jardin chargé!")
        except FileNotFoundError:
            print("Aucune sauvegarde trouvée.")

    def changer_saison(self, nouvelle_saison):
        if nouvelle_saison in ["printemps", "été", "automne", "hiver"]:
            self.saison = nouvelle_saison
            print(f"La saison a changé pour {nouvelle_saison}!")
        else:
            print("Saison invalide!")