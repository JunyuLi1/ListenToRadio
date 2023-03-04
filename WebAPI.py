# webapi.py

# Starter code for assignment 4 in ICS 32
# Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Junyu Li
# junyul24@uci.edu
# 86676906

from abc import ABC, abstractmethod


class WebAPI(ABC):

    def _download_url(self, url: str) -> dict:
        # TODO: Implement web api request code in a way that supports
        # all types of web APIs
        response = None
        r_obj = None
        try:
          response = urllib.request.urlopen(url_to_download)
          json_results = response.read()
          r_obj = json.loads(json_results)
        except urllib.error.HTTPError as e:
          print('Failed to download contents of URL')
          print('Status code: {}'.format(e.code))
        except urllib.error.URLError:
          print('Loss of local connection to the Internet')
        except http.client.InvalidURL:
          raise InvalidAPIkeyError
        except ValueError:
          raise InvalidAPIformatError
        finally:
          if response is not None:
            response.close()
        return r_obj

    def set_apikey(self, apikey: str) -> None:
        self.apikey = apikey

    @abstractmethod
    def load_data(self):
      """Calls the web api using the required values and stores the response in class data attributes."""
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
      except InternetError:
        print('Loss of local connection to the Internet')
      except InvalidAPIkeyError:
        print('Your APIkey is not correct.')
      except APInotFoundError:
        pass
      except InvalidAPIformatError:
        print('Invalid data formatting from the remote API')

    @abstractmethod
    def transclude(self, message: str) -> str:
        pass
