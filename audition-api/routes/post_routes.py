from flask import Blueprint, request, jsonify
from app import db
from models.post_model import Post, post_schema, posts_schema

# Initialize the posts blueprint
posts_bp = Blueprint('post', __name__, url_prefix='/post')


# Define the CRUD operations for Post
@posts_bp.route('/', methods=['POST'])
def add_post():
    text = request.json['text']
    img_link = request.json['img_link']

    post = Post(text, img_link)

    db.session.add(post)
    db.session.commit()

    return post_schema.jsonify(post)


@posts_bp.route('/', methods=['GET'])
def get_posts():
    posts = Post.query.all()
    print(posts[0].type.name)
    result = posts_schema.dump(posts)

    return jsonify(result)


@posts_bp.route('/<id>', methods=['GET'])
def get_post(id):
    post = Post.query.get(id)

    return post_schema.jsonify(post)


@posts_bp.route('/<id>', methods=['PUT'])
def update_post(id):
    post = Post.query.get(id)

    text = request.json['text']
    img_link = request.json['img_link']

    post.text = text
    post.img_link = img_link

    db.session.commit()

    return post_schema.jsonify(post)


@posts_bp.route('/<id>', methods=['DELETE'])
def delete_post(id):
    post = Post.query.get(id)

    db.session.delete(post)
    db.session.commit()

    return post_schema.jsonify(post)
