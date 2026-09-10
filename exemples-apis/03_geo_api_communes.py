"""
03 — Découpage géographique via l'API Géo (JSON / GeoJSON, SANS clé d'API)
-------------------------------------------------------------------------
Source : https://geo.api.gouv.fr/
Idée    : récupérer la liste des communes d'un département, avec population et
          centre géographique -> base pour joindre d'autres données et faire des cartes.

Ce que montre l'exemple :
  - une API REST très simple (paramètres dans l'URL)
  - récupérer aussi la géométrie (contour) au format GeoJSON pour la cartographie
"""
import csv
import json
from pathlib import Path

import requests

OUT = Path(__file__).parent / "data"
OUT.mkdir(exist_ok=True)

DEPARTEMENT = "06"  # Alpes-Maritimes (mettre "75" = Paris, "69" = Rhône, etc.)


def main():
    print(f"→ Communes du département {DEPARTEMENT} (API Géo)...")
    r = requests.get(
        "https://geo.api.gouv.fr/communes",
        params={
            "codeDepartement": DEPARTEMENT,
            "fields": "nom,code,population,centre,codeDepartement",
            "format": "json",
        },
        timeout=30,
    )
    r.raise_for_status()
    communes = r.json()
    (OUT / "geo_communes.json").write_text(
        json.dumps(communes, ensure_ascii=False, indent=2), encoding="utf-8"
    )

    csv_path = OUT / "geo_communes.csv"
    with csv_path.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["code_insee", "nom", "population", "lon", "lat"])
        for c in communes:
            lon, lat = (c.get("centre", {}).get("coordinates", [None, None]) + [None, None])[:2]
            w.writerow([c["code"], c["nom"], c.get("population"), lon, lat])

    print(f"  {len(communes)} communes récupérées")
    for c in communes[:3]:
        print(f"  {c['code']}  {c['nom']:<22} pop={c.get('population')}")

    # Bonus cartographie : le contour d'une commune au format GeoJSON
    code0 = communes[0]["code"]
    g = requests.get(
        f"https://geo.api.gouv.fr/communes/{code0}",
        params={"fields": "nom,contour", "format": "geojson", "geometry": "contour"},
        timeout=30,
    )
    if g.ok:
        (OUT / f"geo_contour_{code0}.geojson").write_text(g.text, encoding="utf-8")
        print(f"  Contour GeoJSON de {code0} enregistré")
    print(f"  ✅ Écrit : {csv_path.relative_to(Path(__file__).parent)}")


if __name__ == "__main__":
    main()
