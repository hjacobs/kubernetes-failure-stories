#!/usr/bin/env python3

import markdown
import requests
import time

from pathlib import Path

with open(Path(__file__).parent / 'template.html') as fd:
    template = fd.read()

while True:
    response = requests.get('https://raw.githubusercontent.com/hjacobs/kubernetes-failure-stories/master/README.md', timeout=5)
    response.raise_for_status()

    html = markdown.markdown(response.text)

    out = template.replace('{{content}}', html)

    with open('index.html', 'w') as fd:
        fd.write(out)

    time.sleep(300)
