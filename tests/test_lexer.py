import pytest
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.lexer import tokenize

def test_simple_expression():
    tokens = tokenize("3 + 5")
    assert tokens == [("NUMBER", 3), ("PLUS", "+"), ("NUMBER", 5)]

def test_parentheses():
    tokens = tokenize("(4 - 1)")
    assert tokens == [("LPAREN", "("), ("NUMBER", 4), ("MINUS", "-"), ("NUMBER", 1), ("RPAREN", ")")]

def test_invalid_character():
    with pytest.raises(RuntimeError):
        tokenize("2 $ 3")