from sqlalchemy import Column, Integer, String, DateTime, func
from db.base import Base


class CryptoModel(Base):
    __tablename__ = 'crypto_data'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    open = Column(String)
    high = Column(String)
    low = Column(String)
    close = Column(String)
    change_percent = Column(String)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
