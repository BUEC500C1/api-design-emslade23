from apiFunctions import getAirportCoordinates
from apiFunctions import hello

def test_airportCheck1():
    assert getAirportCoordinates("Total Rf Heliport") == ['40.07080078', '-74.93360138']


def test_airportCheck2():
    assert getAirportCoordinates("Lowell Field") == ['59.94919968', '-151.6959991']


def test_airportCheck3():
    assert getAirportCoordinates("Williams Ag Airport") == ['39.427188', '-121.763427']


def test_airportCheck4():
    assert getAirportCoordinates("Frazier Lake Airpark") == ['36.95330048', '-121.4649963']


def test_airportErrorCheck1():
    assert getAirportCoordinates("Boston") == "error"


def test_airportErrorCheck2():
    assert getAirportCoordinates("SF") == "error"


def test_airportErrorCheck3():
    assert getAirportCoordinates("hello") == "error"

def test_hellotest():
    assert hello() == "hi"