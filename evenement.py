import random

# Classe pour générer des événements aléatoires dans le jardin
class EvenementAleatoire:
    @staticmethod
    def generer_evenement(jardin):
        # Liste des événements possibles
        evenements = ["tempête", "sécheresse", "parasites", "maladie", None]
        
        # Choisir un événement aléatoire
        event = random.choice(evenements)
        
        # Si un événement est choisi
        if event:
            print(f"Un événement s'est produit : {event}!")
            
            # Appliquer l'effet de l'événement à chaque plante
            for plante in jardin.plantes:
                plante.sante -= 10