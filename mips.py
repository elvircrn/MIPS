from instrmem import *
from bitmanip import *

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
        opcode = extr_hi_bits(instruction, 6)
        rs = extr_range(instruction, 21, 26)
        rt = extr_range(instruction, 16, 21)

        # R type instruction
        if opcode == 0:
            rd = extr_range(instruction, 11, 16)
            shamt = extr_range(instruction, 6, 11)
            funct = extr_range(instruction, 0, 6)

            self.registers.get_register(rd) = self.rtype_functions(funct)(self.registers.get_register(rt), shamt if funct < 4 else self.registers.get_register(rt))

        # I type instruction
        else:
            imm = extr_(instruction, 0, 16)
            self.registers.get_register(rt) = self.itype_functions(opcode)(self.registers.get_register(rs), imm)

    def execute_instructions(self):
        while pc < len(instructions):
            self.execute(instructions[pc])
            pc++
