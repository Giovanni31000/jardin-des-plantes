# Jardin des Plantes

Salut ! Ce projet est un simulateur de jardin virtuel où tu peux planter, arroser, fertiliser et tailler des plantes. Tu peux aussi sauvegarder et charger l'état de ton jardin, changer les saisons et gérer des événements aléatoires qui affectent tes plantes.

## Structure du projet

Le projet est divisé en plusieurs fichiers :

- `plante.py` : Contient la classe `Plante` qui représente une plante dans le jardin.
- `jardin.py` : Contient la classe `Jardin` qui gère les plantes et les actions sur le jardin.
- `evenement.py` : Contient la classe `EvenementAleatoire` qui génère des événements aléatoires affectant les plantes.
- `main.py` : Contient la fonction principale `menu` qui gère l'interface utilisateur et les interactions avec le jardin.

## Utilisation

Pour utiliser ce projet, exécute le fichier `main.py`. Tu verras un menu avec différentes options pour gérer ton jardin.

### Menu des options

1. **Planter une plante** : Ajoute une nouvelle plante au jardin.
2. **Arroser une plante** : Augmente l'humidité d'une plante existante.
3. **Fertiliser une plante** : Augmente la vitesse de croissance d'une plante existante.
4. **Tailler une plante** : Améliore la santé d'une plante existante.
5. **Afficher l'état du jardin** : Affiche l'état actuel de toutes les plantes dans le jardin.
6. **Sauvegarder et quitter** : Sauvegarde l'état actuel du jardin dans un fichier JSON et quitte le programme.
7. **Changer de saison** : Change la saison actuelle du jardin, ce qui affecte la croissance et la santé des plantes.

## Installation

1. Clone le dépôt sur ton IDE: https://github.com/Giovanni31000/jardin-des-plantes.git
2. Assure-toi d'avoir Python installé.
3. Exécute le fichier `main.py` pour démarrer le programme.

## Auteurs

Ce projet a été réalisé par DAMIENS Giovanni.