import logging

import requests
from timebox import auth, decorators, settings

logger = logging.getLogger(__name__)


@decorators.jsonfilter
def main():
    response = requests.get(
        settings.API_BASE + "/project", auth=auth.TokenAuth(settings.API_KEY)
    )
    response.raise_for_status()
    for p in response.json().get("results", []):
        logger.debug("%s", p)
        yield {
            "uid": p["id"],
            "title": p["name"],
            "arg": p["id"],
            "autocomplete": p["name"],
        }
