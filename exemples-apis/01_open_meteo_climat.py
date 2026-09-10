"""
01 — Météo / climat via Open-Meteo (JSON ou CSV, SANS clé d'API)
----------------------------------------------------------------
Source : https://open-meteo.com/en/docs/historical-weather-api
Idée    : récupérer la température moyenne journalière sur 20 ans pour un point
          (ex. Paris) -> parfait pour une thématique "tendance climatique".

Ce que montre l'exemple :
  - construire une requête avec des paramètres (latitude, longitude, dates...)
  - lire une réponse JSON
  - la transformer en CSV exploitable (une ligne par jour)
"""
import csv
import json
from pathlib import Path

import requests

OUT = Path(__file__).parent / "data"
OUT.mkdir(exist_ok=True)

URL = "https://archive-api.open-meteo.com/v1/archive"
PARAMS = {
    "latitude": 48.85,          # Paris
    "longitude": 2.35,
    "start_date": "2004-01-01",
    "end_date": "2024-12-31",
    "daily": "temperature_2m_mean",
    "timezone": "Europe/Paris",
}


def main():
    print("→ Requête Open-Meteo (historique 2004-2024, Paris)...")
    r = requests.get(URL, params=PARAMS, timeout=60)
    r.raise_for_status()
    data = r.json()

    # Sauvegarde du JSON brut (utile pour inspecter la structure)
    (OUT / "open_meteo.json").write_text(
        json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8"
    )

    jours = data["daily"]["time"]
    temps = data["daily"]["temperature_2m_mean"]

    # Écriture d'un CSV : date ; temperature_moyenne
    csv_path = OUT / "open_meteo_paris.csv"
    with csv_path.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["date", "temperature_moyenne_c"])
        w.writerows(zip(jours, temps))

    # Petit résumé : moyenne annuelle sur les 3 premières et 3 dernières années
    print(f"  {len(jours)} jours récupérés ({jours[0]} → {jours[-1]})")
    print(f"  Exemple : {jours[0]} = {temps[0]} °C")
    print(f"  ✅ Écrit : {csv_path.relative_to(Path(__file__).parent)}")


if __name__ == "__main__":
    main()
