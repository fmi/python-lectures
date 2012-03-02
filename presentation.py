#!/usr/bin/python3
import sys
import shpaml

class Presentation:
    def __init__(self, input_file, lecture_name, date, *args):
        self.input_file = input_file
        self.lecture_name = lecture_name
        self.date = date

    @property
    def header(self):
        with open('ui/header.html') as f:
            return f.read().format(title=self.lecture_name, date=self.date)

    @property
    def footer(self):
        with open('ui/footer.html') as f:
            return f.read()

    @property
    def slides(self):
        with open(self.input_file) as f:
            return shpaml.convert_text(f.read())

    def render(self):
        return self.header + self.slides + self.footer


if __name__ == '__main__':
    presentation = Presentation(*sys.argv[1:])
    print(presentation.render())
