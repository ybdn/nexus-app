
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QLabel, QStackedWidget, QPushButton, QSpacerItem, QSizePolicy
from gui.widgets import SideNavigation
from gui.views import DashboardView, PersonnelView, PlanningView, TachesView

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setObjectName("MainWindow")
        self.setWindowTitle("Nexus")
        self.setGeometry(100, 100, 1280, 800)

        # Widget Central
        self.central_widget = QWidget()
        self.central_widget.setObjectName("CentralWidget")
        self.setCentralWidget(self.central_widget)
        self.main_layout = QVBoxLayout(self.central_widget)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)

        # En-tête
        self.header = QWidget()
        self.header.setObjectName("Header")
        self.header_layout = QHBoxLayout(self.header)
        self.header_layout.setContentsMargins(24, 0, 24, 0)
        self.header_layout.setSpacing(0)
        self.title_label = QLabel("Tableau de Bord")
        self.title_label.setObjectName("HeaderTitle")
        self.header_layout.addWidget(self.title_label)
        self.header_layout.addStretch()
        # Placeholder pour actions rapides (notifications, etc.)
        self.action_btn = QPushButton("🔔")
        self.action_btn.setObjectName("HeaderAction")
        self.action_btn.setFixedSize(36, 36)
        self.header_layout.addWidget(self.action_btn)
        self.main_layout.addWidget(self.header)

        # Zone de contenu principale
        self.content_layout = QHBoxLayout()
        self.main_layout.addLayout(self.content_layout)

        # Navigation latérale
        self.side_nav = SideNavigation()
        self.content_layout.addWidget(self.side_nav)

        # Vues
        self.stacked_widget = QStackedWidget()
        self.content_layout.addWidget(self.stacked_widget)

        self.views = {
            "dashboard": DashboardView(),
            "personnel": PersonnelView(),
            "planning": PlanningView(),
            "taches": TachesView(),
        }

        for view in self.views.values():
            self.stacked_widget.addWidget(view)

        # Connexions
        self.side_nav.view_changed.connect(self.change_view)
        self.side_nav.profile_clicked.connect(self.open_profile_menu)

        # Vue initiale
        self.side_nav.buttons["dashboard"].setChecked(True)
        self.change_view("dashboard")

    def change_view(self, name):
        self.stacked_widget.setCurrentWidget(self.views[name])
        # Met à jour le titre de l'en-tête dynamiquement
        titres = {
            "dashboard": "Tableau de Bord",
            "personnel": "Gestion du Personnel",
            "planning": "Planning",
            "taches": "Tâches",
        }
        self.title_label.setText(titres.get(name, "Nexus"))

    def open_profile_menu(self):
        # Placeholder pour menu profil/préférences
        print("Menu profil/préférences ouvert (à implémenter)")

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
