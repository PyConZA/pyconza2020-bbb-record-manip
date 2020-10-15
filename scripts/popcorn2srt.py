#!/usr/bin/env python3

import html
import itertools
import sys
from datetime import datetime, timedelta
from xml.etree import ElementTree as ET

tree = ET.parse(sys.stdin)
popcorn = tree.getroot()

COUNT = itertools.count(1)

def fmt_time(timestamp):
    return timestamp.strftime("%H:%M:%S,000")

def fmt_duration(startsecs, duration):
    starttime = datetime(2020, 1, 1) + timedelta(seconds=startsecs)
    endtime = starttime + timedelta(seconds=10)
    return f"{fmt_time(starttime)} --> {fmt_time(endtime)}"

for chatline in popcorn:
    startsecs = int(chatline.attrib["in"])
    name = chatline.attrib["name"]
    msg = html.unescape(chatline.attrib["message"])

    print(next(COUNT))
    print(fmt_duration(startsecs, 10))
    print(f"{name}: {msg}")
    print()
