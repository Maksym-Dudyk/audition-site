from app import db, ma
from models.user_model import UserSchema
from models.tariff_model import TariffSchema

class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    content = db.Column(db.String(500), nullable=False)
    date = db.Column(db.Date(), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship("User", backref="feedbacks")
    tariff_id = db.Column(db.Integer, db.ForeignKey('tariff.id'))
    tariff = db.relationship("Tariff", backref="feedbacks")

    def __init__(self, name, content, date, user_id):
        self.name = name
        self.content = content
        self.date = date
        self.user_id = user_id

class FeedbackSchema(ma.SQLAlchemyAutoSchema):
    user = ma.Nested(UserSchema)
    tariff = ma.Nested(TariffSchema)
    class Meta:
        model = Feedback

feedback_schema = FeedbackSchema()
feedbacks_schema = FeedbackSchema(many=True)