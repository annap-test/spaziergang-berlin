# Spaziergang Berlin

Ein Tool für individuelle Spaziergänge durch Berlin. Das Backend sammelt Points of Interest (POIs) aus OpenStreetMap und berechnet Routen, das Frontend bietet eine einfache Streamlit-App mit Karte und Eingabefeldern.

## Struktur

```
spaziergang-berlin/
├── backend/
│   ├── data/
│   │   └── sample_pois.geojson
│   ├── router.py
│   ├── data_loader.py
│   ├── scoring.py
│   └── requirements.txt
├── frontend/
│   ├── app.py
│   ├── components/
│   └── requirements.txt
├── notebooks/
│   └── exploration.ipynb
├── .gitignore
├── README.md
└── LICENSE
```

## Installation

Empfohlen: getrennte Umgebungen für Backend und Frontend.

### Backend

1. Python-Umgebung erstellen und aktivieren, z. B. mit venv:
   - Windows: `python -m venv .venv && .venv\\Scripts\\activate`
   - macOS/Linux: `python -m venv .venv && source .venv/bin/activate`
2. Abhängigkeiten installieren: `pip install -r backend/requirements.txt`

### Frontend

1. Python-Umgebung erstellen/aktivieren (oder dieselbe, wenn gewünscht)
2. Abhängigkeiten installieren: `pip install -r frontend/requirements.txt`
3. Starten: `streamlit run frontend/app.py`

## Entwicklung: Lint/Format

- Dev-Tools installieren: `pip install -r dev-requirements.txt`
- Black manuell ausführen:
  - Windows (CMD/PowerShell): `scripts\format.bat`
  - macOS/Linux: `bash scripts/format.sh`
- Pre-commit Hooks (optional):
  - Installieren: `pre-commit install`
  - Manuell prüfen: `pre-commit run --all-files`

## Hinweise

- `backend/data_loader.py` enthält einen Stub für `fetch_pois(...)`, der später mit einer Overpass-Abfrage implementiert wird.
- `frontend/app.py` zeigt eine leere Karte mit Berlin-Ausschnitt und einfache Eingaben.
- `notebooks/exploration.ipynb` ist ein Platzhalter für erste Datenexperimente.
