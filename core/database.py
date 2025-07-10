import sqlite3
import os

# Le fichier de la base de données sera créé dans le même dossier que ce script.
# Pour le partage, ce fichier devra être déplacé dans un dossier réseau.
DATABASE_FILE = "nexus.db"

def initialize_database():
    """
    Initialise la base de données et crée les tables si elles n'existent pas.
    """
    try:
        conn = sqlite3.connect(DATABASE_FILE)
        cursor = conn.cursor()

        # Création de la table 'roles'
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS roles (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE
        )
        """)

        # Création de la table 'users'
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            role_id INTEGER,
            FOREIGN KEY (role_id) REFERENCES roles (id)
        )
        """)

        # Création de la table 'schedules'
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS schedules (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL,
            user_id INTEGER,
            details TEXT,
            FOREIGN KEY (user_id) REFERENCES users (id)
        )
        """)

        # Création de la table 'tasks'
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            assigned_to INTEGER,
            status TEXT DEFAULT 'pending',
            FOREIGN KEY (assigned_to) REFERENCES users (id)
        )
        """)

        conn.commit()
        print(f"Base de données '{DATABASE_FILE}' initialisée avec succès.")

    except sqlite3.Error as e:
        print(f"Erreur lors de l'initialisation de la base de données : {e}")
    finally:
        if conn:
            conn.close()

if __name__ == '__main__':
    # Ce bloc permet de tester l'initialisation directement depuis ce fichier.
    initialize_database()
    print(f"Le fichier '{DATABASE_FILE}' a été créé/vérifié dans le répertoire : {os.path.abspath(os.getcwd())}")
