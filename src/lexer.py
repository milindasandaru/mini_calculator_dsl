import re

token_specification = [
    ('NUMBER',   r'\d+(\.\d*)?'),  # Integer or decimal number
    ('PLUS',     r'\+'),            # Addition operator
    ('MINUS',    r'-'),             # Subtraction operator
    ('TIMES',    r'\*'),            # Multiplication operator
    ('DIVIDE',   r'/'),             # Division operator
    ('LPAREN',   r'\('),            # Left parenthesis
    ('RPAREN',   r'\)'),            # Right parenthesis
    ('SKIP',     r'[ \t]+'),       # Skip over spaces and tabs
    ('MISMATCH', r'.'),             # Any other character
]

# build combine regex
token_regex = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in token_specification)

def tokenize(code: str):
    # Convert input string into a list of tokens.
    tokens = []
    for match in re.finditer(token_regex, code):
        kind = match.lastgroup
        value = match.group()
        if kind == "NUMBER":
            tokens.append((kind, int(value)))
        elif kind == "SKIP":
            continue
        elif kind == "MISMATCH":
            raise RuntimeError(f"Unexpected character: {value}")
        else:
            tokens.append((kind, value))
    return tokens

if __name__=="__main__":
    print(tokenize("2 + 3 * (4 - 1)"))