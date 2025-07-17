from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel, QHBoxLayout, QSpacerItem, QSizePolicy
from PyQt6.QtCore import pyqtSignal, Qt, QSize
import qtawesome as qta

class SideNavigation(QWidget):
    """Panneau de navigation latéral moderne avec avatar/logo et bouton profil."""
    view_changed = pyqtSignal(str)
    profile_clicked = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("SideNav")
        self.setFixedWidth(240)

        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(0, 24, 0, 12)
        self.layout.setSpacing(0)

        # Avatar/logo en haut
        self.logo_container = QHBoxLayout()
        self.logo_container.setContentsMargins(0, 0, 0, 24)
        self.logo_container.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.avatar = QLabel("N")
        self.avatar.setObjectName("NavAvatar")
        self.avatar.setFixedSize(56, 56)
        self.avatar.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.logo_container.addWidget(self.avatar)
        self.layout.addLayout(self.logo_container)

        # Boutons de navigation
        self.buttons = {
            "dashboard": QPushButton(qta.icon('fa5s.home', color='#c9d1d9'), "  Tableau de Bord"),
            "personnel": QPushButton(qta.icon('fa5s.users', color='#c9d1d9'), "  Personnel"),
            "planning": QPushButton(qta.icon('fa5s.calendar-alt', color='#c9d1d9'), "  Planning"),
            "taches": QPushButton(qta.icon('fa5s.tasks', color='#c9d1d9'), "  Tâches"),
        }
        for name, button in self.buttons.items():
            button.setCheckable(True)
            button.setCursor(Qt.CursorShape.PointingHandCursor)
            button.setMinimumHeight(44)
            button.setIconSize(QSize(22, 22))
            button.clicked.connect(lambda checked, n=name: self.view_changed.emit(n))
            self.layout.addWidget(button)

        self.layout.addStretch()

        # Bouton profil/préférences en bas
        self.profile_btn = QPushButton(qta.icon('fa5s.user-cog', color='#c9d1d9'), "  Profil / Préférences")
        self.profile_btn.setObjectName("ProfileButton")
        self.profile_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        self.profile_btn.setMinimumHeight(40)
        self.profile_btn.setIconSize(QSize(20, 20))
        self.profile_btn.clicked.connect(self.profile_clicked.emit)
        self.layout.addWidget(self.profile_btn)