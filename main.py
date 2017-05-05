from table import Table
from mips import MIPS
table = Table()
table.draw()


m = MIPS(0, [])
m.parse_instruction("lw r0, 42(r1)")


