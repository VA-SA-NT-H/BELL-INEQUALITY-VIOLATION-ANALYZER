"""
# BIVA – Bell Inequality Violation Analyzer

This tool simulates the E91 quantum key distribution protocol and calculates:
- CHSH (S) Value
- Quantum Bit Error Rate (QBER)
- Final Key Rate

## How to Run
```bash
pip install -r requirements.txt
streamlit run analyzer/main.py
```

## Project Structure
- `analyzer/` – Core simulation and computation logic
- `ml/` – Machine learning module (e.g. anomaly detection)
- `logs/` – Runtime logs
- `data/` – Generated CSV or JSON results
- `tests/` – Pytest-based unit tests

## Contributors
- Developed during Internship at IIST Trivandrum
"""