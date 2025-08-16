import json
from correlation.correlation_engine import correlate
from parsing.log_parser import parse_logs
from data_ingestion.log_collector import collect_logs

with open("config.json") as f:
    config = json.load(f)

def send_alerts(alerts):
    with open(config["output"]["alerts"], "w") as f:
        json.dump(alerts, f, indent=4)
    for alert in alerts:
        print(f"[ALERT] {alert}")

if __name__ == "__main__":
    logs = collect_logs()
    df = parse_logs(logs)
    alerts = correlate(df)
    send_alerts(alerts)
