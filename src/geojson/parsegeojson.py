import json
import geojson
from src.geojson.savegeojsontodb import DBConnection
from src.utils.static import insert_into_geom, get_parent_city
database = "test"
user = 'postgres'
password = "daysunmon"
host = '127.0.0.1'
table_name = 'geom'
file_location = 'c:\\Users\\ani\\PycharmProjects\\test\data'


def parse_json(file_name):
    """this function take geojson file and return property and co-ordinates """
    """the return co-ordinates are polygon"""
    with open(file_name, "rt")as file:
        json_obj = json.loads(file.read())
        for feature in json_obj["features"]:
            yield json.dumps(feature['properties']), json.dumps(feature['geometry'])


db = DBConnection(database=database, user=user, host=host, password=password)
cur = db.connect()
cur.execute(get_parent_city(100, 100))
for i in cur.fetchall():
    print(i)

db.close()

