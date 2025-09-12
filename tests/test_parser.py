import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.lexer import tokenize
from src.parser import Parser

def test_parse_simple_addition():
    tokens = tokenize("2 + 3")
    parser = Parser(tokens)
    ast = parser.parse()
    assert ast == ("PLUS", ("NUM", 2), ("NUM", 3))

def test_parse_mixed_operations():
    tokens = tokenize("2 + 3 * 4")
    parser = Parser(tokens)
    ast = parser.parse()
    assert ast == ("PLUS", ("NUM", 2), ("MUL", ("NUM", 3), ("NUM", 4)))
