import json
import logging
import sys
import time

from timebox.encoder import encoder

logger = logging.getLogger(__name__)


def jsonfilter(func):
    def inner():
        start = time.time()
        json.dump(({"items": list(func())}), fp=sys.stdout, default=encoder)
        end = time.time()
        logger.debug("Script took %s", end - start)

    return inner


def args(func):
    def inner():
        logger.debug("%s", sys.argv)

        start = time.time()
        r = func(sys.argv[1].split(" "))
        end = time.time()

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

        logger.debug("Script took %s", end - start)

    return inner
