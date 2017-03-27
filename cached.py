#!/usr/bin/env python
# encoding: utf-8

import json
import os
import sys

import workflow


def main(wf):
    response = []
    with open(wf.cachefile('response.json'), 'rb') as fp:
        for favorite in sorted(json.load(fp)['results'], key=lambda f: f['count'], reverse=True):
            icon = wf.cachefile(favorite['title'])
            if os.path.exists(icon) is False:
                icon = workflow.ICON_CLOCK
            response.append({
                'uid': favorite['id'],
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
