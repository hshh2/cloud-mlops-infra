from flask import Blueprint, render_template, jsonify
import random, datetime

main = Blueprint("main", __name__)

# Mock data (replace with real MLflow / Prometheus queries)
mock_runs = [
    {"model": "object_detector_v1", "accuracy": 0.91, "epoch": 50, "status": "Completed"},
    {"model": "object_detector_v2", "accuracy": 0.88, "epoch": 45, "status": "Running"},
]

@main.route("/")
def index():
    return render_template("index.html", runs=mock_runs)

@main.route("/metrics")
def metrics():
    data = {
        "gpu_usage": random.randint(20, 95),
        "cpu_usage": random.randint(10, 90),
        "timestamp": datetime.datetime.now().strftime("%H:%M:%S")
    }
    return jsonify(data)
