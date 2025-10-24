# Gestionnaire de Répertoire Clients

Une **mini-application Flask** permettant de gérer un répertoire client avec les opérations de base du CRUD : **ajout, édition, suppression et consultation des clients**. Ce projet a pour objectif d’apprendre Flask et les bases de la gestion de données dans une application web.

---

## 🛠️ Fonctionnalités

* Ajouter un nouveau client
* Modifier les informations d’un client existant
* Supprimer un client
* Lister tous les clients

---

## 📂 Structure du projet

```
gestion-clients/
│
├── app.py              # Fichier principal de l'application Flask
├── templates/          # Contient les fichiers HTML
│   ├── index.html
│   ├── add_client.html
│   └── edit_client.html
├── static/             # Fichiers statiques (CSS, JS)
├── instance/
|   |──Clients.db          # Base de données flask_sqlalchemy (si utilisée)
└── README.md           # Ce fichier
```

---

## ⚡ Installation et lancement

1. **Cloner le projet**

```bash
git clone https://github.com/hdmanoach/gestion-clients.git
cd gestion-clients
```

2. **Créer un environnement virtuel (optionnel mais recommandé)**

```bash
python -m venv venv
source venv/bin/activate     # Linux/Mac
venv\Scripts\activate        # Windows
```

3. **Installer les dépendances**

```bash
pip install -r requirements.txt
pip install flask  flask_sqlalchemy
```

4. **Lancer l’application**

```bash
python app.py
```

5. **Ouvrir dans le navigateur**

```
http://127.0.0.1:5000
```

---

## 📝 Exemple de base de données

Ce projet utilise ** Flask-SQLAlchemy** pour stocker les clients avec les champs suivants :

* `id` : identifiant unique
* `nom` : nom du client
* `email` : adresse email
* `téléphone` : numéro de téléphone
* `adresse` : adresse du client

---

## 📌 Routes principales

| Route              | Méthode  | Description                 |
| ------------------ | -------- | --------------------------- |
| `/`                | GET      | Liste tous les clients      |
| `/add`             | GET/POST | Ajouter un nouveau client   |
| `/edit/<int:id>`   | GET/POST | Modifier un client existant |
| `/delete/<int:id>` | POST     | Supprimer un client         |

---

## 🛠️ Technologies utilisées

* Python 3.x
* Flask
* Jinja2 (templates HTML)
* Flask-SQLAlchemy (base de données légère)
* HTML/CSS

---

## 📈 Améliorations possibles

* Ajout d’une authentification (login/mot de passe)
* Pagination et recherche des clients
* Utilisation de Bootstrap pour améliorer l’interface
* Passage à une base de données plus robuste (PostgreSQL ou MySQL)
