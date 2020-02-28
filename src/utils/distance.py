# Python 3 program to calculate Distance Between Two Points on Earth
from math import radians, cos, sin, asin, sqrt


def _distance(lat1, lat2, lon1, lon2):
    """calcute distance between two points"""
    # radians which converts from degrees to radians.
    lon1 = radians(lon1)
    lon2 = radians(lon2)
    lat1 = radians(lat1)
    lat2 = radians(lat2)

    # Haversine formula to calculate great circle distance
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2

    c = 2 * asin(sqrt(a))
    # Radius of earth in kilometers. Use 3956 for miles
    r = 6371

    # calculate the result
    return (c * r)


def get_distance_within_km(from_lat, from_long, location, range=5):
    if isinstance(location[1], float) and isinstance(location[2], float):
        if _distance(location[1], from_lat, location[2], from_long) < 6:
            return True
    else:
        return False

