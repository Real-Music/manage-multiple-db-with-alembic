from datetime import datetime
from sqlalchemy import Column, Integer, DateTime, String

from app import Base_Model_Two

class Users(Base_Model_Two):
    __tablename__: str = "users"

    id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    name = Column(String(50), nullable=False)
    username = Column(String(70), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    phone = Column(String(100), unique=True, nullable=True)

    created_on = Column(DateTime, default=datetime.utcnow())
    updated_on = Column(DateTime, onupdate=datetime.utcnow())
    deleted_on = Column(DateTime, nullable=True)