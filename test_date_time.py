import pytest
from DateTimeProject2.date_time import CustomDateTime  

def test_custom_datetime_creation():
    dt1 = CustomDateTime(1999, 7, 14, 12, 30, 45)
    dt2 = CustomDateTime.from_iso_format("1999-07-14T12:30:45")

    assert dt1.year == 1999
    assert dt1.month == 7
    assert dt1.day == 14
    assert dt1.hour == 12
    assert dt1.minute == 30
    assert dt1.second == 45

    assert dt1.to_iso_format() == "1999-07-14T12:30:45"
    assert dt1.to_human_readable_format() == "1999-07-14 12:30:45"

def test_custom_datetime_properties():
    dt1 = CustomDateTime(1999, 7, 14, 12, 30, 45)

    assert dt1.year == 1999
    assert dt1.month == 7
    assert dt1.day == 14
    assert dt1.hour == 12
    assert dt1.minute == 30
    assert dt1.second == 45

def test_custom_datetime_validation():
    assert CustomDateTime.validate_date(1999, 7, 14) == True
    assert CustomDateTime.validate_date(2022, 4, 12) == True
    assert CustomDateTime.validate_date(2022, 13, 1) == False

def test_custom_datetime_difference():
    dt1 = CustomDateTime(1999, 7, 14, 12, 30, 45)
    dt3 = CustomDateTime(2000, 4, 12)

    assert CustomDateTime.date_difference(dt1, dt3, unit='days') == -273
    assert CustomDateTime.date_difference(dt1, dt3, unit='weeks') == -39
    assert CustomDateTime.date_difference(dt1, dt3, unit='months') == -9

def test_custom_datetime_from_string():
    dt4 = CustomDateTime.date_from_string("2002-08-01 08:45:30")

    assert dt4.to_human_readable_format() == "2002-08-01 08:45:30"

if __name__ == "__main__":
    pytest.main()
