from jardin import Jardin
from plante import Plante

# Fonction principale pour gérer le menu du jardin virtuel
def menu():
    jardin = Jardin()  # Crée une instance de Jardin
    while True:
        # Affiche le menu des options
        print("\nMenu du Jardin Virtuel")
        print("1. Planter une plante")
        print("2. Arroser une plante")
        print("3. Fertiliser une plante")
        print("4. Tailler une plante")
        print("5. Afficher l'état du jardin")
        print("6. Sauvegarder et quitter")
        print("7. Changer de saison")
        choix = input("Votre choix : ")  # Demande à l'utilisateur de faire un choix
        
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
                    print("Index invalide!")
            else:
                print("Aucune plante à arroser!")
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
            # Sauvegarder l'état du jardin et quitter
            jardin.sauvegarder()
            print("Jardin sauvegardé. À bientôt!")
            break
        elif choix == "7":
            # Changer la saison du jardin
            saison = input("Entrez la nouvelle saison (printemps, été, automne, hiver) : ").lower()
            jardin.changer_saison(saison)
        else:
            # Si l'utilisateur entre un choix invalide
            print("Choix invalide, veuillez réessayer.")

if __name__ == "__main__":
    menu()  # Exécute le menu principal