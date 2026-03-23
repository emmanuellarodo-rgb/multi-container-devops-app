import random
import time
import json
from logger import log

def generate_metrics():
    while True:
        cpu = random.randint(10, 100)

        data = {
            "cpu": cpu,
            "timestamp": time.time()
        }

        with open("metrics.json", "w") as f:
            json.dump(data, f)

        log(f"Generated CPU usage: {cpu}%")

        time.sleep(3)
