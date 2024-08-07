# Programme d'Extraction des Prix

## Description
Ce projet est un outil de web scraping conçu pour extraire et traiter des données provenant de librairies en ligne. 
Il récupère des informations sur les livres, y compris les titres, les prix, les descriptions et les images, 
et stocke les données dans un format structuré pour une analyse ultérieure.

# Installation
Pour une meilleure pratique, toutes les installations se feront dans un environnement virtuel.

# Étapes d'Installation 
- Installez python grâce au lien :
    ```
    https://www.python.org/downloads/
    ```
    Cochez la case "Add Python(n°version) to Path" pour plus de facilité avec l'invite de commande
- Ouvrez un terminal/invite de commande:
- Créez votre environnement virtuel:
    ```
    python -m venv "nom de l'environnement"
    ```
- Activez votre environnement virtuel:
    Placez-vous dans le dossier de l'environnement
        ```
        cd/"nom de l'environnement"/Script
        ```
    Activez le avec la commande:
        ```
        .\activate
        ```
        Pour vérifier que votre environnement est bien activé, vérifiez si le nom de votre environnement apparaît entre parenthèses au début de la ligne de commande, 
        ou exécutez la commande suivante (si la liste est vide, vous êtes bien dans votre environnement) 
        ```
        pip list
        ```
    Revenez à la racine de votre dossier avec la commande :
        ```
        cd../..
        ```
- Clonez le dépôt grâce à la commande :
    ```
    git clone https://github.com/Nono3428/Projet2_OC.git
    ```
- Installez les dépendances pour le programme :
    ```
    pip install -r requirements.txt
    ```

# Utilisation

- Pour lancer le programme éxcuter la commande :
    ```
    python .\main.py
    ```
    Le programme vous demandera combien de catégories vous souhaitez récupérer (le programme les récupère les unes après les autres).
        Exemple : si vous souhaitez la catégorie "Art" qui correspond à la 25ème place, vous devrez attendre que le programme récupère les 24 catégories précédentes.
    Indiquez le nombre souhaité ou appuyez sur "Entrée" pour récupérer toutes les catégories du site.
        Je précise que si vous voulez récupérer les 10 premières catégories, vous devez indiquer le chiffre 9 (car le programme commence à 0).

Les données seront récupérées et stockées dans des fichiers appropriés. Un dossier 'Data' sera créé, contenant :
- Un dossier 'Fichier_csv' :
    A l'intérieur, toutes les données de chaque livre pour chaque catégorie seront stockées dans des fichiers 'csv'. Chaque catégorie aura son propre fichier 'csv'.
- Un dossier 'Image' :
    A l'intérieur, vous trouverez les images de chaque livre pour chaque catégorie. Comme pour les fichiers 'csv', chaque catégorie aura son propre dossier contenant les photos de chaque livre.

Une fois le programme terminé vous pouvez désactiver votre environnement virtuel :
    Placez-vous dans le dossier de l'environnement 
        ```
        cd/"nom de l'environnement"/Script
        ```
    Effectuez la commande suivante :
        ```
        deactivate
        ```