from flask import Flask, jsonify
from flask_cors import CORS
import threading
import json
from monitor import generate_metrics
from scaler import check_scale

app = Flask(__name__)
CORS(app)

# Start background monitoring
threading.Thread(target=generate_metrics, daemon=True).start()

@app.route("/")
def home():
    return jsonify({"status": "Backend running 🚀"})

@app.route("/metrics")
def metrics():
    try:
        with open("metrics.json") as f:
            data = json.load(f)
        return jsonify(data)
    except:
        return jsonify({"error": "No data"})

@app.route("/scale")
def scale():
    decision = check_scale()
    return jsonify({"decision": decision})

@app.route("/health")
def health():
    return jsonify({"status": "healthy"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
