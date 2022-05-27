import requests
import config as config
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/results", methods=["POST"])
def results():
    city_name = request.form['city']
    json_data = get_weather_data(city_name, config.API)
    data = convert_weather(json_data)
    return render_template("results.html", city=city_name.capitalize(), desc=data['desc'], temp=data['temp'], feels_like=data['feels'], humid=data['humid'])

def convert_weather(json_data):
    description = "mild"
    temperature = json_data["main"]["temp"]
    feels_like = json_data["main"]["feels_like"]
    humidity = json_data["main"]["humidity"]

    if temperature > 28:
        description = "hot"
    elif temperature < 15:
        description = "cold"

    weather_data = {
        "temp": str(temperature),
        "feels": feels_like,
        "humid": str(humidity),
        "desc": description
        }

    return  weather_data

def get_weather_data(city, api):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={api}"
    jsonf = requests.get(url)
    return jsonf.json()

if __name__ == "__main__":
    app.run()




