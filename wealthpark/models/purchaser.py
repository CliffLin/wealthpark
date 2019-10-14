import uuid

from wealthpark.models.utils import GUID
from wealthpark.models import Timestamp
from wealthpark.database import db

class Purchaser(Timestamp):
    __tablename__ = 'purchaser'
    
    id = db.Column(GUID(), primary_key=True, default=str(uuid.uuid4()))
    name = db.Column(db.Text, unique=True)

    def __init__(self, id, name, created_at):
        self.id = id
        self.name = name
        self.created_at = created_at
