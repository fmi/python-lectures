from .base import Syntax

class RawHtml(Syntax):
    ''' This Syntax module allows us to use raw html in our shpaml code '''
    regex = '^([<{]\S.*)'

    def __init__(self, matcher):
        self.matcher = matcher

    def parse(self):
        return self.matcher.group(1).rstrip()



