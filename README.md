Scripts and stuff for manipulating BBB recordings from PyCon ZA 2020
===================================================================

This contains various things for manipulating the BBB recordings from PyCon ZA 2020

Contents:
--------

* ``bbb-recorder/Dockerfile`` - A dockerfile for bundling everything needed to run bbb-recorder in one place.
* ``scripts/obfuscate_chat.py`` - A crude script to replace names in the chat logs (sender name and any exact references in the messages)
* ``scripts/make_title_slides.py`` - A script to generate title slides from an svg template and a tsv of talk metadata. Needs BeautifulSoup, Inkscape and the Unica One font.
* ``resources/talks.tsv`` - The talk metadata
* ``resources/title.svg`` - The title slide template
* ``title_slides`` - The generated slides. Names are temporary.
