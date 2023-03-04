# lastfm.py

# Starter code for assignment 4 in ICS 32
# Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Junyu Li
# junyul24@uci.edu
# 86676906
import urllib
import json
from urllib import request, error

def _download_url(url_to_download: str) -> dict:  # 这里处理Invalid data formatting from the remote API, 是否引发一个新的异常
    response = None
    r_obj = None
    try:
        response = urllib.request.urlopen(url_to_download)
        print(response)
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


def main() -> None:
    apikey = "9e378b414d40568750b1dcbc42d0d6cd"
    url = f"http://ws.audioscrobbler.com/2.0/?method=chart.gettopartists&api_key={apikey}&format=json"
    weather_obj = _download_url(url)
    if weather_obj is not None:
        print(weather_obj)


if __name__ == '__main__':
    main()