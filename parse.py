#!/usr/bin/env python
# encoding: utf-8

import json
import os
import sys
import datetime
from dateutil.parser import parse
from dateutil.tz import tzutc
import requests
import workflow

POMODORO_URL = 'https://tsundere.co/api/pomodoro'


def main(wf):
    now = datetime.datetime.now(tzutc())
    pomodoro = {
        'start': now.isoformat(),
        'end': (now + datetime.timedelta(minutes=int(os.environ['duration']))).isoformat(),
    }
    try:
        pomodoro['title'], pomodoro['category'] = wf.args[0].split('#', 2)
    except:
        pomodoro['title'] = wf.args[0]

    headers = {'Authorization': 'Token %s' % wf.settings['API_KEY']}
    r = requests.get(POMODORO_URL, headers=headers)
    now = datetime.datetime.now(tzutc())
    for p in r.json()['results']:
        dt = parse(p['end'])
        if dt > now:
            print(u'Active Pomodoro: {title} {end}'.format(status=r.status_code, **p).encode('utf8', 'ignore'))
            exit()

    headers['Content-Type'] = 'application/json'
    r = requests.post(POMODORO_URL, data=json.dumps(pomodoro), headers=headers)

    if r.ok:
        print(u'{title} {end}'.format(**r.json()).encode('utf8', 'ignore'))
    elif r.status_code == 409:
        print(u'Active Pomodoro: {title} {end}'.format(status=r.status_code, **r.json()).encode('utf8', 'ignore'))
    else:
        print(r.text)

if __name__ == '__main__':
    sys.exit(workflow.Workflow().run(main))
