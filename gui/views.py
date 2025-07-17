
from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QTableView, QPushButton, QHBoxLayout, QGridLayout, QFrame, QStyledItemDelegate
from PyQt6.QtCore import QAbstractTableModel, Qt
from PyQt6.QtGui import QColor, QPixmap
import qtawesome as qta
from core.services import get_all_users, get_tasks_for_user, get_absences
from PyQt6.QtWidgets import QGraphicsDropShadowEffect
import datetime

class ContentBox(QFrame):
    """Widget de base pour le contenu, style boîte moderne surélevée."""
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("ContentBox")
        self.setGraphicsEffect(None)  # Pour ombre si besoin plus tard

class StatusBoardModel(QAbstractTableModel):
    def __init__(self, data):
        super().__init__()
        self._data = data
        self._headers = ["Logo", "Company", "Position", "Duration", "Job ID", "Status"]

    def data(self, index, role):
        row = self._data[index.row()]
        col = index.column()
        if role == Qt.ItemDataRole.DisplayRole:
            if col == 0:
                return None  # Le logo sera géré par DecorationRole
            return row[self._headers[col]]
        if role == Qt.ItemDataRole.DecorationRole and col == 0:
            pix = QPixmap(row['Logo'])
            if not pix.isNull():
                return pix.scaled(32, 32)
        return None

    def rowCount(self, index):
        return len(self._data)

    def columnCount(self, index):
        return len(self._headers)

    def headerData(self, section, orientation, role):
        if role == Qt.ItemDataRole.DisplayRole and orientation == Qt.Orientation.Horizontal:
            return self._headers[section]

