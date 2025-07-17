
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QLabel, QStackedWidget
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
        self.header_layout.addWidget(QLabel("Nexus"))
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

        # Vue initiale
        self.side_nav.buttons["dashboard"].setChecked(True)
        self.change_view("dashboard")

    def change_view(self, name):
        self.stacked_widget.setCurrentWidget(self.views[name])

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
