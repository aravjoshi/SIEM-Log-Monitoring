import pandas as pd
from data_ingestion.log_collector import collect_logs

def parse_logs(logs):
    parsed = []
    for log_type, entries in logs.items():
        for line in entries:
            parsed.append({"type": log_type, "raw": line.strip()})
    return pd.DataFrame(parsed)

if __name__ == "__main__":
    logs = collect_logs()
    df = parse_logs(logs)
    print("[INFO] Parsed Logs Preview:")
    print(df.head())
