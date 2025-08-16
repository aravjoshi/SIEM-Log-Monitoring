import json
from parsing.log_parser import parse_logs
from data_ingestion.log_collector import collect_logs

with open("config.json") as f:
    config = json.load(f)

def correlate(df):
    alerts = []
    # Rule 1: Multiple failed logins
    failed = df[df["raw"].str.contains("FAILED_LOGIN|Failed password")]
    if len(failed) >= config["alert_thresholds"]["failed_logins"]:
        alerts.append("Multiple failed logins detected.")

    # Rule 2: Suspicious IP activity
    for ip in config["alert_thresholds"]["suspicious_ip"]:
        if df["raw"].str.contains(ip).any():
            alerts.append(f"Suspicious IP activity detected from {ip}.")
    return alerts

if __name__ == "__main__":
    logs = collect_logs()
    df = parse_logs(logs)
    alerts = correlate(df)
    print("[INFO] Correlation Results:", alerts)
