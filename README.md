# Predictive Maintenance for IoT-based Public Buses using Unsupervised Clustering

This repository contains the implementation of the methodology presented in papers [1], [2]:

---

## 📘 Overview

This project implements a predictive maintenance framework that leverages synthetic time-series sensor data and unsupervised learning techniques (K-Means with Euclidean and Dynamic Time Warping metrics) to detect gradual faults in subsystems of IoT-enabled public buses.

The approach includes:
- Synthetic data generation using deep learning and statistical modeling
- Manual injection of temporal trends and degradation patterns
- Clustering-based gradual fault detection on cooling and engine torque systems

---
## Repository Structure:
```
Predictive-Maintenance/  
├── data/                          # Zipped synthetic datasets  
│   ├── Final_cooling_sys_data.zip  
│   ├── Final_engine_sys_data.zip  
│   └── cool_tests.zip  
│  
├── src/                            # Source code and notebooks  
│   ├── cooling/                    # Cooling system clustering and synthetic data generation 
│   ├── engine/                     # Engine system clustering and synthetic data generation
│   ├── GAN_LSTM_generator.ipynb    # GAN-LSTM synthetic data generator  
│   └── validating_synthetic_data.ipynb  # Synthetic vs real data comparison  
│  
├── .gitattributes  
├── .gitignore  
├── LICENSE  
└── README.md  
```
---
## Installation

Create a virtual environment and install dependencies using:

```bash
pip install -r requirements.txt
```
---
## Notes

- The code has been modified to **omit real-world data** for privacy reasons.
- You may need to **update paths** in the scripts depending on your environment.
---
  
## References:

[1]	Vira, G., Killeen, P., Yeap, T., and Kiringa, I. Predictive Maintenance by Detection of Gradual Faults in an IoT-Enabled Public Bus. 2024. IEEE Canadian Conference on Electrical and Computer Engineering.  
[2]	Vira, G., Yeap, T., Kiringa, I. Predictive Maintenance by the Unsupervised Clustering of Gradual Faults in a fleet of IoT-based Public Buses. 2025. ACM Transactions on Sensor Networks.

