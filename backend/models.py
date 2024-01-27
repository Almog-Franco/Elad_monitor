from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from database import Base


class Diapers(Base):
   __tablename__ = 'diapers'

   id = Column(Integer, primary_key=True, index=True)
   date = Column(String,index=True)
   time = Column(String, index=True)
   content = Column(String, index=True)


class Feeding(Base):
    __tablename__ = 'feeding'

    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Integer, index=True)
    date = Column(String, index=True)
    time = Column(String, index=True)
    type = Column(String, index=True)


class Tasks(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    is_finished = Column(Boolean, index=True)
