class Instruction:
    def __init__(self, code, tokens):
        self.code = code
        self.tokens = tokens
    
    def __str__(self):
        return self.code + " ".join(self.tokens)
