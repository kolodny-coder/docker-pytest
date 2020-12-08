from scripts.chp2.video3.mapmaker_exceptions_start import Point
import pytest


def test_make_one_point():
    p1 = Point("Dakar", 14.7167, 17.4677)
    assert p1.get_lat_long() == (14.7167, 17.4677)


def test_invalid_point_generation():  # TO DO
    with pytest.raises(ValueError) as exp:
        Point('Buenos Aires', 12.11386, -555.08269)
    assert (str(exp.value) == 'latitude int should be between -90 to 90 longitude value should be'
                              ' between -180 to 180')


def test_invalid_city_name_data_type():
    with pytest.raises(ValueError) as exp:
        Point(name=123, latitude=45.12345, longitude=-125.32145)
    assert str(exp.value) == 'City name must be a string'
