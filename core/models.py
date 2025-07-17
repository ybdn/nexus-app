from dataclasses import dataclass, field
from datetime import date
from typing import List, Literal, Optional

@dataclass
class User:
    """Représente un utilisateur de l'application."""
    id: int
    username: str
    role: Literal['employe', 'manager', 'admin']
    team_id: Optional[int] = None

@dataclass
class Team:
    """Représente une équipe avec ses membres."""
    id: int
    name: str
    members: List[User] = field(default_factory=list)

@dataclass
class Absence:
    """Représente une demande d'absence."""
    id: int
    user_id: int
    start_date: date
    end_date: date
    reason: str
    status: Literal['en_attente', 'approuvee', 'refusee']

@dataclass
class Task:
    """Représente une tâche assignée à un utilisateur."""
    id: int
    user_id: int
    description: str
    completed: bool = False
