# Navigation Drawer - Barre Latérale Moderne

## 📋 Aperçu

L'application Nexus utilise maintenant un NavigationDrawer moderne pour une barre latérale élégante et rétractable qui s'adapte parfaitement à votre écran.

## 🎯 Fonctionnalités

### ✅ NavigationDrawer

- **Interface moderne** : Utilise le composant NavigationDrawer de Flet
- **Ouverture/Fermeture** : Barre latérale qui se rétracte complètement
- **AppBar intégrée** : Barre d'application avec bouton menu
- **Responsive** : S'adapte automatiquement aux différentes tailles d'écran

### ⌨️ Méthodes de basculement

1. **Bouton Menu** : Cliquez sur l'icône ☰ dans la barre d'application
2. **Raccourci clavier** : Pressez `Ctrl+B` (ou `Cmd+B` sur macOS)
3. **Auto-fermeture** : Se ferme automatiquement après sélection d'un élément

### 💾 Persistance des préférences

- Votre choix d'affichage est automatiquement sauvegardé
- L'application se souvient de votre préférence au redémarrage
- Les préférences sont stockées dans le fichier `user_preferences.json`

### 🎨 Interface améliorée

- **AppBar moderne** : Barre d'application avec titre et bouton menu
- **Navigation fluide** : Sélection intuitive des sections
- **Thème intégré** : Bouton de basculement de thème dans le drawer
- **Espacement optimisé** : Contenu principal avec padding approprié

## 🚀 Utilisation

### Première utilisation

1. Lancez l'application Nexus
2. Connectez-vous avec vos identifiants
3. La barre latérale s'ouvre automatiquement selon vos préférences

### Ouverture de la barre latérale

- **Méthode 1** : Cliquez sur l'icône ☰ dans la barre d'application
- **Méthode 2** : Pressez `Ctrl+B` (Windows/Linux) ou `Cmd+B` (macOS)

### Navigation

- Cliquez sur un élément du drawer pour naviguer
- Le drawer se ferme automatiquement après la sélection
- Le thème peut être changé directement depuis le drawer

## 💡 Conseils d'utilisation

### Quand utiliser le mode réduit ?

- Sur des écrans plus petits (tablettes, petits moniteurs)
- Quand vous avez besoin de plus d'espace pour le contenu principal
- Pour une navigation rapide avec les raccourcis clavier

### Quand utiliser le mode étendu ?

- Sur des écrans larges où l'espace n'est pas limité
- Quand vous préférez voir les labels des sections
- Pour une navigation plus intuitive

## 🔧 Paramètres techniques

### Fichier de préférences

```json
{
  "sidebar_collapsed": false,
  "theme_mode": "light"
}
```

### Durée d'animation

- **Transition** : 300 millisecondes
- **Courbe** : Ease-in-out pour un mouvement naturel

## 🎯 Avantages

1. **Optimisation de l'espace** : Plus de place pour le contenu principal
2. **Ergonomie améliorée** : Navigation rapide avec raccourcis clavier
3. **Personnalisation** : Interface adaptable à vos préférences
4. **Persistance** : Mémorisation de vos choix entre les sessions
5. **Accessibilité** : Support complet des raccourcis clavier

## 🐛 Dépannage

### La barre latérale ne se réduit pas ?

- Vérifiez que vous cliquez bien sur le bouton menu (☰)
- Essayez le raccourci clavier `Ctrl+B` / `Cmd+B`

### Les préférences ne sont pas sauvegardées ?

- Vérifiez les permissions d'écriture dans le dossier de l'application
- Le fichier `user_preferences.json` sera créé automatiquement

### L'animation semble saccadée ?

- Cela peut arriver sur des systèmes moins performants
- L'animation peut être désactivée en modifiant la durée à 0ms dans le code

---

_Cette fonctionnalité améliore l'expérience utilisateur en permettant une interface plus flexible et personnalisable._
