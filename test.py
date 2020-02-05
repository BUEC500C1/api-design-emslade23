from app import getAirportCoordinates


def airportCheck1():
    assert getAirportCoordinates("Total Rf Heliport") == [40.07080078, -74.93360138]


def airportCheck2():
    assert getAirportCoordinates("Lowell Field") == [59.94919968, -151.6959991]


def airportCheck3():
    assert getAirportCoordinates("Williams Ag Airport") == [39.427188, -121.763427]


def airportCheck4():
    assert getAirportCoordinates("Frazier Lake Airpark") == [36.95330048, -121.4649963]


def airportErrorCheck1():
    assert getAirportCoordinates("Boston") == "error"


def airportErrorCheck2():
    assert getAirportCoordinates("SF") == "error"


def airportErrorCheck3():
    assert getAirportCoordinates("hello") == "error"