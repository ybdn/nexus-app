from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton
from PyQt6.QtCore import pyqtSignal
import qtawesome as qta

class SideNavigation(QWidget):
    """Panneau de navigation latéral fixe de style GitHub."""
    view_changed = pyqtSignal(str)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("SideNav")
        self.setFixedWidth(220)

        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(0, 10, 0, 0)
        self.layout.setSpacing(0)

        self.buttons = {
            "dashboard": QPushButton(qta.icon('fa5s.home', color='#c9d1d9'), " Tableau de Bord"),
            "personnel": QPushButton(qta.icon('fa5s.users', color='#c9d1d9'), " Personnel"),
            "planning": QPushButton(qta.icon('fa5s.calendar-alt', color='#c9d1d9'), " Planning"),
            "taches": QPushButton(qta.icon('fa5s.tasks', color='#c9d1d9'), " Tâches"),
        }

        for name, button in self.buttons.items():
            button.setCheckable(True)
            button.clicked.connect(lambda checked, n=name: self.view_changed.emit(n))
            self.layout.addWidget(button)

        self.layout.addStretch()