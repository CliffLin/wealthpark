from wealthpark.database import db
from wealthpark.models.purchaser import Purchaser
from wealthpark.models.product import Product
from wealthpark.models.order import Order

def create_app(app):
    db.init_app(app)
    with app.app_context():
        db.create_all()
    return app
