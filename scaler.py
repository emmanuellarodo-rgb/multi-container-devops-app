import json
from logger import log

def check_scale():
    try:
        with open("metrics.json") as f:
            data = json.load(f)

        cpu = data["cpu"]

        if cpu > 75:
            decision = "SCALE UP 🚀"
        elif cpu < 25:
            decision = "SCALE DOWN ⬇️"
        else:
            decision = "STABLE ✅"

        log(f"Scaling decision: {decision}")
        return decision

    except:
        return "NO DATA"
