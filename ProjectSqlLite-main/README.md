# ProjectSqlLite
**Titre du Projet: Création d'une Application Web pour l'Exploration et l'Exécution de Requêtes SQL sur des Bases de Données SQLite**

**Description du Projet:**
L'objectif de ce projet est de créer une application web permettant aux utilisateurs d'explorer et d'exécuter des requêtes SQL sur des bases de données SQLite. L'application offrira une interface conviviale où les utilisateurs pourront sélectionner un fichier de base de données SQLite, visualiser les tables disponibles, afficher les détails des tables et soumettre des requêtes SQL pour obtenir des résultats instantanés.

---


![Animated GIF](projectsql.gif)

**Préliminaire**
* [lien vers le fichier Google Drive pour sqlite et python](https://drive.google.com/file/d/158QczWn-TwY6TlCo87qZr54FS2iq3376/view?usp=sharing)

**Étapes du Projet:**

1. **Installation des Prérequis:**
   - Installer Python sur le système.
   - Installer les bibliothèques nécessaires à l'aide de pip:
     ```
     pip install streamlit pandas sqlite3
     ```

2. **Création du Fichier Python:**
   - Créer un fichier Python nommé `app.py`.

3. **Importation des Bibliothèques:**
   - Importer les bibliothèques nécessaires dans le fichier `app.py`:
     ```python
     import streamlit as st
     import pandas as pd
     import sqlite3
     import os
     ```

4. **Définition des Fonctions Utiles:**
   - Définir les fonctions pour exécuter des requêtes SQL et obtenir les noms des tables dans la base de données SQLite.

5. **Définition des Pages de l'Application:**
   - Créer une page d'accueil (`Home`) où les utilisateurs peuvent sélectionner un fichier de base de données, explorer les tables et soumettre des requêtes SQL.
   - Créer une page `About` pour afficher des informations sur le développeur ou l'application.

6. **Interface Utilisateur avec Streamlit:**
   - Utiliser Streamlit pour créer une interface utilisateur interactive avec des éléments tels que les zones de texte, les boutons, les sélecteurs, les cadres d'expansion, etc.

7. **Gestion des Entrées Utilisateur:**
   - Demander à l'utilisateur de fournir le chemin du fichier de base de données SQLite.
   - Vérifier si le fichier existe et émettre un message d'erreur le cas échéant.

8. **Connexion à la Base de Données:**
   - Établir une connexion à la base de données SQLite sélectionnée.

9. **Affichage des Détails de la Base de Données:**
   - Afficher les noms des tables disponibles dans un cadre d'expansion.
   - Afficher les détails des colonnes pour chaque table sélectionnée.

10. **Soumission et Exécution des Requêtes SQL:**
    - Permettre aux utilisateurs de soumettre des requêtes SQL via un formulaire.
    - Exécuter la requête SQL soumise et afficher les résultats dans un cadre d'expansion.

11. **Gestion des Erreurs:**
    - Gérer les erreurs de syntaxe SQL et afficher un message d'erreur approprié.

12. **Fermeture de la Connexion à la Base de Données:**
    - Fermer la connexion à la base de données une fois que l'utilisateur a terminé ses activités.

13. **Exécution de l'Application:**
    - Lancer l'application en exécutant le fichier `app.py`.

**Prérequis:**
- Connaissance de base en Python.
- Familiarité avec les requêtes SQL.
- Compréhension de base de Streamlit pour la création d'applications web.
- Un environnement Python configuré avec les bibliothèques requises installées.

En suivant ces étapes et en respectant les prérequis, vous pourrez créer une application web fonctionnelle pour explorer et exécuter des requêtes SQL sur des bases de données SQLite à l'aide de Python et Streamlit.
