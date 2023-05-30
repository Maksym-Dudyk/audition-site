from app import db, ma
from models.post_type_model import PostTypeSchema

# Define the Post model
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(500), nullable=False)
    img_link = db.Column(db.String(200), nullable=False)
    type_id = db.Column(db.Integer, db.ForeignKey('post_type.id'))
    type = db.relationship("PostType", backref="posts")

    def __init__(self, text, img_link):
        self.text = text
        self.img_link = img_link


# Define the Post schema
class PostSchema(ma.SQLAlchemyAutoSchema):
    type = ma.Nested(PostTypeSchema)
    class Meta:
        model = Post

post_schema = PostSchema()
posts_schema = PostSchema(many=True)