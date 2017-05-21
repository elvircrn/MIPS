from mips import MIPS
import re

m = MIPS(0, [])

# Citanje podatkovne memorije
for line in open("ram.txt", "r"):
    words = re.compile('\w+').findall(line)
    if len(words) == 2:
        m.ram[int(words[0])] = int(words[1])

# Citanje stanja registara
for line in open("reg.txt", "r"):
    words = re.compile('\w+').findall(line)
    if len(words) == 2:
        m.registers[int(words[0])] = int(words[1])

# Citanje, izvrsavanje i analiza instrukcija
for line in open("instr.txt", "r"):
    m.parse_instruction(line)

# Sljedece linije zakomentarisati/odkomentarisati po potrebi:

# Ispisivanje stanja podatkovne memorije nakon svake instrukcije
for i, x in enumerate(m.reg_hist):
    print "register state after instruction " + str(i)
    x.print_touched()

# Ispisivanje stanja registara nakon svake instrukcije
for i, x in enumerate(m.ram_hist):
    print "ram state after instruction " + str(i)
    x.print_touched()

# Ispisivanje stanja protocne strukture
m.print_table()



