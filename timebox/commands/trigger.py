import logging
import sys

import requests
from timebox import auth, settings

logger = logging.getLogger(__name__)


def main():
    url = "{}/favorite/{}/start".format(settings.API_BASE, sys.argv[1])
    r = requests.post(url, auth=auth.TokenAuth(settings.API_KEY))

    if r.ok:
        print("{title} {end}".format(**r.json()))
    elif r.status_code == 409:
        print(
            "Cannot replace active Pomodoro: {title} {end}".format(
                status=r.status_code, **r.json()["data"]
            )
        )
    else:
        print(r.text)
