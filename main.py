from mips import MIPS


m = MIPS(0, [])
for line in open("instructions.txt", "r"):
    m.parse_instruction(line)
m.ram.print_vals()
m.registers.print_values()
m.print_table()



