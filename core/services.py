from typing import List, Optional, Literal
from datetime import date, timedelta
from core.models import User, Team, Absence, Task

# --- Données en mémoire pour la simulation ---

_users = {
    1: User(id=1, username="Alice", role="manager", team_id=1),
    2: User(id=2, username="Bob", role="employe", team_id=1),
    3: User(id=3, username="Charlie", role="employe", team_id=1),
    4: User(id=4, username="David", role="manager", team_id=2),
    5: User(id=5, username="Eve", role="employe", team_id=2),
    6: User(id=6, username="Frank", role="admin"),
}

_teams = {
    1: Team(id=1, name="Équipe Alpha"),
    2: Team(id=2, name="Équipe Beta"),
}

_absences = {
    1: Absence(id=1, user_id=3, start_date=date.today() + timedelta(days=2), end_date=date.today() + timedelta(days=3), reason="Maladie", status="approuvee"),
    2: Absence(id=2, user_id=2, start_date=date.today() + timedelta(days=10), end_date=date.today() + timedelta(days=15), reason="Vacances", status="en_attente"),
    3: Absence(id=3, user_id=5, start_date=date.today() + timedelta(days=1), end_date=date.today() + timedelta(days=1), reason="Personnel", status="refusee"),
}

_tasks = {
    1: Task(id=1, user_id=2, description="Préparer le rapport mensuel"),
    2: Task(id=2, user_id=2, description="Contacter le client X", completed=True),
    3: Task(id=3, user_id=3, description="Mettre à jour la documentation API"),
    4: Task(id=4, user_id=5, description="Tester la nouvelle fonctionnalité de paiement"),
}


# Remplir les listes de membres des équipes
for user in _users.values():
    if user.team_id and user.team_id in _teams:
        _teams[user.team_id].members.append(user)

# --- Fonctions du service ---

def get_teams() -> List[Team]:
    """Retourne toutes les équipes."""
    return list(_teams.values())

def get_team(team_id: int) -> Optional[Team]:
    """Retourne une équipe par son ID."""
    return _teams.get(team_id)

def create_team(name: str) -> Team:
    """Crée une nouvelle équipe."""
    new_id = max(_teams.keys()) + 1 if _teams else 1
    new_team = Team(id=new_id, name=name)
    _teams[new_id] = new_team
    return new_team

def get_all_users() -> List[User]:
    """Retourne tous les utilisateurs."""
    return list(_users.values())

def add_member_to_team(team_id: int, user_id: int) -> Optional[Team]:
    """Ajoute un membre à une équipe."""
    team = _teams.get(team_id)
    user = _users.get(user_id)
    if team and user:
        user.team_id = team_id
        team.members.append(user)
        return team
    return None

# --- Fonctions pour les Absences ---

def get_absences() -> List[Absence]:
    """Retourne toutes les demandes d'absence."""
    return list(_absences.values())

def create_absence(user_id: int, start_date: date, end_date: date, reason: str) -> Absence:
    """Crée une nouvelle demande d'absence."""
    new_id = max(_absences.keys()) + 1 if _absences else 1
    new_absence = Absence(
        id=new_id, 
        user_id=user_id, 
        start_date=start_date, 
        end_date=end_date, 
        reason=reason, 
        status="en_attente"
    )
    _absences[new_id] = new_absence
    return new_absence

def update_absence_status(absence_id: int, status: Literal['approuvee', 'refusee']) -> Optional[Absence]:
    """Met à jour le statut d'une absence."""
    if absence_id in _absences:
        _absences[absence_id].status = status
        return _absences[absence_id]
    return None

def get_user_by_id(user_id: int) -> Optional[User]:
    """Trouve un utilisateur par son ID."""
    return _users.get(user_id)

# --- Fonctions pour le Planning ---

def get_planning_for_week(team_id: int, start_of_week: date) -> dict:
    """
    Construit le planning pour une équipe et une semaine données.
    Retourne un dictionnaire avec les noms d'utilisateurs comme clés et une liste de statuts journaliers comme valeurs.
    """
    planning = {}
    team = _teams.get(team_id)
    if not team:
        return {}

    week_dates = [start_of_week + timedelta(days=i) for i in range(7)]
    
    user_absences = [a for a in _absences.values() if a.status == 'approuvee']

    for user in team.members:
        daily_statuses = []
        for day in week_dates:
            status = "Travail"  # Statut par défaut
            for absence in user_absences:
                if absence.user_id == user.id and absence.start_date <= day <= absence.end_date:
                    status = absence.reason
                    break  # Une seule absence par jour est gérée ici
            daily_statuses.append(status)
        planning[user.username] = daily_statuses
        
    return planning

# --- Fonctions pour les Tâches ---

def get_tasks_for_user(user_id: int) -> List[Task]:
    """Retourne toutes les tâches pour un utilisateur donné."""
    return [task for task in _tasks.values() if task.user_id == user_id]

def update_task_status(task_id: int, completed: bool) -> Optional[Task]:
    """Met à jour le statut d'une tâche."""
    if task_id in _tasks:
        _tasks[task_id].completed = completed
        return _tasks[task_id]
    return None

# --- Authentification ---

def authenticate_user(username: str, password: str) -> Optional[User]:
    """
    Authentifie un utilisateur avec son nom d'utilisateur et mot de passe.
    Pour la simulation, on accepte n'importe quel mot de passe pour les utilisateurs existants.
    """
    for user in _users.values():
        if user.username.lower() == username.lower():
            # Pour la simulation, on accepte n'importe quel mot de passe non vide
            if password:
                return user
    return None
