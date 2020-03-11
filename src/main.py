from typing import List
import json
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from src import crud, model, schema
from src.db import SessionLocal, engine
from src.utils.distance import get_distance_within_km
from functools import partial

from fastapi import BackgroundTasks
from worker.celery_app import celery_app

model.Base.metadata.create_all(bind=engine)
app = FastAPI()
# Dependency


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@app.get("/get_location/", response_model=List[schema.GetLocation])
def get_location(latitude: float, longitude: float, db: Session = Depends(get_db)):
    item = crud.get_location(db, latitude, longitude)
    return item


@app.post("/post_location/")
def post_location(item: schema.LocationBase, db: Session = Depends(get_db)):
    item.pincode = "IN/" + item.pincode
    loc_by_pincode = crud.get_location_by_pincode(db, item.pincode)
    nearby_locations = crud.get_all_loc_by_latitute_longitude(db, item.latitude, item.longitude)
    # if pin code is not in db and db has no lat lot in 6 km

    if len(loc_by_pincode) == 0 and len(nearby_locations[1:]) == 0:
        data = crud.create_location(db, item)
        return data
    else:
        return {"response": "location already in database"}

"""
@app.get("/pincode/")
def get_loc_pin(pincode: str, db: Session = Depends(get_db)):
    pincode = "IN/" + pincode
    item = crud.get_location_by_pincode(db, pincode)
    return item
    
"""


@app.get("/get_using_postgres/", response_model=List[schema.GetPostgresLocation])
def get_loc_lat_long(latitude: float, longitude: float, db: Session = Depends(get_db)):
    item = crud.get_all_loc_by_latitute_longitude(db, latitude, longitude)
    return item[1:]


@app.get("/get_using_self/", response_model=List[schema.GetSelfLocation])
def get_loc_by_self(latitude: float, longitude: float, db: Session = Depends(get_db)):
    item = crud.get_all_location(db)
    res = list(filter(partial(get_distance_within_km, latitude, longitude), item))
    return res


@app.get('/detect/')
def get_detected_parent_city(latitude: float, longitude: float, db: Session = Depends(get_db)):
    try:
        item = crud.get_city_within(db, latitude, longitude)
        res = {'name': item[0], 'parent': item[1]}
        return res
    except:
        return {"response": "no place found"}





