# poject structure
* src
  * utils
    * distance.py 'this contains self implement 
    distance logic in python'
    * static 'this files contain static sql etc'
    
  * crud.py this module contain all the operation related to
  create update database
  
  * db.py this module deal with database connection
  * main.py main app
  * model.py contain all the orm models
  schema.py contain all the files related to validation
  
  # ###########################################
  ### The api end-points are
  * get_location args:float, float Return: list
  * post_location args: lat, long, place, city, pin
  * get_using_postgres: args:float float Return: list
    * it return location within 5 km range  
  * get_using_self: args: float, float Return: list 
  this is the python implementation
    * return location within 5 km range
        * default value can be changed by changing default argument
        of get_distance_within_km()
  
  
  