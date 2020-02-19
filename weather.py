import requests
import os
from datetime import datetime

def main():
    try:
        city, country = input('What city and country (two-letter code) would you like the weather for?: ').split() #Take user input

        key = os.environ.get('WEATHER_KEY') #Set weather key
        query = {'q': city + ',' + country, 'units': 'imperial', 'appid': key} #Format query string

        url = 'http://api.openweathermap.org/data/2.5/forecast' #Set url
        data = requests.get(url, params=query).json() 
    
        forecast_items = data['list'] #Get five day list

        for forecast in forecast_items:
            timestamp = forecast['dt']
            date = datetime.fromtimestamp(timestamp) #Get date and time in local time so user knows in real time
            weather_description = forecast['weather'][0]['description'] #Get forecast
            temp = forecast['main']['temp'] #Get temp
            print(f'at {date} forecast is {weather_description} {temp}F') #Print formatted string
    except:
        print('Enter a valid city and country code.')

if __name__ == '__main__':
    main()