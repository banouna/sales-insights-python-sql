# Analyse des ventes 2026 avec Python et SQL

## Présentation

Ce projet consiste à analyser des données de ventes afin d'identifier les produits, catégories et villes qui contribuent le plus au chiffre d'affaires.

Il combine **Python, pandas, Matplotlib et SQL avec SQLite** pour explorer les données, calculer des indicateurs commerciaux, visualiser les résultats et réaliser des analyses complémentaires à l'aide de requêtes SQL.

Les données utilisées sont fictives et servent de support à un projet personnel d'apprentissage et de démonstration.

## Objectifs

- Charger et explorer un fichier CSV avec pandas.
- Vérifier la qualité des données et traiter les anomalies.
- Calculer le chiffre d'affaires à partir des quantités et des prix unitaires.
- Analyser les ventes par produit, catégorie, ville et jour.
- Créer des graphiques avec Matplotlib.
- Générer un rapport HTML récapitulatif.
- Importer les données dans une base SQLite.
- Écrire et exécuter des requêtes SQL d'agrégation.
- Documenter les requêtes et leurs résultats.

## Technologies utilisées

- **Python** : traitement et analyse des données.
- **pandas** : manipulation, nettoyage et agrégation.
- **Matplotlib** : visualisation des résultats.
- **SQL / SQLite** : interrogation des données.
- **CSV** : stockage des données et exportation des résultats.
- **HTML et CSS** : présentation du rapport.
- **Git et GitHub** : versionnement et partage du projet.

## Structure du projet

```text
projet_ventes/
├── data/
│   └── ventes_2026.csv
├── resultats/
│   ├── rapport_ventes.html
│   └── graphiques et fichiers CSV
├── sql/
│   ├── requetes.sql
│   └── analyse_sql.md
├── src/
│   ├── fonctions.py
│   ├── analyse_ventes_2026.py
│   ├── creer_base_sql.py
│   └── executer_sql.py
├── README.md
├── requirements.txt
└── .gitignore
```

La base SQLite est générée localement à partir du fichier CSV à l'aide du script `src/creer_base_sql.py`.

## Installation

1. Installer Python.
2. Cloner le dépôt GitHub ou télécharger le projet.
3. Ouvrir un terminal à la racine du projet.
4. Installer les dépendances :

```bash
python -m pip install -r requirements.txt
```

## Exécution de l'analyse Python

Depuis le dossier principal du projet, lancer :

```bash
python src/analyse_ventes_2026.py
```

Les tableaux, graphiques et rapports sont générés dans le dossier `resultats/`.

## Analyses SQL

### 1. Créer la base de données

```bash
python src/creer_base_sql.py
```

Ce script importe les données du CSV dans une base SQLite et crée la table `ventes`.

### 2. Exécuter une requête SQL

```bash
python src/executer_sql.py
```

Le script lit la requête SQL enregistrée dans le dossier `sql/`, l'exécute sur la base SQLite et affiche les résultats dans le terminal.

Les requêtes et leurs résultats documentés sont disponibles dans :

- `sql/analyse_sql.md`

## Principaux axes d'analyse

- Classement des produits par chiffre d'affaires.
- Analyse des performances par catégorie.
- Répartition du chiffre d'affaires par ville.
- Évolution quotidienne des ventes.
- Utilisation de requêtes SQL avec `SUM()`, `GROUP BY` et `ORDER BY`.

## Compétences démontrées

- Exploration et nettoyage de données.
- Manipulation de données avec pandas.
- Agrégation avec `groupby()`.
- Création de visualisations avec Matplotlib.
- Requêtes SQL d'agrégation et de classement.
- Utilisation de SQLite depuis Python.
- Organisation d'un projet d'analyse de données.
- Documentation et versionnement avec Git et GitHub.

## Améliorations possibles

- Comparer les ventes sur plusieurs périodes.
- Ajouter de nouveaux indicateurs commerciaux.
- Développer un tableau de bord interactif avec Power BI.
- Automatiser davantage la production des rapports.

Projet personnel de pratique en analyse de données. Les données sont fictives et utilisées à des fins pédagogiques.
