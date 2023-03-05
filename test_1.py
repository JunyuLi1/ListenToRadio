from OpenWeather import OpenWeather
from WebAPI import WebAPI
from LastFM import LastFM
"""zipcode = "92617"
ccode = "US"
apikey = "03657b48a28c90947a8068f1f2608dfc"

open_weather = OpenWeather(zipcode, ccode)
open_weather.set_apikey(apikey)
open_weather.load_data()
print(f"The temperature for {zipcode} is {open_weather.temperature} degrees")
print(f"The high for today in {zipcode} will be {open_weather.high_temperature} degrees")
print(f"The low for today in {zipcode} will be {open_weather.low_temperature} degrees")
print(f"The coordinates for {zipcode} are {open_weather.longitude} longitude and {open_weather.latitude} latitude")
print(f"The current weather for {zipcode} is {open_weather.description}")
print(f"The current humidity for {zipcode} is {open_weather.humidity}")
print(f"The sun will set in {open_weather.city} at {open_weather.sunset}")"""


def test_api(message:str, apikey:str, webapi:WebAPI):
  webapi.set_apikey(apikey)
  webapi.load_data()
  result = webapi.transclude(message)
  print(result)


open_weather = OpenWeather() #notice there are no params here...HINT: be sure to use parameter defaults!!!
lastfm = LastFM()

test_api("Testing the weather: @weather", "03657b48a28c90947a8068f1f2608dfc", open_weather)
# expected output should include the original message transcluded with the default weather value for the @weather keyword.

test_api("Testing lastFM: @lastfm", "9e378b414d40568750b1dcbc42d0d6cd", lastfm)
# expected output include the original message transcluded with the default music data assigned to the @lastfm keyword"""