#!/usr/bin/python3
import sys
import shpaml

def build(input_file, lecture_name, date):
    with open('ui/header.html') as f:
        header = f.read().format(title=lecture_name, date=date)
    with open('ui/footer.html') as f:
        footer = f.read()
    slides = shpaml.convert_text(f.read())

    return header + slides + footer


if __name__ == '__main__':
    print(build(sys.argv[1:]))
