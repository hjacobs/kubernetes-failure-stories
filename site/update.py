#!/usr/bin/env python3

import markdown
import requests
import time

from pathlib import Path

template = (Path(__file__).parent / "template.html").read_text()

while True:
    response = requests.get(
        "https://codeberg.org/hjacobs/kubernetes-failure-stories/raw/branch/master/README.md",
        timeout=5,
    )
    response.raise_for_status()

    html = markdown.markdown(response.text)

    out = template.replace("{{content}}", html)

    Path("index.html").write_text(out)

    time.sleep(300)
