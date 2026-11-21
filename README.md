# RouteSafe

University of Jeddah senior project prototype. Python 3.12, Windows PowerShell commands below.

```powershell
python -m venv .venv
.\.venv\Scripts\python -m pip install -r requirements.txt
.\.venv\Scripts\python -m services.risk_model "$env:USERPROFILE\Downloads\DataCoSupplyChainDataset.csv"
.\.venv\Scripts\python -m pytest -q | Tee-Object evidence/test_results.txt
.\.venv\Scripts\python -m scripts.generate_charts
.\.venv\Scripts\python -m streamlit run app/dashboard.py
```

The dispatch board automatically loads the synthetic 23 November 2026 seed. Training uses only five shared pre-dispatch columns and a grouped chronological holdout. Comparison results therefore belong to this run, not the older notebooks. Risk tiers use demo thresholds of 0.33 and 0.66. Scores are not calibrated for a courier in Jeddah. Load only trusted local model artifacts.

Route optimization enumerates each driver's stop permutations and checks shift end, missed promises, late minutes, preferred-window conflicts and driving time in that order. Delivery ETA is service start after waiting for the preferred window. The map connects simulated stops with straight lines. Travel estimates use great-circle distance multiplied by 1.35 and 30 km/h.

The default app is a local, single-supervisor demo. Its built-in courier batch is loaded server-side. The execution screen records observed visits in the local evidence directory. This repository includes the synthetic batch and historical experiment summaries in the report. Historical source datasets stay outside the package. Amazon and historical route experiments remain independent of the DataCo shipment model.

## Repository layout

- app/ — Streamlit dispatch interface
- services/ — risk training, explanations, and route planning
- data/demo/ — synthetic Jeddah dispatch batch
- artifacts/ — trained models and evaluation metrics
- tests/ — automated verification
- scripts/ — chart generation
- assets/ — publication figures
- evidence/ — test output and screenshots

With the virtual environment active, install using `pip install -r requirements.txt` and launch with `streamlit run app/dashboard.py`.
