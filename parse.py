#!/usr/bin/env python
# encoding: utf-8

import json
import os
import sys

import requests
import workflow

FAVORITES_URL = 'https://tsundere.co/api/pomodoro/start'


def main(wf):
    pomodoro = {
        'duration': os.environ['duration']
    }
    try:
        pomodoro['title'], pomodoro['category'] = wf.args[0].split('#', 2)
    except:
        pomodoro['title'] = wf.args[0]

    headers = {'Authorization': 'Token %s' % wf.settings['API_KEY']}

    r = requests.post(FAVORITES_URL, data=json.dumps(pomodoro), headers=headers)

    if r.ok:
        print(u'{title} {end}'.format(**r.json()).encode('utf8', 'ignore'))
    elif r.status_code == 409:
        print(u'Active Pomodoro: {title} {end}'.format(status=r.status_code, **r.json()).encode('utf8', 'ignore'))
    else:
        print(r.text)

if __name__ == '__main__':
    sys.exit(workflow.Workflow().run(main))
