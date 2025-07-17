
from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QTableView, QPushButton, QHBoxLayout, QGridLayout, QFrame
from PyQt6.QtCore import QAbstractTableModel, Qt
from core.services import get_all_users, get_tasks_for_user, get_absences

class ContentBox(QFrame):
    """Widget de base pour le contenu, style boîte GitHub."""
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("ContentBox")

class DashboardView(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(20, 20, 20, 20)

        content_box = ContentBox()
        self.layout.addWidget(content_box)

        box_layout = QVBoxLayout(content_box)
        title = QLabel("Tableau de Bord")
        title.setObjectName("ViewTitle")
        box_layout.addWidget(title)

        self.grid_layout = QGridLayout()
        box_layout.addLayout(self.grid_layout)

        self.grid_layout.addWidget(self.create_card("Employés", str(len(get_all_users()))), 0, 0)
        self.grid_layout.addWidget(self.create_card("Tâches en cours", "5"), 0, 1)
        self.grid_layout.addWidget(self.create_card("Absences prévues", str(len(get_absences()))), 0, 2)

    def create_card(self, title, value):
        card = QFrame()
        card.setObjectName("DashboardCard")
        card_layout = QVBoxLayout(card)

        title_label = QLabel(title)
        title_label.setObjectName("CardTitle")
        card_layout.addWidget(title_label)

        value_label = QLabel(value)
        value_label.setObjectName("CardValue")
        card_layout.addWidget(value_label)

        return card

class PersonnelTableModel(QAbstractTableModel):
    def __init__(self, data):
        super().__init__()
        self._data = data
        self._headers = ["ID", "Nom d'utilisateur", "Rôle", "Équipe ID"]

    def data(self, index, role):
        if role == Qt.ItemDataRole.DisplayRole:
            user = self._data[index.row()]
            return [
                user.id,
                user.username,
                user.role,
                user.team_id
            ][index.column()]

    def rowCount(self, index):
        return len(self._data)

    def columnCount(self, index):
        return len(self._headers)

    def headerData(self, section, orientation, role):
        if role == Qt.ItemDataRole.DisplayRole and orientation == Qt.Orientation.Horizontal:
            return self._headers[section]

class PersonnelView(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(20, 20, 20, 20)

        content_box = ContentBox()
        self.layout.addWidget(content_box)

        box_layout = QVBoxLayout(content_box)

        header_layout = QHBoxLayout()
        title = QLabel("Gestion du Personnel")
        title.setObjectName("ViewTitle")
        header_layout.addWidget(title)
        header_layout.addStretch()
        self.add_button = QPushButton("Ajouter un membre")
        self.add_button.setObjectName("PrimaryButton")
        header_layout.addWidget(self.add_button)
        box_layout.addLayout(header_layout)

        self.table_view = QTableView()
        box_layout.addWidget(self.table_view)

        self.users = get_all_users()
        self.model = PersonnelTableModel(self.users)
        self.table_view.setModel(self.model)

class PlanningView(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(20, 20, 20, 20)
        content_box = ContentBox()
        self.layout.addWidget(content_box)
        box_layout = QVBoxLayout(content_box)
        title = QLabel("Planning")
        title.setObjectName("ViewTitle")
        box_layout.addWidget(title)

class TachesView(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(20, 20, 20, 20)
        content_box = ContentBox()
        self.layout.addWidget(content_box)
        box_layout = QVBoxLayout(content_box)
        title = QLabel("Tâches")
        title.setObjectName("ViewTitle")
        box_layout.addWidget(title)
