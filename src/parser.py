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
    
    