from lexer import lex
from parser import parse


def from_string(json_string):
    tokens = lex(json_string)
    return parse(tokens)[0]


if __name__ == '__main__':
    print(from_string('{"name1":"foo", "name2":"bar"}'))
