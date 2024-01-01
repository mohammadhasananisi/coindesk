from sqlalchemy import Column, Integer, String, DateTime, func, Time
from db.base import Base


class MobileModels(Base):
    __tablename__ = 'mobile_data'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String)
    black = Column(String)
    white = Column(String)
    pink = Column(String)
    gold = Column(String)
    silver = Column(String)


    last_update = Column(Time)
