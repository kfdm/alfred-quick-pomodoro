import datetime
import json
import logging

import requests

from timebox import auth, decorators, settings

logger = logging.getLogger(__name__)


def icon(favorite, fetch):
    path = settings.WORKFLOW_CACHE / favorite["title"]
    logger.debug("Looking up icon: %s", path)
    if path.exists():
        return path
    if "icon" in favorite and favorite["icon"] and fetch:
        # Cache icon
        logger.debug("Downloading: %s", favorite["icon"])
        response = requests.get(favorite["icon"])
        if response.ok:
            with path.open("wb") as fp:
                fp.write(response.content)
            return path
    return settings.ICON_ROOT / "Clock.icns"


def process(favorites, fetch):
    for favorite in sorted(favorites, key=lambda f: f["count"], reverse=True):
        yield {
            "uid": favorite["id"],
            "title": favorite["title"],
            "subtitle": "{} {} [{}]".format(
                favorite["project"]["name"],
                datetime.timedelta(minutes=favorite["duration"]),
                favorite["count"],
            ),
            "arg": favorite["id"],
            "icon": {"path": icon(favorite, fetch)},
            "mods": {
                "cmd": {
                    "arg": 'tell application "Pomodoro" to start "{title} #{category}" duration {duration}'.format(
                        **favorite
                    ),
                    "subtitle": "Launch with Pomodoro.app",
                }
            },
        }


@decorators.jsonfilter
def fetch():
    response = requests.get(
        settings.API_BASE + "/favorite", auth=auth.TokenAuth(settings.API_KEY)
    )
    response.raise_for_status()
    data = response.json()["results"]
    with (settings.WORKFLOW_CACHE / "response.json").open("w", encoding="utf8") as fp:
        json.dump(data, fp)

    yield from process(data, True)


@decorators.jsonfilter
def cached():
    with (settings.WORKFLOW_CACHE / "response.json").open("r", encoding="utf8") as fp:
        data = json.load(fp)

    yield from process(data, False)
