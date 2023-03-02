# openweather.py

# Starter code for assignment 4 in ICS 32
# Programming with Software Libraries in Python

# Replace the following placeholders with your information.
# My API key for Openweather is: 03657b48a28c90947a8068f1f2608dfc
# API keys should be asked for user
# Junyu Li
# junyul24@uci.edu
# 86676906
import urllib
import json
from urllib import request, error


class OpenWeather:
    def __init__(self, zipcode, ccode):
        self.zipcode = zipcode
        self.ccode = ccode
        self.apikey = ''
        self.temperature = 0
        self.high_temperature = 0
        self.low_temperature = 0
        self.longitude = 0
        self.latitude = 0
        self.description = ''
        self.humidity = 0
        self.sunset = 0
        self.city = ''


    def set_apikey(self, apikey: str) -> None:
        '''
        Sets the apikey required to make requests to a web API.
        :param apikey: The apikey supplied by the API service

        '''
        # TODO: assign apikey value to a class data attribute that can be accessed by class members
        self.apikey = apikey

    def load_data(self) -> None:
        '''
        Calls the web api using the required values and stores the response in class data attributes.

        '''
        # TODO: use the apikey data attribute and the urllib module to request data from the web api. See sample code at the begining of Part 1 for a hint.
        # TODO: assign the necessary response data to the required class data attributes
        try:
            url = f"http://api.openweathermap.org/data/2.5/weather?zip={self.zipcode},{self.ccode}&appid={self.apikey}"
            json_obj = _download_url(url)
            self.temperature = json_obj['main']['temp']
            self.high_temperature = json_obj['main']['temp_max']
            self.low_temperature = json_obj['main']['temp_min']
            self.longitude = json_obj['coord']['lon']
            self.latitude = json_obj['coord']['lat']
            self.description = json_obj['weather'][0]['description']
            self.humidity = json_obj['main']['humidity']
            self.sunset = json_obj['sys']['sunset']
            self.city = json_obj['name']
        except json.JSONDecodeError:
            print("Json cannot be decoded.")


def _download_url(url_to_download: str) -> dict:
    response = None
    r_obj = None

    try:
        response = urllib.request.urlopen(url_to_download)
        json_results = response.read()
        r_obj = json.loads(json_results)

    except urllib.error.HTTPError as e:
        print('Failed to download contents of URL')
        print('Status code: {}'.format(e.code))

    finally:
        if response is not None:
            response.close()

    return r_obj


def main() -> None:
    zip = "92617"
    ccode = "US"
    apikey = "03657b48a28c90947a8068f1f2608dfc"
    url = f"http://api.openweathermap.org/data/2.5/weather?zip={zip},{ccode}&appid={apikey}"

    weather_obj = _download_url(url)
    if weather_obj is not None:
        print(weather_obj)
        print(weather_obj['weather'][0]['description'])


if __name__ == '__main__':
    main()
