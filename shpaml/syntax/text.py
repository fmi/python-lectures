from .base import Syntax

class Text(Syntax):
    ''' This is our way to tell the parser:
        "Nothing to see here, move along."
    '''
    regex = '^\| (.*)'

    def __init__(self, matcher):
        self.matcher = matcher

    def parse(self):
        return self.matcher.group(1).rstrip()
