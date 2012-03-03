import sys

from .converter import Convert


def convert_text(in_body):
    '''
    You can call convert_text directly to convert shpaml markup
    to HTML markup.
    '''
    return Convert().tree(in_body)


if __name__ == "__main__":
    if len(sys.argv) == 2:
        shpaml_text = file(sys.argv[1]).read()
    else:
        shpaml_text = sys.stdin.read()
    print(convert_text(shpaml_text))

