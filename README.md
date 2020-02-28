# project structure
 ### src
 * utils all the utilities functions
    * distance.py module contain self implemented distance 
    formula
    * static.py module contain all the static sql statement
 
 * crud.py module deal with all database read and create operations
 * db.py this module deals with database connection
 * model.py contains all the orm models
 * schema.py contains all the schema for data validation
 * main.py contains main function
 
 # ##############################################################
 
 ### api end-point
 * get_location args: float, float Return: list of locations
 * post_location args:pin,city,address,lat,longitude
 * get_using_postgres args:float, float Return: List of location
 * get_using_self args: float, float Return: list of location
    * default range is 5 it can be change by changing the 
    get_distance_within_km() default range argument 