from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, FLOAT
from sqlalchemy.orm import relationship
from .db import Base


class LocationBase(Base):
    __tablename__ = 'location'
    id = Column(Integer, primary_key=True)
    key = Column('key', String(20), index=True)
    latitude = Column('latitude', FLOAT)
    longitude = Column('longitude', FLOAT)
    city = Column('admin', String(40))
    place_name = Column('place_name', String(40))
    accuracy = Column('accuracy', Integer)

class Location(LocationBase):
    distance = Column(FLOAT)


class DetectedPlace(Base):
    __tablename__ = 'geom'
    id = Column(Integer, primary_key=True)
    name = Column('name', String(20))
    city = Column('city', String(20))
    parent = Column('parent', String(20))




