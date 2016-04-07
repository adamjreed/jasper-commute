# -*- coding: utf-8-*-
import re
import urllib
import requests
import time

WORDS = ["COMMUTE"]

def handle(text, mic, profile):
    """
        Responds to user-input, typically speech text, by providing the current
        travel time between configured home and work addresses.

        Arguments:
        text -- user-input, typically transcribed speech
        mic -- used to interact with the user (for both input and output)
        profile -- contains information related to the user (e.g., phone
                   number)
    """
    if 'commute' in profile:
        if 'api_key' in profile['commute']:
            api_key = profile['commute']['api_key']
        else:
            mic.say("Please specify your Google API key in your profile.")
            return

        if 'home_address' in profile['commute']:
            home = profile['commute']['home_address']
        else:
            mic.say("Please specify your home address in your profile.")
            return

        if 'work_address' in profile['commute']:
            work = profile['commute']['work_address']
        else:
            mic.say("Please specify your work address in your profile.")
            return
    else:
        mic.say("You must specify commute information in your profile.")
        return

    query = urllib.urlencode({'key': api_key,
                              'origins': home,
                              'destinations': work,
                              'departure_time': int(time.time())})

    r = requests.get("https://maps.googleapis.com" +
                     "/maps/api/distancematrix/json", query)
    try:
        r.raise_for_status()
    except requests.exceptions.HTTPError:
        self._logger.critical('Request failed with http status %d',
                              r.status_code)
        if r.status_code == requests.codes['forbidden']:
            self._logger.warning('Access forbidden. Please check your ' +
                                 'Google API key.')
        return []

    response = r.json()
    duration = response['rows'][0]['elements'][0]['duration_in_traffic']


    if('text' in duration):
        mic.say("Your commute will take " + duration['text'] + " today.")
    else:
        mic.say("Sorry, I could not get information about your commute.")


def isValid(text):
    """
        Returns True if the input is related to the meaning of life.

        Arguments:
        text -- user-input, typically transcribed speech
    """
    return bool(re.search(r'\bcommute\b', text, re.IGNORECASE))    