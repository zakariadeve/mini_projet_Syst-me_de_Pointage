# 🧪 Guide de Test - EduFlow-Check

Ce fichier décrit comment tester manuellement toutes les fonctionnalités de l'application.

---

## ✅ Checklist de Test

### 1. Lancement de l'Application
- [ ] Naviguer vers `d:\TSDI2éme\python\mini_projet\`
- [ ] Activer l'environnement virtuel : `.venv\Scripts\activate`
- [ ] Lancer l'app : `python app.py`
- [ ] Vérifier le message : "Running on http://localhost:5000"
- [ ] Ouvrir navigateur : http://localhost:5000

---

### 2. Route Accueil (/)
**URL** : http://localhost:5000/

**Attendu** :
- [ ] Header avec titre "🎓 EduFlow-Check"
- [ ] Barre de navigation visible
- [ ] Message "Aucun étudiant pointé pour le moment"
- [ ] Bouton "Commencer à Pointer"
- [ ] Footer avec informations du projet

---

### 3. Formulaire d'Ajout (/ajouter)

#### 3A. Accès au Formulaire (GET)
**URL** : http://localhost:5000/ajouter

**Attendu** :
- [ ] Page avec titre "Ajouter un Étudiant"
- [ ] Champ input pour le nom
- [ ] Bouton "Pointer l'Étudiant"
- [ ] Bouton "Annuler"
- [ ] Zone info avec instructions

#### 3B. Validation de Champ Vide
**Action** :
1. [ ] Cliquer sur le champ "Nom" sans rien écrire
2. [ ] Cliquer sur "Pointer l'Étudiant"

**Attendu** :
- [ ] Message d'erreur : "Le nom ne peut pas être vide!"
- [ ] Rester sur la page du formulaire

#### 3C. Ajout d'un Étudiant (POST)
**Action** :
1. [ ] Entrer "Ahmed Ali" dans le champ
2. [ ] Cliquer sur "Pointer l'Étudiant"

**Attendu** :
- [ ] Redirection vers l'accueil
- [ ] "Ahmed Ali" apparaît dans le tableau
- [ ] Compteur affiche "1 Étudiants Pointés"
- [ ] L'heure est enregistrée (format HH:MM:SS)

#### 3D. Ajouter Plusieurs Étudiants
**Action** :
Répéter 3C avec :
- [ ] "Fatima Bennani"
- [ ] "Mohamed Hassan"
- [ ] "Laila Khnifira"

**Attendu** :
- [ ] 4 lignes dans le tableau (Ahmed + 3 nouveaux)
- [ ] Compteur affiche "4 Étudiants Pointés"
- [ ] Tableau bien formaté avec alternance de couleurs

---

### 4. Pointage Rapide (/pointage/<nom>)

**Action** :
1. Utiliser plusieurs URLs :
   - http://localhost:5000/pointage/Khalid%20Ahmed  
   - http://localhost:5000/pointage/Sara%20Jamal

**Attendu** :
- [ ] Chaque URL redirige automatiquement vers l'accueil
- [ ] Les noms apparaissent dans le tableau
- [ ] Les heures sont automatiquement enregistrées
- [ ] Compteur se met à jour

**Test avec Espaces** :
- [ ] %20 (espace encodé) fonctionne correctement
- [ ] Les noms s'affichent sans encodage

---

### 5. Navigation

#### 5A. Menu de Navigation
En permanence sur toutes les pages :
- [ ] Lien "Accueil" → retour à /
- [ ] Lien "Ajouter Étudiant" → go to /ajouter
- [ ] Lien "Réinitialiser" (rouge) → action destructrice

#### 5B. Bouton Réinitialiser
**Action** :
1. [ ] Sur l'accueil avec étudiants présents
2. [ ] Cliquer sur "Réinitialiser" (red button)

**Attendu** :
- [ ] Redirection vers /
- [ ] Liste complètement vide (presences = [])
- [ ] Message "Aucun étudiant pointé"
- [ ] Compteur = 0

---

### 6. Gestion des Erreurs (404)

**Action** :
Accéder à une route inexistante :
- [ ] http://localhost:5000/inexistant
- [ ] http://localhost:5000/route/fausse
- [ ] http://localhost:5000/admin

**Attendu** :
- [ ] Page d'erreur personnalisée s'affiche
- [ ] Code "404" visible
- [ ] Message : "Page non trouvée"
- [ ] Liens vers les pages disponibles
- [ ] Bouton "Retour à l'Accueil"

---

### 7. Responsive Design (Mobile)

**Action** : Utiliser DevTools (F12) et mode responsive

#### 7A. Écran 768px (Tablette)
- [ ] Navigation empile correctement
- [ ] Tableau reste lisible
- [ ] Boutons s'étendent
- [ ] Pas de débordement

#### 7B. Écran 480px (Téléphone)
- [ ] Header redimensionné (h1 plus petit)
- [ ] Tableau texte réduit mais lisible
- [ ] Boutons prennent 100% de largeur
- [ ] Formulaire bien formaté

---

### 8. Héritage de Templates

**Vérifier la cohérence visuelle** :
- [ ] Header identique sur toutes les pages
- [ ] Navigation identique sur toutes les pages
- [ ] Footer identique sur toutes les pages
- [ ] Styles appliqués uniformément
- [ ] Pas de différences de mise en page

**Vérifier Jinja2** :
- [ ] Boucle `{% for %}` fonctionne dans le tableau
- [ ] Condition `{% if presences %}` affiche le bon contenu
- [ ] Variable `{{ item.nom }}` affiche correctement
- [ ] Filtre `{{ total }}` s'actualise

---

### 9. Données et Persistance (Session)

**Important** : Les données sont stockées en mémoire Python

**Test** :
- [ ] Ajouter 3 étudiants
- [ ] Rafraîchir la page (F5) → données persistent
- [ ] Arrêter et relancer l'app → données perdues (normal!)

---

### 10. CSS et Styling

#### 10A. Couleurs
- [ ] Header : Gradient bleu
- [ ] Boutons primary : Bleu
- [ ] Boutons danger/réinitialiser : Rouge
- [ ] Footer : Gris foncé

#### 10B. Effets
- [ ] Hover sur boutons : Légère animation vers le haut
- [ ] Hover sur lignes du tableau : Fond gris
- [ ] Focus sur inputs : Bordure bleue

#### 10C. Typographie
- [ ] Header bien lisible
- [ ] Texte du corps 1rem (16px)
- [ ] Monospace pour les heures

---

## 📋 Résumé des Points à Vérifier

| Critère | Test | Statut |
|---------|------|--------|
| Structure | Architecture Flask respectée | [ ] |
| Routage | `/` `/pointage/<nom>` `/ajouter` | [ ] |
| Formulaire | GET/POST, validation, redirect | [ ] |
| Templates | Héritage, boucles, conditions | [ ] |
| Erreurs | 404 personnalisée | [ ] |
| CSS | Responsive, cohérent | [ ] |
| Navigation | Tous les liens fonctionnent | [ ] |
| Données | Horodatage correct | [ ] |

---

## 🎯 Checklist Finale (Avant Livraison)

Avant de compresser le projet en .zip :

- [ ] Supprimer le dossier `.venv/`
- [ ] Garder le fichier `requirements.txt`
- [ ] Vérifier la structure complète
- [ ] Tester une dernière fois l'application
- [ ] Vérifier que tous les fichiers sont présents
- [ ] Compresser en `.zip` avec le nom correct : `NOM_PRENOM_EDUFLOW.zip`

---

## 🚀 Commandes Utiles

```bash
# Naviguer au dossier
cd d:\TSDI2éme\python\mini_projet

# Activer l'environnement
.venv\Scripts\activate

# Installer les dépendances
pip install -r requirements.txt

# Lancer l'app
python app.py

# Arrêter l'app
Ctrl + C

# Désactiver l'environnement
deactivate
```

---

**Bon test! 🧪**
