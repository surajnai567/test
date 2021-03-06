from sqlalchemy.orm import Session
from src import model, schema
from sqlalchemy import text
from src.utils import static
from worker.celery_worker import add_location_to_db


def create_location(db: Session, data: schema.LocationBase):
    #new_loc = model.LocationBase(key=data.pincode, latitude=data.latitude, longitude=data.longitude,
                             #accuracy=0, city=data.city, place_name=data.address)
    #db.add(new_loc)
    #db.commit()
    #db.refresh(new_loc)
    a = data.json()
    add_location_to_db.delay(data.json())

    return {"message": "added data successful"}


def get_location(db: Session, latitude: float, longitude: float):
    return db.query(model.Location.place_name, model.Location.city, model.Location.key)\
        .filter(model.Location.latitude == latitude).\
        filter(model.Location.longitude == longitude).all()


def get_location_by_pincode(db: Session, pin_code: str):
    return db.query(model.Location.place_name, model.Location.latitude, model.Location.longitude)\
        .filter(model.Location.key == pin_code).all()


def get_all_nearby_location_by_place(db: Session, place_name=str, range=5):
    loc = db.query(model.Location.place_name, model.Location.distance)\
        .from_statement(text(static.get_distance_query(place_name, range))).all()
    return loc


def get_all_loc_by_latitute_longitude(db: Session, latitude, longitude):
    locations = db.query(model.Location.place_name, model.Location.latitude,
                         model.Location.longitude, model.Location.distance)\
        .from_statement(text(static.get_distance_by_lat_lon(latitude, longitude))).all()
    return locations


def _get_all_loc_by_latitute_longitude(db: Session, latitude, longitude):
    locations = db.query(model.Location.place_name, model.Location.latitude,
                         model.Location.longitude, model.Location.distance)\
        .from_statement(text(static.get_distance_by_lat_lon(latitude, longitude))).one()
    return locations


def get_all_location(db: Session):
    data = db.query(model.LocationBase.place_name, model.LocationBase.latitude,
                    model.LocationBase.longitude).all()
    return data


def get_city_within(db: Session, latitude, longitude):
    loc = db.query(model.DetectedPlace.name, model.DetectedPlace.parent)\
        .from_statement(text(static.get_parent_city(latitude, longitude))).one()
    return loc


