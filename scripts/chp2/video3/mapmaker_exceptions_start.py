class Point():
    def __init__(self, name, latitude, longitude):
        if type(name) != str:
            raise ValueError('City name must be a string')
        self._name = name

        if not (-90 < latitude < 90) or not (-180 < longitude < 180):
            raise ValueError('latitude int should be between -90 to 90 longitude value should be between -180 to 180')
        self._latitude = latitude
        self._longitude = longitude

    def get_lat_long(self):
        return (self._latitude, self._longitude)
