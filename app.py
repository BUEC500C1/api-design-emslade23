# Developed by Elizabeth Slade, U95755315, 2/3/2020.

from flask import render_template, request, Flask

app = Flask(__name__)
app.config["DEBUG"] = True 

@app.route("/", methods=["GET"])
def input():
    return render_template("user_input.html")

@app.route("/", methods=["POST"])
def form_input():
    airportName = request.form["airportName"]
    return render_template("weather_output.html", airportName = airportName)


app.run()