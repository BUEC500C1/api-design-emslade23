# Developed by Elizabeth Slade, U95755315, 2/3/2020.

from flask import render_template, request, Flask

import csv
import requests
import os


def getAirportCoordinates(airportName):
    # gets location of airport given the name of the airport
    with open("airports.csv", 'r') as airportData:
        for element in csv.reader(airportData):
            if element[3] == airportName:
                latLongArray = [element[4], element[5]]
                if type(latLongArray[0]) == int and type(latLongArray[1]) == int:
                    return latLongArray
                else:
                    return "error"
    # error check, if airport is not in there
    return "error"


def weatherInformation(latitude, longitude):
    # using the weather api, find the weather for the airport's location
    appKey = os.environ['app_key']
    url_part = + str(latitude) + "&lon=" + str(longitude) + "&APPID=" + str(appKey) + "&units=imperial"
    api_address="http://api.openweathermap.org/data/2.5/weather?lat=" + url_part
    response = requests.get(api_address).json()
    return response


app = Flask(__name__)
app.config["DEBUG"] = True


@app.route("/", methods=["GET"])
def input():
    return render_template("user_input.html")


@app.route("/", methods=["POST"])
def form_input():
    airportName = request.form["airportName"]
    latLongArray = getAirportCoordinates(airportName)
    if latLongArray == "error":
        return render_template("user_input.html", errorMessage = "Error wrong airport name. It must be exact name!")
    result = weatherInformation(latLongArray[0], latLongArray[1])
    print(result)
    weather = result['weather'][0]['main']
    temp = result['main']['temp']
    feels_like = result['main']['feels_like']
    temp_max = result['main']['temp_max']
    temp_min = result['main']['temp_min']
    humidity = result['main']['humidity']
    return render_template("weather_output.html", weather=weather, temp = temp, feels_like = feels_like, temp_max = temp_max, temp_min = temp_min, humidity = humidity, airportName = airportName)


app.run()
