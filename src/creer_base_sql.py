
import sqlite3
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

fichier_csv = BASE_DIR / "data" / "ventes_2026.csv"

fichier_db = BASE_DIR / "data" / "ventes.db"

df = pd.read_csv(fichier_csv)

connexion = sqlite3.connect(fichier_db)

df.to_sql("ventes", connexion, if_exists="replace", index=False)

connexion.close()

print("Base de données créée avec succès !")
print(f"Nombre de lignes importées : {len(df)}")
