import re

from instrmem import InstrMem
from bitmanip import *
from instruction import Instruction
from registers import RegisterSet
from ram import RAM

class MIPS(object):
    def __init__(self, pc, instructions):
        self.pc = 0
        self.instructions = instructions
        self.registers = RegisterSet()
        self.ram = RAM()
        self.instr_buff = []

        self.strr_type = {
            "sll": (lambda x, y: x << y),
            "srl": (lambda x, y: x >> y),
            "sra": (lambda x, y: x >> y),
            "sllv": (lambda x, y: x << y),
            "srlv": (lambda x, y: x >> y),
            "srav": (lambda x, y: x >> y),
            "add": (lambda x, y: x + y),
            "addu": (lambda x, y: x + y),
            "sub": (lambda x, y: x - y),
            "subu": (lambda x, y: x - y),
            "and": (lambda x, y: x & y),
            "or": (lambda x, y: x | y),
            "xor": (lambda x, y: x ^ y),
            "nor": (lambda x, y: ~(x | y)),
            "slt": (lambda x, y: x < y),
            "sltu": (lambda x, y: x < y)
        }

        self.stri_type = {
            "addi": (lambda x, y: x + y),
            "addiu": (lambda x, y: x + y),
            "andi": (lambda x, y: x & y),
            "ori": (lambda x, y: x | y),
            "xori": (lambda x, y: x ^ y),
        }

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
        self.instr_buff.append(Instruction(words[0], words[1:]))

        instr = words[0]
        
        # Load/Store operations

        # lui $rt, imm
        if words[0] == "lui" and len(words) == 3:
            imm = int(words[2])
            self.registers[words[1]] = imm
        # lw $rt, imm($rs)
        elif words[0] == "lw":
            imm = int(words[2])
            rs = words[3]
            rt = words[1]
            self.registers[rt] = self.ram[self.registers[rs] + imm]
        # sw $rt, imm($rs)
        elif words[0] == "sw":
            rt = words[1]
            imm = int(words[2])
            rs = words[3]
            self.ram[self.registers[rs] + imm] = self.registers[rt]
        # R-type instructions
        # shamt instructions
        elif instr == "sll" or instr == "srl" or instr == "sra":
            shamt = int(words[3])
            rd = words[1]
            rt = words[1]
            self.registers[rd] = self.strr_type[instr](rt, shamt)
        # Non-shamt r-type instructions
        elif instr in self.strr_type:
            rd = words[1]
            rs = words[2]
            rt = words[3]
            self.registers[rd] = self.strr_type[instr](self.registers[rs], self.registers[rt])
        # i-type alul instructions
        elif instr in self.stri_type:
            imm = int(words[3])
            rt = words[1]
            rs = words[2]
            self.registers[rt] = self.stri_type[instr](self.registers[rs], imm)
        else:
            print "Cannot parse instruction: " + instr

        return 0

    # Bytecode format
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
