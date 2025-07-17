# Projet Nexus (Desktop)

Nexus est une application de bureau visant à centraliser la gestion du personnel, des plannings, des services journaliers et des tâches pour une petite organisation. L'objectif est de fournir une source unique de vérité, accessible et en temps réel, via une application locale.

## ✨ Fonctionnalités

- **Gestion de Planning** : Création et visualisation de plannings hebdomadaires et mensuels.
- **Service Journalier** : Génération et suivi du service pour chaque jour.
- **Gestion des Tâches** : Attribution et suivi de tâches pour les équipes.
- **Gestion des Rôles et Permissions** : Contrôle d'accès fin basé sur les rôles (administrateur, manager, employé).
- **Centralisation** : Une seule plateforme pour toutes les informations relatives à l'organisation de l'équipe.
- **Thème sombre inspiré de GitHub** : Interface moderne et personnalisable.
- **Préférences utilisateur** : Thème et état de la barre latérale persistants.

## 🛠️ Technologies

| Partie              | Technologies                                 |
| ------------------- | -------------------------------------------- |
| **Application**     | `Python`, `PyQt6`, `qtawesome`               |
| **Base de données** | `SQLite` (via un fichier partagé `nexus.db`) |

## 📂 Structure du Dépôt

```
.
├── core/
│   ├── __init__.py
│   ├── database.py        # Gestion de la base SQLite (création, tables)
│   ├── models.py          # Modèles de données (User, Team, Absence, Task)
│   ├── preferences.py     # Gestion des préférences utilisateur (JSON)
│   └── services.py        # Logique métier (simulation en mémoire)
├── gui/
│   ├── __init__.py
│   ├── main_window.py     # Fenêtre principale (PyQt6)
│   ├── views.py           # Vues : Dashboard, Personnel, Planning, Tâches
│   ├── widgets.py         # Widgets personnalisés (navigation latérale)
│   └── stylesheet.qss     # Thème sombre inspiré GitHub
├── assets/                # Icônes ou autres ressources
├── main.py                # Point d'entrée principal de l'application
├── requirements.txt       # Dépendances Python
├── user_preferences.json  # Préférences utilisateur (généré au runtime)
└── README.md              # Documentation du projet
```

## 🧩 Modèles de Données (extraits)

```python
from dataclasses import dataclass, field
from typing import List, Literal, Optional

@dataclass
class User:
    id: int
    username: str
    role: Literal['employe', 'manager', 'admin']
    team_id: Optional[int] = None

@dataclass
class Team:
    id: int
    name: str
    members: List[User] = field(default_factory=list)
```

## 🚀 Démarrage Rapide

1. **Cloner le projet** :
   ```bash
   git clone <url_du_projet>
   cd nexus-app
   ```
2. **Créer un environnement virtuel** :
   ```bash
   python -m venv venv
   ```
3. **Activer l'environnement** :
   - Windows : `venv\Scripts\activate`
   - macOS/Linux : `source venv/bin/activate`
4. **Installer les dépendances** :
   ```bash
   pip install -r requirements.txt
   ```
5. **Lancer l'application** :
   ```bash
   python main.py
   ```

Au premier lancement, un fichier `nexus.db` et un fichier `user_preferences.json` seront créés à la racine du projet.

## 🎨 Thème et Préférences Utilisateur

- Le thème sombre est appliqué par défaut (voir `gui/stylesheet.qss`).
- Les préférences utilisateur (état de la barre latérale, mode clair/sombre) sont sauvegardées dans `user_preferences.json`.

## 📦 Déploiement

Le projet peut être packagé en exécutable autonome avec **PyInstaller** :
```bash
pyinstaller --onefile --windowed --name NexusApp main.py
```

## 🌐 Multi-Utilisateurs

Pour partager la base de données :
1. Lancez l'application une première fois pour générer `nexus.db`.
2. Déplacez ce fichier vers un dossier réseau accessible à tous.
3. Modifiez le chemin dans `core/database.py` si besoin.

## 🔗 Ressources complémentaires
- Voir `docs/` pour les spécifications détaillées backend et UI.
- Voir `gui/README_GUI.md` pour la documentation spécifique à l'interface graphique.
