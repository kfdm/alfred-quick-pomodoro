import os
import pathlib
import json
import logging

logging.basicConfig(level=logging.DEBUG)

BUNDLE_ID = os.environ.get(
    "alfred_workflow_bundleid", "net.kungfudiscomonkey.alfred.quickpomodoro"
)
ALFRED_CACHE = (
    pathlib.Path().home() / "Library" / "Caches" / "com.runningwithcrayons.Alfred"
)
ALFRED_VERSION = os.environ.get("alfred_version", "Unknown")
ALFRED_DATA = (
    pathlib.Path().home()
    / "Library"
    / "Application Support"
    / "Alfred"
    / "Workflow Data"
)


if "alfred_workflow_data" in os.environ:
    WORKFLOW_DIR = pathlib.Path(os.environ["alfred_workflow_data"])
else:
    WORKFLOW_DIR = ALFRED_DATA / BUNDLE_ID

with (WORKFLOW_DIR / "settings.json").open() as fp:
    SETTINGS = json.load(fp)

API_KEY = SETTINGS.get("API_KEY")
API_BASE = SETTINGS.setdefault("API_ENDPOINT", "https://tsundere.co/api")
USER_AGENT = "alfred/{}/{}".format(ALFRED_VERSION, BUNDLE_ID)
