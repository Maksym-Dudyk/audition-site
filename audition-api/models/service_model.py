from app import db, ma

class Service(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(500), nullable=False)

    def __init__(self, name, description):
        self.name = name
        self.description = description


# Service Schema
class ServiceSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'description')


# Initialize the schema
service_schema = ServiceSchema()
services_schema = ServiceSchema(many=True)