import requests
import pandas as pd
import os

#Création du dossier data s'il n'existe pas
os.makedirs("../data", exist_ok=True)

#URL de l'API GHO pour la mortalité infantile (0-1 an)
API_URL = "https://ghoapi.azureedge.net/api/MDG_0000000001"

#Liste des pays à suivre (codes ISO3)
PAYS_SELECTION = ["FRA", "SEN", "BRA", "IND", "NGA", "USA", "CHN", "DEU"]

#Requête GET
response = requests.get(API_URL)
data = response.json().get('value', [])
print(f"{len(data)} enregistrements reçus depuis l'API")

#Affichage des codes pays distincts dans le dataset (optionnel)
pays_distincts = set()
for item in data:
    pays_distincts.add(item.get('SpatialDim'))
print("Codes pays distincts trouvés dans l'API :", sorted(pays_distincts))

#Exemple d'enregistrement
if data:
    print("Exemple d'enregistrement:", data[0])

#Extraction et filtrage des données
records = []
for item in data:
    try:
        pays = item.get('SpatialDim')
        annee = item.get('TimeDim')

        #Filtre selon pays, année, sexe et âge
        if (
            pays in PAYS_SELECTION and
            annee and
            item.get('Dim1') == 'SEX_BTSX' and  #sexe total (both sexes)
            item.get('Dim2') == 'AGEGROUP_MONTHS0-11' and  # âge 0-11 mois
            item.get('NumericValue') is not None
        ):
            records.append({
                "pays": pays,
                "annee": int(annee),
                "valeur": item.get('NumericValue')
            })
    except Exception as e:
        print("Erreur lors du parsing :", e)

print(f"{len(records)} enregistrements retenus après filtrage des pays")

if records:
    df = pd.DataFrame(records)
    df.sort_values(by=["pays", "annee"], inplace=True)

    output_path = "../data/mortalite_infantile.csv"
    df.to_csv(output_path, index=False, encoding="utf-8")
    print(f"Fichier sauvegardé : {output_path}")
else:
    print("Aucune donnée valide n'a été extraite.")