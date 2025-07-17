# Spécification Technique du Backend pour Nexus (Version Python Locale)

**Document à destination d'un agent IA développeur.**

**Objectif :** Définir l'architecture, les modèles de données, la logique métier et la couche de persistance pour le backend d'une application de bureau locale Nexus. Ce backend sera écrit en Python standard, sans dépendance à un framework web lourd comme Django.

---

## 1. Introduction et Concept Général

Ce document détaille la "partie cachée" de l'application Flet. Il sert de plan pour créer une couche de services et de gestion de données purement en Python. Le backend fonctionnera localement, interagissant avec une base de données SQLite pour assurer la persistance des données entre les sessions.

Il doit fournir toutes les fonctions nécessaires pour que l'interface utilisateur (définie dans `NEXUS_FLET_UI_SPECIFICATION.md`) puisse afficher des informations et exécuter des actions.

**Principes Clés :**

-   **Simplicité :** Utiliser des bibliothèques Python natives ou standards (`sqlite3`, `dataclasses`, `hashlib`).
-   **Modularité :** Séparer clairement la logique métier (services) de l'accès aux données (DAL).
-   **Performance :** Optimiser les requêtes pour une application de bureau réactive.
-   **Sécurité :** Assurer le hachage systématique des mots de passe.

---

## 2. Architecture du Backend

Le backend sera structuré en trois couches distinctes, contenues dans des modules Python dédiés.

```
+------------------------------------------------------+
|           Interface Utilisateur (Flet UI)            |
+------------------------------------------------------+
                        |
                        | (Appels de fonctions Python)
                        V
+------------------------------------------------------+
|         Couche de Services (services.py)             |
| (Logique métier : validation, calculs, etc.)         |
+------------------------------------------------------+
                        |
                        | (Appels de fonctions de bas niveau)
                        V
+------------------------------------------------------+
|      Couche d'Accès aux Données (database.py)        |
| (Exécute les requêtes SQL brutes)                    |
+------------------------------------------------------+
                        |
                        | (Transactions SQL)
                        V
+------------------------------------------------------+
|        Base de Données (nexus_local.db - SQLite)     |
+------------------------------------------------------+
```

1.  **Couche de Persistance :**
    -   **Technologie :** SQLite.
    -   **Fichier :** `nexus_local.db`. Ce fichier unique contiendra toutes les données de l'application. Il doit être créé au premier lancement si absent.

2.  **Couche d'Accès aux Données (DAL - `database.py`) :**
    -   Ce module est le seul à pouvoir communiquer directement avec la base de données.
    -   Il contiendra des fonctions pour chaque opération CRUD (Create, Read, Update, Delete) nécessaire.
    -   **Responsabilité :** Exécuter des requêtes SQL paramétrées pour éviter les injections SQL. Il ne contient aucune logique métier.

3.  **Couche de Services (`services.py`) :**
    -   C'est le "cerveau" de l'application. L'interface Flet n'appellera que des fonctions de ce module.
    -   **Responsabilité :** Implémenter la logique métier (ex: "un manager peut approuver une absence", "calculer les jours d'une absence", "hacher un mot de passe avant de créer un utilisateur").
    -   Elle orchestre les appels à la couche d'accès aux données.

---

## 3. Modèles de Données Détaillés (Schéma SQL)

Voici les instructions `CREATE TABLE` pour la base de données SQLite. Elles définissent la structure fondamentale de l'application.

```sql
-- Fichier : init.sql (à exécuter par la fonction d'initialisation)

-- Table pour les utilisateurs
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password_hash TEXT NOT NULL,
    role TEXT NOT NULL CHECK(role IN ('employe', 'manager', 'admin')),
    team_id INTEGER,
    FOREIGN KEY (team_id) REFERENCES teams(id) ON DELETE SET NULL
);

-- Table pour les équipes
CREATE TABLE IF NOT EXISTS teams (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE NOT NULL
);

-- Table pour les absences
CREATE TABLE IF NOT EXISTS absences (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    start_date TEXT NOT NULL, -- Format 'YYYY-MM-DD'
    end_date TEXT NOT NULL,   -- Format 'YYYY-MM-DD'
    reason TEXT,
    status TEXT NOT NULL CHECK(status IN ('en_attente', 'approuvee', 'refusee')),
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

-- Table pour les tâches (simplifié)
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    completed INTEGER NOT NULL DEFAULT 0, -- 0 pour false, 1 pour true
    user_id INTEGER NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

-- Table pour les notifications
CREATE TABLE IF NOT EXISTS notifications (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    message TEXT NOT NULL,
    is_read INTEGER NOT NULL DEFAULT 0, -- 0 pour false, 1 pour true
    created_at TEXT NOT NULL, -- Format 'YYYY-MM-DD HH:MM:SS'
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

-- Table pour les événements du planning (plus flexible que des tâches)
CREATE TABLE IF NOT EXISTS planning_events (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    event_date TEXT NOT NULL, -- Format 'YYYY-MM-DD'
    event_type TEXT NOT NULL CHECK(event_type IN ('travail', 'teletravail', 'reunion', 'autre')),
    title TEXT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

```

---

## 4. Spécification des Services (Logique Métier)

Le module `services.py` exposera les fonctions suivantes à l'UI. Les `dataclasses` seront utilisées pour structurer les retours de données complexes.

### 4.1. Service d'Authentification et Utilisateurs

-   `authenticate_user(username: str, password: str) -> User | None:`
    -   Récupère le `password_hash` de l'utilisateur.
    -   Hache le `password` fourni et le compare au hash stocké.
    -   Retourne l'objet `User` si la correspondance est bonne, sinon `None`.

