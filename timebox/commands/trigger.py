import argparse
import logging
import sys

import requests
from timebox import auth, decorators, settings

logger = logging.getLogger(__name__)


@decorators.args
def main(args):
    parser = argparse.ArgumentParser()
    parser.add_argument("id")
    args = parser.parse_args(args)
    logger.debug("%s", args)

    url = "{}/favorite/{}/start".format(settings.API_BASE, args.id)
    return requests.post(url, auth=auth.TokenAuth(settings.API_KEY))
