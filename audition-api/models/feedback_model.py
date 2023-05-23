from app import db, ma

class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    content = db.Column(db.String(500), nullable=False)
    date = db.Column(db.Date(), nullable=False)

    def __init__(self, name, content, date):
        self.name = name
        self.content = content
        self.date = date

class FeedbackSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Feedback

feedback_schema = FeedbackSchema()
feedbacks_schema = FeedbackSchema(many=True)