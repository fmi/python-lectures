#!/usr/bin/python3
import sys
import shpaml

def build(input_file, lecture_name, date):
    with open(input_file) as f:
        slides = shpaml.convert_text(f.read())
    with open('html/layout.html') as f:
        return f.read().format(title=lecture_name, date=date, slides=slides)

if __name__ == '__main__':
    print(build(*sys.argv[1:]))
