import requests

url_postgres = 'http://127.0.0.1:8000/get_using_postgres/'
url_self = 'http://127.0.0.1:8000/get_using_self/'


def get_data_by_ps(latitude, longitude):
    parms = {"latitude": latitude, "longitude": longitude}
    res = requests.get(url_postgres, params=parms)
    return res.json()


def get_data_by_self(latitude, longitude):
    parms = {"latitude": latitude, "longitude": longitude}
    res = requests.get(url_self, params=parms)
    return res.json()


def sort_data(list_of_data):
    res = sorted(list_of_data, key=lambda x: x['place_name'])
    return res


def test_api_detect():
    lat = 28.6333
    long = 77.2167
    postgres = get_data_by_ps(lat, long)
    postgres = sort_data(postgres)
    self = get_data_by_self(lat, long)


