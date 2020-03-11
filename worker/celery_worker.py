from time import sleep
from celery import current_task
from .celery_app import celery_app
from src.model import LocationBase
from src.db import SessionLocal
from src import schema


@celery_app.task
def add_location_to_db(data):
    data = schema.LocationBase.parse_obj(data)
    db = SessionLocal()
    new_loc = LocationBase(key=data.pincode, latitude=data.latitude, longitude=data.longitude,
                             accuracy=0, city=data.city, place_name=data.address)
    db.add(new_loc)
    db.commit()
    db.refresh(new_loc)
    print("data added successfully")




