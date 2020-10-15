#!/usr/bin/python3
#
# Obfuscates names in the chat messages

import os
import sys
import re
import random
from xml.etree.ElementTree import parse

CHAT_FILE = "slides_new.xml"

BACKUP = ".orig"

def usage():
    print(f"{sys.argv[0]} <chat filename>")
    print()
    print(f"The filename must be the processed '{CHAT_FILE}' file from the BBB recording")
    print(f"If a backup file doesn't exist, the original will be copied to {CHAT_FILE + BACKUP}")
    print(f"If a {CHAT_FILE + BACKUP} file exists, we assume it is an existing backup")

def process(filename):
    # Error handling, who needs that
    with open(filename, 'r') as f:
        data = parse(f)
    backup = filename + BACKUP
    if not os.path.exists(backup):
        os.rename(filename, backup)
    newnames = set()
    renames = {}
    for elem in data.getroot():
        name = elem.attrib['name']
        if name not in renames:
            cand = None
            while cand is None or cand in newnames:
                offset = random.randint(1, 10000)
                cand = f'{name[0]}{offset:05d}'
            renames[name] = cand
            newnames.add(cand)
    for elem in data.getroot():
        oldname = elem.attrib['name']
        elem.attrib['name'] = renames[oldname]
        for name in renames:
            if name in elem.attrib['message']:
                oldmsg = elem.attrib['message']
                elem.attrib['message'] = oldmsg.replace(name, renames[name])
        # Replace @Name callouts with something else
        elem.attrib['message'] = re.sub(r'@[A-Za-z]+\b', '@...', elem.attrib['message'])
    with open(filename, 'wb') as f:
        data.write(f)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        usage()
        sys.exit(1)

    if not sys.argv[1].endswith(CHAT_FILE):
        print("Unexpected file name ")
        usage()
        sys.exit(1)

    process(sys.argv[1])
