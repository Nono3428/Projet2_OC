# Programme d'Extraction des Prix

## Description
Ce projet est un outil de web scraping conçu pour extraire et traiter des données provenant de librairies en ligne.

Il récupère des informations sur les livres, y compris les titres, les prix, les descriptions et les images,
et stocke les données dans un format structuré pour une analyse ultérieure.

# Installation

## Prérequis
- Python 3.x

Lors de l'instalation cochez la case "Add Python(n°version) to Path" pour plus de facilité avec l'invite de commande
```
https://www.python.org/
```
- Git  
```
https://git-scm.com/
```
## Étapes d'Installation 
- Ouvrez un terminal/invite de commande:
- Clonez le repo grâce à la commande :
    ```
    git clone https://github.com/Nono3428/Projet2_OC.git
    ```
    Placez-vous dans le dossier
    ```
    cd .\Projet2_OC
    ```
- Créez votre environnement virtuel:
    ```
    python -m venv "env"
    ```
- Activez votre environnement virtuel:
    - Placez-vous dans le dossier de l'environnement
        ```
        cd .\env\Scripts
        ```
    - Activez le avec la commande:
        ```
        .\activate
        ```
        - Pour vérifier que votre environnement est bien activé, vérifiez si le nom de votre environnement apparaît entre parenthèses au début de la ligne de commande, 
        ou exécutez la commande suivante (si la liste est vide, vous êtes bien dans votre environnement) 
        ```
        pip list
        ```
    - Revenez à la racine de votre dossier avec la commande :
        ```
        cd ../..
        ```
- Installez les dépendances pour le programme :
    ```
    pip install -r .\requirements.txt
    ```

# Utilisation

- Pour lancer le programme éxcuter la commande :
    ```
    python .\main.py
    ```
    Le programme vous demandera combien de catégories vous souhaitez récupérer (il les récupère les unes après les autres).

    Indiquez le nombre souhaité ou appuyez sur "Entrée" pour récupérer toutes les catégories du site.

Les données seront récupérées et stockées dans des fichiers appropriés.

Un dossier 'Data' sera créé, contenant 2 sous-dossier :
- Un dossier 'Fichier_csv' :
    - Dans ce dossier les données des livres de chaque catégories seront enregistrés sous forme de fichier 'csv', pour chaque catégories un fichier 'csv' sera crée avec le nom de celle-ci
- Un dossier 'Image' :
    - Dans ce dossier les images des livres de chaque catégories seront enregistrés sous format 'jpg', pour chaque catégories un sous-dossier sera crée avec toutes les images des livres présent dans cette catégories.

Une fois le programme terminé vous pouvez désactiver votre environnement virtuel :
- Placez-vous dans le dossier de l'environnement 
    ```
    cd .\env\Scripts
    ```
- Effectuez la commande suivante :
    ```
    deactivate
    ```