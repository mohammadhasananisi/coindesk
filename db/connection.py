from sqlalchemy import create_engine, Table, MetaData
from sqlalchemy.orm import sessionmaker
from db.base import Base
from datetime import datetime

from db.crypto_models import CryptoModel
from db.mobile_models import MobileModels


class DB:
    def __init__(self):
        super(DB, self).__init__()
        self.engine = create_engine('sqlite:///my_database.db')
        Base.metadata.create_all(self.engine)  # Create all tables

        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def get_data_db(self):
        return self.session.query(CryptoModel).all()

    def set_data_db(self, **kwargs):
        d = CryptoModel(
            **kwargs,
        )
        self.session.add(d)
        self.session.commit()
        return True

    def get_mobile_data_db(self):
        return self.session.query(MobileModels).all()

    # def set_mobile_data_db(self, **kwargs):
    #     title = kwargs['title']
    #     # if name exist in db delete it
    #     self.session.query(MobileModels).filter(
    #         MobileModels.title == title).delete()

    #     d = MobileModels(
    #         **kwargs,
    #         created_at=datetime.now(),
    #     )
    #     print(datetime.now())
    #     self.session.add(d)
    #     self.session.commit()
    #     return True