-   `create_user(username: str, password: str, role: str, team_id: int = None) -> User:`
    -   Hache le mot de passe avec `hashlib.sha256`.
    -   Appelle la DAL pour insérer le nouvel utilisateur.
    -   Retourne l'objet `User` créé.

-   `get_user_by_id(user_id: int) -> User:`
    -   Récupère un utilisateur par son ID.

-   `get_all_users() -> List[User]:`
    -   Récupère tous les utilisateurs.

-   `update_user_role(user_id: int, new_role: str):`
    -   Met à jour le rôle d'un utilisateur.

-   `assign_user_to_team(user_id: int, team_id: int):`
    -   Assigne ou change l'équipe d'un utilisateur.

### 4.2. Service des Équipes

-   `create_team(name: str) -> Team:`
    -   Crée une nouvelle équipe.

-   `get_team_by_id(team_id: int) -> Team:`
    -   Récupère une équipe et la liste de ses membres (`User` objects).

-   `get_all_teams() -> List[Team]:`
    -   Récupère toutes les équipes avec leurs membres.

-   `rename_team(team_id: int, new_name: str):`
    -   Renomme une équipe.

-   `delete_team(team_id: int):`
    -   Supprime une équipe. Les `user.team_id` des membres seront mis à `NULL` grâce au `ON DELETE SET NULL`.

-   `get_team_members(team_id: int) -> List[User]:`
    -   Retourne la liste des utilisateurs d'une équipe.

### 4.3. Service des Absences

-   `create_absence(user_id: int, start_date: date, end_date: date, reason: str) -> Absence:`
    -   Crée une demande d'absence avec le statut "en_attente".
    -   Génère une notification pour le manager de l'équipe.

-   `get_absences_for_user(user_id: int) -> List[Absence]:`
    -   Récupère toutes les absences d'un utilisateur.

-   `get_pending_absences_for_manager(manager_id: int) -> List[Absence]:`
    -   Récupère toutes les absences "en_attente" des employés des équipes gérées par le manager. (Logique complexe ici).

-   `get_all_absences() -> List[Absence]:`
    -   Fonction pour les admins, récupère toutes les absences.

-   `update_absence_status(absence_id: int, status: Literal['approuvee', 'refusee'], manager_id: int):`
    -   Vérifie que `manager_id` a le droit de valider.
    -   Met à jour le statut de l'absence.
    -   Génère une notification pour l'employé concerné.

### 4.4. Service du Planning

-   `get_planning_for_week(team_id: int, start_of_week: date) -> Dict[int, Dict[date, List[Union[Absence, PlanningEvent]]]]:`
    -   C'est la fonction la plus complexe.
    -   Pour une semaine donnée, elle doit retourner une structure de données qui, pour chaque membre de l'équipe, liste les événements (absences, travail, etc.) de chaque jour.
    -   Exemple de retour : `{ user_id_1: { date_1: [event_1], date_2: [event_2] }, user_id_2: ... }`

-   `create_planning_event(user_id: int, event_date: date, event_type: str, title: str) -> PlanningEvent:`
    -   Permet à un manager d'ajouter un événement au planning d'un utilisateur.

### 4.5. Service des Notifications

-   `get_unread_notifications(user_id: int) -> List[Notification]:`
    -   Récupère les notifications non lues pour un utilisateur.

-   `mark_notification_as_read(notification_id: int):`
    -   Passe le flag `is_read` à 1.

-   `create_notification(user_id: int, message: str) -> Notification:`
    -   Fonction utilitaire appelée par les autres services.

---

## 5. Gestion des Données et Initialisation

Le module `database.py` doit contenir une fonction `init_db()`.

-   `init_db():`
    -   Vérifie si le fichier `nexus_local.db` existe.
    -   Sinon, se connecte (ce qui crée le fichier) et exécute le script SQL de création des tables.
    -   **Peuplement (Seeding) :** Pour le développement, cette fonction devrait aussi peupler la base avec des données de test (un admin, quelques employés, une ou deux équipes, etc.) pour que l'application soit immédiatement utilisable.

---

## 6. Plan de Développement Suggéré

1.  **Étape 1 : Base de Données et DAL**
    -   Créer le module `database.py`.
    -   Implémenter la fonction `init_db()` avec la création des tables.
    -   Ajouter une fonction de peuplement (`seed_db()`) avec des données initiales.
    -   Écrire les fonctions CRUD de base pour chaque table (ex: `_create_user`, `_get_user_by_id`).

2.  **Étape 2 : Service Utilisateurs et Authentification**
    -   Créer le module `services.py`.
    -   Implémenter la logique de hachage de mot de passe.
    -   Développer les fonctions `authenticate_user` et `create_user`.

3.  **Étape 3 : Service Équipes**
    -   Implémenter la logique de création, lecture, et gestion des équipes et de leurs membres.

4.  **Étape 4 : Service Absences**
    -   Implémenter la création et la gestion des absences.
    -   Développer la logique de notification (appel à `create_notification`).
    -   Implémenter la logique de validation par les managers.

5.  **Étape 5 : Service Planning**
    -   Développer la fonction complexe `get_planning_for_week` en agrégeant les données des absences et des événements.

6.  **Étape 6 : Finalisation**
    -   Compléter les services restants (Tâches, Notifications).
    -   Revoir et documenter chaque fonction de service avec des docstrings claires.
    -   S'assurer que toutes les interactions avec la base de données sont bien paramétrées pour la sécurité.
