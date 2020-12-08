class Point():
    store_points = []
    def __init__(self, name, latitude, longtitude):

        if not isinstance(name, str):
            raise ValueError('Invalid name type, Should be string')
        self._name = name

        if not (-90 <= latitude <= 90) or not (-180 <= longtitude <= 180):
            raise ValueError('Invalid latitude, longtitude combination')
        self._latitude = latitude
        self._longtitude = longtitude
        Point.store_points.append(self)

    def get_lat_long(self):
        return self._latitude, self._longtitude