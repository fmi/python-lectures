import re
from .syntax import Syntax
from .syntax.indent import Indent
from .syntax.raw_html import RawHtml

def html_block_tag(line):
    if re.match(RawHtml.regex, line):
        return (line, None)
    else:
        start_tag, end_tag = Syntax().apply_id_and_classes(line)
        return (start_tag, end_tag)


def find_indentation(line):
    return Indent(re.match(Indent.regex, line)).parse()

