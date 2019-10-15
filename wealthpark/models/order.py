from datetime import datetime
import uuid

from sqlalchemy.ext.declarative import declared_attr, has_inherited_table

from wealthpark.models.utils import GUID
from wealthpark.models import Timestamp, Base
from wealthpark.database import db

class Order(Base, Timestamp):
    __tablename__ = 'order'
    
    id = db.Column(GUID(), primary_key=True, default=str(uuid.uuid4()))
    purchaser_id = db.Column(db.ForeignKey('purchaser.id'))
    product_id = db.Column(db.ForeignKey('product.id'))
    purchase_timestamp = db.Column(db.TIMESTAMP)

    purchaser = db.relationship("Purchaser")
    product = db.relationship("Product")

    def __init__(self, purchase_id, product_id, purchase_timestamp):
        self.purchase_timestamp = datetime.fromtimestamp(purchase_timestamp)
        self.product_id = product_id
        self.purchase_id = purchase_id
