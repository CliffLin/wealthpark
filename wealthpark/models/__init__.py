# pylint: disable=no-member

from wealthpark.database import db

class Base:
    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

class Timestamp(db.Model):
    __abstract__ = True

    created_at = db.Column(db.DateTime, default=db.func.now())
    updated_at = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now())
