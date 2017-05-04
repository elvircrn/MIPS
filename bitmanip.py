"""Bits is a 32-bit number"""
def extr_hi_bits(bits, width):
    return ((bits & (-(1 << width))) >> (32 - width))

def extr_lo_bits(bits, width):
    return (bits & ((1 << width) - 1))

def extr_range(bits, x, y):
    return extr_lo_bits(bits >> x, (y - x))
