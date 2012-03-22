import re

from .syntax import rules
from .indenter import Indent
from .utils import html_block_tag, find_indentation

class Convert:
    def tree(self, in_body):
        return self.document(in_body,
                             branch_method=html_block_tag,
                             indentation_method=find_indentation)

    def line(self, line):
        line = line.strip()
        for method in rules:
            m = re.match(method.regex, line)
            if m:
                return method(m).parse()

    def document(self, in_body, branch_method, indentation_method):
        indent = Indent()
        for prefix, line, kind in self.get_lines(in_body, indentation_method):
            if kind == 'branch':
                start, end = branch_method(line)
                if end:
                    indent.push(prefix, start, end)
                else:
                    indent.add(prefix, start)

            elif kind == 'leaf':
                if line == 'PASS':
                    indent.pop(prefix)
                else:
                    line = self.line(line)
                    indent.add(prefix, line)
            else:
                indent.insert('', line)
        return indent.body()

    def get_prefixed_lines(self, in_body, indentation_method):
        lines = in_body.split('\n')
        return [indentation_method(line) for line in lines]

    def get_lines(self, in_body, indentation_method):
        '''
        Splits out lines from a file and identifies whether lines
        are branches, leafs, or blanks.
        '''
        prefixed_lines = self.get_prefixed_lines(in_body, indentation_method)
        lookaheads = [len(prefix) for prefix, line in prefixed_lines if line]
        lookaheads.pop(0)
        lookaheads.append(None)
        lines = []
        plain_block = -1
        for prefix, line in prefixed_lines:
            if line:
                follower_length = lookaheads.pop(0)

                if plain_block == -1:
                    if line[-1] == ':':
                        line = line[:-1]
                        plain_block = len(prefix)
                elif len(prefix) > plain_block:
                    line = "|{}{}".format(' ' * (len(prefix) - plain_block - 4), line)
                    prefix = ' ' * (plain_block+5)
                    follower_length = len(prefix)
                else:
                    plain_block = -1

                if follower_length is None:
                    kind = 'leaf'
                elif follower_length <= len(prefix):
                    kind = 'leaf'
                else:
                    kind = 'branch'
            else:
                kind = 'blank'
            lines.append((prefix, line, kind))
        return lines

