import json
import requests

from flask import Flask, request
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from apscheduler.schedulers.background import BackgroundScheduler

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password@mysql-consumer:3306/db-consumer'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

URL_REGISTER = "http://register:8082"


class Metric(db.Model):
    __tablename__ = 'metrics'
    id = db.Column('id', db.String(250), primary_key=True)
    metric = db.Column(db.String(100))
    created_at = db.Column(db.String(50))


@app.route("/", methods=['POST'])
def index():
    body = request.json
    response = json.loads(body)
    data = []
    for i in range(len(response)):
        data.append(Metric(id=response[i]['id'], metric=response[i]['metric'], created_at=response[i]['created_at']))
    db.session.bulk_save_objects(data)
    db.session.commit()
    return "ok", 200


def register():
    metrics = Metric.query.order_by(Metric.created_at).limit(1).all()
    data = []
    for item in metrics:
        data.append({
            'id': item.id,
            'metric': item.metric,
            'created_at': item.created_at,
        })
        Metric.query.filter_by(id=item.id).delete()

    print("sending request to: ", URL_REGISTER)
    response = requests.post(URL_REGISTER, json=json.dumps(data))
    print("response with status code:", response.status_code)


schedule = BackgroundScheduler(daemon=True)
schedule.add_job(id='Scheduled Task', func=register, trigger='interval', seconds=5)
schedule.start()

if __name__ == "__main__":
    db.create_all()
    app.run(host='0.0.0.0', port=8081, debug=True)
