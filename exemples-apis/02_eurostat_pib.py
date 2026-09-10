"""
02 — PIB par habitant via Eurostat (format JSON-stat, SANS clé d'API)
--------------------------------------------------------------------
Source : https://ec.europa.eu/eurostat/web/user-guides/data-browser/api-data-access
Jeu     : nama_10r_2gdp = PIB aux prix courants par région (NUTS2).
Idée    : récupérer le PIB/habitant de toutes les régions françaises pour une année.

Ce que montre l'exemple :
  - interroger une API statistique européenne
  - décoder le format JSON-stat (valeurs indexées + dimensions séparées)
  - filtrer sur la France et exporter un CSV région ; PIB/hab
"""
import csv
import json
from pathlib import Path

import requests

OUT = Path(__file__).parent / "data"
OUT.mkdir(exist_ok=True)

URL = "https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/nama_10r_2gdp"
PARAMS = {
    "format": "JSON",
    "unit": "EUR_HAB",   # euros par habitant
    "time": "2021",
}


def flatten_jsonstat(data):
    """Renvoie {code_geo: (label, valeur)} pour un JSON-stat où seule la
    dimension 'geo' varie (les autres dimensions étant figées à 1 catégorie)."""
    sizes = data["size"]
    ids = data["id"]
    geo = data["dimension"]["geo"]
    index = geo["category"]["index"]     # code -> position
    labels = geo["category"]["label"]    # code -> nom

    # "stride" de la dimension geo = produit des tailles des dimensions suivantes
    pos_geo = ids.index("geo")
    stride = 1
    for s in sizes[pos_geo + 1:]:
        stride *= s

    values = data["value"]  # dict {index_lineaire(str ou int): valeur}
    out = {}
    for code, position in index.items():
        lin = position * stride
        val = values.get(str(lin), values.get(lin))
        if val is not None:
            out[code] = (labels.get(code, code), val)
    return out


def main():
    print("→ Requête Eurostat (PIB/hab par région, 2021)...")
    r = requests.get(URL, params=PARAMS, timeout=60)
    r.raise_for_status()
    data = r.json()
    (OUT / "eurostat_pib.json").write_text(
        json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8"
    )

    tous = flatten_jsonstat(data)
    # On garde les RÉGIONS françaises = NUTS2 (code de type "FRxx", 4 caractères).
    # On exclut FR (pays, NUTS0) et FR1/FRK... (grandes zones, NUTS1) pour éviter les doublons.
    fr = {c: v for c, v in tous.items() if c.startswith("FR") and len(c) == 4}

    csv_path = OUT / "eurostat_pib_regions_fr.csv"
    with csv_path.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["code_nuts", "region", "pib_hab_eur_2021"])
        for code, (label, val) in sorted(fr.items(), key=lambda kv: -kv[1][1]):
            w.writerow([code, label, val])

    print(f"  {len(fr)} régions FR récupérées")
    top = sorted(fr.items(), key=lambda kv: -kv[1][1])[:3]
    for code, (label, val) in top:
        print(f"  {code}  {label:<28} {val:>8,} €/hab")
    print(f"  ✅ Écrit : {csv_path.relative_to(Path(__file__).parent)}")


if __name__ == "__main__":
    main()
