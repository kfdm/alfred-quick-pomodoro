import os
import pathlib
import json
import logging

# Alfred Defaults
LIBRARY = pathlib.Path().home() / "Library"
ALFRED_CACHE = LIBRARY / "Caches" / "com.runningwithcrayons.Alfred"
ALFRED_DATA = LIBRARY / "Application Support" / "Alfred" / "Workflow Data"

# System Default
ICON_ROOT = pathlib.Path(
    "/System/Library/CoreServices/CoreTypes.bundle/Contents/Resources"
)

# Alfred Environment Settings

if os.environ.get("alfred_debug") == "1":
    logging.basicConfig(level=logging.DEBUG)
else:
    logging.basicConfig(level=logging.INFO)

BUNDLE_ID = os.environ.get(
    "alfred_workflow_bundleid", "net.kungfudiscomonkey.alfred.quickpomodoro"
)

ALFRED_VERSION = os.environ.get("alfred_version", "Unknown")


# Remaining derived settings

if "alfred_workflow_data" in os.environ:
    WORKFLOW_DIR = pathlib.Path(os.environ["alfred_workflow_data"])
else:
    WORKFLOW_DIR = ALFRED_DATA / BUNDLE_ID

if "alfred_workflow_cache" in os.environ:
    WORKFLOW_CACHE = pathlib.Path(os.environ["alfred_workflow_cache"])
else:
    WORKFLOW_CACHE = ALFRED_CACHE / BUNDLE_ID


with (WORKFLOW_DIR / "settings.json").open() as fp:
    SETTINGS = json.load(fp)

API_KEY = SETTINGS.get("API_KEY")
API_BASE = SETTINGS.setdefault("API_ENDPOINT", "https://tsundere.co/api")
USER_AGENT = "alfred/{}/{}".format(ALFRED_VERSION, BUNDLE_ID)
