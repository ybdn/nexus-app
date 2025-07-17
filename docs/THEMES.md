# Système de Thèmes - Nexus

## Fonctionnalités

L'application Nexus dispose désormais d'un système de thèmes avec deux modes :

### Mode Clair

- Interface lumineuse avec des couleurs claires
- Meilleure lisibilité en environnement lumineux
- Thème par défaut au démarrage

### Mode Sombre

- Interface sombre avec des couleurs adaptées
- Réduction de la fatigue oculaire en environnement peu lumineux
- Meilleur pour un usage prolongé

## Comment basculer entre les thèmes

### Sur l'écran de connexion

- Un bouton avec l'icône soleil/lune est disponible en haut à droite
- Cliquez sur ce bouton pour basculer entre les modes

### Dans l'application principale

- Un bouton similaire est disponible en bas de la barre de navigation latérale
- Le thème sélectionné est conservé pendant toute la session

## Détails techniques

### Couleurs adaptatives

- Les couleurs des statuts (Planning, Absences) s'adaptent automatiquement au thème
- Utilisation des couleurs système de Material Design 3
- Transparence et opacité optimisées pour chaque mode

### Composants affectés

- **Planning** : Couleurs des statuts de travail, maladie, vacances, personnel
- **Absences** : Couleurs des statuts en attente, approuvées, refusées
- **Navigation** : Adaptation automatique de la barre latérale
- **Formulaires** : Champs de saisie et boutons adaptés

### Configuration

- Thème basé sur une couleur de base bleue
- Material Design 3 activé pour une meilleure cohérence
- Thèmes personnalisés définis dans `main_window.py`

## Améliorations futures possibles

- Sauvegarde de la préférence de thème entre les sessions
- Thème automatique basé sur l'heure du jour
- Thèmes colorés personnalisés
- Mode contraste élevé pour l'accessibilité
