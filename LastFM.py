# lastfm.py

# Starter code for assignment 4 in ICS 32
# Programming with Software Libraries in Python
# My apikey for lastfm is: 9e378b414d40568750b1dcbc42d0d6cd
# Replace the following placeholders with your information.

# Junyu Li
# junyul24@uci.edu
# 86676906
import urllib
import json
from urllib import request, error
from WebAPI import WebAPI


class LastFM(WebAPI):

    def __init__(self):
        self.toptagname = ''
        self.apikey = ''

    def load_data(self) -> None:
        '''
        Calls the web api using the required values and stores the response in class data attributes.
        '''
        # TODO: use the apikey data attribute and the urllib module to request data from the web api. See sample code at the begining of Part 1 for a hint.
        # TODO: assign the necessary response data to the required class data attributes
        try:
            url = f"http://ws.audioscrobbler.com/2.0/?method=tag.getTopTags&api_key={self.apikey}&format=json"
            json_obj = self._download_url(url)
        except Exception as e:
            print(f'Failed to download contents of URL because {e}')
        else:
            self.toptagname = json_obj['toptags']['tag'][0]['name']

    def transclude(self, message: str) -> str:
        '''
        Replaces keywords in a message with associated API data.
        :param message: The message to transclude

        :returns: The transcluded message
        '''
        # TODO: write code necessary to transclude keywords in the message parameter with appropriate data from API
        newmessage = message.replace('@lastfm', self.toptagname)
        return newmessage


def main() -> None:
    apikey = "9e378b414d40568750b1dcbc42d0d6cd"
    url = f"http://ws.audioscrobbler.com/2.0/?method=tag.getTopTags&api_key={apikey}&format=json"
    obj = LastFM()
    weather_obj = obj._download_url(url)
    if weather_obj is not None:
        print(weather_obj)
    obj.set_apikey(apikey)
    obj.load_data()
    print(obj.toptagname)


if __name__ == '__main__':
    main()
