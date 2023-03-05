# ds_protocol.py

# Starter code for assignment 3 in ICS 32
# Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Junyu Li
# junyul24@uci.edu
# 86676906
import json
import time
from collections import namedtuple

# Namedtuple to hold the values retrieved from json messages.
# TODO: update this named tuple to use DSP protocol keys
DataTuple = namedtuple('DataTuple', ['response', 'type', 'message', 'token'])


def extract_json(json_msg: str) -> DataTuple:
    """
  Call the json.loads function on a json string and convert it to a DataTuple object

  TODO: replace the pseudo placeholder keys with actual DSP protocol keys
  """
    try:
        json_obj = json.loads(json_msg)
        response = json_obj['response']
        type = json_obj['response']['type']
        message = json_obj['response']['message']
        if 'token' in json_obj['response']:
            token = json_obj['response']['token']
        else:
            token = None
    except json.JSONDecodeError:
        print("Json cannot be decoded.")
    else:
        return DataTuple(response, type, message, token)


def join_action(name, pwd):
    """Process join action and return an information."""
    dic = {"join": {"username": name, "password": pwd, "token": ""}}
    str1 = json.dumps(dic)
    return str1


def post_action(usertoken, post):
    timestamp = time.time()
    """Process post action and return the json format."""
    dic = {"token": usertoken, "post": {"entry": post, "timestamp": timestamp}}
    str1 = json.dumps(dic)
    return str1


def bio_action(useertoken, bio):
    """Process with bio action"""
    dic = {"token": useertoken, "bio": {"entry": bio, "timestamp": ""}}
    str1 = json.dumps(dic)
    return str1
