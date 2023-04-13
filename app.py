from flask import Flask,render_template,request
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('web.html')
@app.route('/',methods=['GET','POST'])
def get_climate():
    city = request.form['city']
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid=6ccc1f0ed34bb16d718940f247dd4c70'

    response=requests.get(url)
    weather=response.json()

    if weather['cod'] == 200:
        temp_celsius = round(weather['main']['temp'] - 273.15,2)
        temp_farenheit = round((temp_celsius * 9/5)+32,2)
        return render_template('web.html',temperature_celsius=temp_celsius,temperature_fahrenheit=temp_farenheit,city_name=weather['name'])
    else:
        return render_template('web.html',error_message='City not found!')
    
if __name__ == '__main__':
    app.run(debug=True)
