#!/usr/bin/env python
# encoding: utf-8

import json
import os
import sys

import workflow
import workflow.web as web

FAVORITES_URL = 'http://tsundere.co/api/favorite?format=json'


def main(wf):
    response = []
    params = dict(count=20, format='json')
    headers = {'Authorization': 'Token %s' % wf.settings['API_KEY']}
    r = workflow.web.get(FAVORITES_URL, params, headers)
    r.raise_for_status()

    with open(wf.cachefile('response.json'), 'wb') as fp:
        fp.write(r.text.encode('utf8', 'ignore'))

    for favorite in sorted(r.json()['results'], key=lambda f: f['category']):
        icon = wf.cachefile(favorite['title'])
        if os.path.exists(icon) is False:
            if favorite['icon']:
                request = web.get(favorite['icon'])
                request.save_to_path(icon)
            else:
                icon = workflow.ICON_CLOCK
        response.append({
            'title': favorite['title'],
            'subtitle': favorite['category'],
            'arg': json.dumps(favorite),
            'icon': {'path': icon},
            'mods': {
                'cmd': {
                    'arg': u'tell application "Pomodoro" to start "{title} #{category}" duration {duration}'.format(**favorite),
                    'subtitle': 'Launch with Pomodoro.app'
                }
            }
        })
    print(json.dumps({'items': response}))

if __name__ == u'__main__':
    sys.exit(workflow.Workflow().run(main))
