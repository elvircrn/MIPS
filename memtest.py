from table import Table
from mips import MIPS

def mem_test():
    m = MIPS(0, [])
    m.parse_instruction("lui r1, 10")
    m.parse_instruction("sw r1, 10(r0)")

    assert(m.ram[10] == 10)
    assert(m.registers[1] == 10)

    print "Memory tests passed"
