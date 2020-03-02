# project structure
 ### src
 * geojson
    * this module contain all the logic for geojson parsing and loading it into 
    db
 * pytest this module contain all the test logic for testing all end points.
 
 * utils all the utilities functions
    * distance.py module contain self implemented distance 
    formula.
    * static.py module contain all the static sql statement.
 
 * crud.py module deal with all database read and create operations
 * db.py this module deals with database connection
 * model.py contains all the orm models
 * schema.py contains all the schema for data validation
 * main.py contains main function
 # ##################################################################
 #### table structure for geojson data is
 id int| property jsonb | coordinate geometry
 
 # ##############################################################
 
 ### api end-points
 * /get_location/ args: float, float Return: list of locations
 ![img](getlog.jpg)
 
 * /post_location/ args:pin,city,address,lat,longitude
 
 * /get_using_postgres/ args:float, float Return: List of location
    * it fetch all location with in 5 km
    
 * /get_using_self/ args: float, float Return: list of location
    * default range is 5 it can be change by changing the 
    get_distance_within_km() default range argument 
    * this function is slower than get_using_postgres because it is depend
    on python object comparision (first it fetch all record then use comparision)
    
  * /detect/ args: float, float return: place_name and area in which the place falls.