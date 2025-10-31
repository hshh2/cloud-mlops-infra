from prometheus_client import start_http_server, Gauge
import random, time

gpu_usage = Gauge('gpu_usage', 'Current GPU usage percentage')
training_jobs = Gauge('training_jobs_active', 'Number of active training jobs')

if __name__ == "__main__":
    start_http_server(8000)
    while True:
        gpu_usage.set(random.uniform(20, 90))
        training_jobs.set(random.randint(0, 5))
        time.sleep(5)
