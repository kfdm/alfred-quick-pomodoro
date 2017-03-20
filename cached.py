#!/usr/bin/env python
# encoding: utf-8

import json
import os
import sys

import workflow


def main(wf):
    with open(wf.cachefile('response.json'), 'rb') as fp:
        for favorite in sorted(json.load(fp)['results'], key=lambda f: f['category']):
            icon = wf.cachefile(favorite['title'])
            if os.path.exists(icon) is False:
                icon = workflow.ICON_CLOCK
            wf.add_item(
                title=favorite['title'],
                subtitle=favorite['category'],
                valid=True,
                arg=u'tell application "Pomodoro" to start "{title} #{category}" duration {duration}'.format(**favorite),
                icon=icon,
            )
        wf.send_feedback()

if __name__ == u'__main__':
    sys.exit(workflow.Workflow().run(main))
