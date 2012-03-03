#!/usr/bin/env python3
import sys
import yaml

import presentation

with open('index.yaml', 'r') as f:
    slides = yaml.load(f)

def lecture(index):
    ''' Builds specific lecture, by the given index from index.yml '''
    date, slug, title = slides[index].values()
    with open('compiled/{}.html'.format(slug), 'w+') as f:
        f.write(presentation.build('lectures/{}.shpaml'.format(slug), title, date))

def build_all_presentations():
    ''' Gives every single presentation with a slug to lecture() '''
    for slide_index in slides:
        if 'slug' in slides[slide_index]:
            lecture(slide_index)

if __name__ == '__main__':
    if len(sys.argv) == 1:
        build_all_presentations()
    else:
        lecture(int(sys.argv[1]))
