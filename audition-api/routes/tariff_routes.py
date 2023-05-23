from flask import Blueprint, jsonify, request
from app import db
from models.tariff_model import Tariff, tariff_schema, tariffs_schema

tariff_bp = Blueprint('tariff', __name__, url_prefix="/tariff")

# Create a new tariff
@tariff_bp.route('/', methods=['POST'])
def create_tariff():
    name = request.json['name']
    description = request.json['description']
    price = request.json['price']

    new_tariff = Tariff(name, description, price)

    db.session.add(new_tariff)
    db.session.commit()

    return tariff_schema.jsonify(new_tariff)

# Retrieve all tariff
@tariff_bp.route('/', methods=['GET'])
def get_tariffs():
    print("lol")
    all_tariffs = Tariff.query.all()
    result = tariffs_schema.dump(all_tariffs)
    return jsonify(result)

# Retrieve a single tariff
@tariff_bp.route('/<id>', methods=['GET'])
def get_tariff(id):
    tariff = Tariff.query.get(id)
    return tariff_schema.jsonify(tariff)

# Update a tariff
@tariff_bp.route('/<id>', methods=['PUT'])
def update_tariff(id):
    tariff = Tariff.query.get(id)

    name = request.json['name']
    description = request.json['description']
    price = request.json['price']

    tariff.name = name
    tariff.description = description
    tariff.price = price

    db.session.commit()

    return tariff_schema.jsonify(tariff)

# Delete a tariff
@tariff_bp.route('/<id>', methods=['DELETE'])
def delete_tariff(id):
    tariff = Tariff.query.get(id)

    db.session.delete(tariff)
    db.session.commit()

    return tariff_schema.jsonify(tariff)
