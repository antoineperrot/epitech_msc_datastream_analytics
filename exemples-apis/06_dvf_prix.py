"""
06 — Prix immobiliers réels via DVF géolocalisé (fichiers CSV, SANS clé)
-----------------------------------------------------------------------
Source : https://www.data.gouv.fr/datasets/demandes-de-valeurs-foncieres-geolocalisees
Fichiers Etalab prêts à l'emploi, découpés par année / département / commune :
   https://files.data.gouv.fr/geo-dvf/latest/csv/<annee>/communes/<dept>/<code_commune>.csv
Idée   : LE cœur du sujet -> le prix réel des ventes immobilières.
         Ici on calcule le prix médian au m² d'une commune pour une année.

Ce que montre l'exemple :
  - télécharger un fichier CSV distant (éventuellement compressé .gz)
  - le parser et calculer un indicateur simple (prix médian au m²)
"""
import csv
import gzip
import io
import statistics
from pathlib import Path

import requests

OUT = Path(__file__).parent / "data"
OUT.mkdir(exist_ok=True)

ANNEE = "2023"
DEPT = "06"
CODE_COMMUNE = "06088"  # Nice
BASE = f"https://files.data.gouv.fr/geo-dvf/latest/csv/{ANNEE}/communes/{DEPT}/{CODE_COMMUNE}"


def telecharger_csv(base_url):
    """Récupère le CSV (essaie .csv puis .csv.gz) et renvoie le texte décodé."""
    for suffixe, compresse in ((".csv", False), (".csv.gz", True)):
        r = requests.get(base_url + suffixe, timeout=60)
        if r.status_code == 200:
            print(f"  fichier : {base_url + suffixe}")
            if compresse:
                return gzip.decompress(r.content).decode("utf-8")
            return r.text
    r.raise_for_status()


def main():
    print(f"→ Ventes DVF {ANNEE} pour la commune {CODE_COMMUNE}...")
    texte = telecharger_csv(BASE)
    (OUT / "dvf_commune.csv").write_text(texte, encoding="utf-8")

    reader = csv.DictReader(io.StringIO(texte))
    prix_m2 = []
    n_ventes = 0
    for row in reader:
        if row.get("nature_mutation") != "Vente":
            continue
        if row.get("type_local") not in ("Appartement", "Maison"):
            continue
        try:
            valeur = float(row["valeur_fonciere"])
            surface = float(row["surface_reelle_bati"])
        except (ValueError, KeyError):
            continue
        if surface > 0 and valeur > 0:
            n_ventes += 1
            prix_m2.append(valeur / surface)

    if prix_m2:
        # --- AVANT nettoyage : les données brutes DVF contiennent des aberrations
        # (ventes multi-lots où la valeur totale est portée par une seule ligne,
        #  dépendances/garages, surfaces erronées...) -> la fourchette explose.
        print(f"  {n_ventes} ventes (appart./maison) brutes")
        print(f"  Brut     -> médiane {statistics.median(prix_m2):,.0f} €/m² | "
              f"fourchette {min(prix_m2):,.0f} → {max(prix_m2):,.0f} €/m²")

        # --- APRÈS nettoyage : on ne garde que les prix plausibles (500 → 25 000 €/m²)
        propre = [p for p in prix_m2 if 500 <= p <= 25000]
        print(f"  Nettoyé  -> {len(propre)} ventes | médiane {statistics.median(propre):,.0f} €/m² | "
              f"fourchette {min(propre):,.0f} → {max(propre):,.0f} €/m²")
        print("  (leçon : la donnée brute DOIT être nettoyée avant analyse — c'est au barème !)")
    print(f"  ✅ Écrit : data/dvf_commune.csv")


if __name__ == "__main__":
    main()
