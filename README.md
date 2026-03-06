# 🎓 EduFlow-Check
## Système de Pointage Automatisé avec Flask

### Description
EduFlow-Check est une application web Flask pour automatiser le pointage des présences dans un centre de formation. Elle permet de gérer les entrées des étudiants en temps réel via une interface web moderne et intuitive.

---

## 📁 Structure du Projet

```
mini_projet/
├── app.py                 # Application Flask principale
├── templates/             # Dossier des templates HTML
│   ├── base.html         # Template de base (héritage)
│   ├── index.html        # Page d'accueil (liste des présences)
│   ├── formulaire.html   # Formulaire d'ajout d'étudiant
│   └── erreur_404.html   # Page d'erreur personnalisée
├── static/               # Dossier des fichiers statiques
│   └── styles.css        # Feuille de styles CSS
├── .venv/                # Environnement virtuel Python
└── README.md            # Ce fichier
```

---

## 🚀 Installation et Démarrage

### Prérequis
- Python 3.7+
- pip (gestionnaire de paquets Python)

### 1. Créer et activer l'environnement virtuel
```bash
python -m venv .venv
.venv\Scripts\activate  # Sur Windows
source .venv/bin/activate  # Sur macOS/Linux
```

### 2. Installer les dépendances
```bash
pip install flask
```

### 3. Lancer l'application
```bash
python app.py
```

L'application sera accessible à : **http://localhost:5000**

---

## 📋 Fonctionnalités Implémentées

### 1. **Route Accueil (`/`)**
- Affiche la liste complète des étudiants pointés
- Affiche le nombre total d'étudiants présents
- Affiche "Aucun étudiant" si la liste est vide

### 2. **Route Pointage Rapide (`/pointage/<nom>`)**
- Route dynamique qui ajoute directement un étudiant
- Redirige vers l'accueil après l'ajout
- Enregistre automatiquement l'heure du pointage

### 3. **Route Formulaire (`/ajouter`)**
- **GET** : Affiche un formulaire d'ajout
- **POST** : Ajoute l'étudiant saisi à la liste
- Valide que le champ n'est pas vide
- Redirige vers l'accueil après l'ajout

### 4. **Gestion des Erreurs (`/erreur_404`)**
- Page d'erreur personnalisée pour les routes inexistantes
- Affiche des liens vers les pages disponibles
- Design cohérent avec le reste de l'application

### 5. **Route Bonus (`/reinitialiser`)**
- Réinitialise la liste des présences
- Utile pour recommencer le pointage

---

## 🎨 Design et Templates

### Héritage Jinja2
- **base.html** : Template de base avec header, navigation et footer
- **index.html** : Étend base.html pour afficher les présences
- **formulaire.html** : Étend base.html pour le formulaire
- **erreur_404.html** : Étend base.html pour les erreurs

### Styles CSS
- Design moderne et responsive
- Gradients et animations fluides
- Support complet du mobile (responsive design)
- Couleurs professionnelles

---

## 📝 Exemples d'Utilisation

### 1. Pointage via Formulaire
```
1. Accéder à http://localhost:5000/ajouter
2. Entrer le nom de l'étudiant
3. Cliquer sur "Pointer l'Étudiant"
4. Retour automatique à la liste des présences
```

### 2. Pointage Rapide via URL
```
http://localhost:5000/pointage/Ahmed%20Ali
http://localhost:5000/pointage/Fatima%20Bennani
```

### 3. Réinitialiser la Liste
```
http://localhost:5000/reinitialiser
```

---

## 🔒 Sécurité et Validation

✅ Validation des champs vides
✅ Utilisation de `request.form` pour récupérer les données POST
✅ Utilisation de `redirect()` et `url_for()` pour éviter les soumissions multiples
✅ Page 404 personnalisée
✅ Échappement automatique des variables dans les templates (protection XSS)

---

## 📊 Structure des Données

### Liste presences
Chaque étudiant est stocké comme un dictionnaire :
```python
{
    'nom': 'Ahmed Ali',
    'heure': '14:35:42'
}
```

---

## 🛠️ Technologie Utilisée

| Technologie | Version | Usage |
|-------------|---------|-------|
| **Flask** | Latest | Framework web Python |
| **Python** | 3.13+ | Langage de programmation |
| **Jinja2** | Built-in | Moteur de templates |
| **HTML5** | Latest | Markup |
| **CSS3** | Latest | Stylisation |

---

## 📌 Critères de Notation (20 points)

| Critère | Points | Statut |
|---------|--------|--------|
| Structure du projet | 3 | ✅ |
| Routage dynamique | 4 | ✅ |
| Gestion des formulaires | 5 | ✅ |
| Qualité du Templating | 5 | ✅ |
| Gestion des erreurs | 3 | ✅ |

---

## 💡 Conseil de l'Expert

> "Rappelez-vous ce que vous faisiez avec socket.recv(). Ici, Flask parse tout pour vous dans request.form. Soyez rigoureux sur les noms de vos variables !"

---

## 👨‍🏫 Informations du Projet

- **Module** : Du Socket au Web avec Flask
- **Durée** : 60 minutes
- **Intervenant** : KHNIFIRA Houssam
- **Date** : 2026

---

## 📦 Livrable

Le projet doit être livré sous forme d'archive .zip nommée :
```
NOM_PRENOM_EDUFLOW.zip
```

**À exclure** : Le dossier `.venv` (utiliser un fichier requirements.txt à la place)

### Générer requirements.txt
```bash
pip freeze > requirements.txt
```

---

## 🎯 Points Clés

✅ Application Flask entièrement fonctionnelle
✅ Routes GET et POST implémentées
✅ Templates avec héritage Jinja2
✅ Design responsive et moderne
✅ Validation des formulaires
✅ Gestion des erreurs
✅ Enregistrement automatique des heures

---

**Développé avec ❤️ par AHMED ZAKARIA**
