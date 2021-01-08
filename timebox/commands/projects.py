#!/usr/bin/env python
# encoding: utf-8

import datetime
import json
import os
import sys

import workflow


def main(wf):
    response = []
    response.append({'test'})
    print(json.dumps({'items': response}))

if __name__ == u'__main__':
    sys.exit(workflow.Workflow().run(main))
