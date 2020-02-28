def get_distance_query(place_name, range_in_km):
    range_in_km = range_in_km * 1000
    return """
create extension if not exists cube;
create extension if not exists earthdistance;

select place_name, earth_distance(
  ll_to_earth(a.latitude, a.longitude),
  ll_to_earth(hr_jax.latitude, hr_jax.longitude)
) / 1000.00 as distance
from location as a,
lateral (
  select id, latitude, longitude from location where place_name = '{}'
) as hr_jax
where a.id <> hr_jax.id
and earth_distance(
  ll_to_earth(a.latitude, a.longitude),
  ll_to_earth(hr_jax.latitude, hr_jax.longitude)
) < {}
order by distance;
""".format(place_name, range_in_km)

def get_distance_by_lat_lon(latitude, longitude, range_in_km = 10):
    range_in_km = range_in_km * 1000
    return """
create extension if not exists cube;
create extension if not exists earthdistance;

select place_name,latitude, longitude, earth_distance(
  ll_to_earth(a.latitude, a.longitude),
  ll_to_earth({}, {})
) / 1000.00 as distance
from location as a
where earth_distance(
  ll_to_earth(a.latitude, a.longitude),
  ll_to_earth({}, {})
) < {}
order by distance;
  """.format(latitude, longitude, latitude, longitude, range_in_km)

