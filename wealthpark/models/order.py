import uuid

from wealthpark.models.utils import GUID
from wealthpark.models import Timestamp, Base
from wealthpark.database import db

class Order(Base, Timestamp):
    __tablename__ = 'order'
    
    id = db.Column(GUID(), primary_key=True, default=str(uuid.uuid4()))
    purchaser_id = db.Column(GUID(), db.ForeignKey('purchaser.id'))
    product_id = db.Column(GUID(), db.ForeignKey('product.id'))

    def __init__(self, id, name, created_at):
        self.id = id
        self.name = name
        self.created_at = created_at
