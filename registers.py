"""Contains a set of registers."""
class RegisterSet:
    def __init__(self):
        self.registers = [0 for _ in range(32)]

    @property
    def get_register(self, code):
        return self.registers[code]
