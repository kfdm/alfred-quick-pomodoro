import argparse
import datetime
import logging

import requests

from timebox import auth, decorators, settings

logger = logging.getLogger(__name__)


@decorators.trigger
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--project")
    parser.add_argument("--duration", type=int, default=25)
    parser.add_argument("title", nargs="+")
    args = parser.parse_args()
    logger.debug("%s", args)

    start = datetime.datetime.now().astimezone()
    end = start + datetime.timedelta(minutes=args.duration)

    return requests.post(
        settings.API_BASE + "/pomodoro",
        auth=auth.TokenAuth(settings.API_KEY),
        json={
            "project": args.project,
            "start": start.isoformat(),
            "end": end.isoformat(),
            "title": " ".join(args.title),
        },
    )
