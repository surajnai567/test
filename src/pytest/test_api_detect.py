import requests
import csv

url = 'http://127.0.0.1:8000/detect/'
test_file_name = 'detect.csv'


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
                yield line[0], line[1], float(line[2]), float(line[3])
            except:
                continue


def get_data_from_detect_api(url, latitude, longitude):
    """get data from /detect endpoint and return response"""
    param = {"latitude": latitude, "longitude": longitude}
    res = requests.get(url, params=param)
    return res.json()


def test_detect():
    for name, parent, lat, long in get_data_for_check(filename=test_file_name):
        res = get_data_from_detect_api(url, lat, long)
        assert res['name'] == name
        assert res['parent'] == parent
