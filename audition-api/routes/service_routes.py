from flask import Blueprint, request
from app import db
from models.service_model import Service, service_schema, services_schema

# Initialize the posts blueprint
services_bp = Blueprint('services', __name__, url_prefix='/service')

# Create a new service
@services_bp.route('/', methods=['POST'])
def add_service():
    name = request.json['name']
    description = request.json['description']

    new_service = Service(name, description)

    db.session.add(new_service)
    db.session.commit()

    return service_schema.jsonify(new_service)


# Get all services
@services_bp.route('/', methods=['GET'])
def get_services():
    services = Service.query.all()
    return services_schema.jsonify(services)


# Get a single service
@services_bp.route('/<id>', methods=['GET'])
def get_service(id):
    service = Service.query.get(id)

    return service_schema.jsonify(service)


# Update a service
@services_bp.route('/<id>', methods=['PUT'])
def update_service(id):
    service = Service.query.get(id)

    name = request.json['name']
    description = request.json['description']

    service.name = name
    service.description = description

    db.session.commit()

    return service_schema.jsonify(service)


# Delete a service
@services_bp.route('/<id>', methods=['DELETE'])
def delete_service(id):
    service = Service.query.get(id)

    db.session.delete(service)
    db.session.commit()

    return service_schema.jsonify(service)