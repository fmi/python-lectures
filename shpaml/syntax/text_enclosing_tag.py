from .base import Syntax

class TextEnclosingTag(Syntax):
    ''' For HTML one-liners you can use the pipe character
    followed by a space to separate markup from content.
    '''
    regex = '(.*) \| (.*)'

    def __init__(self, matcher):
        self.matcher = matcher

    def parse(self):
        tag, text = self.matcher.groups()
        return self.enclose_tag(tag, text)
