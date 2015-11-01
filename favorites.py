# encoding: utf-8

import sys
import workflow


def main(wf):
    params = dict(auth_token=API_KEY, count=20, format='json')
    headers = {'Authorization': 'Token %s' % API_KEY}
    r = workflow.web.get(FAVORITES_URL, params, headers)
    r.raise_for_status()

    for favorite in r.json()['results']:
        wf.add_item(
            title=favorite['title'],
            subtitle=favorite['category'],
            valid=True,
            arg=u'tell application "Pomodoro" to start "{title} #{category}" duration {duration}'.format(**favorite)
        )
    wf.send_feedback()

if __name__ == u'__main__':
    sys.exit(workflow.Workflow().run(main))
