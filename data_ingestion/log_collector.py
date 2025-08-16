import json
import pandas as pd

with open("config.json") as f:
    config = json.load(f)

def collect_logs():
    logs = {}
    for name, path in config["log_sources"].items():
        with open(path, "r") as file:
            logs[name] = file.readlines()
    return logs

if __name__ == "__main__":
    logs = collect_logs()
    for log_type, entries in logs.items():
        print(f"[INFO] Collected {len(entries)} entries from {log_type}")
 
