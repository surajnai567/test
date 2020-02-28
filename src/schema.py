from typing import List
from pydantic import BaseModel, Field


class LocationBase(BaseModel):
    pincode: str
    latitude: float
    longitude: float
    accuracy: int
    city: str
    address: str


class Location(LocationBase):
    id: int

    class Config:
        orm_mode = True


class LocationCreate(LocationBase):
    pass


class GetLocation(BaseModel):
    place_name: str
    city: str
    key: str

    class Config:
        orm_mode = True


class GetPostgresLocation(BaseModel):
    place_name: str
    latitude: str
    longitude: str
    distance: float

    class Config:
        orm_mode = True