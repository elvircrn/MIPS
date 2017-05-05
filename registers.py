"""Contains a set of registers."""
class RegisterSet:
    def __init__(self):
        self.registers = [0 for _ in range(32)]

    def __getitem__(self, code):
        """ Register name given in the format R<id> """
        if isinstance(code, basestring):
            return self.registers[int(code[1:])]

        """ Register name given in the format <id> """
        return self.registers[code]

    def __setitem__(self, code, value):
        """ Register name given in the format R<id> """
        if isinstance(code, basestring):
            self.registers[int(code[1:])] = value

        elif isinstance(code, int):
            """ Register name given in the format <id> """
            self.registers[int(code)] = value



    