class DashboardView(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QHBoxLayout(self)
        self.layout.setContentsMargins(20, 20, 20, 20)
        self.layout.setSpacing(24)

        # Zone centrale (accueil + cards stats + tableau)
        central_widget = QWidget()
        central_layout = QVBoxLayout(central_widget)
        central_layout.setContentsMargins(0, 0, 0, 0)
        central_layout.setSpacing(24)

        # Message d'accueil et date
        welcome_box = QWidget()
        welcome_layout = QVBoxLayout(welcome_box)
        welcome_layout.setContentsMargins(0, 0, 0, 0)
        welcome_layout.setSpacing(2)
        welcome_label = QLabel("Welcome John!")
        welcome_label.setStyleSheet("font-size:2.2rem;font-weight:700;color:#222b45;")
        date_label = QLabel(datetime.date.today().strftime("%B %d, %Y"))
        date_label.setStyleSheet("font-size:1.1rem;color:#8a94a6;font-weight:500;margin-bottom:8px;")
        welcome_layout.addWidget(welcome_label)
        welcome_layout.addWidget(date_label)
        central_layout.addWidget(welcome_box)

        # Cards statistiques en ligne
        stats_layout = QHBoxLayout()
        stats_layout.setSpacing(24)
        stats_layout.setContentsMargins(0, 0, 0, 0)
        stats_layout.addWidget(self.create_card("Employés", str(len(get_all_users())), qta.icon('fa5s.users', color='#2563eb')))
        stats_layout.addWidget(self.create_card("Tâches en cours", "5", qta.icon('fa5s.tasks', color='#2563eb')))
        stats_layout.addWidget(self.create_card("Absences prévues", str(len(get_absences())), qta.icon('fa5s.calendar-alt', color='#2563eb')))
        stats_layout.addStretch()
        central_layout.addLayout(stats_layout)

        # Tableau Status Board
        status_data = [
            {"Logo": "assets/logos/apple.png", "Company": "Apple", "Position": "Visual Designer", "Duration": "Full time", "Job ID": "123456789", "Status": "Phone Interview"},
            {"Logo": "assets/logos/booster.png", "Company": "Booster", "Position": "Product Designer", "Duration": "Full time", "Job ID": "123456788", "Status": "Applied"},
            {"Logo": "assets/logos/google.png", "Company": "Google", "Position": "Interactive Designer", "Duration": "Full time", "Job ID": "123456787", "Status": "Zoom Call"},
            {"Logo": "assets/logos/instagram.png", "Company": "Instagram", "Position": "Product Designer", "Duration": "12-months", "Job ID": "123456786", "Status": "Round 2 Interview"},
            {"Logo": "assets/logos/omada.png", "Company": "Omada Health", "Position": "UX/ UI Designer", "Duration": "Full time", "Job ID": "123456785", "Status": "Phone Interview"},
        ]
        self.status_model = StatusBoardModel(status_data)
        self.status_table = QTableView()
        self.status_table.setModel(self.status_model)
        self.status_table.setAlternatingRowColors(True)
        self.status_table.setSelectionBehavior(QTableView.SelectionBehavior.SelectRows)
        self.status_table.setEditTriggers(QTableView.EditTrigger.NoEditTriggers)
        self.status_table.verticalHeader().setVisible(False)
        self.status_table.setStyleSheet("background:#fff;border-radius:12px;")
        self.status_table.setMinimumHeight(280)
        self.status_table.setMaximumHeight(340)
        self.status_table.setColumnWidth(0, 44)
        central_layout.addWidget(self.status_table)

        self.layout.addWidget(central_widget, stretch=3)

        # Panneau latéral droit
        right_panel = QWidget()
        right_layout = QVBoxLayout(right_panel)
        right_layout.setContentsMargins(0, 0, 0, 0)
        right_layout.setSpacing(24)

        # Card Interviews
        interview_card = QWidget()
        interview_card.setObjectName("RightCard")
        interview_layout = QVBoxLayout(interview_card)
        interview_layout.setContentsMargins(18, 18, 18, 18)
        interview_title = QLabel("Interviews")
        interview_title.setStyleSheet("font-weight:600;font-size:1.1rem;color:#222b45;")
        interview_layout.addWidget(interview_title)
        interview_content = QLabel("Figma | Product Designer\nMay 4, 2020 @12:30 pm - 1:00 pm\nInterview | Chad Lee")
        interview_content.setStyleSheet("color:#2563eb;font-size:1rem;margin-top:8px;")
        interview_layout.addWidget(interview_content)
        right_layout.addWidget(interview_card)

        # Card Roles
        roles_card = QWidget()
        roles_card.setObjectName("RightCard")
        roles_layout = QVBoxLayout(roles_card)
        roles_layout.setContentsMargins(18, 18, 18, 18)
        roles_title = QLabel("Roles")
        roles_title.setStyleSheet("font-weight:600;font-size:1.1rem;color:#222b45;")
        roles_layout.addWidget(roles_title)
        for label, value in [("Visual Designer",6),("Product Designer",4),("Interactive Designer",6),("UX/UI Designer",2)]:
            role_box = QLabel(f"{value}  {label}")
            role_box.setStyleSheet("background:#2563eb;color:#fff;border-radius:10px;padding:8px 16px;margin-top:8px;font-size:1rem;")
            roles_layout.addWidget(role_box)
        right_layout.addWidget(roles_card)
        right_layout.addStretch()

        self.layout.addWidget(right_panel, stretch=1)

    def create_card(self, title, value, icon):
        card = QFrame()
        card.setObjectName("DashboardCard")
        card_layout = QVBoxLayout(card)
        card_layout.setContentsMargins(18, 18, 18, 18)
        card_layout.setSpacing(8)

        # Ajout de l'ombre portée
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(24)
        shadow.setColor(QColor(59, 130, 246, 40))  # Bleu, faible opacité
        shadow.setOffset(0, 6)
        card.setGraphicsEffect(shadow)

        icon_label = QLabel()
        icon_label.setPixmap(icon.pixmap(32, 32))
        icon_label.setObjectName("CardIcon")
        card_layout.addWidget(icon_label, alignment=Qt.AlignmentFlag.AlignLeft)

        title_label = QLabel(title)
        title_label.setObjectName("CardTitle")
        card_layout.addWidget(title_label, alignment=Qt.AlignmentFlag.AlignLeft)

        value_label = QLabel(value)
        value_label.setObjectName("CardValue")
        card_layout.addWidget(value_label, alignment=Qt.AlignmentFlag.AlignLeft)

        return card

class PersonnelTableModel(QAbstractTableModel):
    def __init__(self, data):
        super().__init__()
        self._data = data
        self._headers = ["ID", "Nom d'utilisateur", "Rôle", "Équipe ID", "Statut"]

    def data(self, index, role):
        if role == Qt.ItemDataRole.DisplayRole:
            user = self._data[index.row()]
            values = [
                user.id,
                user.username,
                user.role,
                user.team_id,
            ]
            # Statut fictif
            if user.role in ("admin", "manager"):
                statut = "Actif"
            else:
                statut = "Absent"
            values.append(statut)
            return values[index.column()]

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

        # Affichage des badges de statut dans la colonne Statut
        class StatusBadgeDelegate(QStyledItemDelegate):
            def createEditor(self, parent, option, index):
                return None  # Pas d'édition
            def paint(self, painter, option, index):
                if index.column() == 4:
                    value = index.data()
                    label = QLabel(value)
                    label.setProperty('class', 'StatusBadge')
                    label.setProperty('statut', value)
                    label.setStyleSheet('')  # Force l'application du style
                    label.resize(option.rect.size())
                    painter.save()
                    painter.translate(option.rect.topLeft())
                    label.render(painter)
                    painter.restore()
                else:
                    super().paint(painter, option, index)
        self.table_view.setItemDelegate(StatusBadgeDelegate(self.table_view))

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
