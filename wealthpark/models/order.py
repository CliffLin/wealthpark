from datetime import datetime


from wealthpark.models import Timestamp, Base
from wealthpark.database import db

class Order(Base, Timestamp):
    __tablename__ = 'order'
    __table_args__ = {'sqlite_autoincrement': True}

    id = db.Column(db.Integer, primary_key=True)
    purchaser_id = db.Column(db.ForeignKey('purchaser.id'))
    product_id = db.Column(db.ForeignKey('product.id'))
    purchase_timestamp = db.Column(db.TIMESTAMP)

    purchaser = db.relationship('Purchaser')
    product = db.relationship('Product')

    def __init__(self, purchaser_id, product_id, purchase_timestamp):
        self.purchase_timestamp = datetime.fromtimestamp(purchase_timestamp)
        self.product_id = product_id
        self.purchaser_id = purchaser_id
