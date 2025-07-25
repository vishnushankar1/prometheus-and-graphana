from flask import Flask, jsonify
import random
import time

app=Flask(__name__)
total_requests=0

@app.route("/metrics",methods=['Get'])
def metrics():
    global total_requests
    total_requests+=1

    request_processing_latency=round(random.uniform(0.1,1.5),3)
    model_prediction_success_rate=round(random.uniform(80,100),2)

    # Return the metrics in Prometheus format
    prometheus_metrics = (
        f"# HELP total_api_requests_total Total number of API requests\n"
        f"# TYPE total_api_requests_total counter\n"
        f"total_api_requests_total {total_requests}\n"
        f"\n"
        f"# HELP request_processing_latency_seconds Latency for request processing\n"
        f"# TYPE request_processing_latency_seconds gauge\n"
        f"request_processing_latency_seconds {request_processing_latency}\n"
        f"\n"
        f"# HELP model_prediction_success_rate Model prediction success rate\n"
        f"# TYPE model_prediction_success_rate gauge\n"
        f"model_prediction_success_rate {model_prediction_success_rate}\n"
    )

    return prometheus_metrics, 200, {"Content-Type": "text/plain; charset=utf-8"}

@app.route('/',methods=['Get'])
def index():
    return jsonify({"message":"welcome to the flask metrics app! Acess metrics for prometheus metrics"})



if __name__=="__main__":
    app.run(host="0.0.0.0", port=5000)