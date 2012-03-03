from .base import Syntax

class RawText(Syntax):
    regex = '(.*)'

    def __init__(self, matcher):
        self.matcher = matcher

    def parse(self):
        return self.matcher.group(1).rstrip()
