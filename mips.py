from instrmem import *
from bitmanip import *
import re
from registers import *
from ram import *

class MIPS(object):
    def __init__(self, pc, instructions):
        self.pc = 0
        self.instructions = instructions
        self.registers = RegisterSet()
        self.ram = RAM()

        self.rtype_functions = {
            0: (lambda x, y: x << y),
            2: (lambda x, y: x >> y),
            3: (lambda x, y: x >> y),
            4: (lambda x, y: x << y),
            6: (lambda x, y: x >> y),
            7: (lambda x, y: x >> y),
            32: (lambda x, y: x + y),
            33: (lambda x, y: x + y),
            34: (lambda x, y: x - y),
            35: (lambda x, y: x - y),
            36: (lambda x, y: x & y),
            37: (lambda x, y: x | y),
            38: (lambda x, y: x ^ y),
            39: (lambda x, y: ~(x | y)),
            42: (lambda x, y: x < y),
            43: (lambda x, y: x < y)
        }

        self.itype_functions = {
            8: (lambda x, imm: x + imm),
            9: (lambda x, imm: x + imm),
            10: (lambda x, imm: x < imm),
            11: (lambda x, imm: x < imm),
            12: (lambda x, imm: x & imm),
            13: (lambda x, imm: x | imm),
            14: (lambda x, imm: x ^ imm)
        }

    """ instr is of type string """
    def parse_instruction(self, instr):
        words = re.compile('\w+').findall(instr)

        print words
        
        #load or store constants
        if words[0] == "lwi"  and len(words) == 3:
            imm = int(words[2])
            self.registers[words[1]] = imm
        elif words[0] == "lw":
            self.registers[words[1]] = self.registers[words[3]] + int(words[2])
        elif words[0] == "sw":
            self.registers[words[2]] = self.registers[words[3]] + int(words[1])

        return 0

    def exectue(self, instruction):
        opcode = extr_hi_bits(instruction, 6)
        rs = extr_range(instruction, 21, 26)
        rt = extr_range(instruction, 16, 21)

        # R type instruction
        if opcode == 0:
            rd = extr_range(instruction, 11, 16)
            shamt = extr_range(instruction, 6, 11)
            funct = extr_range(instruction, 0, 6)

            self.registers[rd] = self.rtype_functions(funct)(self.registers[rt], shamt if funct < 4 else self.registers[rt])

        # I type instruction
        else:
            imm = extr_(instruction, 0, 16)
            self.registers[rt] = self.itype_functions(opcode)(self.registers[rs], imm)

    def execute_instructions(self):
        while pc < len(instructions):
            self.execute(instructions[pc])
            pc += 1
