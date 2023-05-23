from app import db, app
from routes.feedback_routes import feedback_bp
from routes.post_routes import posts_bp
from routes.service_routes import services_bp
from routes.tariff_routes import tariff_bp

app.register_blueprint(feedback_bp)
app.register_blueprint(posts_bp)
app.register_blueprint(services_bp)
app.register_blueprint(tariff_bp)


with app.app_context():
    db.create_all()
app.run()
