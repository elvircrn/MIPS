from instrmem import *


class MIPS(object):
    def __init__(self, pc, instructions):
        self.pc = 0
        self.instructions = instructions
        self.registers = RegisterSet()

    def exectue(self):
        

    def execute_instructions(self):
        while pc < len(instructions):
            
            pc++

mips = MIPS(0, InstrMem())
print "It works!"
