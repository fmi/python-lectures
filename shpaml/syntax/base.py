import re


class Syntax:
    PASS_SYNTAX = 'PASS'
    TAG_WHITESPACE_ATTRS = '(\S+)(s*?)(.*)'
    TAG_AND_ID = '(.*)#(.*)'
    DOT_FOR_CLASSES = '.'
    DIV_SHORTCUT = '[\.#]'

    @property
    def convert(self):
        from converter import Convert
        return Convert()

    def enclose_tag(self, tag, text):
        start_tag, end_tag = self.apply_id_and_classes(tag)
        return start_tag + text + end_tag

    def apply_id_and_classes(self, markup):
        if re.match(self.DIV_SHORTCUT, markup):
            markup = 'div' + markup
        tag, whitespace, attrs = re.match(self.TAG_WHITESPACE_ATTRS, markup).groups()
        tag, id_ = self.tag_and_id(tag)
        tag, classes = self.tag_and_classes(tag)
        if classes:
            attrs += ' class="%s"' % classes
        if id_:
            attrs += ' id="%s"' % id_
        start_tag = tag + whitespace + attrs
        return ('<%s>' % start_tag, '</%s>' % tag)

    def tag_and_id(self, tag):
        m = re.match(self.TAG_AND_ID, tag)
        if m:
            return m.groups()
        else:
            return tag, None

    def tag_and_classes(self, tag):
        frags = tag.split(self.DOT_FOR_CLASSES)
        tag = frags[0]
        classes = ' '.join(frags[1:])
        return tag, classes
