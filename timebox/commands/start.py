import argparse
import datetime
import logging

import requests
from timebox import auth, decorators, settings

logger = logging.getLogger(__name__)


@decorators.args
def main(args):
    parser = argparse.ArgumentParser()
    parser.add_argument("--project")
    parser.add_argument("--duration", type=int)
    parser.add_argument("title")
    args = parser.parse_args(args)
    logger.debug("%s", args)

    start = datetime.datetime.now()
    end = start + datetime.timedelta(minutes=args.duration)

    r = requests.post(
        settings.API_BASE + "/pomodoro",
        auth=auth.TokenAuth(settings.API_KEY),
        json={
            "project": args.project,
            "start": start.isoformat(),
            "end": end.isoformat(),
            "title": args.title,
        },
    )

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
