from sqlalchemy import Column, Integer, String, TIMESTAMP, Float
from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base

from cfg import DB_CONNSTR

# from constants import DEFAULT_CONNSTR

engine = create_engine(DB_CONNSTR)
meta = MetaData(engine)
Base = declarative_base(metadata=meta)


class Analytics(Base):
    __tablename__ = "analytics"
    id = Column(Integer, autoincrement=True, primary_key=True)
    date = Column(TIMESTAMP, nullable=False)
    channel = Column(String, nullable=False)
    country = Column(String, nullable=False)
    os = Column(String, nullable=False)
    impressions = Column(Integer, nullable=False)
    clicks = Column(Integer, nullable=False)
    installs = Column(Integer, nullable=False)
    spend = Column(Float, nullable=False)
    revenue = Column(Float, nullable=False)
