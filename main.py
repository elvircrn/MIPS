from table import Table
from mips import MIPS
table = Table()
table.draw()


m = MIPS(0, [])
m.parse_instruction("lui r1, 10")
m.parse_instruction("sw r1, 10(r0)")
m.ram.print_vals()
m.registers.print_values()


