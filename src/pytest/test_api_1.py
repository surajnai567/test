import requests
import csv

url = 'http://127.0.0.1:8000/get_location/'
file_path = "C:\\Users\\ani\\Desktop\\india.csv"


def get_data_for_check(filename):
    """get data from csv file for comparison"""
    is_col = True
    with open(filename) as f:
        csv_read = csv.reader(f)
        for line in csv_read:
            if is_col:
                is_col = False
                continue
            try:
                yield line[1], line[2], float(line[3]), float(line[4])
            except:
                continue


def get_param(latitude, longitude):
    return {"latitude": latitude, "longitude": longitude}


def test_get_location():
    """test function for testing get_location end points"""
    for place, admin, lat, lon in get_data_for_check(file_path):
        response = requests.get(url, params=get_param(lat, lon))
        assert response.json()[0]['place_name'] == place
        assert response.json()[0]['admin'] == admin


