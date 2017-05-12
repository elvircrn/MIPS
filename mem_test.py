from table import Table
from mips import MIPS

m = MIPS(0, [])
m.parse_instruction("lui r1, 10")
m.parse_instruction("sw r1, 10(r0)")

assert(m.ram[10] == 10)
assert(m.registers[1] == 10)

