class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0
    
    def peek(self):
        return self.tokens[self.pos] if self.pos < len(self.tokens) else None
    
    def consume(self, expected_type=None):
        token = self.peek()
        if token is None:
            return None
        if expected_type and token[0] != expected_type:
            raise RuntimeError(f"Expected {expected_type}, got {token}")
        self.pos += 1
        return token
    
    def parse(self):
        node = self.expr()
        # Ensure all tokens are consumed
        if self.peek() is not None:
            raise RuntimeError(f"Unexpected token {self.peek()}")
        return node
    
    def expr(self):
        # expr -> term ((PLUS|MINUS) term)*
        node = self.term()
        while self.peek() and self.peek()[0] in ("PLUS", "MINUS"):
            op = self.consume()[0]
            right = self.term()
            node = (op, node, right)
        return node

    def term(self):
        # term -> factor ((TIMES|DIVIDE) factor)*
        node = self.factor()
        while self.peek() and self.peek()[0] in ("TIMES", "DIVIDE"):
            tok_type = self.consume()[0]
            right = self.factor()
            # Normalize operator names for evaluator
            op = "MUL" if tok_type == "TIMES" else "DIV"
            node = (op, node, right)
        return node
    
    def factor(self):
        token = self.peek()
        if token is None:
            raise RuntimeError("Unexpected end of input")
        if token[0] == "NUMBER":
            self.consume("NUMBER")
            return ("NUM", token[1])
        elif token[0] == "LPAREN":
            self.consume("LPAREN")
            node = self.expr()
            self.consume("RPAREN")
            return node
        else:
            raise RuntimeError(f"Unexpected token {token}")