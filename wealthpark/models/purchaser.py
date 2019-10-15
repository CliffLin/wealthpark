import uuid

from wealthpark.models.utils import GUID
from wealthpark.models import Timestamp, Base
from wealthpark.database import db

class Purchaser(Base, Timestamp):
    __tablename__ = 'purchaser'
    
    id = db.Column(GUID(), primary_key=True, default=str(uuid.uuid4()))
    name = db.Column(db.Text, unique=True)

    def __init__(self, name):
        self.name = name
