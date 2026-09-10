"""
05 — Classe énergétique (DPE) via l'ADEME / data-fair (JSON ou CSV, SANS clé)
----------------------------------------------------------------------------
Source  : https://data.ademe.fr/datasets/dpe03existant
Endpoint: /data-fair/api/v1/datasets/dpe03existant/lines
Idée    : récupérer les diagnostics de performance énergétique d'une commune
          (15,5 M de lignes au total !) -> variable "classe énergétique du bâti".

Ce que montre l'exemple :
  - interroger une API "data-fair" avec recherche plein texte (q) et sélection de champs
  - le MÊME endpoint peut renvoyer du JSON ou du CSV (paramètre format)
"""
import csv
import json
from pathlib import Path

import requests

OUT = Path(__file__).parent / "data"
OUT.mkdir(exist_ok=True)

BASE = "https://data.ademe.fr/data-fair/api/v1/datasets/dpe03existant/lines"
CODE_POSTAL = "11000"  # Carcassonne
CHAMPS = "etiquette_dpe,etiquette_ges,nom_commune_ban,code_postal_ban,annee_construction,surface_habitable_logement"


def main():
    print(f"→ DPE pour le code postal {CODE_POSTAL} (ADEME)...")
    r = requests.get(
        BASE,
        params={
            "size": 50,
            "select": CHAMPS,
            "q": CODE_POSTAL,             # recherche...
            "q_fields": "code_postal_ban",  # ...restreinte au champ code postal
        },
        timeout=60,
    )
    r.raise_for_status()
    payload = r.json()
    (OUT / "ademe_dpe.json").write_text(
        json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8"
    )

    lignes = payload.get("results", [])
    csv_path = OUT / "ademe_dpe.csv"
    with csv_path.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["etiquette_dpe", "etiquette_ges", "commune", "code_postal",
                    "annee_construction", "surface_m2"])
        for d in lignes:
            w.writerow([
                d.get("etiquette_dpe"), d.get("etiquette_ges"),
                d.get("nom_commune_ban"), d.get("code_postal_ban"),
                d.get("annee_construction"), d.get("surface_habitable_logement"),
            ])

    print(f"  total base = {payload.get('total'):,} diagnostics | échantillon = {len(lignes)}")
    # Répartition des étiquettes dans l'échantillon
    from collections import Counter
    rep = Counter(d.get("etiquette_dpe") for d in lignes)
    print("  Répartition des étiquettes (échantillon) :", dict(sorted(rep.items())))
    print(f"  ✅ Écrit : {csv_path.relative_to(Path(__file__).parent)}")


if __name__ == "__main__":
    main()
