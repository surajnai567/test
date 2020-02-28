from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from src import crud, model, schema
from src.db import SessionLocal, engine

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
    items = crud.get_location_by_pincode(db, item.pincode)
    # if pin code is not in db and min distance is 5
    if len(items) == 0:
        # add data to dbms
        return item
    return {"response": "location already exist"}

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
