# encoding: utf-8

import os
import sys
import workflow
import workflow.web as web

FAVORITES_URL = 'http://tsundere.co/api/favorite/?format=json'


def main(wf):
    params = dict(count=20, format='json')
    headers = {'Authorization': 'Token %s' % wf.settings['API_KEY']}
    r = workflow.web.get(FAVORITES_URL, params, headers)
    r.raise_for_status()

    for favorite in sorted(r.json()['results'], key=lambda f: f['category']):
        icon = wf.datafile(favorite['title'])
        if os.path.exists(icon) is False:
            if favorite['icon']:
                request = web.get(favorite['icon'])
                request.save_to_path(icon)
            else:
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
