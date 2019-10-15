from wealthpark.models import Timestamp, Base
from wealthpark.database import db

class Product(Base, Timestamp):
    __tablename__ = 'product'
    __table_args__ = {'sqlite_autoincrement': True}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, unique=True)

    def __init__(self, name):
        self.name = name
