"""
Module de gestion des préférences utilisateur.
"""
import json
import os

PREFERENCES_FILE = "user_preferences.json"

def get_default_preferences():
    """Retourne les préférences par défaut."""
    return {
        "sidebar_collapsed": False,
        "theme_mode": "light"
    }

def load_preferences():
    """Charge les préférences utilisateur depuis le fichier."""
    if os.path.exists(PREFERENCES_FILE):
        try:
            with open(PREFERENCES_FILE, 'r', encoding='utf-8') as f:
                preferences = json.load(f)
                # Fusionner avec les préférences par défaut pour gérer les nouvelles options
                default_prefs = get_default_preferences()
                default_prefs.update(preferences)
                return default_prefs
        except (json.JSONDecodeError, IOError):
            # En cas d'erreur, retourner les préférences par défaut
            return get_default_preferences()
    return get_default_preferences()

def save_preferences(preferences):
    """Sauvegarde les préférences utilisateur dans le fichier."""
    try:
        with open(PREFERENCES_FILE, 'w', encoding='utf-8') as f:
            json.dump(preferences, f, indent=2, ensure_ascii=False)
    except IOError:
        # En cas d'erreur de sauvegarde, ne pas interrompre l'application
        print("Avertissement : Impossible de sauvegarder les préférences utilisateur.")

def update_preference(key, value):
    """Met à jour une préférence spécifique."""
    preferences = load_preferences()
    preferences[key] = value
    save_preferences(preferences)
    return preferences
