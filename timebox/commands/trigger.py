#!/usr/bin/env python
# encoding: utf-8

import sys
import requests
import workflow

FAVORITES_URL = 'https://tsundere.co/api/favorite/{id}/start'


def main(wf):
    headers = {'Authorization': 'Token %s' % wf.settings['API_KEY']}
    r = requests.post(FAVORITES_URL.format(id=wf.args[0]), headers=headers)

    if r.ok:
        print(u'{title} {end}'.format(**r.json()).encode('utf8', 'ignore'))
    elif r.status_code == 409:
        print(u'Cannot replace active Pomodoro: {title} {end}'.format(status=r.status_code, **r.json()['data']).encode('utf8', 'ignore'))
    else:
        print(r.text)

if __name__ == '__main__':
    sys.exit(workflow.Workflow().run(main))
