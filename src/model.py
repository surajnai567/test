from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, FLOAT
from sqlalchemy.orm import relationship
from .db import Base


class Location(Base):
    __tablename__ = 'location'
    id = Column(Integer, primary_key=True)
    key = Column('key', String(20), index=True)
    latitude = Column('latitude', FLOAT)
    longitude = Column('longitude', FLOAT)
    city = Column('admin', String(40))
    place_name = Column('place_name', String(40))
    accuracy = Column('accuracy', Integer)
    distance = Column(FLOAT)



