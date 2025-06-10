# BIVA – Bell Inequality Violation Analyzer

This tool simulates the E91 quantum key distribution protocol and calculates:
- CHSH (S) Value
- Quantum Bit Error Rate (QBER)
- Final Key Rate

## Objective of this project
The objective of the Bell Inequality Violation Analyzer (BIVA) project is to simulate and analyze quantum entanglement using Bell’s inequality tests, particularly the CHSH inequality, to verify violations predicted by quantum mechanics.
This tool aims to:
- Generate entangled quantum states.
- Perform measurements at varying angles (user-defined).
- Compute the CHSH S-value to test for Bell inequality violation.
- Calculate Quantum Bit Error Rate (QBER) and key generation rate.
- Visualize the raw quantum measurement results.
- Identify potential anomalies in entanglement-based Quantum Key Distribution (QKD) through interactive charts and metrics.

## Features
- Quantum circuit simulation using Qiskit Aer
- Interactive Streamlit UI
- Custom basis angle input for Alice and Bob
- Real-time CHSH S-value, QBER, and Key Rate metrics
- Visual comparison of raw bits
- Anomaly detection using ML (coming soon)
- Key saving and result exporting

## How to Run
```bash
pip install -r requirements.txt
streamlit run main.py
```
## Sample output

![Screenshot from 2025-06-10 22-25-38](https://github.com/user-attachments/assets/b4c7fa9d-2739-40e3-a38b-e5f6f21e047c)
![Screenshot from 2025-06-10 22-26-36](https://github.com/user-attachments/assets/ee259474-8557-4414-b58d-c1765608b813)
![Screenshot from 2025-06-10 22-26-57](https://github.com/user-attachments/assets/a914bb4a-9f63-444b-9465-aa70e3b4871b)
![Screenshot from 2025-06-10 22-27-16](https://github.com/user-attachments/assets/707bc3bf-c0e4-4fa7-a6e1-d2d257463cd9)
![Screenshot from 2025-06-10 22-27-36](https://github.com/user-attachments/assets/fcc169dc-e25d-4e6f-b424-b735df718d22)
![Screenshot from 2025-06-10 22-27-59](https://github.com/user-attachments/assets/a0ba850d-699c-4f97-9110-aba331478196)

## Contributors
- Developed during Internship at IIST Trivandrum
