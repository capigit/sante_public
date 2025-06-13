import pandas as pd

# Charger les données brutes
input_path = "../data/mortalite_infantile.csv"
output_path = "../data/mortalite_infantile_clean.csv"

# Lire le fichier CSV brut
df = pd.read_csv(input_path)

# Garder uniquement les colonnes utiles
colonnes_utiles = [
    'SpatialDim', 'TimeDim', 'Dim1', 'Dim2', 
    'NumericValue', 'Low', 'High'
]
df = df[colonnes_utiles]

# Renommer les colonnes pour plus de clarté
df.columns = [
    'pays_code', 'annee', 'sexe', 'tranche_age',
    'valeur', 'borne_basse', 'borne_haute'
]

# Nettoyage des types
df['annee'] = pd.to_numeric(df['annee'], errors='coerce')
df['valeur'] = pd.to_numeric(df['valeur'], errors='coerce')
df['borne_basse'] = pd.to_numeric(df['borne_basse'], errors='coerce')
df['borne_haute'] = pd.to_numeric(df['borne_haute'], errors='coerce')

# Supprimer les lignes sans valeur numérique
df = df.dropna(subset=['valeur'])

# Sauvegarder le fichier nettoyé
df.to_csv(output_path, index=False)
print(f"Fichier nettoyé sauvegardé : {output_path}")
print(f"{len(df)} lignes conservées après nettoyage")