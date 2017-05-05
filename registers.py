"""Contains a set of registers."""
class RegisterSet:
    def __init__(self):
        self.registers = [0 for _ in range(32)]

    def __getitem__(self, code):
        """ Register name given in the format R<id> """
        if isinstance(code, string):
            return self.registers[int(code[1:])]

        """ Register name given in the format <id> """
        return self.registers[code]

    
