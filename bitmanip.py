"""Bits is a 32-bit number"""

"""Extracts the last width most significant bits"""
def extr_hi_bits(bits, width):
    return ((bits & (-(1 << width))) >> (32 - width))

"""Extracts the first width lowest bits"""
def extr_lo_bits(bits, width):
    return (bits & ((1 << width) - 1))

"""Bits in the [x, y) range"""
def extr_range(bits, x, y):
    return extr_lo_bits(bits >> x, (y - x))
