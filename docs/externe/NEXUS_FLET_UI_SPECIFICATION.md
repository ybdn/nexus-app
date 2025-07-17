# Spécification d'Interface Utilisateur pour Nexus (Version Flet)

**Document à destination d'un agent IA développeur.**

**Objectif :** Créer une application de bureau locale et fonctionnelle en Python avec le framework Flet, en se basant sur les fonctionnalités de l'application web Nexus existante.

---

## 1. Introduction et Concept Général

**Nexus** est une application de gestion d'équipe conçue pour optimiser la planification, le suivi des tâches, la gestion des absences et la communication interne.

Cette version locale doit reprendre les fonctionnalités essentielles de manière simple, rapide et intuitive, en utilisant les composants natifs offerts par Flet pour garantir la performance et la simplicité du code.

**Public Cible de l'Application Flet :**
- **Managers d'équipe :** Pour la planification, la validation des absences et le suivi des projets.
- **Employés :** Pour consulter leur planning, déclarer des absences et voir les tâches assignées.

---

## 2. Principes Directeurs pour l'UI (Flet)

1.  **Clarté et Simplicité :** L'interface doit être épurée. Chaque écran doit servir un objectif unique et clair.
2.  **Composants Natifs :** Utiliser en priorité les composants standards de Flet (`ft.TextField`, `ft.DataTable`, `ft.AlertDialog`, `ft.NavigationRail`, etc.) pour une expérience cohérente.
3.  **Réactivité :** L'interface doit se mettre à jour de manière fluide en réponse aux actions de l'utilisateur (ex: ajout d'une tâche, changement de vue du planning).
4.  **Navigation Centrale :** La navigation principale entre les modules (Planning, Équipes, Absences, etc.) doit être persistante et toujours accessible.
5.  **Feedback Utilisateur :** Fournir des confirmations visuelles pour les actions (ex: `ft.SnackBar` pour "Absence enregistrée") et des indicateurs de chargement (`ft.ProgressRing`) si des opérations prennent du temps.

---

## 3. Architecture de l'Interface Utilisateur (UI)

L'application sera structurée autour d'une vue principale contenant une barre de navigation latérale et une zone de contenu qui affichera l'écran sélectionné.

### 3.1. Structure Globale et Navigation

-   **Conteneur Principal :** `ft.Row`
    -   **Rail de Navigation :** `ft.NavigationRail` à gauche. C'est le composant principal pour changer de vue.
        -   **Destinations :**
            -   `ft.NavigationRailDestination(icon=ft.icons.CALENDAR_MONTH, label="Planning")`
            -   `ft.NavigationRailDestination(icon=ft.icons.GROUP, label="Équipes")`
            -   `ft.NavigationRailDestination(icon=ft.icons.BEACH_ACCESS, label="Absences")`
            -   `ft.NavigationRailDestination(icon=ft.icons.TASK, label="Tâches")`
            -   `ft.NavigationRailDestination(icon=ft.icons.NOTIFICATIONS, label="Notifications")`
            -   `ft.NavigationRailDestination(icon=ft.icons.ADMIN_PANEL_SETTINGS, label="Admin")`
    -   **Séparateur Vertical :** `ft.VerticalDivider`
    -   **Zone de Contenu :** `ft.Column(expand=True)` qui affichera la vue active.

-   **Barre d'Application (Optionnelle mais recommandée) :** `ft.AppBar` en haut pour afficher le titre de l'écran actuel et un bouton de déconnexion/profil utilisateur.

### 3.2. Écran de Connexion (Vue Initiale)

-   **Objectif :** Permettre à l'utilisateur de s'authentifier.
-   **Composants Flet :**
    -   `ft.Column` centré verticalement et horizontalement.
    -   `ft.Text("Nexus", size=32)`
    -   `ft.TextField(label="Nom d'utilisateur")`
    -   `ft.TextField(label="Mot de passe", password=True)`
    -   `ft.FilledButton(text="Se connecter", on_click=...)`

---

## 4. Écrans Détaillés et Leurs Composants

### 4.1. Écran "Planning"

-   **Objectif :** Visualiser les plannings des équipes et des individus.
-   **Composants Flet :**
    -   **Filtres (en haut) :** `ft.Row`
        -   `ft.Dropdown(label="Équipe", options=[...])` pour filtrer par équipe.
        -   `ft.Dropdown(label="Vue", options=["Mois", "Semaine"])` pour changer la granularité.
        -   `ft.DatePicker` pour sélectionner une date spécifique.
    -   **Vue Calendrier :**
        -   Ce sera la partie la plus complexe. Flet n'a pas de calendrier complexe natif.
        -   **Suggestion d'implémentation :** Utiliser une `ft.GridView` ou un `ft.Column` de `ft.Row` pour simuler une grille. Chaque cellule sera un `ft.Container` avec une couleur de fond différente selon l'événement (travail, absence, etc.) et un `ft.Text` pour le nom de la personne.
        -   Un `ft.DataTable` est une alternative plus simple pour une vue "liste" ou "semaine".
            -   **Colonnes :** `ft.DataColumn("Employé")`, `ft.DataColumn("Lundi")`, `ft.DataColumn("Mardi")`, ...
            -   **Lignes :** `ft.DataRow` avec des `ft.DataCell` contenant des `ft.Container` colorés.
    -   **Interactivité :**
        -   Cliquer sur une cellule pourrait ouvrir un `ft.AlertDialog` pour afficher les détails de l'événement ou en créer un nouveau.

### 4.2. Écran "Équipes"

-   **Objectif :** Gérer les équipes et leurs membres.
-   **Composants Flet :**
    -   `ft.Row` pour les actions principales :
        -   `ft.FilledButton("Créer une équipe", on_click=...)`
    -   `ft.ListView` ou `ft.Column` pour afficher la liste des équipes.
    -   **Pour chaque équipe :**
        -   Un `ft.Card` ou `ft.Container` avec un `ft.Column`.
        -   `ft.Text(value="Nom de l'équipe", weight=ft.FontWeight.BOLD)`
        -   Un `ft.DataTable` pour lister les membres.
            -   **Colonnes :** `ft.DataColumn("Nom")`, `ft.DataColumn("Rôle")`, `ft.DataColumn("Actions")`.
            -   **Cellules d'actions :** `ft.IconButton(icon=ft.icons.DELETE)` pour retirer un membre.
        -   `ft.Row` avec des boutons : `ft.TextButton("Ajouter un membre")`, `ft.TextButton("Renommer")`, `ft.TextButton("Supprimer l'équipe")`.
    -   **Dialogues (`ft.AlertDialog`) :**
        -   Pour la création/renommage d'équipe (un `ft.TextField` et un bouton "Valider").
        -   Pour l'ajout d'un membre (un `ft.Dropdown` avec la liste des utilisateurs et un bouton "Ajouter").

### 4.3. Écran "Absences"

-   **Objectif :** Gérer les demandes d'absence (création, validation, refus).
-   **Composants Flet :**
    -   `ft.Row` pour les actions :
        -   `ft.FilledButton("Déclarer une absence", on_click=...)`
    -   `ft.DataTable` pour afficher les demandes d'absence.
        -   **Colonnes :** `ft.DataColumn("Employé")`, `ft.DataColumn("Date début")`, `ft.DataColumn("Date fin")`, `ft.DataColumn("Motif")`, `ft.DataColumn("Statut")`, `ft.DataColumn("Actions")`.
        -   **Statut :** Utiliser un `ft.Chip` avec des couleurs différentes (ex: orange pour "En attente", vert pour "Approuvée", rouge pour "Refusée").
        -   **Actions (pour les managers) :** `ft.Row` avec `ft.IconButton(icon=ft.icons.CHECK, tooltip="Approuver")` et `ft.IconButton(icon=ft.icons.CLOSE, tooltip="Refuser")`.
    -   **Dialogue de déclaration (`ft.AlertDialog`) :**
        -   `ft.DatePicker` pour la date de début.
        -   `ft.DatePicker` pour la date de fin.
        -   `ft.TextField(label="Motif")`.
        -   Bouton "Envoyer".

### 4.4. Écran "Tâches" (plus simple)

-   **Objectif :** Afficher une liste de tâches assignées à l'utilisateur.
-   **Composants Flet :**
    -   `ft.Text("Mes Tâches", size=24)`
    -   `ft.ListView` pour la liste des tâches.
    -   **Pour chaque tâche :**
        -   `ft.Checkbox(label="Description de la tâche")`

### 4.5. Écran "Notifications"

-   **Objectif :** Afficher les notifications non lues.
-   **Composants Flet :**
    -   `ft.ListView`
    -   **Pour chaque notification :**
        -   `ft.ListTile(title=ft.Text("Titre de la notif"), subtitle=ft.Text("Détail..."), leading=ft.Icon(ft.icons.INFO))`
        -   Un bouton "Marquer comme lu" peut être ajouté.

### 4.6. Écran "Administration"

-   **Objectif :** Gérer les utilisateurs et les paramètres globaux.
-   **Composants Flet :**
    -   `ft.Tabs` pour séparer les sections.
        -   `ft.Tab(text="Utilisateurs")`
            -   `ft.DataTable` listant les utilisateurs (`Nom`, `Email`, `Rôle`, `Actions`).
            -   Bouton `ft.FilledButton("Créer un utilisateur")`.
        -   `ft.Tab(text="Paramètres")`
            -   Contrôles pour les paramètres de l'application (ex: `ft.Switch(label="Activer les notifications par email")`).

---

## 5. Maquettes d'Interface (ASCII Art)

Ces maquettes conceptuelles illustrent la disposition attendue des composants Flet pour les écrans principaux.

### 5.1. Vue Principale (Layout Général)

```
+------------------------------------------------------------------------------+
| [Nexus] - Planning                                        [Profil Icon]    |
+------------------------------------------------------------------------------+
| NAV      |                                                                 |
|----------|                                                                 |
| [Icon]   |                                                                 |
| Planning |                                                                 |
|          |                                                                 |
| [Icon]   |                                                                 |
| Équipes  |                 <-- CONTENU DE L'ÉCRAN ACTIF -->                  |
|          |                                                                 |
| [Icon]   |                                                                 |
| Absences |                                                                 |
|          |                                                                 |
| ...      |                                                                 |
|          |                                                                 |
+------------------------------------------------------------------------------+
```

### 5.2. Écran de Connexion

```
+------------------------------------------------------+
|                                                      |
|                       Nexus                          |
|                                                      |
|      +-----------------------------------------+     |
|      | Nom d'utilisateur                       |     |
|      +-----------------------------------------+     |
|                                                      |
|      +-----------------------------------------+     |
|      | Mot de passe                            |     |
|      +-----------------------------------------+     |
|                                                      |
|                  +-----------------+                 |
|                  |  Se connecter   |                 |
|                  +-----------------+                 |
|                                                      |
+------------------------------------------------------+
```

### 5.3. Écran Planning (Vue Semaine - DataTable)

```
+------------------------------------------------------------------------------+
| [Dropdown: Équipe Alpha] [Dropdown: Vue Semaine] [DatePicker]                |
+------------------------------------------------------------------------------+
| Employé      | Lundi 15      | Mardi 16      | Mercredi 17   | ...          |
|--------------|---------------|---------------|---------------|--------------|
| Alice        | [Travail]     | [Travail]     | [ABSENCE]     | ...          |
|--------------|---------------|---------------|---------------|--------------|
| Bob          | [Télétravail] | [Travail]     | [Travail]     | ...          |
|--------------|---------------|---------------|---------------|--------------|
| Charlie      | [Travail]     | [ABSENCE]     | [ABSENCE]     | ...          |
+------------------------------------------------------------------------------+
```

### 5.4. Écran Équipes

```
+------------------------------------------------------------------------------+
|                                                 [+ Créer une équipe]         |
+------------------------------------------------------------------------------+
|                                                                              |
|  +------------------------------------------------------------------------+  |
|  | Équipe Alpha                                                           |  |
|  |------------------------------------------------------------------------|  |
|  | Nom         | Rôle      | Actions                                      |  |
|  |-------------|-----------|----------------------------------------------|  |
|  | Alice       | Dev       | [Icon: Supprimer]                            |  |
|  | Bob         | QA        | [Icon: Supprimer]                            |  |
|  |             |           |                                              |  |
|  | [+ Ajouter Membre] [Renommer] [Supprimer Équipe]                       |  |
|  +------------------------------------------------------------------------+  |
|                                                                              |
|  +------------------------------------------------------------------------+  |
|  | Équipe Beta                                                            |  |
|  | ...                                                                    |  |
|  +------------------------------------------------------------------------+  |
+------------------------------------------------------------------------------+
```

### 5.5. Écran Absences

```
+------------------------------------------------------------------------------+
|                                                 [+ Déclarer une absence]     |
+------------------------------------------------------------------------------+
| Employé | Début      | Fin        | Motif       | Statut        | Actions    |
|---------|------------|------------|-------------|---------------|------------|
| Charlie | 16/07/2025 | 17/07/2025 | Maladie     | [Approuvée]   |            |
|---------|------------|------------|-------------|---------------|------------|
| Alice   | 17/07/2025 | 17/07/2025 | Perso       | [En attente]  | [V] [X]    |
|---------|------------|------------|-------------|---------------|------------|
| Bob     | 21/07/2025 | 25/07/2025 | Vacances    | [Refusée]     |            |
+------------------------------------------------------------------------------+
```

---

## 6. Modèle de Données Simplifié (Classes Python)

Pour simuler le backend, l'IA devra utiliser des classes de données simples. L'utilisation de `@dataclass` est recommandée.

```python
from dataclasses import dataclass, field
from datetime import date
from typing import List, Literal

@dataclass
class User:
    id: int
    username: str
    role: Literal['employe', 'manager', 'admin']
    team_id: int = None

@dataclass
class Team:
    id: int
    name: str
    members: List[User] = field(default_factory=list)

@dataclass
class Absence:
    id: int
    user_id: int
    start_date: date
    end_date: date
    reason: str
    status: Literal['en_attente', 'approuvee', 'refusee']

# etc. pour les Tâches, Planning...
```

---

## 6. Logique Applicative (Backend Local)

L'IA devra créer une classe ou un module `api_service.py` qui simulera les appels à la base de données. Ce service contiendra des données en mémoire et des fonctions pour les manipuler.

**Exemples de fonctions :**
-   `get_user(username, password) -> User | None`
-   `get_teams() -> List[Team]`
-   `create_team(name: str) -> Team`
-   `get_absences() -> List[Absence]`
-   `approve_absence(absence_id: int)`
-   `get_planning_for_week(team_id: int, week_start_date: date) -> dict`

---

## 7. Plan de Développement Suggéré

L'IA devrait suivre ces étapes pour un développement incrémental :

1.  **Étape 1 : Squelette de l'Application**
    -   Mettre en place la structure principale avec `ft.NavigationRail` et la zone de contenu.
    -   Créer des vues vides pour chaque module.

2.  **Étape 2 : Authentification**
    -   Créer l'écran de connexion.
    -   Implémenter la logique de base pour passer de l'écran de connexion à l'application principale.

3.  **Étape 3 : Module "Équipes"**
    -   Implémenter le modèle de données `User` et `Team`.
    -   Créer le service pour gérer les équipes.
    -   Construire l'UI pour afficher, créer, et gérer les équipes et leurs membres. C'est un bon module pour commencer car il est central.

4.  **Étape 4 : Module "Absences"**
    -   Implémenter le modèle `Absence` et le service associé.
    -   Construire l'UI pour lister les absences et les gérer (création/validation).

5.  **Étape 5 : Module "Planning"**
    -   C'est le plus complexe. Le développer après les autres modules qui l'alimentent en données (équipes, absences).
    -   Commencer avec une vue `DataTable` simple (vue semaine) avant de tenter une grille plus complexe (vue mois).

6.  **Étape 6 : Modules restants**
    -   Implémenter les écrans plus simples : Tâches, Notifications, Administration.

7.  **Étape 7 : Finitions**
    -   Ajouter du feedback utilisateur (SnackBars, indicateurs de chargement).
    -   Peaufiner le style et la disposition.
    -   Assurer la persistance des données (ex: sauvegarde/chargement depuis un fichier JSON au démarrage/fermeture).
