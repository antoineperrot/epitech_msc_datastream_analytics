# Exemples de récupération de données — Homepedia

Six exemples **prêts à lancer** pour démarrer la collecte de données du projet immobilier.
Chaque script interroge une API/source réelle, affiche un résumé et enregistre le résultat
en **JSON + CSV** dans le dossier `data/`.

> ✅ Tous les scripts ont été **testés le 10/09/2026**. La plupart des sources sont
> **sans clé d'API** — vous pouvez démarrer immédiatement.

## Installation

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Lancer un exemple

```bash
python 01_open_meteo_climat.py     # les résultats vont dans ./data/
```

## Les 6 exemples

| # | Script | Source | Donnée | Clé ? | Format |
|---|--------|--------|--------|:-----:|--------|
| 01 | `01_open_meteo_climat.py` | Open-Meteo | Températures journalières depuis 1940 | non | JSON/CSV |
| 02 | `02_eurostat_pib.py` | Eurostat | PIB / habitant par région (NUTS2) | non | JSON-stat |
| 03 | `03_geo_api_communes.py` | API Géo (Etalab) | Communes + population + contours | non | JSON/GeoJSON |
| 04 | `04_georisques_catnat.py` | Géorisques | Arrêtés catastrophe naturelle par commune | non | JSON |
| 05 | `05_ademe_dpe.py` | ADEME (data-fair) | Classe énergétique (DPE) des logements | non | JSON/CSV |
| 06 | `06_dvf_prix.py` | DVF géolocalisé (Etalab) | **Prix réels des ventes immobilières** | non | CSV |

## Ce que chaque exemple illustre (au-delà de « récupérer la donnée »)

- **01 Open-Meteo** — construire une requête paramétrée ; transformer du JSON en CSV.
- **02 Eurostat** — décoder un format statistique structuré (JSON-stat) ; filtrer sur la France.
  Montre aussi les **niveaux NUTS** (pays / grande zone / région) — utile pour les échelles du sujet.
- **03 API Géo** — récupérer le **contour GeoJSON** d'une commune : la brique de base des cartes.
- **04 Géorisques** — croiser un **risque** (inondation, sécheresse…) avec un territoire par code INSEE.
- **05 ADEME DPE** — filtrer une base de **15,5 M de lignes** côté serveur (recherche par champ) ;
  le même endpoint renvoie du JSON **ou** du CSV (`format=csv`).
- **06 DVF** — le **cœur du sujet** (le prix). Montre concrètement pourquoi il faut
  **nettoyer** la donnée : la médiane brute est polluée par des aberrations (ventes multi-lots,
  garages…), qu'on filtre pour obtenir un prix/m² crédible.

## Deux patterns à retenir (débloquent des centaines de jeux de données)

Beaucoup de portails open data français exposent **automatiquement** une API :

- **data-fair** (ex. ADEME) : `…/data-fair/api/v1/datasets/<id>/lines?q=…&q_fields=…&select=…&format=csv`
- **OpenDataSoft** : `…/api/explore/v2.1/catalog/datasets/<id>/records?…` (JSON) et `…/exports/csv` (CSV)

Repérer laquelle des deux formes utilise un site, et vous savez déjà l'interroger.

## Idées d'enchaînement (croiser les sources = valeur du projet)

- **Prix (06) × PIB/hab (02)** : les prix suivent-ils la richesse régionale ?
- **Prix (06) × risques (04)** : les zones les plus exposées sont-elles décotées… ou pas encore ?
- **DPE (05) × prix (06)** : quelle décote pour une passoire thermique (étiquette F/G) ?
- Tout **rattaché au code INSEE** (03) pour agréger ville → département → région.
