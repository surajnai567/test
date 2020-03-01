import psycopg2


class DBConnection:
    instance = None
    """singleton db class for db connection"""
    """call connect method to get a cursor"""
    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(DBConnection)
            return cls.instance
        return cls.instance

    def __init__(self, database, user, password, host):
        self.databse = database
        self.password = password
        self.username = user
        #self.port = port
        self.hostname = host
        self._connection = None
        self._cursor = None

    def __del__(self):
        try:
            self._cursor.close()
            self._connection.close()
        except:
            pass

    def connect(self):
        try:
            self._connection = psycopg2.\
                connect(database=self.databse, user=self.username, password=self.password, host=self.hostname)
            self._cursor = self._connection.cursor()
            return self._cursor

        except:
            pass

    def close(self):
        try:
            self._connection.commit()
            self._cursor.close()
            self._connection.close()
        except:
            pass

