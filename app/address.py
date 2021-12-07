from datetime import datetime
from sqlalchemy import Column, Integer, DateTime, String

from app import Base_Model_One

class Address(Base_Model_One):
    __tablename__: str = "address"

    id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    user_id = Column(Integer, nullable=True)
    street = Column(String(100), nullable=True)
    suite = Column(String(100), nullable=True)
    city = Column(String(150), nullable=True)
    zipcode = Column(String(150), nullable=True)

    created_on = Column(DateTime, default=datetime.utcnow())
    updated_on = Column(DateTime, onupdate=datetime.utcnow())
    deleted_on = Column(DateTime, nullable=True)