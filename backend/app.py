from flask import Flask, jsonify
from schema.database import *

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///takehome.db"
db.init_app(app)

with app.app_context():
    db.create_all()

from api.list_doctors import *

if __name__ == "__main__":
    app.run(debug=True, port=8000)
