from .base import Syntax

class OuterClosingTag(Syntax):
    regex = '(.*?) > (.*)'

    def __init__(self, matcher):
        self.matcher = matcher

    def parse(self):
        tag, text = self.matcher.groups()
        text = self.convert.line(text)
        return self.enclose_tag(tag, text)

