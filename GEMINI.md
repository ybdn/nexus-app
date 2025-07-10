# Instructions pour Gemini

Ce fichier contient les instructions et conventions pour le projet **Nexus (Desktop)**.

## Vue d'ensemble du projet

L'objectif est de créer une application de bureau en Python pour la gestion d'équipe (personnel, plannings, tâches). L'application utilise une base de données SQLite centralisée sur un lecteur réseau pour permettre un accès partagé des données entre plusieurs postes.

Pour plus de détails, consultez le `README.md`.

## Technologies

- **Langage** : Python 3
- **Interface Graphique (GUI)** : `customtkinter`
- **Base de données** : `sqlite3` (module natif de Python)
- **Packaging** : `PyInstaller` (prévu pour la distribution)

## Structure des Fichiers

- `main.py`: Point d'entrée de l'application. Orchestre l'initialisation de la base de données et le lancement de l'interface graphique.
- `core/`: Contient la logique métier de base.
  - `database.py`: Gère la connexion à la base de données SQLite, la création des tables et les opérations CRUD.
- `gui/`: Contient tous les composants de l'interface graphique.
  - `main_window.py`: Définit la fenêtre principale de l'application.
- `assets/`: Contient les ressources statiques (icônes, images, etc.).
- `requirements.txt`: Liste les dépendances Python du projet.

## Scripts Utiles

- **Installer les dépendances** :
  ```bash
  pip install -r requirements.txt
  ```
- **Lancer l'application en mode développement** :
  ```bash
  python main.py
  ```
- **Créer un exécutable pour la distribution** (exemple) :
  ```bash
  pyinstaller --onefile --windowed --name NexusApp main.py
  ```

## Conventions de code

- **Style de code** : Suivre les conventions de la [PEP 8](https://www.python.org/dev/peps/pep-0008/).
- **Nommage** :
  - Noms de variables et de fonctions : `snake_case` (ex: `ma_variable`).
  - Noms de classes : `PascalCase` (ex: `MaClasse`).
- **Typage** : Utiliser les indications de type (`type hints`) de Python autant que possible pour améliorer la clarté et la robustesse du code.
- **Documentation** : Rédiger les docstrings en français pour les modules, classes et fonctions importants.
- **Langue** : Le code, les commentaires et la documentation doivent être en **français**.
