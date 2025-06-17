import psutil
import time
import requests
from datetime import datetime
import argparse

BACKEND_URL = "http://localhost:8080/api/metrics/saveMetric"



def send_cpu_metric():
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent
    
    payload_cpu = {
        "metricType": "CPU",
        "value": cpu,
        "unit": "%",
        "timestamp": datetime.now().isoformat(),
        "serverId": SERVER_ID,
        "source": SOURCE
    }
    
    payload_memory = {
        "metricType": "MEMORY",
        "value": memory,
        "unit": "%",
        "timestamp": datetime.now().isoformat(),
        "serverId": SERVER_ID,
        "source": SOURCE
    }
    
    payload_disk = {
        "metricType": "DISK_USAGE",
        "value": disk,
        "unit": "%",
        "timestamp": datetime.now().isoformat(),
        "serverId": SERVER_ID,
        "source": SOURCE
    }

    try:
        response_cpu = requests.post(BACKEND_URL, json=payload_cpu)
        response_memory = requests.post(BACKEND_URL, json=payload_memory)
        response_disk = requests.post(BACKEND_URL, json=payload_disk)

        if response_cpu.status_code == 200 and response_memory.status_code == 200 and response_disk.status_code==200:
            print(f"✅ Sent CPU metric: {cpu}%")
            print(f"✅ Sent MEMORY metric: {memory}%")
            print(f"✅ Sent DISK metric: {disk}%")
        else:
            print(f"❌ Failed to send metric: {response_cpu.status_code} - {response_cpu.text}")
    except Exception as e:
        print(f"🚨 Error sending metric: {e}")

def collect_and_send():
    while True:
        send_cpu_metric()
        time.sleep(10)
        
parser = argparse.ArgumentParser(description="InfraWatch Metric Agent")
parser.add_argument('--serverId', type=int, required=True, help='ID of the server')
parser.add_argument('--source', type=str, required=True, help='Name of the source agent')

args = parser.parse_args()
SERVER_ID = args.serverId
SOURCE = args.source


if __name__ == "__main__":
    collect_and_send()
