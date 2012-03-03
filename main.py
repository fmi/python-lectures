#!/usr/bin/env python3
import yaml

import presentation

with open('index.yaml', 'r') as f:
    slides = yaml.load(f)

def lecture(index):
    date, slug, title = slides[index].values()
    with open('lectures/{}.html'.format(slug), 'w+') as f:
        f.write(presentation.build('{}.shpaml'.format(slug), title, date))

def build_all_presentations():
    for slide_index in slides:
        if 'slug' in slides[slide_index]:
            lecture(slide_index)

if __name__ == '__main__':
    build_all_presentations()
