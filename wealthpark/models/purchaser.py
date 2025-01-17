from wealthpark.models import Timestamp, Base
from wealthpark.database import db

class Purchaser(Base, Timestamp):
    __tablename__ = 'purchaser'
    __table_args__ = {'sqlite_autoincrement': True}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, unique=True)
    purchaser_id = db.relationship('Purchaser', secondary='order', backref='purchaser')

    def __init__(self, name):
        self.name = name
