# Projet Nexus (Desktop)

Nexus est une application de bureau visant à centraliser la gestion du personnel, des plannings, des services journaliers et des tâches pour une petite organisation. L'objectif est de fournir une source unique de vérité, accessible et en temps réel, via une application locale.

## ✨ Fonctionnalités

- **Gestion de Planning** : Création et visualisation de plannings mensuels prévisionnels.
- **Service Journalier** : Génération et suivi du service pour chaque jour.
- **Gestion des Tâches** : Attribution et suivi de tâches pour les équipes.
- **Gestion des Rôles et Permissions** : Contrôle d'accès fin basé sur les rôles (administrateur, chef d'équipe, membre).
- **Centralisation** : Une seule plateforme pour toutes les informations relatives à l'organisation de l'équipe.

## 🛠️ Technologies

| Partie              | Technologies                                 |
| ------------------- | -------------------------------------------- |
| **Application**     | `Python`, `CustomTkinter`                    |
| **Base de données** | `SQLite` (via un fichier partagé `nexus.db`) |

## 📂 Structure du Dépôt

.
├── core/
│ ├── **init**.py
│ └── database.py # Logique pour la connexion et les opérations sur la BDD SQLite.
├── gui/
│ ├── **init**.py
│ └── main_window.py # Code pour la fenêtre principale de l'application.
├── assets/ # Dossier pour les icônes ou autres ressources.
├── main.py # Point d'entrée principal de l'application.
├── requirements.txt # Fichier listant les dépendances Python.
└── README.md # Documentation du projet.

## 🚀 Démarrage Rapide

Pour installer et lancer l'application, suivez ces étapes :

1. **Cloner le projet** (si vous utilisez git) :

   ```bash
   git clone <url_du_projet>
   cd nexus_app
   ```

2. **Créer un environnement virtuel** :

   ```bash
   python -m venv venv
   ```

3. **Activer l'environnement** :

   - Sur Windows :

     ```bash
     .\venv\Scripts\activate
     ```

   - Sur macOS/Linux :

     ```bash
     source venv/bin/activate
     ```

4. **Installer les dépendances** :

   ```bash
   pip install -r requirements.txt
   ```

**5. Lancer l'application** :

```bash
python main.py
```

Au premier lancement, un fichier `nexus.db` sera créé à la racine du projet.

## 📦 Déploiement

Le projet est conçu pour être packagé en un fichier `.exe` autonome à l'aide de **PyInstaller**.

```bash
# Exemple de commande de packaging
pyinstaller --onefile --windowed --name NexusApp main.py
```

## 🌐 Configuration Multi-Utilisateurs

Pour que plusieurs utilisateurs puissent accéder aux mêmes données, le fichier `nexus.db` doit être partagé :

1. Lancez l'application une première fois pour générer `nexus.db`.
2. Déplacez ce fichier `nexus.db` vers un lecteur réseau accessible par tous les postes de travail (par exemple, `Z:\DossierPartage\nexus.db`).
3. (Étape future) Mettez à jour le chemin dans `core/database.py` pour pointer vers l'emplacement réseau du fichier.
