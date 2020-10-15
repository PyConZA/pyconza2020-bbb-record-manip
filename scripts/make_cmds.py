#!/usr/bin/python3                                                                                                                                          
#
# Turn a list of 'name' - 'url' lines into a set of pastable commands

with open('list') as f:
    print('#!/bin/bash')
    for line in f.readlines():
        name, url = line.strip().split(' - ')
        print(f'docker run -ti -v /tmp/output:/data pyconza-bbb-export "{url}" "{name}_fixed" 0 true')
