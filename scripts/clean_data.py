import pandas as pd
import os

# Chargement des données brutes
df = pd.read_csv("../data/mortalite_infantile.csv")

# Renommation des colonnes pour plus de clarté
df = df.rename(columns={
    "pays": "Pays",
    "annee": "Année",
    "valeur": "Taux_mortalité"
})

# Conversion des types
df["Année"] = df["Année"].astype(int)
df["Taux_mortalité"] = pd.to_numeric(df["Taux_mortalité"], errors="coerce")

# Suppression des lignes avec valeur manquante
df = df.dropna()

# Tri (facultatif mais propre)
df = df.sort_values(by=["Pays", "Année"])

# Création du dossier clean
os.makedirs("../data/clean", exist_ok=True)

# Sauvegarde
df.to_csv("../data/clean/mortalite_infantile_clean.csv", index=False)
print("Fichier nettoyé sauvegardé dans data/clean/mortalite_infantile_clean.csv")