class Indent:
    def __init__(self):
        self.stack = []
        self.lines = []

    def push(self, prefix, start, end):
        self.add(prefix, start)
        self.stack.append((prefix, end))

    def pop_whitespace(self, lines):
        whitespace_lines = []
        while lines and lines[-1] == '':
            whitespace_lines.append(lines.pop())
        return whitespace_lines

    def add(self, prefix, line):
        self.pop(prefix)
        self.insert(prefix, line)

    def insert(self, prefix, line):
        line = ''.join(line)
        self.lines.append(prefix+line)

    def pop(self, prefix):
        while self.stack:
            start_prefix, end =  self.stack[-1]
            if len(prefix) <= len(start_prefix):
                self.close_block(start_prefix, end)
                self.stack.pop()
            else:
                return

    def close_block(self, start_prefix, end):
        whitespace_lines = self.pop_whitespace(self.lines)
        self.insert(start_prefix, end)
        self.lines += whitespace_lines

    def body(self):
        self.pop('')
        return '\n'.join(self.lines)

