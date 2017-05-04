from instrmem import *

class MIPS(object):
    def __init__(self, pc, instructions):
        self.pc = 0
        self.instructions = instructions
        self.registers = RegisterSet()

        self.rtype_functions = dict {
            0: (lambda x, y: x << y)
            2: (lambda x, y: x >> y)
            3: (lambda x, y: x >> y)
            4: (lambda x, y: x << y)
            6: (lambda x, y: x >> y)
            7: (lambda x, y: x >> y)
            32: (lambda x, y: x + y)
            33: (lambda x, y: x + y)
            34: (lambda x, y: x - y)
            35: (lambda x, y: x - y)
            36: (lambda x, y: x & y)
            37: (lambda x, y: x | y)
            38: (lambda x, y: x ^ y)
            39: (lambda x, y: ~(x | y))
            42: (lambda x, y: x < y)
            43: (lambda x, y: x < y)
        }

        self.itype_functions = dict {
            8: (lambda x, imm: x + imm)
            9: (lambda x, imm: x + imm)
            10: (lambda x, imm: x < imm)
            11: (lambda x, imm: x < imm)
            12: (lambda x, imm: x & imm)
            13: (lambda x, imm: x | imm)
            14: (lambda x, imm: x ^ imm)
        }

    def exectue(self, instruction):
        

    def execute_instructions(self):
        while pc < len(instructions):
            self.execute(instructions[pc])
            pc++
