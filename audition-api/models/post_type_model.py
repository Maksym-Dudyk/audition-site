from app import db, ma

class PostType(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    def __init__(self, name):
        self.name = name
    

# Post Type Schema
class PostTypeSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name')


# Initialize the schema
service_schema = PostTypeSchema()
services_schema = PostTypeSchema(many=True)