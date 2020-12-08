from scripts.chp2.video2.mapmaker_start import Point
import pytest


def test_make_one_point():
    p1 = Point('Dakar', 14.7167, 17.4677)
    assert p1.get_lat_long() == (14.7167, 17.4677)


def test_invaild_point_generation():
    with pytest.raises(ValueError) as exp:
        Point('Dakar', latitude=-100, longtitude=160)
    assert str(exp.value) == 'Invalid latitude, longtitude combination'


def test_invalid_city_name_data_type():
    with pytest.raises(ValueError) as exp:
        Point(313, 14.7167, 17.4677)
    assert str(exp.value) == 'Invalid name type, Should be string'

def test_store_points():
    Point.store_points = []
    p2 = Point('Dakar', 14.7167, 17.4677)
    assert Point.store_points == [p2]
