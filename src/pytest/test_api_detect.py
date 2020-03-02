import requests

url = 'http://127.0.0.1:8000/detect/'


def get_data_from_url(url, latitude, longitude):
    """get data from /detect endpoint and return response"""
    param = {"latitude": latitude, "longitude": longitude}
    res = requests.get(url, params=param)
    return res.text

print(get_data_from_url(url, 100,200))