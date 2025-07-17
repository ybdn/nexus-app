# Interface Graphique Nexus (PyQt6)

Ce document décrit l'architecture et l'utilisation de l'interface graphique de l'application Nexus, développée avec **PyQt6**.

## 🖥️ Présentation Générale

L'interface graphique propose une expérience moderne, sombre et épurée, inspirée de GitHub, pour la gestion du personnel, des plannings et des tâches.

- **Navigation latérale** persistante (SideNavigation)
- **Vues principales** : Tableau de bord, Personnel, Planning, Tâches
- **Thème sombre** personnalisable via `stylesheet.qss`
- **Préférences utilisateur** (état de la barre latérale, thème) persistées dans `user_preferences.json`

## 📐 Architecture du GUI

```
MainWindow (QMainWindow)
│
├── Header (QWidget) : Titre de l'application
│
├── Content Area (QHBoxLayout)
│   ├── SideNavigation (QWidget)
│   │   └── Boutons : Tableau de Bord, Personnel, Planning, Tâches
│   └── QStackedWidget
│       ├── DashboardView (QWidget)
│       ├── PersonnelView (QWidget)
│       ├── PlanningView (QWidget)
│       └── TachesView (QWidget)
```

### Fichiers principaux :
- `main_window.py` : Fenêtre principale, gestion de la navigation et du layout
- `views.py` : Définition des vues (Dashboard, Personnel, Planning, Tâches)
- `widgets.py` : Composant de navigation latérale (SideNavigation)
- `stylesheet.qss` : Thème sombre (couleurs, boutons, tableaux, etc.)

## 🗂️ Détail des Vues

- **DashboardView** : Affiche des indicateurs clés (nombre d'employés, tâches en cours, absences prévues)
- **PersonnelView** : Liste des utilisateurs, bouton d'ajout, tableau interactif
- **PlanningView** : Vue du planning hebdomadaire (structure prête à être enrichie)
- **TachesView** : Liste des tâches (structure prête à être enrichie)

## 🧭 Navigation

- La navigation latérale permet de changer de vue instantanément.
- Le bouton actif est mis en surbrillance (bleu).
- Les préférences de navigation (vue active, état réduit/étendu) sont sauvegardées.

## 🎨 Thème & Personnalisation

- Le thème sombre est défini dans `gui/stylesheet.qss`.
- Les couleurs, polices et styles sont inspirés de GitHub Dark.
- Les boutons principaux et dangereux sont stylisés (`PrimaryButton`, `DangerButton`).
- Les préférences utilisateur (thème, sidebar) sont stockées dans `user_preferences.json`.

## 🛠️ Dépendances spécifiques

- `PyQt6` : Bibliothèque principale pour l'UI
- `qtawesome` : Icônes modernes pour la navigation

Installez-les avec :
```bash
pip install PyQt6 qtawesome
```

## 🚀 Exemple minimal de lancement

```python
import sys
from PyQt6.QtWidgets import QApplication
from gui.main_window import MainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    try:
        with open("gui/stylesheet.qss", "r") as f:
            app.setStyleSheet(f.read())
    except FileNotFoundError:
        print("Feuille de style non trouvée.")
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
```

## 🔗 Pour aller plus loin
- Voir le README principal pour l'architecture globale et la gestion des données.
- Voir `core/preferences.py` pour la gestion des préférences utilisateur.
- Voir `docs/THEMES.md` pour les détails sur le système de thèmes. 