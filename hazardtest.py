from mips import MIPS

m = MIPS(0, [])

m.parse_instruction("add r6, r16, r5")
m.parse_instruction("sub r1, r6, r3")
m.parse_instruction("or r8, r6, r2")
m.parse_instruction("lw r1, 100(r7)")
m.parse_instruction("xor r10, r1, r11")
m.parse_instruction("sw r3, 50(r0)")
m.parse_instruction("nop")

for i, x in enumerate(m.reg_hist):
    print "register state after instruction " + str(i)
    x.print_touched()

for i, x in enumerate(m.ram_hist):
    print "ram state after instruction " + str(i)
    x.print_touched()

print "Nacin tumacenja ovog testa:\n" \
        + "Ispisuju se samo oni registri i samo one celije RAM-a nad\n" \
        + "kojima se vrsila operacija upisivanja. Ako neki registar\n" \
        + "ako neki RAM nije ispisan u konzoli pri ispisivanju stanja\n" \
        + "registara/rama nakon neke instrukcije, pretpostavlja se da\n" \
        + "oni imaju defaultnu vrijednost(0)."


m.print_table()
