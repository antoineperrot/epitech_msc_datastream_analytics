"""
04 — Risques naturels via Géorisques (JSON, SANS token en v1)
------------------------------------------------------------
Source : https://www.georisques.gouv.fr/doc-api
Endpoint : /api/v1/gaspar/catnat = arrêtés de catastrophe naturelle par commune.
Idée    : compter/inspecter les catastrophes naturelles d'une commune
          -> thématique "risque climatique & immobilier".

Ce que montre l'exemple :
  - interroger une API publique par code INSEE
  - gérer la pagination simple et exporter un CSV des événements
"""
import csv
import json
from pathlib import Path

import requests

OUT = Path(__file__).parent / "data"
OUT.mkdir(exist_ok=True)

CODE_INSEE = "06088"  # Nice (essayer 30007 = Alès, 13055 = Marseille...)


def main():
    print(f"→ Arrêtés catastrophe naturelle pour la commune {CODE_INSEE}...")
    r = requests.get(
        "https://georisques.gouv.fr/api/v1/gaspar/catnat",
        params={"code_insee": CODE_INSEE, "page_size": 100},
        timeout=30,
    )
    r.raise_for_status()
    payload = r.json()
    (OUT / "georisques_catnat.json").write_text(
        json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8"
    )

    # La réponse contient les événements sous la clé "data" (liste de dicts)
    evenements = payload.get("data", payload if isinstance(payload, list) else [])

    csv_path = OUT / "georisques_catnat.csv"
    with csv_path.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["libelle_risque", "date_debut", "date_fin", "date_arrete"])
        for e in evenements:
            w.writerow([
                e.get("libelle_risque_jo"),
                e.get("date_debut_evt"),
                e.get("date_fin_evt"),
                e.get("date_publication_arrete"),
            ])

    print(f"  {len(evenements)} arrêtés récupérés")
    for e in evenements[:5]:
        print(f"  {e.get('date_debut_evt', '?'):<12} {e.get('libelle_risque_jo')}")
    print(f"  ✅ Écrit : {csv_path.relative_to(Path(__file__).parent)}")


if __name__ == "__main__":
    main()
