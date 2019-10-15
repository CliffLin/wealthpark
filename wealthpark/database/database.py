from wealthpark.database import db

def create_app(app):
    db.init_app(app)
    with app.app_context():
        db.create_all()
    return app
