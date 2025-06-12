# Projet Santé Publique - Mortalité Infantile

Ce projet automatise la collecte, le traitement et la visualisation de données de santé publique à partir de sources ouvertes.

## 🔍 Indicateur suivi

- Taux de mortalité infantile (moins de 1 an, pour 1 000 naissances vivantes)

## 📁 Structure

- `scripts/collect_gho_data.py` : script de collecte depuis l'OMS
- `data/mortalite_infantile.csv` : données traitées prêtes pour analyse
- `notebooks/` : notebooks Jupyter pour l'analyse
- `requirements.txt` : dépendances Python

## 🚀 Exécution

```bash
pip install -r requirements.txt
python scripts/collect_gho_data.py