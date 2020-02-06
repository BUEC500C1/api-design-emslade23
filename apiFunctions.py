import csv
import requests

def getAirportCoordinates(airportName):
    # gets location of airport given the name of the airport
    with open("airports.csv", 'r') as airportData:
        for element in csv.reader(airportData):
            if element[3] == airportName:
                return [element[4], element[5]]
    # error check, if airport is not in there
    return "error"

def hello():
    return "hi"