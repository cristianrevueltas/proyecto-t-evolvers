import json
import random
import requests
import uuid
from datetime import datetime

from apscheduler.schedulers.background import BackgroundScheduler
from flask import Flask

MIN = 10
MAX = 100
LIST = ["kwh", "temp"]
URL_CONSUMER = "http://consumer:8081"


def sensor():
    data = []
    number = random.randint(MIN, MAX)
    for i in range(number):
        item = random.choice(LIST)
        data.append({
            'id': str(uuid.uuid4()),
            'metric': str(i) + " " + item,
            'created_at': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        })
    print("sending request to:", URL_CONSUMER)
    response = requests.post(URL_CONSUMER, json=json.dumps(data))
    print("response with status code:", response.status_code)


schedule = BackgroundScheduler(daemon=True)
schedule.add_job(func=sensor, trigger='interval', seconds=5)
schedule.start()

app = Flask(__name__)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
