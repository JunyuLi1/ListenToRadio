# webapi.py

# Starter code for assignment 4 in ICS 32
# Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Junyu Li
# junyul24@uci.edu
# 86676906
from abc import ABC, abstractmethod
import urllib
import json
from urllib import request, error

class WebAPI(ABC):
    apikey: str

    def _download_url(self, url: str) -> dict:
        # TODO: Implement web api request code in a way that supports
        # all types of web APIs
        response = None
        r_obj = None
        try:
            response = urllib.request.urlopen(url)
            json_results = response.read()
            r_obj = json.loads(json_results)
        except urllib.error.HTTPError as e:
            print('Failed to download contents of URL')
            print('Status code: {}'.format(e.code))
            print('The remote API is unavailable')
        except urllib.error.URLError:
            print('Loss of local connection to the Internet')
        except json.JSONDecodeError:
            print('Invalid data formatting from the remote API')
        finally:
            if response is not None:
                response.close()
        return r_obj

    def set_apikey(self, apikey: str) -> None:
        self.apikey = apikey

    @abstractmethod
    def load_data(self):
        pass

    @abstractmethod
    def transclude(self, message: str) -> str:
        pass
