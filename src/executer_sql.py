import sqlite3
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

fichier_db = BASE_DIR / "data" / "ventes.db"
fichier_sql = BASE_DIR / "sql" / "requetes.sql"

# Lire la requête SQL depuis le fichier
requete = fichier_sql.read_text(encoding="utf-8")

# Se connecter à la base de données
with sqlite3.connect(fichier_db) as connexion:
    resultat = pd.read_sql_query(requete, connexion)

# Afficher le résultat
print(resultat.to_string(index=False))

