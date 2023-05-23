from flask import Flask
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import json
 
app = Flask(__name__)
cors = CORS(app)

with open("secret.json") as data:
    SECRET = json.load(data)

DB_URI = "mysql+mysqlconnector://{user}:{password}@{host}:{port}/{db}".format(
    user=SECRET["user"],
    host=SECRET["host"],
    password=SECRET["password"],
    port=SECRET["port"],
    db=SECRET["db"]
)


app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


@app.after_request
@app.route("/", methods=["OPTIONS"])
def after_request(response):
    header = response.headers
    header['Access-Control-Allow-Origin'] = '*'
    return response

db = SQLAlchemy(app)
ma = Marshmallow(app)