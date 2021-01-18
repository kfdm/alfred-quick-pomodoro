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
    parser.add_argument("title", nargs="+")
    args = parser.parse_args(args)
    logger.debug("%s", args)

    start = datetime.datetime.now()
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
