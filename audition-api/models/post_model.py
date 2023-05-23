from app import db, ma


# Define the Post model
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(500), nullable=False)
    img_link = db.Column(db.String(200), nullable=False)

    def __init__(self, text, img_link):
        self.text = text
        self.img_link = img_link


# Define the Post schema
class PostSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Post

post_schema = PostSchema()
posts_schema = PostSchema(many=True)