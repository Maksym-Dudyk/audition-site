from app import db, ma

class Tariff(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    price = db.Column(db.Float(), nullable=False)

    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price

class TariffSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Tariff
        
tariff_schema = TariffSchema()
tariffs_schema = TariffSchema(many=True)