# 📦 Projet SQLAlchemy - Démo Seigneur des Anneaux

Ce projet illustre la mise en place d’une petite application console basée sur SQLAlchemy, en manipulant plusieurs entités liées à l’univers du Seigneur des Anneaux.

---

## ⚙️ Création et activation de l’environnement virtuel

```bash
# Création de l’environnement virtuel
py -3 -m venv .venv

# Activation de l’environnement (Windows)
.\.venv\Scripts\activate
```

---

## 🛠️ Configuration de la base PostgreSQL

Dans un fichier `config.py`, renseignez vos informations de connexion PostgreSQL :

```python
# Paramètres de connexion
scheme         = "postgresql+psycopg2"
username       = "votre_utilisateur"
password       = "votre_mot_de_passe"
hostname       = "localhost"
port           = "5432"
database_name  = "nom_de_votre_base"

# Construction de l'URL de connexion
URL_DB = f"{scheme}://{username}:{password}@{hostname}:{port}/{database_name}"
```

---

## 🎯 Objectif pédagogique

L’objectif est de construire une application console interactive permettant de gérer :

- Les personnages
- Les races
- Les anneaux
- Les quêtes

Chaque entité est reliée via des relations claires (1:N, N:N) et exploite soit SQLAlchemy ORM, soit du SQL brut.

Une classe `Anneau` a notamment été implémentée pour manipuler la table correspondante uniquement via des requêtes SQL brutes (`text()`), avant d’être intégrée au menu principal de l'application.

---

## 🚀 Lancement

Une fois votre base de données PostgreSQL prête et vos entités définies, lancez simplement :

```bash
python app/main.py
```

---
