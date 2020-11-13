from app.models import db
from sqlalchemy.schema import Column
from sqlalchemy.types import Integer, String


class Package(db.Model):
    __tablename__ = 'packages'

    id = Column(Integer, primary_key=True)
    sender = Column(String(255))
    recipient = Column(String(255))
    origin = Column(String(255))
    destination = Column(String(255))
    location = Column(String(255))
