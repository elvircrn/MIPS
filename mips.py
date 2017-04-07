from instrmem import *

class MIPS(object):
    def __init__(self, pc, instructions):
        self.pc = 0
        self.instructions = instructions

mips = MIPS(0, InstrMem())
print "It works!"