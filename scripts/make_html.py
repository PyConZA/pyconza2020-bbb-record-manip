#!/usr/bin/python3                                                                                     
#
# Make a index.html page for a list of mp4 files

import pathlib

p = pathlib.Path('/var/bigbluebutton/published/presentation/converted')

with open('/var/bigbluebutton/published/presentation/converted/index.html', 'w') as out:
    out.write('<html>\n<head><title>Converted videos</title></head>\n<body>\n')
    out.write('<ul>\n')
    for movie in p.glob('*mp4'):
        out.write(f'<li><a href="{ movie.name }">{ movie.name }</a></li>\n')
    out.write('</ul>\n</body>\n</html>\n')

