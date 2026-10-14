# Analyse des ventes 2026 avec Python

## Présentation

Ce projet consiste à analyser des données de ventes à l'aide de Python afin d'identifier les produits, catégories et villes qui contribuent le plus au chiffre d'affaires.

Il permet de mettre en pratique les principales étapes d'un projet d'analyse de données : chargement, vérification, nettoyage, analyse, visualisation et exportation des résultats.

## Objectifs

- Charger et explorer un fichier CSV avec pandas.
- Vérifier la qualité des données et traiter les anomalies.
- Calculer le chiffre d'affaires à partir des quantités et des prix unitaires.
- Analyser les performances par produit, ville, catégorie et jour.
- Créer des graphiques pour faciliter l'interprétation des résultats.
- Générer un rapport HTML récapitulatif.

## Technologies utilisées

- Python
- pandas
- Matplotlib
- CSV
- HTML et CSS

## Structure du projet

```text
projet_ventes/
├── data/
│   └── ventes_2026.csv
├── resultats/
│   ├── rapport_ventes.html
│   └── graphiques PNG
├── src/
│   ├── fonctions.py
│   └── analyse_ventes_2026.py
├── README.md
└── requirements.txt
```

## Installation

1. Installer Python.
2. Télécharger ou cloner le projet.
3. Installer les dépendances :

```bash
python -m pip install -r requirements.txt
```

## Exécution

Depuis le dossier principal du projet, lancer :

```bash
python src/analyse_ventes_2026.py
```

Les résultats sont enregistrés dans le dossier `resultats/`.

## Résultats attendus

Le projet produit notamment :

- Un classement des produits par chiffre d'affaires.
- Une analyse des ventes par ville et par catégorie.
- Une évolution quotidienne du chiffre d'affaires.
- Des graphiques de comparaison et de répartition.
- Un rapport HTML regroupant les principaux indicateurs.

## Compétences démontrées

- Manipulation de données avec pandas.
- Nettoyage et contrôle de la qualité des données.
- Agrégation et analyse avec `groupby()`.
- Création de visualisations avec Matplotlib.
- Organisation d'un projet Python en plusieurs modules.
- Génération de rapports et utilisation de GitHub.

## Améliorations possibles

- Ajouter des filtres interactifs.
- Comparer les performances sur plusieurs périodes.
- Automatiser la génération du rapport.
- Développer un tableau de bord interactif.

---

Projet personnel de pratique en analyse de données avec Python.