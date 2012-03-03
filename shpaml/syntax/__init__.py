from .base import Syntax
from .indent import Indent
from .outer_closing_tag import OuterClosingTag
from .raw_html import RawHtml
from .raw_text import RawText
from .self_closing_tag import SelfClosingTag
from .text import Text
from .text_enclosing_tag import TextEnclosingTag

rules = [RawHtml, Text, OuterClosingTag, TextEnclosingTag, SelfClosingTag, RawText]
__all__ = rules + [Syntax, Indent]
