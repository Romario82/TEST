from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from data.db.connect_db import engine

Base = declarative_base()

class DBContact(Base):
    __tablename__ = 'contacts'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, index=True)
    surname = Column(String, nullable=False, index=True)
    email = Column(String, nullable=False, index=True)
    phone = Column(String, nullable=False, index=True)
    birthday = Column(String, nullable=False, index=True)
    text = Column(String, nullable=True, index=True)
    #id_user = Column(Integer, ForeignKey('users.id'))




Base.metadata.create_all(bind=engine)
