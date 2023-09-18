from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/weather')
def weather():
    apikey = "51d207a89e98e05940c23a3de9b80a5c"
    apiUrl = "http://api.openweathermap.org/data/2.5/weather?"
    latitude = request.args.get('lat')
    longitude = request.args.get('lon')

    complete_url = apiUrl + f"appid={apikey}&lat={latitude}&lon={longitude}&units=metric&lang=en"
    response = requests.get(complete_url)
    data = response.json()

    if data["cod"] != "404":
        y = data["main"]
        todayTemperature = y["temp"]
        todayFeelsLike = y["feels_like"]
        todayHumidity = y["humidity"]
        z = data["weather"]
        todayDescription = z[0]["description"]
        todayIcon = z[0]["icon"]
        w = data["clouds"]
        todayClouds = w["all"]

        weather_data = {
            "temperature": round(todayTemperature),
            "humidity": todayHumidity,
            "description": todayDescription,
            "feels_like": round(todayFeelsLike),
            "icon": todayIcon,
            "clouds": todayClouds
        }

        return jsonify(weather_data)
    else:
        return jsonify({"error": "City Not Found"})

if __name__ == '__main__':
    app.run()