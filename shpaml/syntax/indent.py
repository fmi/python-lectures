from .base import Syntax

class Indent(Syntax):
    regex = '(\s*)(.*)'

    def __init__(self, matcher):
        self.matcher = matcher

    def parse(self):
        prefix, line = self.matcher.groups()
        line = line.rstrip()
        if line == '':
            prefix = ''
        return prefix, line

