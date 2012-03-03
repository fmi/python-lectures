from .base import Syntax

class SelfClosingTag(Syntax):
    regex = '> (.*)'

    def __init__(self, matcher):
        self.matcher = matcher

    def parse(self):
        tag = self.matcher.group(1).strip()
        return '<%s />' % tag

