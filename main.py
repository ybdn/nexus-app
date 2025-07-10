from core.database import initialize_database
from gui.main_window import App

def main():
    """
    Point d'entrée principal de l'application.
    """
    # 1. S'assurer que la base de données et les tables sont prêtes
    print("Initialisation de la base de données...")
    initialize_database()

    # 2. Créer et lancer l'interface graphique
    print("Lancement de l'application...")
    app = App()
    app.mainloop()

if __name__ == "__main__":
    main()
