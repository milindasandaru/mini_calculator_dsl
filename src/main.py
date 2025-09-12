import sys
from lexer import tokenize
from parser import Parser
from evaluator import eval_ast

def run(code: str):
    tokens = tokenize(code)
    parser = Parser(tokens)
    ast = parser.parse()
    result = eval_ast(ast)
    return result

def main():
    if len(sys.argv) > 1:
        with open(sys.argv[1]) as f:
            code = f.read()
            print(run(code))
    else:
        while True:
            try:
                line = input("calc> ")
                if line.strip().lower() in ("exit", "quit"):
                    break
                print(run(line))
            except Exception as e:
                print("Error: ", e)

if __name__== "__main__":
    main()