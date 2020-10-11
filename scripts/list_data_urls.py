#!/usr/bin/python3
#
# Crude script to download all the files from a BBB presenation
#

import sys
import requests

def usage():
    print(f'{sys.argv[0]} <url>')
    print('Where url is the link the BBB presentation playback')
    print('i.e. https://<host>/playback/presentation/2.0/playback.html?meetingId=<meetingId>')


def process(base_url):
    meeting_id = base_url.split('?meetingId=')[1]
    base_url = base_url.split('playback/')[0] + 'presentation/' + meeting_id
    # Create all the urls
    print(f'webcam video url:      {base_url}video/webcams.webm')
    print(f'deskshare video url:   {base_url}/deskshare/deskshare.webm')
    print(f'deskshare events url:  {base_url}/deskshare.xml')
    print(f'cursor events url:     {base_url}/cursor.xml')
    print(f'metadata url:          {base_url}/metadata.xml')
    print(f'pazooms url:           {base_url}/panzooms.xml')
    print(f'shapes.svg url:        {base_url}/shapes.svg')
    print(f'slides_new.xml:        {base_url}/slides_new.xml')
    # Get the shapes.svg and parse out the hreg links
    r = requests.get(f'{base_url}/shapes.svg')
    urls = set()
    for line in r.text.splitlines():
        if 'xlink:href' in line:
            data = line.split('xlink:href')[1]
            url = base_url + '/' + data.split('"')[1]
            urls.add(url)
    for url in sorted(urls):
        print(f'internal url:       {url}')


if __name__ == "__main__":
    if len(sys.argv) != 2:
        usage()
        sys.exit(1)
    if '/playback/presentation/2.0/playback.html?meetingId=' not in sys.argv[1]:
        usage()
        sys.exit(1)
    process(sys.argv[1])

