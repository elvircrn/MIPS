from table import Table
from mips import MIPS
table = Table()
table.draw()


m = MIPS(0, [])
m.parse_instruction("lwi r0, 10")
print m.registers[0]


m.parse_instruction("r0, 10")


m.ram.print_vals()
