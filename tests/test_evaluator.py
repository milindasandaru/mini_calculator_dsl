import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.lexer import tokenize
from src.parser import Parser
from src.evaluator import eval_ast

def evaluate_expr(expr: str):
    tokens = tokenize(expr)
    parser = Parser(tokens)
    ast = parser.parse()
    return eval_ast(ast)

def test_addition():
    assert evaluate_expr("2 + 3") == 5

def test_precedence():
    assert evaluate_expr("2 + 3 * 4") == 14  # Multiplication first

def test_parentheses():
    assert evaluate_expr("(2 + 3) * 4") == 20

def test_division():
    assert evaluate_expr("10 / 2") == 5
