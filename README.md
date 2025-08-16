# SIEM-Log-Monitoring

## 🔎 Overview
This project demonstrates a **mini SIEM (Security Information and Event Management)** system.  
It collects logs, parses them, correlates events, and raises alerts for suspicious activity.  
Built for **learning, portfolio showcase, and interview discussion**.

---

## ⚡ Features
- Log ingestion (system, firewall, auth logs)
- Log parsing & normalization
- Correlation engine for anomaly detection
- Alerting mechanism (console + JSON alerts)
- Mock logs included for testing
- Modular design (can integrate real-time sources later)

---

## 📂 Project Structure
- **config.json** → Global config (log paths, thresholds, alert rules)  
- **/data_ingestion/** → Collects logs  
- **/parsing/** → Parses & normalizes log lines  
- **/correlation/** → Detects suspicious patterns  
- **/alerting/** → Manages alerts  
- **/mock_logs/** → Sample logs (system, firewall, auth)  
- **/docs/** → Documentation  

---

## 🚀 Quick Start
```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Run collector → parser → correlation → alerting
python data_ingestion/log_collector.py
python parsing/log_parser.py
python correlation/correlation_engine.py
python alerting/alert_manager.py
