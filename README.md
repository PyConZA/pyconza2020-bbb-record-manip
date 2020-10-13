Scripts and stuff for manipulating BBB recordings from PyCon ZA 2020
===================================================================

This contains various things for manipulating the BBB recordings from PyCon ZA 2020

Contents:
--------

``bbb-recorder/Dockerfile`` - A dockerfile for bundling everything needed to run bbb-recorder in one place.

``scripts/obfuscate_chat.py`` - A crude script to replace names in the chat logs (sender name and any exact references in the messages)

``scripts/popcorn2srt.py`` - A cruder script to convert chat logs into srt-format subtitles

``scripts/make_cmds.py`` - Generate a list of docker run commands from a list of names & urls (used to create shell scripts to do the conversion)

``scripts/make_html.py`` - Generate index.html file to make a list of mp4 downloadable (because we disable autoindex for BBB)
