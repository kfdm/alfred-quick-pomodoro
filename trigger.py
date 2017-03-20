#!/usr/bin/env python
# encoding: utf-8

import sys

import requests
import workflow

FAVORITES_URL = 'https://tsundere.co/api/pomodoro/start'


def main(wf):
    headers = {'Authorization': 'Token %s' % wf.settings['API_KEY']}
    r = requests.post(FAVORITES_URL, data=wf.args[0], headers=headers)

    if r.ok:
        print(u'{title} {end}'.format(**r.json()))
    elif r.status_code == 409:
        print(u'Active Pomodoro: {title} {end}'.format(status=r.status_code, **r.json()))
    else:
        print(r.text)

if __name__ == '__main__':
    sys.exit(workflow.Workflow().run(main))
