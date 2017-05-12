from bitmanip import *


def bit_test():
    # 100111010
    assert(extr_lo_bits(314, 4) == 10)
    assert(extr_lo_bits(314, 0) == 0)

    # 10011101000000000000000000000000(2634022912)
    assert(extr_hi_bits(2634022912, 4) == 9)

    #                        8    3
    #                        ......
    # 00000000000000000000000100111010
    assert(extr_range(314, 3, 9) == 39)

    print "Bit tests passed"
