from flask import Blueprint, request, jsonify
from models.feedback_model import Feedback, feedback_schema, feedbacks_schema
from app import db

feedback_bp = Blueprint('feedback', __name__, url_prefix='/feedback')

# Create feedback
@feedback_bp.route('/', methods=['POST'])
def create_feedback():
    name = request.json['name']
    content = request.json['content']
    date = request.json['date']
    new_feedback = Feedback(name, content, date)
    db.session.add(new_feedback)
    db.session.commit()
    return feedback_schema.jsonify(new_feedback)

# Get all feedbacks
@feedback_bp.route('/', methods=['GET'])
def get_all_feedbacks():
    all_feedbacks = Feedback.query.all()
    result = feedbacks_schema.dump(all_feedbacks)
    return jsonify(result)

# Get a single feedback
@feedback_bp.route('/<id>', methods=['GET'])
def get_feedback(id):
    feedback = Feedback.query.get(id)
    return feedback_schema.jsonify(feedback)

# Update a feedback
@feedback_bp.route('/<id>', methods=['PUT'])
def update_feedback(id):
    feedback = Feedback.query.get(id)
    name = request.json['name']
    content = request.json['content']
    date = request.json['date']
    feedback.name = name
    feedback.content = content
    feedback.date = date
    db.session.commit()
    return feedback_schema.jsonify(feedback)

# Delete a feedback
@feedback_bp.route('/<id>', methods=['DELETE'])
def delete_feedback(id):
    feedback = Feedback.query.get(id)
    db.session.delete(feedback)
    db.session.commit()
    return feedback_schema.jsonify(feedback)
