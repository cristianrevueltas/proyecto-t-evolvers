import json

from flask import Flask, request
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password@mysql-register:3306/db-register'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)


class Register(db.Model):
    __tablename__ = 'registers'
    id = db.Column('id', db.String(250), primary_key=True)
    metric = db.Column(db.String(100))
    created_at = db.Column(db.String(50))


@app.route("/", methods=['POST'])
def index():
    body = request.json
    response = json.loads(body)
    data = []
    for i in range(len(response)):
        data.append(Register(id=response[i]['id'], metric=response[i]['metric'], created_at=response[i]['created_at']))
    db.session.bulk_save_objects(data)
    db.session.commit()
    return "ok", 200


if __name__ == "__main__":
    db.create_all()
    app.app_context()
    app.run(host='0.0.0.0', port=8082, debug=True)
